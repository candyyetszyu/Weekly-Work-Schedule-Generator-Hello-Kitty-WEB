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
        self.root.geometry("700x800")
        self.root.resizable(True, True)
        
        # Set window icon and configure
        self.root.configure(bg='#f0f8ff')  # Light blue background
        
        # Configure modern style
        self.setup_styles()
        
        self.create_widgets()
        
    def setup_styles(self):
        """Configure modern styles for the GUI"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure colors
        style.configure('Title.TLabel', 
                       font=('Helvetica', 18, 'bold'), 
                       foreground='#2c3e50',
                       background='#f0f8ff')
        
        style.configure('Header.TLabel', 
                       font=('Helvetica', 12, 'bold'), 
                       foreground='#34495e',
                       background='#f0f8ff')
        
        style.configure('Info.TLabel', 
                       font=('Helvetica', 10), 
                       foreground='#7f8c8d',
                       background='#f0f8ff')
        
        style.configure('Success.TLabel', 
                       font=('Helvetica', 10), 
                       foreground='#27ae60',
                       background='#f0f8ff')
        
        style.configure('Error.TLabel', 
                       font=('Helvetica', 10), 
                       foreground='#e74c3c',
                       background='#f0f8ff')
        
        # Frame styles
        style.configure('Card.TFrame', 
                       background='#ffffff',
                       relief='solid',
                       borderwidth=1)
        
        # Button styles
        style.configure('Primary.TButton', 
                       font=('Helvetica', 11, 'bold'),
                       background='#3498db',
                       foreground='white')
        
        style.configure('Success.TButton', 
                       font=('Helvetica', 11),
                       background='#2ecc71',
                       foreground='white')
        
        style.configure('Warning.TButton', 
                       font=('Helvetica', 11),
                       background='#e67e22',
                       foreground='white')
        
        # Progress bar style
        style.configure('Custom.Horizontal.TProgressbar',
                       background='#3498db',
                       troughcolor='#ecf0f1')
        
    def create_widgets(self):
        # Main frame with background
        main_frame = tk.Frame(self.root, bg='#f0f8ff', padx=30, pady=30)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title with modern styling
        title_frame = tk.Frame(main_frame, bg='#f0f8ff')
        title_frame.pack(fill=tk.X, pady=(0, 30))
        
        title_label = tk.Label(title_frame, 
                              text="🗓 Weekly Work Schedule Generator", 
                              font=("Helvetica", 24, "bold"),
                              fg='#2c3e50',
                              bg='#f0f8ff')
        title_label.pack()
        
        subtitle_label = tk.Label(title_frame,
                                 text="Create professional work schedules with ease",
                                 font=("Helvetica", 12),
                                 fg='#7f8c8d',
                                 bg='#f0f8ff')
        subtitle_label.pack(pady=(5, 0))
        
        # Mode selection with modern card design
        mode_frame = tk.Frame(main_frame, bg='#ffffff', relief='solid', bd=1, padx=20, pady=20)
        mode_frame.pack(fill=tk.X, pady=(0, 20))
        
        mode_title = tk.Label(mode_frame, text="📋 Mode Selection", 
                             font=("Helvetica", 14, "bold"),
                             fg='#2c3e50',
                             bg='#ffffff')
        mode_title.pack(anchor=tk.W, pady=(0, 15))
        
        self.mode_var = tk.StringVar(value="1")
        
        # Mode 1
        mode1_frame = tk.Frame(mode_frame, bg='#ffffff')
        mode1_frame.pack(fill=tk.X, pady=5)
        
        mode1_radio = tk.Radiobutton(mode1_frame, 
                                   text="📅 Mode 1: Input total weekly hours", 
                                   variable=self.mode_var, 
                                   value="1", 
                                   command=self.on_mode_change,
                                   font=("Helvetica", 11),
                                   fg='#34495e',
                                   bg='#ffffff',
                                   selectcolor='#3498db')
        mode1_radio.pack(anchor=tk.W)
        
        mode1_desc = tk.Label(mode1_frame, 
                             text="   Specify weekly hours and total number of days",
                             font=("Helvetica", 9),
                             fg='#7f8c8d',
                             bg='#ffffff')
        mode1_desc.pack(anchor=tk.W, padx=(20, 0))
        
        # Mode 2
        mode2_frame = tk.Frame(mode_frame, bg='#ffffff')
        mode2_frame.pack(fill=tk.X, pady=5)
        
        mode2_radio = tk.Radiobutton(mode2_frame, 
                                   text="📊 Mode 2: Input total overall hours", 
                                   variable=self.mode_var, 
                                   value="2", 
                                   command=self.on_mode_change,
                                   font=("Helvetica", 11),
                                   fg='#34495e',
                                   bg='#ffffff',
                                   selectcolor='#3498db')
        mode2_radio.pack(anchor=tk.W)
        
        mode2_desc = tk.Label(mode2_frame, 
                             text="   System will automatically distribute across weeks",
                             font=("Helvetica", 9),
                             fg='#7f8c8d',
                             bg='#ffffff')
        mode2_desc.pack(anchor=tk.W, padx=(20, 0))
        
        # Input parameters with modern card design
        input_frame = tk.Frame(main_frame, bg='#ffffff', relief='solid', bd=1, padx=20, pady=20)
        input_frame.pack(fill=tk.X, pady=(0, 20))
        
        input_title = tk.Label(input_frame, text="⚙️ Schedule Parameters", 
                              font=("Helvetica", 14, "bold"),
                              fg='#2c3e50',
                              bg='#ffffff')
        input_title.pack(anchor=tk.W, pady=(0, 15))
        
        # Create a grid for input fields
        input_grid = tk.Frame(input_frame, bg='#ffffff')
        input_grid.pack(fill=tk.X)
        
        # Start date
        tk.Label(input_grid, text="📅 Start Date (YYYY-MM-DD):", 
                font=("Helvetica", 11, "bold"),
                fg='#34495e',
                bg='#ffffff').grid(row=0, column=0, sticky=tk.W, pady=8, padx=(0, 20))
        
        self.date_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
        self.date_entry = tk.Entry(input_grid, textvariable=self.date_var, 
                                 font=("Helvetica", 11),
                                 width=15,
                                 relief='solid',
                                 bd=1)
        self.date_entry.grid(row=0, column=1, sticky=tk.W, pady=8)
        
        # Start week
        tk.Label(input_grid, text="📊 Starting Week Number:", 
                font=("Helvetica", 11, "bold"),
                fg='#34495e',
                bg='#ffffff').grid(row=1, column=0, sticky=tk.W, pady=8, padx=(0, 20))
        
        self.week_var = tk.StringVar(value="1")
        self.week_entry = tk.Entry(input_grid, textvariable=self.week_var, 
                                 font=("Helvetica", 11),
                                 width=15,
                                 relief='solid',
                                 bd=1)
        self.week_entry.grid(row=1, column=1, sticky=tk.W, pady=8)
        
        # Hours input
        tk.Label(input_grid, text="⏰ Total Hours:", 
                font=("Helvetica", 11, "bold"),
                fg='#34495e',
                bg='#ffffff').grid(row=2, column=0, sticky=tk.W, pady=8, padx=(0, 20))
        
        self.hours_var = tk.StringVar(value="10")
        self.hours_entry = tk.Entry(input_grid, textvariable=self.hours_var, 
                                  font=("Helvetica", 11),
                                  width=15,
                                  relief='solid',
                                  bd=1)
        self.hours_entry.grid(row=2, column=1, sticky=tk.W, pady=8)
        
        # Days input (for mode 1)
        self.days_label = tk.Label(input_grid, text="📅 Total Days:", 
                                  font=("Helvetica", 11, "bold"),
                                  fg='#34495e',
                                  bg='#ffffff')
        self.days_label.grid(row=3, column=0, sticky=tk.W, pady=8, padx=(0, 20))
        
        self.days_var = tk.StringVar(value="7")
        self.days_entry = tk.Entry(input_grid, textvariable=self.days_var, 
                                 font=("Helvetica", 11),
                                 width=15,
                                 relief='solid',
                                 bd=1)
        self.days_entry.grid(row=3, column=1, sticky=tk.W, pady=8)
        
        # Output settings with modern card design
        output_frame = tk.Frame(main_frame, bg='#ffffff', relief='solid', bd=1, padx=20, pady=20)
        output_frame.pack(fill=tk.X, pady=(0, 20))
        
        output_title = tk.Label(output_frame, text="📁 Output Settings", 
                               font=("Helvetica", 14, "bold"),
                               fg='#2c3e50',
                               bg='#ffffff')
        output_title.pack(anchor=tk.W, pady=(0, 15))
        
        # Filename section
        filename_section = tk.Frame(output_frame, bg='#ffffff')
        filename_section.pack(fill=tk.X, pady=(0, 15))
        
        tk.Label(filename_section, text="📄 Output Filename:", 
                font=("Helvetica", 11, "bold"),
                fg='#34495e',
                bg='#ffffff').pack(anchor=tk.W, pady=(0, 5))
        
        filename_input_frame = tk.Frame(filename_section, bg='#ffffff')
        filename_input_frame.pack(fill=tk.X)
        
        self.filename_var = tk.StringVar(value="my_schedule")
        self.filename_entry = tk.Entry(filename_input_frame, textvariable=self.filename_var, 
                                     font=("Helvetica", 11),
                                     width=25,
                                     relief='solid',
                                     bd=1)
        self.filename_entry.pack(side=tk.LEFT, padx=(0, 10))
        
        browse_btn = tk.Button(filename_input_frame, text="📂 Browse", 
                              command=self.browse_location,
                              font=("Helvetica", 10),
                              bg='#95a5a6',
                              fg='white',
                              relief='flat',
                              padx=15,
                              pady=5)
        browse_btn.pack(side=tk.LEFT)
        
        # Export options section
        export_section = tk.Frame(output_frame, bg='#ffffff')
        export_section.pack(fill=tk.X)
        
        tk.Label(export_section, text="📊 Export Formats:", 
                font=("Helvetica", 11, "bold"),
                fg='#34495e',
                bg='#ffffff').pack(anchor=tk.W, pady=(0, 10))
        
        export_options_frame = tk.Frame(export_section, bg='#ffffff')
        export_options_frame.pack(fill=tk.X)
        
        self.export_txt = tk.BooleanVar(value=True)
        self.export_xlsx = tk.BooleanVar(value=True)
        self.export_docx = tk.BooleanVar(value=True)
        
        # Export checkboxes with custom styling
        txt_cb = tk.Checkbutton(export_options_frame, text="📄 Text (.txt)", 
                               variable=self.export_txt,
                               font=("Helvetica", 10),
                               fg='#34495e',
                               bg='#ffffff',
                               selectcolor='#3498db')
        txt_cb.pack(side=tk.LEFT, padx=(0, 20))
        
        xlsx_cb = tk.Checkbutton(export_options_frame, text="📊 Excel (.xlsx)", 
                                variable=self.export_xlsx,
                                font=("Helvetica", 10),
                                fg='#34495e',
                                bg='#ffffff',
                                selectcolor='#3498db')
        xlsx_cb.pack(side=tk.LEFT, padx=(0, 20))
        
        docx_cb = tk.Checkbutton(export_options_frame, text="📝 Word (.docx)", 
                                variable=self.export_docx,
                                font=("Helvetica", 10),
                                fg='#34495e',
                                bg='#ffffff',
                                selectcolor='#3498db')
        docx_cb.pack(side=tk.LEFT)
        
        # Action buttons with modern styling
        button_frame = tk.Frame(main_frame, bg='#f0f8ff')
        button_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Generate button (primary action)
        generate_btn = tk.Button(button_frame, text="🚀 Generate Schedule", 
                                command=self.generate_schedule,
                                font=("Helvetica", 12, "bold"),
                                bg='#3498db',
                                fg='white',
                                relief='flat',
                                padx=30,
                                pady=12,
                                cursor='hand2')
        generate_btn.pack(side=tk.LEFT, padx=(0, 15))
        
        # Clear button
        clear_btn = tk.Button(button_frame, text="🔄 Clear Form", 
                             command=self.clear_form,
                             font=("Helvetica", 11),
                             bg='#95a5a6',
                             fg='white',
                             relief='flat',
                             padx=20,
                             pady=10,
                             cursor='hand2')
        clear_btn.pack(side=tk.LEFT, padx=(0, 15))
        
        # Exit button
        exit_btn = tk.Button(button_frame, text="❌ Exit", 
                            command=self.root.quit,
                            font=("Helvetica", 11),
                            bg='#e74c3c',
                            fg='white',
                            relief='flat',
                            padx=20,
                            pady=10,
                            cursor='hand2')
        exit_btn.pack(side=tk.LEFT)
        
        # Information section with modern card design
        info_frame = tk.Frame(main_frame, bg='#ffffff', relief='solid', bd=1, padx=20, pady=20)
        info_frame.pack(fill=tk.X, pady=(0, 20))
        
        info_title = tk.Label(info_frame, text="ℹ️ Information & Tips", 
                             font=("Helvetica", 14, "bold"),
                             fg='#2c3e50',
                             bg='#ffffff')
        info_title.pack(anchor=tk.W, pady=(0, 15))
        
        info_text = """📋 Mode 1: Specify weekly hours and total number of days
📊 Mode 2: Specify total overall hours (auto-distributed across weeks)
⏰ Time slots: 30-minute increments between 09:00-18:00
📅 Daily work: 30-120 minutes per day
⏱️ Maximum: 15 hours per week
🎯 All times rounded to 30-minute units for consistency"""
        
        info_label = tk.Label(info_frame, text=info_text, 
                             font=("Helvetica", 10),
                             fg='#7f8c8d',
                             bg='#ffffff',
                             justify=tk.LEFT,
                             anchor=tk.W)
        info_label.pack(anchor=tk.W)
        
        # Progress bar with modern styling
        progress_frame = tk.Frame(main_frame, bg='#f0f8ff')
        progress_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.progress = ttk.Progressbar(progress_frame, 
                                      mode='indeterminate',
                                      style='Custom.Horizontal.TProgressbar',
                                      length=400)
        self.progress.pack(pady=10)
        
        # Status label with modern styling
        status_frame = tk.Frame(main_frame, bg='#f0f8ff')
        status_frame.pack(fill=tk.X)
        
        self.status_var = tk.StringVar(value="✨ Ready to generate your schedule!")
        status_label = tk.Label(status_frame, 
                               textvariable=self.status_var, 
                               font=("Helvetica", 11),
                               fg='#3498db',
                               bg='#f0f8ff')
        status_label.pack(pady=5)
        
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
        self.status_var.set("🚀 Generating your schedule...")
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
            
            self.status_var.set("✅ Schedule generated successfully!")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate schedule:\n{str(e)}")
            self.status_var.set("❌ Error occurred during generation")
        
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
        self.status_var.set("✨ Ready to generate your schedule!")

def main():
    root = tk.Tk()
    app = ScheduleGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 