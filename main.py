"""Entry point for TempCraft."""
import sys
import os

# Add root dir to sys.path so we can run directly
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from tempcraft.core.engine import ConversionEngine
from tempcraft.data.repository import ConversionRepository
from tempcraft.services.analytics import AnalyticsService
from tempcraft.services.logging import logger
from tempcraft.ui.app import TempCraftApp

def main():
    logger.info("Starting TempCraft...")
    try:
        # Dependency Injection setup
        engine = ConversionEngine()
        repository = ConversionRepository()
        analytics = AnalyticsService(repository)
        
        # Launch App
        app = TempCraftApp(engine=engine, repository=repository, analytics=analytics)
        app.mainloop()
        logger.info("TempCraft exited normally.")
    except Exception as e:
        logger.critical(f"Application crashed: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    main()
