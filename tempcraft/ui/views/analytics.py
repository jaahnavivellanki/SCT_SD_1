import customtkinter as ctk
from tempcraft.services.analytics import AnalyticsService
from datetime import datetime

class AnalyticsView(ctk.CTkFrame):
    def __init__(self, master, analytics_service: AnalyticsService, **kwargs):
        super().__init__(master, **kwargs)
        self.analytics = analytics_service
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        
        # Header
        self.header = ctk.CTkLabel(self, text="Dashboard Analytics", font=ctk.CTkFont(size=32, weight="bold"), anchor="w")
        self.header.grid(row=0, column=0, pady=(0, 30), sticky="w")
        
        # Metrics Grid
        self.metrics_grid = ctk.CTkFrame(self, fg_color="transparent")
        self.metrics_grid.grid(row=1, column=0, sticky="nsew")
        self.metrics_grid.grid_columnconfigure((0, 1, 2), weight=1, uniform="col")
        
        self.metric_cards = {}
        self._create_metric_card("Total Conversions", 0, 0)
        self._create_metric_card("Most Used Scale", 0, 1)
        self._create_metric_card("Last Conversion", 0, 2)
        
        self.refresh()
        
    def _create_metric_card(self, title: str, row: int, col: int):
        card = ctk.CTkFrame(self.metrics_grid, fg_color="#252525", corner_radius=12, border_width=1, border_color="#333333")
        card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
        card.grid_columnconfigure(0, weight=1)
        
        lbl_title = ctk.CTkLabel(card, text=title, font=ctk.CTkFont(size=14), text_color="#AAAAAA")
        lbl_title.grid(row=0, column=0, pady=(20, 5), padx=20, sticky="w")
        
        lbl_val = ctk.CTkLabel(card, text="--", font=ctk.CTkFont(size=28, weight="bold"))
        lbl_val.grid(row=1, column=0, pady=(0, 20), padx=20, sticky="w")
        
        self.metric_cards[title] = lbl_val
        
    def refresh(self):
        metrics = self.analytics.get_dashboard_metrics()
        
        # Calculate Last Conversion
        records = self.analytics.repository.get_all()
        last_conv = "N/A"
        if records:
            last_record = records[-1]
            try:
                # Try parsing the ISO format and making it human-readable
                dt = datetime.fromisoformat(last_record.timestamp)
                last_conv = dt.strftime("%Y-%m-%d %H:%M")
            except Exception:
                last_conv = last_record.timestamp[:16] # Fallback
                
        self.metric_cards["Total Conversions"].configure(text=str(metrics.get("total_conversions", 0)))
        self.metric_cards["Most Used Scale"].configure(text=metrics.get("most_used_source", "N/A"))
        self.metric_cards["Last Conversion"].configure(text=last_conv)
