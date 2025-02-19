from flask import Flask, render_template, jsonify, request
import gpiod
import threading
import time

app = Flask(__name__)

# Set up the GPIO chip (usually "gpiochip0" on Raspberry Pi)
chip = gpiod.Chip("gpiochip0")

# Define GPIO pins for the LEDs
RED_PIN = 17
YELLOW_PIN = 27
GREEN_PIN = 22

# Request GPIO lines for output (default off)
red_line = chip.get_line(RED_PIN)
yellow_line = chip.get_line(YELLOW_PIN)
green_line = chip.get_line(GREEN_PIN)

red_line.request(consumer="flask", type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])
yellow_line.request(consumer="flask", type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])
green_line.request(consumer="flask", type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])

# Stoplight state and system flags
lights = ["green", "yellow", "red"]
current_index = 0            # Logical index for the current light
automatic_running = False    # Auto mode off by default
system_on = False            # System is off by default

# Global settings for auto durations (in seconds)
auto_durations = {"green": 3.0, "yellow": 2.0, "red": 3.0}

# Event for cancelable waiting in auto cycle
stop_event = threading.Event()

def update_lights():
    """Update physical LEDs. If the system is off, turn off all LEDs."""
    if not system_on:
        red_line.set_value(0)
        yellow_line.set_value(0)
        green_line.set_value(0)
    else:
        red_line.set_value(1 if lights[current_index] == "red" else 0)
        yellow_line.set_value(1 if lights[current_index] == "yellow" else 0)
        green_line.set_value(1 if lights[current_index] == "green" else 0)

def automatic_cycle():
    """Automatically cycle the stoplight using the durations in auto_durations."""
    global current_index, automatic_running, auto_durations, system_on
    while automatic_running and system_on:
        current_light = lights[current_index]
        duration = auto_durations.get(current_light, 3.0)
        if stop_event.wait(duration):
            break
        current_index = (current_index + 1) % len(lights)
        update_lights()

@app.route("/")
def index():
    """Render the main page."""
    return render_template("stoplightv2.html")

@app.route("/get_light", methods=["GET"])
def get_light():
    """Return the current light state; return 'off' if system is off."""
    if not system_on:
        return jsonify({"light": "off"})
    return jsonify({"light": lights[current_index]})

@app.route("/manual_cycle", methods=["POST"])
def manual_cycle():
    """Manually cycle to the next light (if system is on and auto mode is off)."""
    global current_index
    if system_on and not automatic_running:
        current_index = (current_index + 1) % len(lights)
        update_lights()
    return jsonify({"light": lights[current_index] if system_on else "off"})

@app.route("/start_auto", methods=["POST"])
def start_auto():
    """Start automatic cycling (only if system is on)."""
    global automatic_running
    if system_on and not automatic_running:
        automatic_running = True
        stop_event.clear()
        thread = threading.Thread(target=automatic_cycle, daemon=True)
        thread.start()
    return jsonify({"status": "running", "system_on": system_on})

@app.route("/stop_auto", methods=["POST"])
def stop_auto():
    """Stop automatic cycling."""
    global automatic_running
    automatic_running = False
    stop_event.set()
    return jsonify({"status": "stopped"})

@app.route("/update_settings", methods=["POST"])
def update_settings():
    """Update auto durations based on user input."""
    global auto_durations
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "No data provided"}), 400
    try:
        auto_durations["green"] = float(data.get("green", auto_durations["green"]))
        auto_durations["yellow"] = float(data.get("yellow", auto_durations["yellow"]))
        auto_durations["red"] = float(data.get("red", auto_durations["red"]))
        return jsonify({"status": "success", "auto_durations": auto_durations})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route("/get_mode", methods=["GET"])
def get_mode():
    """Return current mode: 'off', 'auto', or 'manual'."""
    if not system_on:
        return jsonify({"mode": "off"})
    return jsonify({"mode": "auto" if automatic_running else "manual"})

@app.route("/get_system_state", methods=["GET"])
def get_system_state():
    """Return the current system state."""
    return jsonify({"system_on": system_on})

@app.route("/turn_on", methods=["POST"])
def turn_on():
    """Turn on the system and reset to manual mode."""
    global system_on, automatic_running, current_index
    system_on = True
    automatic_running = False  # Ensure auto mode is off
    current_index = 0          # Reset to initial state (typically 'green')
    update_lights()
    return jsonify({"status": "system turned on", "system_on": system_on})

@app.route("/turn_off", methods=["POST"])
def turn_off():
    """Turn off the system (stop auto mode and turn off all LEDs)."""
    global system_on, automatic_running
    system_on = False
    automatic_running = False
    stop_event.set()
    update_lights()
    return jsonify({"status": "system turned off", "system_on": system_on})

if __name__ == "__main__":
    try:
        update_lights()  # Ensure LEDs are off at startup.
        app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
    except KeyboardInterrupt:
        red_line.release()
        yellow_line.release()
        green_line.release()
