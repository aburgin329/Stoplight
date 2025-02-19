# Stoplight Control System – Hardware Support Documentation

## Overview

The Stoplight Control System is built on a **Raspberry Pi 5** and is designed to control a physical stoplight (LEDs) via GPIO. This document outlines the **hardware components, wiring, troubleshooting steps, and escalation procedures**.

---

## Hardware Components

- **Raspberry Pi 5** – The core of the system.
- **Stoplight LEDs** – Three LEDs representing:
  - **Green LED** – "Go"
  - **Yellow LED** – "Caution"
  - **Red LED** – "Stop"
- **Resistors** – Typically **220Ω to 330Ω** to limit current and protect the LEDs.
- **Breadboard & Jumper Wires** – Used for prototyping circuit connections.
- **GPIO Interface Library** – The Flask application uses **gpiod** for GPIO control.

---

## Wiring Diagram & File Structure

### Wiring Diagram (Simplified)

```
   +3.3V (or 5V)
       │
    [Resistor]
       │
     LED (Red/Yellow/Green)
       │
     GPIO Pin
       │
      GND
```

### GPIO Pin Assignments
- **Red LED:** GPIO **17**
- **Yellow LED:** GPIO **27**
- **Green LED:** GPIO **22**

### File Structure
```
/home/pi/stoplightv2
├── stoplightv2.py      # Main Flask application
└── templates
    └── stoplightv2.html   # Web interface
```

---

## Common Hardware Issues & Troubleshooting

### 1. LED Not Lighting Up

**Symptoms:**
- LED remains off when expected to be lit.

**Troubleshooting Steps:**
1. **Check Wiring:** Ensure the LED, resistor, and ground connections are correct.
2. **Verify Resistor Value:** Should be **220Ω–330Ω**.
3. **Test LED Individually:** Use a **multimeter** or a simple test circuit.
4. **Check Connections:** Ensure jumper wires and breadboard connections are secure.

---

### 2. No Response from GPIO

**Symptoms:**
- Flask application does not change LED state.

**Troubleshooting Steps:**
1. **Verify GPIO Access:** Ensure the Pi’s GPIO is enabled.
2. **Check Permissions:** Ensure the Flask application user has access to GPIO.
3. **Check for Conflicting Services:** Ensure no other process (e.g., `pigpiod`) is interfering with **gpiod**.
4. **Check Logs:** Review system logs for GPIO errors.

---

### 3. Hardware Damage or Component Failure

**Symptoms:**
- One LED consistently fails to light.

**Troubleshooting Steps:**
1. **Swap Components:** Test with a known-working LED or resistor.
2. **Inspect Circuit:** Look for loose connections or damage.
3. **Review Schematics:** Verify wiring against the design.

---

## Escalation Procedures

If the issue cannot be resolved at **Tier 1 Support**, escalate with:

- **Detailed Description** – Identify the issue (e.g., LED not lighting, no GPIO response).
- **Troubleshooting Steps Taken** – List all attempted fixes.
- **Wiring Diagrams/Photos** – Provide a visual reference.
- **Logs/Output** – Include any relevant error messages.
- **Environment Details** – Raspberry Pi model, OS version, and any modifications.

---

## Contact Information

For unresolved issues, contact **Tier 2 Support** via the designated support channel (e.g., email or ticket system).

---

This guide is intended as a **quick-reference manual** for hardware support. Feel free to modify or expand it as needed.

