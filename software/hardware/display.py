"""
LED display controller for showing target information
"""

import logging
from typing import Optional

logger = logging.getLogger(__name__)

class DisplayController:
    """Controls the LED display for showing target information"""
    
    def __init__(self):
        self.display = None
        self.current_text = ""
        
    def initialize(self):
        """Initialize the display"""
        try:
            logger.info("Initializing display...")
            # Initialize display hardware (placeholder)
            # self.display = SSD1306_I2C(128, 64, I2C(0))
            logger.info("Display initialized")
            return True
        except Exception as e:
            logger.error(f"Failed to initialize display: {e}")
            return False
    
    def show_target(self, name: str, description: str = ""):
        """
        Display target information on the screen
        
        Args:
            name: Target name to display
            description: Optional description
        """
        try:
            # Format the display text
            display_text = f"{name}\n{description}" if description else name
            
            logger.info(f"Displaying: {display_text}")
            
            # Update display (placeholder)
            # self.display.fill(0)  # Clear screen
            # self.display.text(display_text, 0, 0, 1)
            # self.display.show()
            
            self.current_text = display_text
            
        except Exception as e:
            logger.error(f"Failed to update display: {e}")
    
    def show_status(self, status: str):
        """Display system status"""
        self.show_target("Status", status)
    
    def clear(self):
        """Clear the display"""
        try:
            # self.display.fill(0)
            # self.display.show()
            self.current_text = ""
            logger.info("Display cleared")
        except Exception as e:
            logger.error(f"Failed to clear display: {e}")
    
    def cleanup(self):
        """Clean up display resources"""
        logger.info("Cleaning up display...")
        self.clear()
