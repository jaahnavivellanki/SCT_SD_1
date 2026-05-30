import customtkinter as ctk
from tempcraft.data.repository import ConversionRepository
from datetime import datetime

class HistoryView(ctk.CTkFrame):
    def __init__(self, master, repository: ConversionRepository, **kwargs):
        super().__init__(master, **kwargs)
        self.repository = repository
        
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Header area
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.grid(row=0, column=0, sticky="ew", pady=(0, 20))
        self.header_frame.grid_columnconfigure(0, weight=1)
        
        self.header = ctk.CTkLabel(self.header_frame, text="Conversion History", font=ctk.CTkFont(size=32, weight="bold"))
        self.header.grid(row=0, column=0, sticky="w")
        
        self.clear_btn = ctk.CTkButton(self.header_frame, text="Clear All", width=120, fg_color="#FF4C4C", hover_color="#CC0000", command=self.clear_history)
        self.clear_btn.grid(row=0, column=1, sticky="e")
        
        # List area
        self.scrollable = ctk.CTkScrollableFrame(self, fg_color="#1A1A1A", corner_radius=12)
        self.scrollable.grid(row=1, column=0, sticky="nsew")
        self.scrollable.grid_columnconfigure(0, weight=1)
        
        self.refresh()
        
    def refresh(self):
        # Clear existing
        for widget in self.scrollable.winfo_children():
            widget.destroy()
            
        records = self.repository.get_all()
        
        if not records:
            lbl = ctk.CTkLabel(self.scrollable, text="No history yet.", font=ctk.CTkFont(size=14), text_color="#AAAAAA")
            lbl.grid(row=0, column=0, pady=40)
            return
            
        for i, record in enumerate(reversed(records)):
            self._create_history_row(i, record)
            
    def _create_history_row(self, index: int, record):
        row_frame = ctk.CTkFrame(self.scrollable, fg_color="#252525", corner_radius=8, height=60)
        row_frame.grid(row=index, column=0, sticky="ew", pady=5, padx=10)
        row_frame.grid_columnconfigure(1, weight=1)
        row_frame.grid_propagate(False) # Keep fixed height
        
        # Parse timestamp
        try:
            dt = datetime.fromisoformat(record.timestamp)
            time_str = dt.strftime("%b %d, %H:%M")
        except:
            time_str = record.timestamp[:10]
            
        lbl_time = ctk.CTkLabel(row_frame, text=time_str, font=ctk.CTkFont(size=12), text_color="#888888", width=100, anchor="w")
        lbl_time.grid(row=0, column=0, padx=(20, 10), pady=20)
        
        # Content
        content_text = f"{record.source_value} {record.source_unit}   ➔   {record.target_value:.2f} {record.target_unit}"
        lbl_content = ctk.CTkLabel(row_frame, text=content_text, font=ctk.CTkFont(size=16, weight="bold"), anchor="w")
        lbl_content.grid(row=0, column=1, padx=10, pady=20, sticky="ew")
        
        # Category tag
        cat_frame = ctk.CTkFrame(row_frame, fg_color="#333333", corner_radius=4)
        cat_frame.grid(row=0, column=2, padx=20, pady=15)
        lbl_cat = ctk.CTkLabel(cat_frame, text=record.category, font=ctk.CTkFont(size=12), text_color="#BBBBBB")
        lbl_cat.pack(padx=10, pady=2)
            
    def clear_history(self):
        self.repository.clear()
        self.refresh()
