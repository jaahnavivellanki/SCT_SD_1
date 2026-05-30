"""Centralized exception definitions for TempCraft."""

class TempCraftException(Exception):
    """Base exception for all custom TempCraft errors."""
    pass

class ConversionError(TempCraftException):
    """Raised when a conversion calculation fails."""
    pass

class PluginError(TempCraftException):
    """Raised when there is an issue loading or running a plugin."""
    pass

class StorageError(TempCraftException):
    """Raised when there is an issue reading or writing to persistent storage."""
    pass
