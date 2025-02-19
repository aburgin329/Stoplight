# Stoplight Control System – Hardware and Software Support Documentation

## Overview

The Stoplight Control System is built on a **Raspberry Pi 5** and is designed to control a physical stoplight (LEDs) via GPIO. This document outlines the **hardware components, wiring, troubleshooting steps, and escalation procedures**.

---

## Hardware Components

- **Raspberry Pi 5** – The core of the system.
- **Stoplight LEDs** – Three LEDs representing:
  - **Green LED** – "Go"
  - **Yellow LED** – "Caution"
  - **Red LED** – "Stop"
- **Resistors** – **75Ω** to limit current and protect the LEDs.
- **Breadboard & Jumper Wires** – Used for circuit connections.
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
2. **Verify Resistor Value:** Use multimeter  to verify resistor is **75Ω** 
3. **Test LED Individually:** Use a **multimeter** or a simple test circuit.
4. **Check Connections:** Ensure the jumper wires are connected to the proper GPIO pins. Ensure jumper wires and breadboard connections are secure.
    ,--------------------------------.
| oooooooooooooooooooo J8 PoE +====
| 1ooooooooooooooooooo   12   | USB
|  Wi                    oo   +====
|  Fi  Pi Model 5B V1.3          |
| |D     ,---.           1o   +====
| |S     |SoC|            RUN | USB
| |I     `---'                +====
| |0               C|            |
|                  S|       +======
|                  I| |A|   |   Net
| pwr      |HDMI|  0| |u|   +======
`-| |------|    |-----|x|--------'

   3V3  (1) (2)  5V    
 GPIO2  (3) (4)  5V    
 GPIO3  (5) (6)  GND   
 GPIO4  (7) (8)  GPIO14
   GND  (9) (10) GPIO15
GPIO17 (11) (12) GPIO18
GPIO27 (13) (14) GND   
GPIO22 (15) (16) GPIO23
   3V3 (17) (18) GPIO24
GPIO10 (19) (20) GND   
 GPIO9 (21) (22) GPIO25
GPIO11 (23) (24) GPIO8 
   GND (25) (26) GPIO7 
 GPIO0 (27) (28) GPIO1 
 GPIO5 (29) (30) GND   
 GPIO6 (31) (32) GPIO12
GPIO13 (33) (34) GND   
GPIO19 (35) (36) GPIO16
GPIO26 (37) (38) GPIO20
   GND (39) (40) GPIO21

---

### 2. Hardware Damage or Component Failure

**Symptoms:**
- One LED consistently fails to light.

**Troubleshooting Steps:**
1. **Swap Components:** Test with a known-working LED or resistor.
2. **Inspect Circuit:** Look for loose connections or damage.
3. **Review Schematics:** Verify wiring against the design.

---

### 3. Hardware Damage or Component Failure

**Symptoms:**
- One LED consistently fails to light.

**Troubleshooting Steps:**
1. **Swap Components:** Test with a known-working LED or resistor.
2. **Inspect Circuit:** Look for loose connections or damage.
3. **Review Schematics:** Verify wiring against the design.

---



