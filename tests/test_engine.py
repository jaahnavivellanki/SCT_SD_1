import pytest
from tempcraft.core.engine import ConversionEngine
from tempcraft.core.exceptions import PluginError

def test_engine_loads_plugins():
    engine = ConversionEngine()
    assert "Temperature" in engine.get_categories()

def test_engine_unsupported_category():
    engine = ConversionEngine()
    with pytest.raises(PluginError):
        engine.convert("Unsupported", 0, "Celsius", "Fahrenheit")
