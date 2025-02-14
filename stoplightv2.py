from flask import Flask, render_template, jsonify, request
import gpiod
import threading
import time

app = Flask(__name__)

# Set up the GPIO chip (usually "gpiochip0" on Raspberry Pi)
chip = gpiod.Chip("gpiochip0")

# Define your GPIO pins
RED_PIN = 17
YELLOW_PIN = 27
GREEN_PIN = 22

# Request each GPIO line for output. Default value is off (0).
red_line = chip.get_line(RED_PIN)
yellow_line = chip.get_line(YELLOW_PIN)
green_line = chip.get_line(GREEN_PIN)

red_line.request(consumer="flask", type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])
yellow_line.request(consumer="flask", type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])
green_line.request(consumer="flask", type=gpiod.LINE_REQ_DIR_OUT, default_vals=[0])

# Define stoplight states and initial conditions
lights = ["green", "yellow", "red"]
current_index = 0  # index for current light
automatic_running = False  # auto mode not running by default
system_on = True           # system is on by default

# Global settings for auto durations (in seconds)
auto_durations = {"green": 3.0, "yellow": 2.0, "red": 3.0}

# Event for cancelable waiting in auto cycle
stop_event = threading.Event()

def update_lights():
    """Update physical LEDs. If system is off, turn all lights off."""
    if not system_on:
        red_line.set_value(0)
        yellow_line.set_value(0)
        green_line.set_value(0)
    else:
        red_line.set_value(1 if lights[current_index] == "red" else 0)
        yellow_line.set_value(1 if lights[current_index] == "yellow" else 0)
        green_line.set_value(1 if lights[current_index] == "green" else 0)

def automatic_cycle():
    """Automatically cycle the lights using the specified durations."""
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
    """Return the current light (or 'off' if system is off)."""
    if not system_on:
        return jsonify({"light": "off"})
    return jsonify({"light": lights[current_index]})

@app.route("/manual_cycle", methods=["POST"])
def manual_cycle():
    """Manually cycle to the next light (only if system is on and auto mode is off)."""
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
    """Return current mode: 'off', 'auto' or 'manual'."""
    if not system_on:
        return jsonify({"mode": "off"})
    return jsonify({"mode": "auto" if automatic_running else "manual"})

@app.route("/get_system_state", methods=["GET"])
def get_system_state():
    """Return whether the system is on."""
    return jsonify({"system_on": system_on})

@app.route("/turn_on", methods=["POST"])
def turn_on():
    """Turn on the system. Does not start auto mode automatically."""
    global system_on
    system_on = True
    update_lights()
    return jsonify({"status": "system turned on", "system_on": system_on})

@app.route("/turn_off", methods=["POST"])
def turn_off():
    """Turn off the system. Stops auto mode and turns off all lights."""
    global system_on, automatic_running
    system_on = False
    automatic_running = False
    stop_event.set()
    update_lights()
    return jsonify({"status": "system turned off", "system_on": system_on})

if __name__ == "__main__":
    try:
        update_lights()
        app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
    except KeyboardInterrupt:
        red_line.release()
        yellow_line.release()
        green_line.release()
