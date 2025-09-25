#!/usr/bin/env python3
"""
Example usage of the improved ConfigManager API
Demonstrates how to use the configuration system without needing to know indices
"""

from utils.config import ConfigManager

def main():
    # Initialize configuration
    config = ConfigManager("config")
    
    print("=== anywharrow Configuration Examples ===\n")
    
    # 1. List all available targets (no index needed!)
    print("Available targets:")
    target_names = config.list_target_names()
    for i, name in enumerate(target_names):
        print(f"  {i}: {name}")
    print()
    
    # 2. Get a specific target by name (much easier than index!)
    mars_target = config.get_target_by_name("Mars")
    if mars_target:
        print(f"Mars target: {mars_target}")
    print()
    
    # 3. Get target by index (if you really need it)
    first_target = config.get_target(0)
    if first_target:
        print(f"First target: {first_target['name']}")
    print()
    
    # 4. Get nested settings easily
    update_interval = config.get_nested_setting("behavior", "update_interval_seconds", default=60)
    print(f"Update interval: {update_interval} seconds")
    
    smooth_transition = config.get_nested_setting("behavior", "smooth_transition", default=True)
    print(f"Smooth transitions: {smooth_transition}")
    
    # 5. Get device location
    device_lat = config.get_nested_setting("device", "location", "latitude", default=0.0)
    device_lon = config.get_nested_setting("device", "location", "longitude", default=0.0)
    print(f"Device location: {device_lat}, {device_lon}")
    
    # 6. Get hardware settings
    azimuth_pin = config.get_nested_setting("hardware", "servo_azimuth_pin", default=18)
    elevation_pin = config.get_nested_setting("hardware", "servo_elevation_pin", default=19)
    print(f"Servo pins: Azimuth={azimuth_pin}, Elevation={elevation_pin}")
    
    print("\n=== Usage Examples ===")
    print("# Get target by name (recommended):")
    print("target = config.get_target_by_name('Mars')")
    print()
    print("# Get nested settings:")
    print("interval = config.get_nested_setting('behavior', 'update_interval_seconds')")
    print()
    print("# List all targets:")
    print("names = config.list_target_names()")
    print()
    print("# Find target index if needed:")
    print("index = config.get_target_index('Jupiter')")

if __name__ == "__main__":
    main()
