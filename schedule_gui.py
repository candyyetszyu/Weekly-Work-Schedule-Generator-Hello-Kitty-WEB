#!/usr/bin/env python3
"""
GUI Interface for Weekly Work Schedule Generator
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from datetime import datetime, timedelta
import generate_schedule_cli_copy
import os
from PIL import Image, ImageTk

class ScheduleGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎀 Hello Kitty Schedule Generator 🎀")
        self.root.geometry("850x950")
        self.root.resizable(True, True)
        
        # Set window icon and configure
        self.root.configure(bg='#ffe6f2')  # Light pink background
        
        # Load and set background image
        self.setup_background()
        
        # Configure Hello Kitty style
        self.setup_styles()
        
        self.create_widgets()
        
    def setup_background(self):
        """Setup Hello Kitty background image"""
        try:
            # Check if background image exists
            if os.path.exists('hello_kitty_bg.png'):
                # Load the background image
                bg_image = Image.open('hello_kitty_bg.png')
                # Resize to fit window
                bg_image = bg_image.resize((850, 950), Image.Resampling.LANCZOS)
                self.bg_photo = ImageTk.PhotoImage(bg_image)
                
                # Create background label
                self.bg_label = tk.Label(self.root, image=self.bg_photo)
                self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
                self.bg_label.lower()  # Put background behind other widgets
                
                print("🌸 Hello Kitty background loaded successfully!")
            else:
                print("⚠️ Background image not found, using solid color background")
                self.bg_photo = None
                self.bg_label = None
                
        except Exception as e:
            print(f"⚠️ Could not load background image: {e}")
            self.bg_photo = None
            self.bg_label = None
        
    def setup_styles(self):
        """Configure Hello Kitty styles for the GUI"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure Hello Kitty colors
        style.configure('Title.TLabel', 
                       font=('Comic Sans MS', 20, 'bold'), 
                       foreground='#ff69b4',
                       background='#ffe6f2')
        
        style.configure('Header.TLabel', 
                       font=('Comic Sans MS', 14, 'bold'), 
                       foreground='#ff1493',
                       background='#ffe6f2')
        
        style.configure('Info.TLabel', 
                       font=('Comic Sans MS', 11), 
                       foreground='#c71585',
                       background='#ffe6f2')
        
        style.configure('Success.TLabel', 
                       font=('Comic Sans MS', 11), 
                       foreground='#ff69b4',
                       background='#ffe6f2')
        
        style.configure('Error.TLabel', 
                       font=('Comic Sans MS', 11), 
                       foreground='#ff1493',
                       background='#ffe6f2')
        
        # Frame styles with semi-transparent background
        style.configure('Card.TFrame', 
                       background='#fff0f5',
                       relief='solid',
                       borderwidth=2)
        
        # Button styles
        style.configure('Primary.TButton', 
                       font=('Comic Sans MS', 12, 'bold'),
                       background='#ff69b4',
                       foreground='white')
        
        style.configure('Success.TButton', 
                       font=('Comic Sans MS', 11),
                       background='#ff1493',
                       foreground='white')
        
        style.configure('Warning.TButton', 
                       font=('Comic Sans MS', 11),
                       background='#ffb6c1',
                       foreground='white')
        
        # Progress bar style
        style.configure('Custom.Horizontal.TProgressbar',
                       background='#ff69b4',
                       troughcolor='#ffe6f2')
        
    def create_widgets(self):
        # Main frame with transparent background to show Hello Kitty image
        main_frame = tk.Frame(self.root, bg='#ffe6f2', padx=40, pady=40)  # Same as root background
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title with Hello Kitty styling
        title_frame = tk.Frame(main_frame, bg='#ffe6f2')
        title_frame.pack(fill=tk.X, pady=(0, 30))
        
        title_label = tk.Label(title_frame, 
                              text="🎀 Hello Kitty Schedule Generator 🎀", 
                              font=("Comic Sans MS", 26, "bold"),
                              fg='#ff69b4',
                              bg='#ffe6f2')
        title_label.pack()
        
        subtitle_label = tk.Label(title_frame,
                                 text="✨ Create magical work schedules with Hello Kitty ✨",
                                 font=("Comic Sans MS", 14),
                                 fg='#ff1493',
                                 bg='#ffe6f2')
        subtitle_label.pack(pady=(8, 0))
        
        # Mode selection with Hello Kitty card design
        mode_frame = tk.Frame(main_frame, bg='#fff8fa', relief='solid', bd=2, padx=25, pady=25)
        mode_frame.pack(fill=tk.X, pady=(0, 20))
        
        mode_title = tk.Label(mode_frame, text="🎀 Choose Your Magic Mode 🎀", 
                             font=("Comic Sans MS", 16, "bold"),
                             fg='#ff69b4',
                             bg='#fff8fa')
        mode_title.pack(anchor=tk.W, pady=(0, 15))
        
        self.mode_var = tk.StringVar(value="1")
        
        # Mode 1
        mode1_frame = tk.Frame(mode_frame, bg='#fff8fa')
        mode1_frame.pack(fill=tk.X, pady=8)
        
        mode1_radio = tk.Radiobutton(mode1_frame, 
                                   text="🌸 Mode 1: Input total weekly hours", 
                                   variable=self.mode_var, 
                                   value="1", 
                                   command=self.on_mode_change,
                                   font=("Comic Sans MS", 12),
                                   fg='#ff1493',
                                   bg='#fff8fa',
                                   selectcolor='#ff69b4')
        mode1_radio.pack(anchor=tk.W)
        
        mode1_desc = tk.Label(mode1_frame, 
                             text="   ✨ Specify weekly hours and total number of days",
                             font=("Comic Sans MS", 10),
                             fg='#c71585',
                             bg='#fff8fa')
        mode1_desc.pack(anchor=tk.W, padx=(25, 0))
        
        # Mode 2
        mode2_frame = tk.Frame(mode_frame, bg='#fff8fa')
        mode2_frame.pack(fill=tk.X, pady=8)
        
        mode2_radio = tk.Radiobutton(mode2_frame, 
                                   text="🎀 Mode 2: Input total overall hours", 
                                   variable=self.mode_var, 
                                   value="2", 
                                   command=self.on_mode_change,
                                   font=("Comic Sans MS", 12),
                                   fg='#ff1493',
                                   bg='#fff8fa',
                                   selectcolor='#ff69b4')
        mode2_radio.pack(anchor=tk.W)
        
        mode2_desc = tk.Label(mode2_frame, 
                             text="   ✨ System will automatically distribute across weeks",
                             font=("Comic Sans MS", 10),
                             fg='#c71585',
                             bg='#fff8fa')
        mode2_desc.pack(anchor=tk.W, padx=(25, 0))
        
        # Input parameters with Hello Kitty card design
        input_frame = tk.Frame(main_frame, bg='#fff8fa', relief='solid', bd=2, padx=25, pady=25)
        input_frame.pack(fill=tk.X, pady=(0, 20))
        
        input_title = tk.Label(input_frame, text="🌸 Schedule Parameters 🌸", 
                              font=("Comic Sans MS", 16, "bold"),
                              fg='#ff69b4',
                              bg='#fff8fa')
        input_title.pack(anchor=tk.W, pady=(0, 15))
        
        # Create a grid for input fields
        input_grid = tk.Frame(input_frame, bg='#fff8fa')
        input_grid.pack(fill=tk.X)
        
        # Start date
        tk.Label(input_grid, text="🎀 Start Date (YYYY-MM-DD):", 
                font=("Comic Sans MS", 12, "bold"),
                fg='#ff1493',
                bg='#fff8fa').grid(row=0, column=0, sticky=tk.W, pady=10, padx=(0, 25))
        
        self.date_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
        self.date_entry = tk.Entry(input_grid, textvariable=self.date_var, 
                                 font=("Comic Sans MS", 11),
                                 width=18,
                                 relief='solid',
                                 bd=2,
                                 bg='#fff8fa')
        self.date_entry.grid(row=0, column=1, sticky=tk.W, pady=10)
        
        # Start week
        tk.Label(input_grid, text="🎀 Starting Week Number:", 
                font=("Comic Sans MS", 12, "bold"),
                fg='#ff1493',
                bg='#fff8fa').grid(row=1, column=0, sticky=tk.W, pady=10, padx=(0, 25))
        
        self.week_var = tk.StringVar(value="1")
        self.week_entry = tk.Entry(input_grid, textvariable=self.week_var, 
                                 font=("Comic Sans MS", 11),
                                 width=18,
                                 relief='solid',
                                 bd=2,
                                 bg='#fff8fa')
        self.week_entry.grid(row=1, column=1, sticky=tk.W, pady=10)
        
        # Hours input
        tk.Label(input_grid, text="🌸 Total Hours:", 
                font=("Comic Sans MS", 12, "bold"),
                fg='#ff1493',
                bg='#fff8fa').grid(row=2, column=0, sticky=tk.W, pady=10, padx=(0, 25))
        
        self.hours_var = tk.StringVar(value="10")
        self.hours_entry = tk.Entry(input_grid, textvariable=self.hours_var, 
                                  font=("Comic Sans MS", 11),
                                  width=18,
                                  relief='solid',
                                  bd=2,
                                  bg='#fff8fa')
        self.hours_entry.grid(row=2, column=1, sticky=tk.W, pady=10)
        
        # Days input (for mode 1)
        self.days_label = tk.Label(input_grid, text="🎀 Total Days:", 
                                  font=("Comic Sans MS", 12, "bold"),
                                  fg='#ff1493',
                                  bg='#fff8fa')
        self.days_label.grid(row=3, column=0, sticky=tk.W, pady=10, padx=(0, 25))
        
        self.days_var = tk.StringVar(value="7")
        self.days_entry = tk.Entry(input_grid, textvariable=self.days_var, 
                                 font=("Comic Sans MS", 11),
                                 width=18,
                                 relief='solid',
                                 bd=2,
                                 bg='#fff8fa')
        self.days_entry.grid(row=3, column=1, sticky=tk.W, pady=10)
        
        # Output settings with Hello Kitty card design
        output_frame = tk.Frame(main_frame, bg='#fff8fa', relief='solid', bd=2, padx=35, pady=35)
        output_frame.pack(fill=tk.X, pady=(0, 25))
        
        output_title = tk.Label(output_frame, text="🎀 Output Settings 🎀", 
                               font=("Comic Sans MS", 16, "bold"),
                               fg='#ff69b4',
                               bg='#fff8fa')
        output_title.pack(anchor=tk.W, pady=(0, 20))
        
        # Filename section
        filename_section = tk.Frame(output_frame, bg='#fff8fa')
        filename_section.pack(fill=tk.X, pady=(0, 20))
        
        tk.Label(filename_section, text="🌸 Output Filename:", 
                font=("Comic Sans MS", 12, "bold"),
                fg='#ff1493',
                bg='#fff8fa').pack(anchor=tk.W, pady=(0, 12))
        
        filename_input_frame = tk.Frame(filename_section, bg='#fff8fa')
        filename_input_frame.pack(fill=tk.X)
        
        self.filename_var = tk.StringVar(value="hello_kitty_schedule")
        self.filename_entry = tk.Entry(filename_input_frame, textvariable=self.filename_var, 
                                     font=("Comic Sans MS", 11),
                                     width=32,
                                     relief='solid',
                                     bd=2,
                                     bg='#fff8fa')
        self.filename_entry.pack(side=tk.LEFT, padx=(0, 15))
        
        browse_btn = tk.Button(filename_input_frame, text="🎀 Browse", 
                              command=self.browse_location,
                              font=("Comic Sans MS", 10),
                              bg='#ffb6c1',
                              fg='white',
                              relief='flat',
                              padx=20,
                              pady=8)
        browse_btn.pack(side=tk.LEFT)
        
        # Export options section
        export_section = tk.Frame(output_frame, bg='#fff8fa')
        export_section.pack(fill=tk.X, pady=(0, 10))
        
        tk.Label(export_section, text="🌸 Export Formats:", 
                font=("Comic Sans MS", 12, "bold"),
                fg='#ff1493',
                bg='#fff8fa').pack(anchor=tk.W, pady=(0, 15))
        
        export_options_frame = tk.Frame(export_section, bg='#fff8fa')
        export_options_frame.pack(fill=tk.X)
        
        self.export_txt = tk.BooleanVar(value=True)
        self.export_xlsx = tk.BooleanVar(value=True)
        self.export_docx = tk.BooleanVar(value=True)
        
        # Export checkboxes with Hello Kitty styling
        txt_cb = tk.Checkbutton(export_options_frame, text="🌸 Text (.txt)", 
                               variable=self.export_txt,
                               font=("Comic Sans MS", 11),
                               fg='#ff1493',
                               bg='#fff8fa',
                               selectcolor='#ff69b4')
        txt_cb.pack(side=tk.LEFT, padx=(0, 30))
        
        xlsx_cb = tk.Checkbutton(export_options_frame, text="🎀 Excel (.xlsx)", 
                                variable=self.export_xlsx,
                                font=("Comic Sans MS", 11),
                                fg='#ff1493',
                                bg='#fff8fa',
                                selectcolor='#ff69b4')
        xlsx_cb.pack(side=tk.LEFT, padx=(0, 30))
        
        docx_cb = tk.Checkbutton(export_options_frame, text="🌸 Word (.docx)", 
                                variable=self.export_docx,
                                font=("Comic Sans MS", 11),
                                fg='#ff1493',
                                bg='#fff8fa',
                                selectcolor='#ff69b4')
        docx_cb.pack(side=tk.LEFT, padx=(0, 10))
        
        # Action buttons with Hello Kitty styling
        button_frame = tk.Frame(main_frame, bg='#ffe6f2')
        button_frame.pack(fill=tk.X, pady=(10, 25))
        
        # Generate button (primary action)
        generate_btn = tk.Button(button_frame, text="🌸 Generate Magic Schedule 🌸", 
                                command=self.generate_schedule,
                                font=("Comic Sans MS", 13, "bold"),
                                bg='#ff69b4',
                                fg='white',
                                relief='flat',
                                padx=35,
                                pady=15,
                                cursor='hand2')
        generate_btn.pack(side=tk.LEFT, padx=(0, 25))
        
        # Clear button
        clear_btn = tk.Button(button_frame, text="🎀 Clear Form", 
                             command=self.clear_form,
                             font=("Comic Sans MS", 12),
                             bg='#ffb6c1',
                             fg='white',
                             relief='flat',
                             padx=25,
                             pady=12,
                             cursor='hand2')
        clear_btn.pack(side=tk.LEFT, padx=(0, 25))
        
        # Exit button
        exit_btn = tk.Button(button_frame, text="🌸 Exit", 
                            command=self.root.quit,
                            font=("Comic Sans MS", 12),
                            bg='#ffc0cb',
                            fg='white',
                            relief='flat',
                            padx=25,
                            pady=12,
                            cursor='hand2')
        exit_btn.pack(side=tk.LEFT)
        
        # Information section with Hello Kitty card design
        info_frame = tk.Frame(main_frame, bg='#fff8fa', relief='solid', bd=2, padx=25, pady=25)
        info_frame.pack(fill=tk.X, pady=(0, 20))
        
        info_title = tk.Label(info_frame, text="🌸 Hello Kitty Tips & Information 🌸", 
                             font=("Comic Sans MS", 16, "bold"),
                             fg='#ff69b4',
                             bg='#fff8fa')
        info_title.pack(anchor=tk.W, pady=(0, 15))
        
        info_text = """🎀 Mode 1: Specify weekly hours and total number of days
🌸 Mode 2: Specify total overall hours (auto-distributed across weeks)
✨ Time slots: 30-minute increments between 09:00-18:00
🎀 Daily work: 30-120 minutes per day
🌸 Maximum: 15 hours per week
✨ All times rounded to 30-minute units for consistency"""
        
        info_label = tk.Label(info_frame, text=info_text, 
                             font=("Comic Sans MS", 11),
                             fg='#c71585',
                             bg='#fff8fa',
                             justify=tk.LEFT,
                             anchor=tk.W)
        info_label.pack(anchor=tk.W)
        
        # Progress bar with Hello Kitty styling
        progress_frame = tk.Frame(main_frame, bg='#ffe6f2')
        progress_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.progress = ttk.Progressbar(progress_frame, 
                                      mode='indeterminate',
                                      style='Custom.Horizontal.TProgressbar',
                                      length=450)
        self.progress.pack(pady=12)
        
        # Status label with Hello Kitty styling
        status_frame = tk.Frame(main_frame, bg='#ffe6f2')
        status_frame.pack(fill=tk.X)
        
        self.status_var = tk.StringVar(value="🌸 Ready to create your magical Hello Kitty schedule! 🌸")
        status_label = tk.Label(status_frame, 
                               textvariable=self.status_var, 
                               font=("Comic Sans MS", 12),
                               fg='#ff69b4',
                               bg='#ffe6f2')
        status_label.pack(pady=8)
        
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
        self.status_var.set("🌸 Creating your magical Hello Kitty schedule... 🌸")
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
            
            self.status_var.set("🌸 Hello Kitty schedule created successfully! 🌸")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to generate schedule:\n{str(e)}")
            self.status_var.set("🌸 Oops! Something went wrong with the magic... 🌸")
        
        finally:
            self.progress.stop()
    
    def clear_form(self):
        """Clear all form fields"""
        self.date_var.set(datetime.now().strftime("%Y-%m-%d"))
        self.week_var.set("1")
        self.hours_var.set("10")
        self.days_var.set("7")
        self.filename_var.set("hello_kitty_schedule")
        self.export_txt.set(True)
        self.export_xlsx.set(True)
        self.export_docx.set(True)
        self.status_var.set("🌸 Ready to create your magical Hello Kitty schedule! 🌸")

def main():
    root = tk.Tk()
    app = ScheduleGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 