"""Temperature conversion plugin."""
from typing import List
from tempcraft.plugins.base_plugin import BaseConversionPlugin
from tempcraft.core.exceptions import ConversionError

class TemperaturePlugin(BaseConversionPlugin):
    """Plugin for converting between temperature units."""
    
    @property
    def category(self) -> str:
        return "Temperature"
        
    @property
    def units(self) -> List[str]:
        return ["Celsius", "Fahrenheit", "Kelvin"]
        
    def convert(self, value: float, source_unit: str, target_unit: str) -> float:
        """Convert temperature values between Celsius, Fahrenheit, and Kelvin."""
        if source_unit not in self.units or target_unit not in self.units:
            raise ConversionError(f"Unsupported units for Temperature: {source_unit}, {target_unit}")
            
        if source_unit == target_unit:
            return value
            
        # Convert source to Celsius first
        if source_unit == "Celsius":
            celsius = value
        elif source_unit == "Fahrenheit":
            celsius = (value - 32) * 5/9
        elif source_unit == "Kelvin":
            celsius = value - 273.15
            
        # Convert Celsius to target
        if target_unit == "Celsius":
            return celsius
        elif target_unit == "Fahrenheit":
            return (celsius * 9/5) + 32
        elif target_unit == "Kelvin":
            return celsius + 273.15
            
        raise ConversionError("Failed to perform conversion.")
