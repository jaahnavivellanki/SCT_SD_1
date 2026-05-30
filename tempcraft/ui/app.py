import customtkinter as ctk
from tempcraft.config.settings import WINDOW_GEOMETRY, THEME_MODE, COLOR_THEME, APP_NAME, APP_VERSION
from tempcraft.core.engine import ConversionEngine
from tempcraft.data.repository import ConversionRepository
from tempcraft.services.analytics import AnalyticsService
from tempcraft.models.conversion import ConversionRecord

from tempcraft.ui.views.convert import ConvertView
from tempcraft.ui.views.history import HistoryView
from tempcraft.ui.views.analytics import AnalyticsView

ctk.set_appearance_mode(THEME_MODE)
ctk.set_default_color_theme(COLOR_THEME)

class TempCraftApp(ctk.CTk):
    def __init__(self, engine: ConversionEngine, repository: ConversionRepository, analytics: AnalyticsService):
        super().__init__()
        self.engine = engine
        self.repository = repository
        self.analytics = analytics
        
        self.title(APP_NAME)
        self.geometry(WINDOW_GEOMETRY)
        self.configure(fg_color="#121212") # Main background
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # --- Sidebar ---
        self.sidebar_frame = ctk.CTkFrame(self, width=220, corner_radius=0, fg_color="#1A1A1A")
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1) # Push footer to bottom
        
        # Logo
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="🌡️ TempCraft", font=ctk.CTkFont(family="Roboto", size=24, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(30, 30), sticky="w")
        
        # Nav Buttons
        self.nav_buttons = {}
        self._create_nav_button("convert", "⚡ Quick Convert", 1)
        self._create_nav_button("history", "🕒 History", 2)
        self._create_nav_button("analytics", "📊 Analytics", 3)
        
        # Footer
        self.footer_frame = ctk.CTkFrame(self.sidebar_frame, fg_color="transparent")
        self.footer_frame.grid(row=5, column=0, sticky="s", pady=(0, 20), padx=20)
        
        self.version_label = ctk.CTkLabel(self.footer_frame, text=f"Version {APP_VERSION}", font=ctk.CTkFont(size=11), text_color="gray")
        self.version_label.pack(anchor="w")
        
        self.tech_label = ctk.CTkLabel(self.footer_frame, text="Built with Python & CustomTkinter", font=ctk.CTkFont(size=10), text_color="gray")
        self.tech_label.pack(anchor="w")
        
        # --- Views Container ---
        self.views_container = ctk.CTkFrame(self, fg_color="transparent")
        self.views_container.grid(row=0, column=1, sticky="nsew", padx=30, pady=30)
        self.views_container.grid_rowconfigure(0, weight=1)
        self.views_container.grid_columnconfigure(0, weight=1)
        
        # Views
        self.views = {
            "convert": ConvertView(self.views_container, self.engine, self.on_conversion_success, fg_color="transparent"),
            "history": HistoryView(self.views_container, self.repository, fg_color="transparent"),
            "analytics": AnalyticsView(self.views_container, self.analytics, fg_color="transparent")
        }
        
        self.current_view = None
        self.select_frame("convert")
        
    def _create_nav_button(self, name: str, text: str, row: int):
        btn = ctk.CTkButton(
            self.sidebar_frame, text=text, anchor="w", fg_color="transparent", 
            text_color="#DDDDDD", hover_color="#2A2A2A", font=ctk.CTkFont(size=14),
            command=lambda: self.select_frame(name)
        )
        btn.grid(row=row, column=0, padx=15, pady=5, sticky="ew")
        self.nav_buttons[name] = btn
        
    def select_frame(self, name: str):
        if self.current_view:
            self.views[self.current_view].grid_forget()
            # Reset button style
            self.nav_buttons[self.current_view].configure(fg_color="transparent", text_color="#DDDDDD")
            
        self.current_view = name
        
        # Update button style for active
        self.nav_buttons[name].configure(fg_color="#2A2A2A", text_color="#FFFFFF")
        
        # Show new view
        if hasattr(self.views[name], "refresh"):
            self.views[name].refresh()
        self.views[name].grid(row=0, column=0, sticky="nsew")
            
    def on_conversion_success(self, record: ConversionRecord):
        self.repository.add(record)
