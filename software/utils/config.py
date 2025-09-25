"""
Configuration management for the anywharrow device
"""

import json
import logging
from pathlib import Path
from typing import Dict, List, Any, Optional

logger = logging.getLogger(__name__)

class ConfigManager:
    """Manages device configuration and target data"""
    
    def __init__(self, config_path: str = "config"):
        self.config_path = Path(config_path)
        self.targets = []
        self.settings = {}
        
        self._load_config()
    
    def _load_config(self):
        """Load configuration from files"""
        try:
            # Load targets
            targets_file = self.config_path / "targets.json"
            if targets_file.exists():
                with open(targets_file, 'r') as f:
                    data = json.load(f)
                    self.targets = data.get("targets", [])
            
            # Load device settings
            settings_file = self.config_path / "settings.json"
            if settings_file.exists():
                with open(settings_file, 'r') as f:
                    self.settings.update(json.load(f))
            
            logger.info(f"Loaded {len(self.targets)} targets from configuration")
            
        except Exception as e:
            logger.error(f"Failed to load configuration: {e}")
    
    def get_targets(self) -> List[Dict[str, Any]]:
        """Get list of targets"""
        return self.targets
    
    def get_target(self, index: int) -> Optional[Dict[str, Any]]:
        """Get specific target by index"""
        if 0 <= index < len(self.targets):
            return self.targets[index]
        return None
    
    def get_target_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        """Get target by name (case-insensitive)"""
        for target in self.targets:
            if target.get("name", "").lower() == name.lower():
                return target
        return None
    
    def get_target_index(self, name: str) -> Optional[int]:
        """Get the index of a target by name"""
        for i, target in enumerate(self.targets):
            if target.get("name", "").lower() == name.lower():
                return i
        return None
    
    def list_target_names(self) -> List[str]:
        """Get list of all target names"""
        return [target.get("name", "") for target in self.targets]
    
    def get_setting(self, key: str, default: Any = None) -> Any:
        """Get a configuration setting"""
        return self.settings.get(key, default)
    
    def get_nested_setting(self, *keys: str, default: Any = None) -> Any:
        """Get a nested setting using dot notation or multiple keys"""
        current = self.settings
        for key in keys:
            if isinstance(current, dict) and key in current:
                current = current[key]
            else:
                return default
        return current
    
    def update_setting(self, key: str, value: Any):
        """Update a configuration setting"""
        self.settings[key] = value
    
    def add_target(self, target: Dict[str, Any]):
        """Add a new target"""
        self.targets.append(target)
        self._save_targets()
    
    def remove_target(self, index: int):
        """Remove a target by index"""
        if 0 <= index < len(self.targets):
            del self.targets[index]
            self._save_targets()
    
    def _save_targets(self):
        """Save targets to file"""
        try:
            targets_file = self.config_path / "targets.json"
            data = {"targets": self.targets}
            
            with open(targets_file, 'w') as f:
                json.dump(data, f, indent=2)
                
            logger.info("Targets saved to configuration")
            
        except Exception as e:
            logger.error(f"Failed to save targets: {e}")
