#!/usr/bin/env python3
"""
anywharrow - Main control program
A desktop device that points to any location in the universe
"""

import time
import json
import logging
from pathlib import Path

from positioning.astronomy import AstronomyCalculator
from kinematics.gimbal_control import GimbalController
from hardware.display import DisplayController
from hardware.imu import IMUController
from utils.config import ConfigManager

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class AnywharrowController:
    """Main controller for the anywharrow device"""
    
    def __init__(self, config_path="config"):
        self.config = ConfigManager(config_path)
        self.astronomy = AstronomyCalculator()
        self.gimbal = GimbalController()
        self.display = DisplayController()
        self.imu = IMUController()
        
        self.current_target_index = 0
        self.targets = self.config.get_targets()
        
    def initialize(self):
        """Initialize all hardware components"""
        logger.info("Initializing anywharrow...")
        
        try:
            self.gimbal.initialize()
            self.display.initialize()
            self.imu.initialize()
            logger.info("Hardware initialization complete")
            return True
        except Exception as e:
            logger.error(f"Hardware initialization failed: {e}")
            return False
    
    def get_next_target(self):
        """Get the next target in the rotation"""
        target = self.targets[self.current_target_index]
        self.current_target_index = (self.current_target_index + 1) % len(self.targets)
        return target
    
    def calculate_target_position(self, target):
        """Calculate the position of a target relative to the device"""
        if target["type"] == "earth_location":
            return self.astronomy.calculate_earth_location_azimuth_elevation(
                target["latitude"], target["longitude"]
            )
        elif target["type"] in ["planet", "star", "satellite", "deep_space"]:
            return self.astronomy.calculate_celestial_azimuth_elevation(target["name"])
        else:
            logger.warning(f"Unknown target type: {target['type']}")
            return None, None
    
    def move_to_target(self, target):
        """Move the gimbal to point at the specified target"""
        azimuth, elevation = self.calculate_target_position(target)
        
        if azimuth is None or elevation is None:
            logger.error(f"Could not calculate position for target: {target['name']}")
            return False
        
        logger.info(f"Moving to {target['name']}: Az={azimuth:.1f}°, El={elevation:.1f}°")
        
        # Move gimbal smoothly to target position
        success = self.gimbal.move_to_position(azimuth, elevation)
        
        if success:
            # Update display with target information
            self.display.show_target(target["name"], target.get("description", ""))
            logger.info(f"Successfully pointed to {target['name']}")
        
        return success
    
    def run(self):
        """Main control loop"""
        logger.info("Starting anywharrow control loop...")
        
        if not self.initialize():
            logger.error("Failed to initialize hardware. Exiting.")
            return
        
        try:
            while True:
                # Get next target
                target = self.get_next_target()
                logger.info(f"Targeting: {target['name']}")
                
                # Move to target
                if self.move_to_target(target):
                    # Wait for the specified interval
                    interval = self.config.get_nested_setting("behavior", "update_interval_seconds", default=60)
                    time.sleep(interval)
                else:
                    # If movement failed, wait a bit and try next target
                    time.sleep(5)
                    
        except KeyboardInterrupt:
            logger.info("Shutting down anywharrow...")
            self.cleanup()
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            self.cleanup()
    
    def cleanup(self):
        """Clean up resources"""
        self.gimbal.cleanup()
        self.display.cleanup()
        logger.info("Cleanup complete")

if __name__ == "__main__":
    controller = AnywharrowController()
    controller.run()
