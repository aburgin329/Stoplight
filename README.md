# Stoplight

Sure! Here's the complete README file with all the information included:

```markdown
# Flask GPIO Stoplight Control

This project is a Flask-based web application to control a stoplight using GPIO pins on a Raspberry Pi. The application allows manual and automatic cycling of the stoplight's red, yellow, and green lights.

## Features

- **Manual Mode**: Manually cycle through the stoplight colors.
- **Automatic Mode**: Automatically cycle through the stoplight colors with configurable durations.
- **System Control**: Turn the system on or off.
- **Status Endpoints**: Get the current light, mode, and system state.

## Requirements

- Flask
- gpiod
- threading
- time

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name
   ```

2. Install the required Python packages:
   ```bash
   pip install Flask gpiod
   ```

3. Run the application:
   ```bash
   python app.py
   ```

## Usage

- Access the web interface at `http://<your-raspberry-pi-ip>:5000`.
- Use the provided endpoints to control the stoplight:

  - `GET /get_light`: Get the current light.
  - `POST /manual_cycle`: Manually cycle to the next light.
  - `POST /start_auto`: Start automatic cycling.
  - `POST /stop_auto`: Stop automatic cycling.
  - `POST /update_settings`: Update auto durations.
  - `GET /get_mode`: Get the current mode.
  - `GET /get_system_state`: Get the system state.
  - `POST /turn_on`: Turn on the system.
  - `POST /turn_off`: Turn off the system.

## Endpoints

- **`GET /`**: Render the main page.
- **`GET /get_light`**: Return the current light (or 'off' if the system is off).
- **`POST /manual_cycle`**: Manually cycle to the next light (only if the system is on and auto mode is off).
- **`POST /start_auto`**: Start automatic cycling (only if the system is on).
- **`POST /stop_auto`**: Stop automatic cycling.
- **`POST /update_settings`**: Update auto durations based on user input.
- **`GET /get_mode`**: Return current mode: 'off', 'auto', or 'manual'.
- **`GET /get_system_state`**: Return whether the system is on.
- **`POST /turn_on`**: Turn on the system. Does not start auto mode automatically.
- **`POST /turn_off`**: Turn off the system. Stops auto mode and turns off all lights.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
```

You can copy this content into your `README.md` file. If you need any further adjustments or have more questions, feel free to ask!
