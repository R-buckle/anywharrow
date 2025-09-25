# anywharrow Build Instructions

## Prerequisites

### Hardware Components
- Raspberry Pi 4B (4GB recommended)
- 2x MG996R servos (or SG90 for lighter loads)
- MPU-6050 IMU sensor
- 0.96" OLED display (128x64)
- 5V 3A wall adapter
- Breadboard and jumper wires
- 3D printed or laser-cut gimbal frame

### Software Requirements
- Raspberry Pi OS (latest)
- Python 3.8+
- Git

## Installation Steps

### 1. System Setup
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python dependencies
sudo apt install python3-pip python3-venv

# Install additional packages
sudo apt install git i2c-tools
```

### 2. Enable Hardware Interfaces
```bash
# Enable I2C and SPI
sudo raspi-config
# Navigate to: Interfacing Options > I2C > Enable
# Navigate to: Interfacing Options > SPI > Enable
```

### 3. Clone and Setup Project
```bash
# Clone repository
git clone <repository-url>
cd anywharrow

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

### 4. Hardware Assembly

#### Gimbal Assembly
1. Print or cut gimbal frame parts
2. Install bearings for smooth rotation
3. Mount servos in gimbal frame
4. Attach arrow to elevation servo

#### Electronics Wiring
1. Connect servos to GPIO pins (18, 19)
2. Connect IMU to I2C bus
3. Connect display to I2C bus
4. Connect power supply

#### Final Assembly
1. Mount electronics in base
2. Install gimbal assembly
3. Connect all wiring
4. Secure with enclosure

### 5. Configuration
```bash
# Edit device location in config/settings.json
# Add your latitude and longitude

# Test hardware
python software/test_hardware.py

# Run the main program
python software/main.py
```

## Testing and Calibration

### Hardware Testing
1. **Servo Test**: Verify servo movement range
2. **IMU Test**: Check orientation readings
3. **Display Test**: Confirm text display
4. **Power Test**: Ensure stable power supply

### Software Testing
1. **Positioning**: Test astronomical calculations
2. **Movement**: Verify smooth gimbal control
3. **Targets**: Test with known locations
4. **Timing**: Check update intervals

### Calibration Procedure
1. **IMU Calibration**: Level device and calibrate sensors
2. **Servo Calibration**: Set center positions
3. **Orientation Calibration**: Align with true north
4. **Target Verification**: Test with known celestial objects

## Troubleshooting

### Common Issues
- **Servo Jitter**: Check power supply and wiring
- **IMU Drift**: Recalibrate sensors
- **Display Issues**: Check I2C connections
- **Position Errors**: Verify device location settings

### Debug Mode
```bash
# Run with debug logging
python software/main.py --debug

# Test individual components
python software/test_astronomy.py
python software/test_gimbal.py
```

## Maintenance

### Regular Tasks
- **Clean Servos**: Remove dust and debris
- **Check Connections**: Verify all wiring
- **Update Software**: Keep dependencies current
- **Calibrate IMU**: Periodic sensor calibration

### Performance Monitoring
- **Log Analysis**: Review system logs
- **Position Accuracy**: Test pointing precision
- **Movement Smoothness**: Check for jerky motion
- **Display Readability**: Ensure clear text display
