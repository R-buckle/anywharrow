# anywharrow

A desktop device that points to any location in the universe - inspired by NASA JPL's "Line of Sight" installation.

## 🎯 Project Overview

The anywharrow is a 2-DOF gimbal-mounted arrow that automatically points to various locations in space and on Earth, displaying the target name on an LED screen. The device cycles through a predefined list of targets every minute, creating a mesmerizing display of cosmic awareness.

### Key Features
- **🌍 Universal Coverage**: Points to planets, stars, cities, and deep space objects
- **🔄 Automatic Operation**: Cycles through targets every minute
- **📱 Real-time Updates**: Uses current astronomical data (no API fees)
- **🎨 Smooth Movement**: Elegant transitions between targets
- **🖥️ Desktop Size**: Compact 6cm display design
- **⚡ Open Source**: Fully documented and customizable

## 🚀 Quick Start

### Prerequisites
- Raspberry Pi 4B (recommended)
- Python 3.8+
- Basic electronics components (see [Build Guide](docs/build/README.md))

### Installation
```bash
# Clone the repository
git clone <repository-url>
cd anywharrow

# Install dependencies
pip install -r requirements.txt

# Configure your device location
# Edit config/settings.json with your coordinates

# Run the software
python software/main.py
```

## 📁 Project Structure

```
anywharrow/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── config/                     # Configuration files
│   ├── targets.json            # Target locations database
│   └── settings.json           # Device settings
├── software/                   # Python software
│   ├── main.py                 # Main control program
│   ├── positioning/            # Astronomical calculations
│   ├── kinematics/              # Gimbal control
│   ├── hardware/              # Hardware interfaces
│   └── utils/                 # Utilities
├── mechanical/                 # Mechanical design files
├── electrical/                 # Circuit diagrams and wiring
├── data/                      # Ephemeris and location data
└── docs/                      # Documentation
    ├── design/                # Technical specifications
    ├── build/                 # Assembly instructions
    ├── user/                  # User manual
    └── project_management.md  # Development roadmap
```

## 🛠️ Hardware Requirements

### Core Components
- **Microcontroller**: Raspberry Pi 4B (4GB recommended)
- **Gimbal**: 2-DOF servo-controlled gimbal
- **Servos**: 2x MG996R or SG90 servos
- **IMU**: MPU-6050 or BNO055 for orientation sensing
- **Display**: 0.96" OLED (128x64) for target information
- **Power**: 5V 3A wall adapter

### Optional Enhancements
- **Larger Display**: Scale up for bigger installations
- **Precision Servos**: Higher accuracy pointing
- **Network Features**: Remote control and monitoring
- **Additional Sensors**: Weather, light, environmental data

## 📚 Documentation

- **[Design Documentation](docs/design/README.md)**: Technical specifications and architecture
- **[Build Instructions](docs/build/README.md)**: Complete assembly guide
- **[User Manual](docs/user/README.md)**: Operation and troubleshooting
- **[Project Management](docs/project_management.md)**: Development roadmap and timeline

## 🎮 Usage

### Automatic Operation
The device operates automatically, cycling through targets every minute. No user intervention required.

### Target Types
- **Celestial Objects**: Mars, Jupiter, International Space Station, Vega
- **Earth Locations**: New York City, Tokyo, Mount Everest
- **Deep Space**: Andromeda Galaxy, nebulae, other astronomical objects

### Configuration
- **Targets**: Edit `config/targets.json` to add/modify targets
- **Settings**: Adjust behavior in `config/settings.json`
- **Location**: Set device coordinates for accurate pointing

## 🔧 Development

### Software Architecture
- **Modular Design**: Separate modules for positioning, kinematics, hardware control
- **Free Data Sources**: Uses Skyfield with JPL ephemeris data (no API fees)
- **Smooth Movement**: Configurable transition timing between targets
- **IMU Integration**: Orientation sensing for calibration and correction

### Key Technologies
- **Python 3.8+**: Core programming language
- **Skyfield**: Astronomical calculations and ephemeris data
- **AstroPy**: Coordinate transformations and time handling
- **NumPy/SciPy**: Mathematical operations for kinematics
- **Control Systems**: Smooth gimbal movement algorithms

## 🎯 Project Status

**Current Phase**: Software Foundation
**Progress**: Project structure and initial code complete
**Next Milestone**: Working software simulation
**Timeline**: 6-8 months (part-time development)

## 🤝 Contributing

This project is open source! Contributions welcome:
- **Issues**: Report bugs and feature requests
- **Pull Requests**: Submit improvements
- **Documentation**: Help improve guides and examples
- **Hardware**: Share mechanical designs and improvements

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **NASA JPL**: Inspiration from the "Line of Sight" installation
- **Skyfield**: Astronomical calculations by Brandon Rhodes
- **AstroPy**: Astronomical computing in Python
- **Open Source Community**: Libraries and tools that make this possible

---

**anywharrow** - Pointing to the universe, one target at a time. 🌌