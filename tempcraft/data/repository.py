"""Data repository for JSON persistence."""
import json
import os
from typing import List, Optional
from tempcraft.config.settings import STORAGE_FILE
from tempcraft.models.conversion import ConversionRecord
from tempcraft.core.exceptions import StorageError

class ConversionRepository:
    """Handles CRUD operations for conversion history using a JSON file."""
    
    def __init__(self, storage_path: str = str(STORAGE_FILE)):
        self.storage_path = storage_path
        self._ensure_storage_exists()
        
    def _ensure_storage_exists(self):
        """Creates the JSON file with an empty list if it doesn't exist."""
        if not os.path.exists(self.storage_path):
            try:
                with open(self.storage_path, 'w', encoding='utf-8') as f:
                    json.dump([], f)
            except Exception as e:
                raise StorageError(f"Failed to initialize storage: {e}")
                
    def get_all(self) -> List[ConversionRecord]:
        """Retrieve all conversion records."""
        try:
            with open(self.storage_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [ConversionRecord.from_dict(item) for item in data]
        except json.JSONDecodeError:
            # Handle corrupted file
            return []
        except Exception as e:
            raise StorageError(f"Failed to read from storage: {e}")
            
    def add(self, record: ConversionRecord):
        """Add a new conversion record."""
        records = self.get_all()
        records.append(record)
        self._save(records)
        
    def clear(self):
        """Clear all records."""
        self._save([])
        
    def _save(self, records: List[ConversionRecord]):
        """Save a list of records back to JSON."""
        try:
            with open(self.storage_path, 'w', encoding='utf-8') as f:
                json.dump([r.to_dict() for r in records], f, indent=4)
        except Exception as e:
            raise StorageError(f"Failed to write to storage: {e}")
