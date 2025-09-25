# anywharrow User Manual

## Overview

The anywharrow is a desktop device that automatically points to various locations in the universe. It displays the target name on a small screen and physically orients itself to point in the direction of the target.

## Features

- **Automatic Operation**: Cycles through targets every minute
- **Universe Coverage**: Points to planets, stars, cities, and more
- **Smooth Movement**: Elegant transitions between targets
- **Real-time Updates**: Uses current astronomical data
- **Desktop Size**: Compact 6cm display design

## Getting Started

### First Time Setup
1. **Power On**: Connect the wall adapter
2. **Wait for Initialization**: Device will calibrate sensors
3. **First Movement**: Arrow will point to first target
4. **Display**: Target name appears on screen

### Understanding the Display
- **Target Name**: Current location being pointed to
- **Description**: Additional information about the target
- **Status Indicators**: System status and errors

## Target Types

### Celestial Objects
- **Planets**: Mars, Jupiter, Saturn, Venus, Mercury
- **Stars**: Bright stars like Vega, Sirius
- **Satellites**: International Space Station
- **Deep Space**: Galaxies, nebulae

### Earth Locations
- **Cities**: New York, Tokyo, London
- **Landmarks**: Mount Everest, Grand Canyon
- **Coordinates**: Any specific location on Earth

## Operation

### Automatic Mode
The device operates automatically, cycling through targets every minute. No user intervention required.

### Target Information
Each target displays:
- **Name**: Primary identifier
- **Type**: Planet, city, star, etc.
- **Description**: Additional context

### Movement Behavior
- **Smooth Transitions**: 5-second movement between targets
- **Range Limits**: Points within physical constraints
- **Calibration**: Self-correcting orientation

## Configuration

### Adding Targets
Targets are managed through configuration files:
- **Location**: `config/targets.json`
- **Format**: JSON with target specifications
- **Types**: Celestial, Earth locations, custom coordinates

### Settings
Device settings in `config/settings.json`:
- **Update Interval**: Time between targets (default: 60 seconds)
- **Movement Speed**: Transition duration
- **Display Options**: Text size and format

## Troubleshooting

### Common Issues

#### Device Not Moving
- **Check Power**: Ensure wall adapter is connected
- **Servo Issues**: Verify servo connections
- **Software Error**: Check system logs

#### Incorrect Pointing
- **Location Setting**: Verify device coordinates
- **Calibration**: Recalibrate IMU sensors
- **Target Data**: Check target configuration

#### Display Problems
- **Screen Blank**: Check I2C connections
- **Text Unreadable**: Adjust display settings
- **No Updates**: Verify target data

### Error Messages
- **"Hardware Error"**: Check physical connections
- **"Position Error"**: Astronomical calculation failed
- **"Target Error"**: Invalid target configuration

## Maintenance

### Regular Care
- **Dust Removal**: Clean device surface
- **Connection Check**: Verify all wiring
- **Software Updates**: Keep system current

### Calibration
- **IMU Calibration**: Level device and run calibration
- **Servo Calibration**: Center servos for accurate movement
- **Orientation**: Align with true north

### Performance
- **Smooth Movement**: Check for jerky motion
- **Accuracy**: Test with known locations
- **Timing**: Verify update intervals

## Technical Specifications

### Hardware
- **Display**: 6cm LED screen
- **Movement**: 2-DOF gimbal with servos
- **Sensors**: IMU for orientation
- **Power**: 5V 3A wall adapter

### Software
- **Platform**: Raspberry Pi 4B
- **Language**: Python 3.8+
- **Libraries**: Skyfield, AstroPy, NumPy
- **Data**: Free JPL ephemeris data

### Performance
- **Accuracy**: ±5° (hardware dependent)
- **Update Rate**: 1 minute intervals
- **Movement Speed**: 5-second transitions
- **Range**: Full sky coverage

## Support

### Documentation
- **Design Docs**: Technical specifications
- **Build Guide**: Assembly instructions
- **Code Repository**: Source code and examples

### Community
- **Issues**: Report problems and bugs
- **Contributions**: Share improvements
- **Discussions**: Community support

## License

This project is open source. See LICENSE file for details.
