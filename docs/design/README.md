# anywharrow Design Documentation

## System Architecture

The anywharrow device consists of three main subsystems:

### 1. Mechanical System
- **2-DOF Gimbal**: Two servo-controlled axes for azimuth and elevation
- **Arrow Mount**: Secure mounting for the pointing arrow
- **Base Structure**: Stable platform for the entire assembly

### 2. Electrical System
- **Microcontroller**: Raspberry Pi 4B for processing and control
- **Servo Motors**: 2x MG996R or SG90 servos for gimbal control
- **IMU Sensor**: MPU-6050 or BNO055 for orientation sensing
- **Display**: 0.96" OLED for target information
- **Power Supply**: 5V 3A wall adapter

### 3. Software System
- **Positioning Module**: Astronomical calculations using Skyfield
- **Kinematics Module**: Gimbal control and smooth movement
- **Hardware Interface**: Servo, IMU, and display control
- **Configuration**: Target database and device settings

## Design Considerations

### Accuracy Requirements
- **Software**: High precision astronomical calculations
- **Hardware**: Moderate precision for cost-effective prototype
- **Calibration**: IMU-based orientation correction

### Movement Characteristics
- **Smooth Transitions**: Configurable movement duration
- **Range Limits**: Azimuth 0-360°, Elevation -90° to +90°
- **Speed Control**: Variable movement speed for different targets

### Target Types
- **Celestial Objects**: Planets, stars, satellites
- **Earth Locations**: Cities, landmarks, coordinates
- **Deep Space**: Galaxies, nebulae, other astronomical objects

## Future Enhancements
- **Larger Display**: Scale up for bigger installations
- **Higher Accuracy**: Precision servos and calibration
- **Network Features**: Remote control and monitoring
- **Additional Sensors**: Weather, light, or other environmental data
