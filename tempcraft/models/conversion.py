"""Data models for TempCraft."""
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class ConversionRecord:
    """Represents a single conversion operation."""
    source_value: float
    source_unit: str
    target_value: float
    target_unit: str
    category: str = "Temperature"
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    def to_dict(self) -> dict:
        """Convert record to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "source_value": self.source_value,
            "source_unit": self.source_unit,
            "target_value": self.target_value,
            "target_unit": self.target_unit,
            "category": self.category,
            "timestamp": self.timestamp
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "ConversionRecord":
        """Create a ConversionRecord from a dictionary."""
        return cls(**data)
