#!/usr/bin/env python3
"""
GUI Interface for Weekly Work Schedule Generator
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime, timedelta
import generate_schedule_cli_copy
import os

class ScheduleGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🗓 Weekly Work Schedule Generator")
        self.root.geometry("600x700")
        self.root.resizable(True, True)
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        
        self.create_widgets()
        
    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="🗓 Weekly Work Schedule Generator", 
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Mode selection
        mode_frame = ttk.LabelFrame(main_frame, text="Mode Selection", padding="10")
        mode_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        self.mode_var = tk.StringVar(value="1")
        ttk.Radiobutton(mode_frame, text="Mode 1: Input total weekly hours", 
                       variable=self.mode_var, value="1", 
                       command=self.on_mode_change).grid(row=0, column=0, sticky=tk.W, pady=2)
        ttk.Radiobutton(mode_frame, text="Mode 2: Input total overall hours", 
                       variable=self.mode_var, value="2", 
                       command=self.on_mode_change).grid(row=1, column=0, sticky=tk.W, pady=2)
        
        # Input frame
        input_frame = ttk.LabelFrame(main_frame, text="Schedule Parameters", padding="10")
        input_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        # Start date
        ttk.Label(input_frame, text="Start Date (YYYY-MM-DD):").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.date_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
        self.date_entry = ttk.Entry(input_frame, textvariable=self.date_var, width=15)
        self.date_entry.grid(row=0, column=1, sticky=tk.W, padx=(10, 0), pady=2)
        
        # Start week
        ttk.Label(input_frame, text="Starting Week Number:").grid(row=1, column=0, sticky=tk.W, pady=2)
        self.week_var = tk.StringVar(value="1")
        self.week_entry = ttk.Entry(input_frame, textvariable=self.week_var, width=15)
        self.week_entry.grid(row=1, column=1, sticky=tk.W, padx=(10, 0), pady=2)
        
        # Hours input
        ttk.Label(input_frame, text="Total Hours:").grid(row=2, column=0, sticky=tk.W, pady=2)
        self.hours_var = tk.StringVar(value="10")
        self.hours_entry = ttk.Entry(input_frame, textvariable=self.hours_var, width=15)
        self.hours_entry.grid(row=2, column=1, sticky=tk.W, padx=(10, 0), pady=2)
        
        # Days input (for mode 1)
        self.days_label = ttk.Label(input_frame, text="Total Days:")
        self.days_label.grid(row=3, column=0, sticky=tk.W, pady=2)
        self.days_var = tk.StringVar(value="7")
        self.days_entry = ttk.Entry(input_frame, textvariable=self.days_var, width=15)
        self.days_entry.grid(row=3, column=1, sticky=tk.W, padx=(10, 0), pady=2)
        
        # Output frame
        output_frame = ttk.LabelFrame(main_frame, text="Output Settings", padding="10")
        output_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        # Filename
        ttk.Label(output_frame, text="Output Filename:").grid(row=0, column=0, sticky=tk.W, pady=2)
        self.filename_var = tk.StringVar(value="my_schedule")
        filename_frame = ttk.Frame(output_frame)
        filename_frame.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(10, 0), pady=2)
        
        self.filename_entry = ttk.Entry(filename_frame, textvariable=self.filename_var, width=20)
        self.filename_entry.pack(side=tk.LEFT)
        
        ttk.Button(filename_frame, text="Browse", command=self.browse_location).pack(side=tk.LEFT, padx=(5, 0))
        
        # Export options
        export_frame = ttk.Frame(output_frame)
        export_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 0))
        
        self.export_txt = tk.BooleanVar(value=True)
        self.export_xlsx = tk.BooleanVar(value=True)
        self.export_docx = tk.BooleanVar(value=True)
        
        ttk.Checkbutton(export_frame, text="Export to .txt", variable=self.export_txt).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Checkbutton(export_frame, text="Export to .xlsx", variable=self.export_xlsx).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Checkbutton(export_frame, text="Export to .docx", variable=self.export_docx).pack(side=tk.LEFT)
        
        # Buttons
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=2, pady=(0, 20))
        
        ttk.Button(button_frame, text="Generate Schedule", command=self.generate_schedule, 
                  style="Accent.TButton").pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(button_frame, text="Clear", command=self.clear_form).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(button_frame, text="Exit", command=self.root.quit).pack(side=tk.LEFT)
        
        # Status and info
        info_frame = ttk.LabelFrame(main_frame, text="Information", padding="10")
        info_frame.grid(row=5, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        info_text = """• Mode 1: Specify weekly hours and total days
• Mode 2: Specify total overall hours (auto-distributed)
• Time slots: 30-minute increments between 09:00-18:00
• Daily work: 30-120 minutes per day
• Maximum: 15 hours per week
• All times rounded to 30-minute units"""
        
        info_label = ttk.Label(info_frame, text=info_text, justify=tk.LEFT)
        info_label.grid(row=0, column=0, sticky=tk.W)
        
        # Progress bar
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate')
        self.progress.grid(row=6, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Status label
        self.status_var = tk.StringVar(value="Ready to generate schedule")
        status_label = ttk.Label(main_frame, textvariable=self.status_var, 
                                font=("Arial", 9), foreground="blue")
        status_label.grid(row=7, column=0, columnspan=2)
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Initial mode setup
        self.on_mode_change()
        
    def on_mode_change(self):
        """Handle mode change"""
        mode = self.mode_var.get()
        if mode == "1":
            self.days_label.config(text="Total Days:")
            self.hours_entry.config(state="normal")
            self.days_entry.config(state="normal")
        else:
            self.days_label.config(text="Days (auto-calculated):")
            self.hours_entry.config(state="normal")
            self.days_entry.config(state="disabled")
            self.days_var.set("Auto")
    
    def browse_location(self):
        """Browse for save location"""
        filename = filedialog.asksaveasfilename(
            defaultextension="",
            filetypes=[("All files", "*.*")],
            title="Choose save location"
        )
        if filename:
            # Remove extension if present
            base_name = os.path.splitext(filename)[0]
            self.filename_var.set(os.path.basename(base_name))
    
    def validate_inputs(self):
        """Validate all inputs"""
        try:
            # Validate date
            datetime.strptime(self.date_var.get(), "%Y-%m-%d")
            
            # Validate week number
            week = int(self.week_var.get())
            if week < 1:
                raise ValueError("Week number must be at least 1")
            
            # Validate hours
            hours = float(self.hours_var.get())
            if hours <= 0:
                raise ValueError("Hours must be greater than 0")
            if hours > 15:
                raise ValueError("Hours cannot exceed 15")
            
            # Validate days (for mode 1)
            if self.mode_var.get() == "1":
                days = int(self.days_var.get())
                if days < 1:
                    raise ValueError("Days must be at least 1")
            
            # Validate filename
            if not self.filename_var.get().strip():
                raise ValueError("Please enter a filename")
            
            return True
            
        except ValueError as e:
            messagebox.showerror("Validation Error", str(e))
            return False
    
    def generate_schedule(self):
        """Generate the schedule"""
        if not self.validate_inputs():
            return
        
        # Start progress
        self.progress.start()
        self.status_var.set("Generating schedule...")
        self.root.update()
        
        try:
            # Get inputs
            start_date = self.date_var.get()
            start_week = int(self.week_var.get())
            filename = self.filename_var.get().strip()
            mode = self.mode_var.get()
            
            if mode == "1":
                total_hours = float(self.hours_var.get())
                total_days = int(self.days_var.get())
                
                # Call the original function
                generate_schedule_cli_copy.generate_schedule(
                    start_date, total_hours, total_days, filename, start_week
                )
                
            else:  # mode 2
                total_overall_hours = float(self.hours_var.get())
                
                # Call the total hours function
                generate_schedule_cli_copy.generate_schedule_total_hours(
                    start_date, total_overall_hours, filename, start_week
                )
            
            # Check which files were created
            created_files = []
            if self.export_txt.get() and os.path.exists(f"{filename}.txt"):
                created_files.append(".txt")
            if self.export_xlsx.get() and os.path.exists(f"{filename}.xlsx"):
                created_files.append(".xlsx")
            if self.export_docx.get() and os.path.exists(f"{filename}.docx"):
                created_files.append(".docx")
            
            # Show success message
            files_text = ", ".join(created_files) if created_files else "No files"
            messagebox.showinfo("Success", 
                              f"Schedule generated successfully!\n\n"
                              f"Files created: {files_text}\n"
                              f"Location: {os.getcwd()}")
            
            self.status_var.set("Schedule generated successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate schedule:\n{str(e)}")
            self.status_var.set("Error occurred during generation")
        
        finally:
            self.progress.stop()
    
    def clear_form(self):
        """Clear all form fields"""
        self.date_var.set(datetime.now().strftime("%Y-%m-%d"))
        self.week_var.set("1")
        self.hours_var.set("10")
        self.days_var.set("7")
        self.filename_var.set("my_schedule")
        self.export_txt.set(True)
        self.export_xlsx.set(True)
        self.export_docx.set(True)
        self.status_var.set("Ready to generate schedule")

def main():
    root = tk.Tk()
    app = ScheduleGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 