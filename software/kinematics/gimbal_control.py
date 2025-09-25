"""
2-DOF gimbal control with kinematics calculations
"""

import time
import math
import logging
from typing import Tuple, Optional

logger = logging.getLogger(__name__)

class GimbalController:
    """Controls the 2-DOF gimbal mechanism"""
    
    def __init__(self):
        self.azimuth_angle = 0.0
        self.elevation_angle = 0.0
        self.azimuth_servo = None
        self.elevation_servo = None
        
    def initialize(self):
        """Initialize servo connections"""
        try:
            # Initialize servos (placeholder - actual implementation depends on hardware)
            logger.info("Initializing gimbal servos...")
            # self.azimuth_servo = Servo(pin=18)
            # self.elevation_servo = Servo(pin=19)
            logger.info("Gimbal servos initialized")
            return True
        except Exception as e:
            logger.error(f"Failed to initialize gimbal: {e}")
            return False
    
    def move_to_position(self, azimuth: float, elevation: float, 
                        smooth: bool = True, duration: float = 2.0) -> bool:
        """
        Move gimbal to specified azimuth and elevation
        
        Args:
            azimuth: Target azimuth in degrees (0-360)
            elevation: Target elevation in degrees (-90 to 90)
            smooth: Whether to move smoothly or instantly
            duration: Duration of smooth movement in seconds
            
        Returns:
            bool: Success status
        """
        try:
            # Clamp angles to valid ranges
            azimuth = self._clamp_azimuth(azimuth)
            elevation = self._clamp_elevation(elevation)
            
            logger.info(f"Moving gimbal to Az={azimuth:.1f}°, El={elevation:.1f}°")
            
            if smooth:
                self._smooth_move(azimuth, elevation, duration)
            else:
                self._instant_move(azimuth, elevation)
            
            # Update internal state
            self.azimuth_angle = azimuth
            self.elevation_angle = elevation
            
            return True
            
        except Exception as e:
            logger.error(f"Failed to move gimbal: {e}")
            return False
    
    def _clamp_azimuth(self, angle: float) -> float:
        """Clamp azimuth angle to 0-360 degrees"""
        return angle % 360.0
    
    def _clamp_elevation(self, angle: float) -> float:
        """Clamp elevation angle to -90 to 90 degrees"""
        return max(-90.0, min(90.0, angle))
    
    def _smooth_move(self, target_az: float, target_el: float, duration: float):
        """Move smoothly to target position"""
        start_az = self.azimuth_angle
        start_el = self.elevation_angle
        
        steps = int(duration * 50)  # 50 Hz update rate
        step_time = duration / steps
        
        for i in range(steps + 1):
            progress = i / steps
            
            # Linear interpolation
            current_az = start_az + (target_az - start_az) * progress
            current_el = start_el + (target_el - start_el) * progress
            
            # Apply to servos
            self._set_servo_positions(current_az, current_el)
            time.sleep(step_time)
    
    def _instant_move(self, azimuth: float, elevation: float):
        """Move instantly to target position"""
        self._set_servo_positions(azimuth, elevation)
    
    def _set_servo_positions(self, azimuth: float, elevation: float):
        """Set servo positions (hardware-specific implementation)"""
        # Convert angles to servo pulse widths
        # This is a placeholder - actual implementation depends on servo type
        
        # Typical servo range: 1ms to 2ms pulse width for 0-180 degrees
        # Adjust based on your specific servo specifications
        
        azimuth_pulse = self._angle_to_pulse(azimuth)
        elevation_pulse = self._angle_to_pulse(elevation)
        
        # Apply to servos (placeholder)
        logger.debug(f"Setting servos: Az={azimuth_pulse:.1f}ms, El={elevation_pulse:.1f}ms")
        
        # TODO: Implement actual servo control
        # self.azimuth_servo.set_pulse_width(azimuth_pulse)
        # self.elevation_servo.set_pulse_width(elevation_pulse)
    
    def _angle_to_pulse(self, angle: float) -> float:
        """Convert angle to servo pulse width in milliseconds"""
        # Convert to 0-180 range for servo
        servo_angle = (angle + 90) % 180
        
        # Convert to pulse width (1ms to 2ms for 0-180 degrees)
        pulse_width = 1.0 + (servo_angle / 180.0)
        
        return pulse_width
    
    def get_current_position(self) -> Tuple[float, float]:
        """Get current gimbal position"""
        return self.azimuth_angle, self.elevation_angle
    
    def cleanup(self):
        """Clean up resources"""
        logger.info("Cleaning up gimbal controller...")
        # Stop servos in center position
        self.move_to_position(0, 0, smooth=False)
