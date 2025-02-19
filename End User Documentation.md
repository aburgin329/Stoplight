# Stoplight Control System – End-User Documentation

## 1. Overview

The Stoplight Control System is a web-based interface that lets you control a physical stoplight (LEDs) connected to a Raspberry Pi. Using this system you can:

- **Turn the System On/Off:** Power the stoplight system on and off.
- **Manual Mode:** Manually change the light (cycle through Green, Yellow, Red).
- **Automatic Mode:** Start and stop an automatic light cycle.
- **Settings:** Adjust the time durations for each light (Green, Yellow, and Red).

The system is controlled through your web browser, and all changes you make are sent to the Raspberry Pi, which then controls the actual hardware.

---

## 2. Getting Started

### 2.1 Accessing the Interface

1. **Connect to the Network:**  
   Ensure your computer or mobile device is on the same network as the Raspberry Pi.

2. **Open a Web Browser:**  
   Launch your preferred web browser (e.g., Chrome, Firefox, Edge).

3. **Enter the URL:**  
   Type the Raspberry Pi’s IP address followed by `:5000` in the address bar. For example:  192.168.1.2:5000


The main page titled **"Stoplight Control"** will load.

---

### 2.2 Understanding the Layout

- **Header:**  
A black bar at the top always displays the title **"Stoplight Control."**

- **Stoplight Display:**  
In the center of the page, you’ll see a representation of the stoplight with three circles (for Green, Yellow, and Red).

- **Power Button:**  
Directly under the stoplight is the power button (displayed as a power icon). This button is used to turn off the system.

- **Control Sections:**  
Below the stoplight and power button, you’ll find:

- **Automatic Controls:**  
 Buttons to **Start Auto, Stop Auto**, and access **Settings**.

- **Manual Controls:**  
 A button for **Manual Cycle** (to manually step through the light sequence).

- **Off pop up:**  
 When the system is off, an overlay pop up appears with the message:  
 > "System is powered off. Press 'Turn On' to power on."  
 In this state, only the **"Turn On"** button is active.

---

## 3. Operating the System

### 3.1 Turning the System On

- When the system is off:
- An overlay pop up will appear.
- Click the **"Turn On"** button in the pop up.
- A message **"Powering on…"** will briefly display while the system turns on.
- The pop up will close, and the main controls (stoplight, power button, and control sections) will be visible.

---

### 3.2 Turning the System Off

- When the system is on:
- The power button appears directly below the stoplight.
- Click the power button (**⏻**).
- A confirmation pop up will appear asking,  
 > "Are you sure you want to power off the system?"  
- Click **"Yes"** to power off. A **"Powering off…"** message will briefly display, then the system will turn off and the off pop up will appear.

---

### 3.3 Manual Mode

- **Manual Cycle:**
- When the system is on and auto mode is off, click the **"Manual Cycle"** button to change the light to the next state:  
 **Green → Yellow → Red**.

---

### 3.4 Automatic Mode

- **Starting Auto Mode:**
- Click the **"Start Auto"** button.
- The system will begin cycling the stoplight automatically using preset durations.
- In this mode, manual controls are disabled.

- **Stopping Auto Mode:**
- Click the **"Stop Auto"** button.
- A confirmation pop up will appear. Click **"Yes"** to stop auto mode.
- Once stopped, manual controls become available again.

---

### 3.5 Adjusting Settings

- **Accessing Settings:**
- Click the **"Settings"** button in the **Automatic Controls** section.
- A confirmation pop up appears warning that modifying settings will stop auto mode. Click **"Yes"** to continue.

- **Updating Durations:**
- In the **Settings pop up**, enter new durations (in seconds) for the **Green, Yellow, and Red** lights.
- Click **"Save"** to update the settings.
- A confirmation message will appear indicating that the settings were updated successfully.

---

## 4. Troubleshooting FAQs

### Q1: The Stoplight LEDs are not changing.
- Ensure that your Raspberry Pi is properly connected to the stoplight hardware.
- Verify that the system is turned on via the **"Turn On"** pop up.
- Refresh the web page or restart the system if necessary.

### Q2: I don’t see the control buttons.
- Make sure you are accessing the correct **IP address and port** (default port is **5000**).
- Confirm that the system is powered on. If off, the off pop up will be displayed.

### Q3: Auto mode is not stopping.
- Ensure that you are clicking **"Stop Auto"** and confirming the action.
- Check the system logs if you have access to them for any errors.

### Q4: The settings are not updating.
- Verify that you have entered **valid numerical values** in the settings fields.
- If issues persist, restart the system and try updating settings again.

---


