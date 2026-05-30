"""Base class for all conversion plugins."""
from abc import ABC, abstractmethod
from typing import List

class BaseConversionPlugin(ABC):
    """Abstract base class that all conversion plugins must implement."""
    
    @property
    @abstractmethod
    def category(self) -> str:
        """The category of this plugin, e.g., 'Temperature', 'Length'."""
        pass
        
    @property
    @abstractmethod
    def units(self) -> List[str]:
        """List of supported units."""
        pass
        
    @abstractmethod
    def convert(self, value: float, source_unit: str, target_unit: str) -> float:
        """Perform the actual conversion."""
        pass
