import customtkinter as ctk
from typing import Callable
from tempcraft.core.engine import ConversionEngine
from tempcraft.models.conversion import ConversionRecord

class ConvertView(ctk.CTkFrame):
    def __init__(self, master, engine: ConversionEngine, on_conversion: Callable[[ConversionRecord], None], **kwargs):
        super().__init__(master, **kwargs)
        self.engine = engine
        self.on_conversion = on_conversion
        
        self.categories = self.engine.get_categories()
        self.current_category = self.categories[0] if self.categories else "Temperature"
        self.units = self.engine.get_units(self.current_category) if self.categories else []
        
        # Center the main card
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)
        
        # Main Card
        self.card = ctk.CTkFrame(self, fg_color="#252525", corner_radius=16, border_width=1, border_color="#333333")
        self.card.grid(row=1, column=1, padx=20, pady=20, sticky="nsew")
        self.card.grid_columnconfigure(0, weight=1)
        
        # Header
        self.header = ctk.CTkLabel(self.card, text="Quick Convert", font=ctk.CTkFont(size=28, weight="bold"))
        self.header.grid(row=0, column=0, pady=(30, 20))
        
        # Input Field
        self.entry = ctk.CTkEntry(self.card, placeholder_text="Enter value...", width=300, height=45, font=ctk.CTkFont(size=16), corner_radius=8)
        self.entry.grid(row=1, column=0, pady=15, padx=40)
        
        # Dropdowns
        self.source_var = ctk.StringVar(value=self.units[0] if self.units else "")
        self.source_menu = ctk.CTkOptionMenu(self.card, values=self.units, variable=self.source_var, width=300, height=45, font=ctk.CTkFont(size=14), corner_radius=8)
        self.source_menu.grid(row=2, column=0, pady=10, padx=40)
        
        self.target_var = ctk.StringVar(value=self.units[1] if len(self.units) > 1 else (self.units[0] if self.units else ""))
        self.target_menu = ctk.CTkOptionMenu(self.card, values=self.units, variable=self.target_var, width=300, height=45, font=ctk.CTkFont(size=14), corner_radius=8)
        self.target_menu.grid(row=3, column=0, pady=10, padx=40)
        
        # Convert Button
        self.convert_btn = ctk.CTkButton(self.card, text="Convert", width=300, height=50, font=ctk.CTkFont(size=16, weight="bold"), corner_radius=8, command=self.do_convert, hover_color="#3A7EBF")
        self.convert_btn.grid(row=4, column=0, pady=(20, 30), padx=40)
        
        # Result Card (Nested)
        self.result_card = ctk.CTkFrame(self.card, fg_color="#1E1E1E", corner_radius=12, border_width=1, border_color="#3A7EBF")
        self.result_card.grid(row=5, column=0, pady=(0, 40), padx=40, sticky="ew")
        self.result_card.grid_columnconfigure(0, weight=1)
        
        self.result_label = ctk.CTkLabel(self.result_card, text="Result: --", font=ctk.CTkFont(size=22, weight="bold"), text_color="#FFFFFF")
        self.result_label.grid(row=0, column=0, pady=20)
        
        # Bind Enter
        self.entry.bind("<Return>", lambda e: self.do_convert())
        
    def do_convert(self):
        try:
            val_str = self.entry.get().strip()
            if not val_str:
                self.result_label.configure(text="Error: Empty Input", text_color="#FF4C4C")
                self.result_card.configure(border_color="#FF4C4C")
                return
                
            val = float(val_str)
            src = self.source_var.get()
            tgt = self.target_var.get()
            
            res = self.engine.convert(self.current_category, val, src, tgt)
            self.result_label.configure(text=f"{res:.2f} {tgt}", text_color="#00FFCC")
            self.result_card.configure(border_color="#00FFCC")
            
            record = ConversionRecord(
                source_value=val,
                source_unit=src,
                target_value=res,
                target_unit=tgt,
                category=self.current_category
            )
            self.on_conversion(record)
        except ValueError:
            self.result_label.configure(text="Error: Invalid Number", text_color="#FF4C4C")
            self.result_card.configure(border_color="#FF4C4C")
        except Exception as e:
            self.result_label.configure(text=f"Error: {e}", text_color="#FF4C4C")
            self.result_card.configure(border_color="#FF4C4C")
