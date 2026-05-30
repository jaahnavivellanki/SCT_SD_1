import pytest
from tempcraft.plugins.temperature import TemperaturePlugin
from tempcraft.core.exceptions import ConversionError

def test_temperature_plugin_celsius_to_fahrenheit():
    plugin = TemperaturePlugin()
    assert plugin.convert(0, "Celsius", "Fahrenheit") == 32.0
    assert plugin.convert(100, "Celsius", "Fahrenheit") == 212.0

def test_temperature_plugin_unsupported_unit():
    plugin = TemperaturePlugin()
    with pytest.raises(ConversionError):
        plugin.convert(0, "Celsius", "Unsupported")
