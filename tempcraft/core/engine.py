"""Core conversion engine responsible for managing plugins and executing conversions."""
from typing import Dict, List, Type
from tempcraft.plugins.base_plugin import BaseConversionPlugin
from tempcraft.plugins.temperature import TemperaturePlugin
from tempcraft.core.exceptions import PluginError, ConversionError
from tempcraft.services.logging import logger

class ConversionEngine:
    """Manages conversion plugins and delegates conversion tasks."""
    
    def __init__(self):
        self._plugins: Dict[str, BaseConversionPlugin] = {}
        self._load_plugins()
        
    def _load_plugins(self):
        """Discovers and instantiates available plugins."""
        try:
            # In a fully dynamic system, we'd use importlib to scan the plugins directory.
            # For simplicity, we register known plugins here.
            plugins_to_load = [TemperaturePlugin]
            
            for plugin_class in plugins_to_load:
                plugin_instance = plugin_class()
                self._plugins[plugin_instance.category] = plugin_instance
                logger.debug(f"Loaded plugin: {plugin_instance.category}")
        except Exception as e:
            logger.error(f"Failed to load plugins: {e}")
            raise PluginError(f"Plugin loading failed: {e}")
            
    def get_categories(self) -> List[str]:
        """Return a list of supported conversion categories."""
        return list(self._plugins.keys())
        
    def get_units(self, category: str) -> List[str]:
        """Return a list of supported units for a given category."""
        if category not in self._plugins:
            raise PluginError(f"Category '{category}' not supported.")
        return self._plugins[category].units
        
    def convert(self, category: str, value: float, source_unit: str, target_unit: str) -> float:
        """Execute a conversion using the appropriate plugin."""
        if category not in self._plugins:
            raise PluginError(f"Category '{category}' not supported.")
            
        try:
            result = self._plugins[category].convert(value, source_unit, target_unit)
            logger.info(f"Converted {value} {source_unit} to {result} {target_unit} ({category})")
            return result
        except ConversionError as ce:
            logger.error(f"Conversion error: {ce}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error during conversion: {e}")
            raise ConversionError(f"Unexpected error: {e}")
