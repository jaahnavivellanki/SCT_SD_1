"""Analytics service to generate insights from conversion history."""
from collections import Counter
from typing import Dict, Any, List
from tempcraft.data.repository import ConversionRepository

class AnalyticsService:
    """Provides analytical data based on the conversion repository."""
    
    def __init__(self, repository: ConversionRepository):
        self.repository = repository
        
    def get_dashboard_metrics(self) -> Dict[str, Any]:
        """Calculates key metrics for the analytics dashboard."""
        records = self.repository.get_all()
        
        total_conversions = len(records)
        
        if total_conversions == 0:
            return {
                "total_conversions": 0,
                "most_used_category": "N/A",
                "most_used_source": "N/A",
                "most_used_target": "N/A"
            }
            
        categories = [r.category for r in records]
        sources = [r.source_unit for r in records]
        targets = [r.target_unit for r in records]
        
        return {
            "total_conversions": total_conversions,
            "most_used_category": Counter(categories).most_common(1)[0][0],
            "most_used_source": Counter(sources).most_common(1)[0][0],
            "most_used_target": Counter(targets).most_common(1)[0][0],
        }
