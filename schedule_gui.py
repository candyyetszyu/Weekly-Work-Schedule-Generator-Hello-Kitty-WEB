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
        self.root.geometry("650x750")
        self.root.resizable(True, True)
        
        # Set window icon and configure
        self.root.configure(bg='#ffe6f2')  # Light pink background
        
        # Load Hello Kitty element
        self.load_hello_kitty_element()
        
        # Configure Hello Kitty style
        self.setup_styles()
        
        self.create_widgets()
        
    def load_hello_kitty_element(self):
        """Load Hello Kitty element/icon"""
        try:
            # Look for common Hello Kitty image files
            possible_files = ['hello_kitty.png', 'hello_kitty.jpg', 'hello_kitty.jpeg', 
                            'hellokitty.png', 'hellokitty.jpg', 'hk.png', 'kitty.png']
            
            for filename in possible_files:
                if os.path.exists(filename):
                    # Load and resize the Hello Kitty element
                    hk_image = Image.open(filename)
                    # Resize to small icon size (80x80)
                    hk_image = hk_image.resize((80, 80), Image.Resampling.LANCZOS)
                    self.hk_photo = ImageTk.PhotoImage(hk_image)
                    print(f"🌸 Hello Kitty element loaded: {filename}")
                    return
                    
            print("⚠️ No Hello Kitty image found. Please place a Hello Kitty image file in the directory.")
            self.hk_photo = None
                
        except Exception as e:
            print(f"⚠️ Could not load Hello Kitty element: {e}")
            self.hk_photo = None
        
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
        # Create main canvas with scrollbar
        self.canvas = tk.Canvas(self.root, bg='#ffe6f2', highlightthickness=0)
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        scrollable_frame = tk.Frame(self.canvas, bg='#ffe6f2')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Main frame with equal padding on left and right
        main_frame = tk.Frame(scrollable_frame, bg='#ffe6f2', padx=20, pady=15)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title with Hello Kitty styling
        title_frame = tk.Frame(main_frame, bg='#ffe6f2')
        title_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Create a horizontal frame for title and Hello Kitty element
        title_content = tk.Frame(title_frame, bg='#ffe6f2')
        title_content.pack()
        
        # Add Hello Kitty element if available
        if hasattr(self, 'hk_photo') and self.hk_photo:
            hk_label = tk.Label(title_content, image=self.hk_photo, bg='#ffe6f2')
            hk_label.pack(side=tk.LEFT, padx=(0, 15))
        
        # Title text frame
        title_text_frame = tk.Frame(title_content, bg='#ffe6f2')
        title_text_frame.pack(side=tk.LEFT)
        
        title_label = tk.Label(title_text_frame, 
                              text="🎀 Hello Kitty Schedule Generator 🎀", 
                              font=("Comic Sans MS", 18, "bold"),
                              fg='#ff69b4',
                              bg='#ffe6f2')
        title_label.pack()
        
        subtitle_label = tk.Label(title_text_frame,
                                 text="✨ Create magical work schedules with Hello Kitty ✨",
                                 font=("Comic Sans MS", 11),
                                 fg='#ff1493',
                                 bg='#ffe6f2')
        subtitle_label.pack(pady=(3, 0))
        
        # Mode selection with Hello Kitty card design
        mode_frame = tk.Frame(main_frame, bg='#fff8fa', relief='solid', bd=2, padx=25, pady=15)
        mode_frame.pack(fill=tk.X, pady=(0, 10))
        
        mode_title = tk.Label(mode_frame, text="🎀 Choose Your Magic Mode 🎀", 
                             font=("Comic Sans MS", 14, "bold"),
                             fg='#ff69b4',
                             bg='#fff8fa')
        mode_title.pack(anchor=tk.W, pady=(0, 8))
        
        self.mode_var = tk.StringVar(value="1")
        
        # Mode 1
        mode1_frame = tk.Frame(mode_frame, bg='#fff8fa')
        mode1_frame.pack(fill=tk.X, pady=3)
        
        mode1_radio = tk.Radiobutton(mode1_frame, 
                                   text="🌸 Mode 1: Input total weekly hours", 
                                   variable=self.mode_var, 
                                   value="1", 
                                   command=self.on_mode_change,
                                   font=("Comic Sans MS", 11),
                                   fg='#ff1493',
                                   bg='#fff8fa',
                                   selectcolor='#ff69b4')
        mode1_radio.pack(anchor=tk.W)
        
        mode1_desc = tk.Label(mode1_frame, 
                             text="   ✨ Specify weekly hours and total number of days",
                             font=("Comic Sans MS", 9),
                             fg='#c71585',
                             bg='#fff8fa')
        mode1_desc.pack(anchor=tk.W, padx=(20, 0))
        
        # Mode 2
        mode2_frame = tk.Frame(mode_frame, bg='#fff8fa')
        mode2_frame.pack(fill=tk.X, pady=3)
        
        mode2_radio = tk.Radiobutton(mode2_frame, 
                                   text="🎀 Mode 2: Input total overall hours", 
                                   variable=self.mode_var, 
                                   value="2", 
                                   command=self.on_mode_change,
                                   font=("Comic Sans MS", 11),
                                   fg='#ff1493',
                                   bg='#fff8fa',
                                   selectcolor='#ff69b4')
        mode2_radio.pack(anchor=tk.W)
        
        mode2_desc = tk.Label(mode2_frame, 
                             text="   ✨ System will automatically distribute across weeks",
                             font=("Comic Sans MS", 9),
                             fg='#c71585',
                             bg='#fff8fa')
        mode2_desc.pack(anchor=tk.W, padx=(20, 0))
        
        # Input parameters with Hello Kitty card design
        input_frame = tk.Frame(main_frame, bg='#fff8fa', relief='solid', bd=2, padx=25, pady=15)
        input_frame.pack(fill=tk.X, pady=(0, 10))
        
        input_title = tk.Label(input_frame, text="🌸 Schedule Parameters 🌸", 
                              font=("Comic Sans MS", 14, "bold"),
                              fg='#ff69b4',
                              bg='#fff8fa')
        input_title.pack(anchor=tk.W, pady=(0, 8))
        
        # Create a grid for input fields
        input_grid = tk.Frame(input_frame, bg='#fff8fa')
        input_grid.pack(fill=tk.X)
        
        # Start date
        tk.Label(input_grid, text="🎀 Start Date (YYYY-MM-DD):", 
                font=("Comic Sans MS", 11, "bold"),
                fg='#ff1493',
                bg='#fff8fa').grid(row=0, column=0, sticky=tk.W, pady=5, padx=(0, 20))
        
        self.date_var = tk.StringVar(value=datetime.now().strftime("%Y-%m-%d"))
        self.date_entry = tk.Entry(input_grid, textvariable=self.date_var, 
                                 font=("Comic Sans MS", 10),
                                 width=16,
                                 relief='solid',
                                 bd=1,
                                 bg='white')
        self.date_entry.grid(row=0, column=1, sticky=tk.W, pady=5)
        
        # Start week
        tk.Label(input_grid, text="🎀 Starting Week Number:", 
                font=("Comic Sans MS", 11, "bold"),
                fg='#ff1493',
                bg='#fff8fa').grid(row=1, column=0, sticky=tk.W, pady=5, padx=(0, 20))
        
        self.week_var = tk.StringVar(value="1")
        self.week_entry = tk.Entry(input_grid, textvariable=self.week_var, 
                                 font=("Comic Sans MS", 10),
                                 width=16,
                                 relief='solid',
                                 bd=1,
                                 bg='white')
        self.week_entry.grid(row=1, column=1, sticky=tk.W, pady=5)
        
        # Hours input
        tk.Label(input_grid, text="🌸 Total Hours:", 
                font=("Comic Sans MS", 11, "bold"),
                fg='#ff1493',
                bg='#fff8fa').grid(row=2, column=0, sticky=tk.W, pady=5, padx=(0, 20))
        
        self.hours_var = tk.StringVar(value="10")
        self.hours_entry = tk.Entry(input_grid, textvariable=self.hours_var, 
                                  font=("Comic Sans MS", 10),
                                  width=16,
                                  relief='solid',
                                  bd=1,
                                  bg='white')
        self.hours_entry.grid(row=2, column=1, sticky=tk.W, pady=5)
        
        # Days input (for mode 1)
        self.days_label = tk.Label(input_grid, text="🎀 Total Days:", 
                                  font=("Comic Sans MS", 11, "bold"),
                                  fg='#ff1493',
                                  bg='#fff8fa')
        self.days_label.grid(row=3, column=0, sticky=tk.W, pady=5, padx=(0, 20))
        
        self.days_var = tk.StringVar(value="7")
        self.days_entry = tk.Entry(input_grid, textvariable=self.days_var, 
                                 font=("Comic Sans MS", 10),
                                 width=16,
                                 relief='solid',
                                 bd=1,
                                 bg='white')
        self.days_entry.grid(row=3, column=1, sticky=tk.W, pady=5)
        
        # Output settings with Hello Kitty card design
        output_frame = tk.Frame(main_frame, bg='#fff8fa', relief='solid', bd=2, padx=25, pady=15)
        output_frame.pack(fill=tk.X, pady=(0, 10))
        
        output_title = tk.Label(output_frame, text="🎀 Output Settings 🎀", 
                               font=("Comic Sans MS", 14, "bold"),
                               fg='#ff69b4',
                               bg='#fff8fa')
        output_title.pack(anchor=tk.W, pady=(0, 8))
        
        # Create grid layout for better organization
        settings_grid = tk.Frame(output_frame, bg='#fff8fa')
        settings_grid.pack(fill=tk.X)
        
        # Row 1: Filename
        tk.Label(settings_grid, text="🌸 Filename:", 
                font=("Comic Sans MS", 11, "bold"),
                fg='#ff1493',
                bg='#fff8fa').grid(row=0, column=0, sticky=tk.W, pady=5, padx=(0, 15))
        
        self.filename_var = tk.StringVar(value="hello_kitty_schedule")
        self.filename_entry = tk.Entry(settings_grid, textvariable=self.filename_var, 
                                     font=("Comic Sans MS", 10),
                                     width=18,
                                     relief='solid',
                                     bd=1,
                                     bg='white')
        self.filename_entry.grid(row=0, column=1, sticky=tk.W, pady=5, padx=(0, 10))
        
        browse_btn = tk.Button(settings_grid, text="Browse", 
                              command=self.browse_location,
                              font=("Comic Sans MS", 9),
                              bg='#ff69b4',
                              fg='white',
                              activebackground='#ff1493',
                              activeforeground='white',
                              relief='raised',
                              bd=1,
                              padx=12,
                              pady=3,
                              cursor='hand2')
        browse_btn.grid(row=0, column=2, sticky=tk.W, pady=5)
        
        # Row 2: Export formats label
        tk.Label(settings_grid, text="🎀 Export as:", 
                font=("Comic Sans MS", 11, "bold"),
                fg='#ff1493',
                bg='#fff8fa').grid(row=1, column=0, sticky=tk.W, pady=(8, 3), padx=(0, 15))
        
        # Row 3: Export checkboxes
        export_frame = tk.Frame(settings_grid, bg='#fff8fa')
        export_frame.grid(row=2, column=0, columnspan=3, sticky=tk.W, pady=(0, 3))
        
        self.export_txt = tk.BooleanVar(value=True)
        self.export_xlsx = tk.BooleanVar(value=True)
        self.export_docx = tk.BooleanVar(value=True)
        
        # Export checkboxes in a more compact layout
        txt_cb = tk.Checkbutton(export_frame, text="📄 Text", 
                               variable=self.export_txt,
                               font=("Comic Sans MS", 10),
                               fg='#c71585',
                               bg='#fff8fa',
                               selectcolor='#ff69b4',
                               activebackground='#fff8fa')
        txt_cb.pack(side=tk.LEFT, padx=(0, 25))
        
        xlsx_cb = tk.Checkbutton(export_frame, text="📊 Excel", 
                                variable=self.export_xlsx,
                                font=("Comic Sans MS", 10),
                                fg='#c71585',
                                bg='#fff8fa',
                                selectcolor='#ff69b4',
                                activebackground='#fff8fa')
        xlsx_cb.pack(side=tk.LEFT, padx=(0, 25))
        
        docx_cb = tk.Checkbutton(export_frame, text="📝 Word", 
                                variable=self.export_docx,
                                font=("Comic Sans MS", 10),
                                fg='#c71585',
                                bg='#fff8fa',
                                selectcolor='#ff69b4',
                                activebackground='#fff8fa')
        docx_cb.pack(side=tk.LEFT)
        
        # Action buttons with Hello Kitty styling
        button_frame = tk.Frame(main_frame, bg='#ffe6f2')
        button_frame.pack(fill=tk.X, pady=(5, 10))
        
        # Generate button (primary action) - special Hello Kitty magic color
        generate_btn = tk.Button(button_frame, text="🌸 Generate Magic Schedule 🌸", 
                                command=self.generate_schedule,
                                font=("Comic Sans MS", 11, "bold"),
                                bg='#ff1493',  # Deep pink - very distinct magic color
                                fg='#000080',
                                activebackground='#dc143c',  # Crimson when pressed
                                activeforeground='white',
                                relief='raised',
                                bd=3,
                                padx=20,
                                pady=8,
                                cursor='hand2')
        generate_btn.pack(side=tk.LEFT, padx=(0, 12))
        
        # Clear button - soft mint theme
        clear_btn = tk.Button(button_frame, text="🎀 Clear Form", 
                             command=self.clear_form,
                             font=("Comic Sans MS", 10),
                             bg='#98fb98',  # Pale green
                             fg='#000080',  # Dark green text
                             activebackground='#90ee90',
                             activeforeground='#006400',
                             relief='raised',
                             bd=2,
                             padx=18,
                             pady=8,
                             cursor='hand2')
        clear_btn.pack(side=tk.LEFT, padx=(0, 12))
        
        # Exit button - soft sky blue theme
        exit_btn = tk.Button(button_frame, text="🌸 Exit", 
                            command=self.root.quit,
                            font=("Comic Sans MS", 10),
                            bg='#87ceeb',  # Sky blue
                            fg='#000080',  # Navy blue text
                            activebackground='#87cefa',
                            activeforeground='#000080',
                            relief='raised',
                            bd=2,
                            padx=18,
                            pady=8,
                            cursor='hand2')
        exit_btn.pack(side=tk.LEFT)
        
        # Information section with Hello Kitty card design
        info_frame = tk.Frame(main_frame, bg='#fff8fa', relief='solid', bd=2, padx=25, pady=10)
        info_frame.pack(fill=tk.X, pady=(0, 10))
        
        info_title = tk.Label(info_frame, text="🌸 Hello Kitty Tips & Information 🌸", 
                             font=("Comic Sans MS", 12, "bold"),
                             fg='#ff69b4',
                             bg='#fff8fa')
        info_title.pack(anchor=tk.W, pady=(0, 5))
        
        info_text = """🎀 Mode 1: Specify weekly hours and total number of days
🌸 Mode 2: Specify total overall hours (auto-distributed across weeks)
✨ Time slots: 30-minute increments between 09:00-18:00
🎀 Daily work: 30-120 minutes per day, Maximum: 15 hours per week"""
        
        info_label = tk.Label(info_frame, text=info_text, 
                             font=("Comic Sans MS", 9),
                             fg='#c71585',
                             bg='#fff8fa',
                             justify=tk.LEFT,
                             anchor=tk.W)
        info_label.pack(anchor=tk.W)
        
        # Progress bar with Hello Kitty styling
        progress_frame = tk.Frame(main_frame, bg='#ffe6f2')
        progress_frame.pack(fill=tk.X, pady=(5, 5))
        
        self.progress = ttk.Progressbar(progress_frame, 
                                      mode='indeterminate',
                                      style='Custom.Horizontal.TProgressbar',
                                      length=300)
        self.progress.pack(pady=5)
        
        # Status label with Hello Kitty styling
        status_frame = tk.Frame(main_frame, bg='#ffe6f2')
        status_frame.pack(fill=tk.X)
        
        self.status_var = tk.StringVar(value="🌸 Ready to create your magical Hello Kitty schedule! 🌸")
        status_label = tk.Label(status_frame, 
                               textvariable=self.status_var, 
                               font=("Comic Sans MS", 10),
                               fg='#ff69b4',
                               bg='#ffe6f2')
        status_label.pack(pady=5)
        
        # Add mouse wheel scrolling to canvas
        def _on_mousewheel(event):
            self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")
        self.canvas.bind_all("<MouseWheel>", _on_mousewheel)
        
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
                
                # Call the original function with export format selections
                generate_schedule_cli_copy.generate_schedule(
                    start_date, total_hours, total_days, filename, start_week,
                    self.export_txt.get(), self.export_xlsx.get(), self.export_docx.get()
                )
                
            else:  # mode 2
                total_overall_hours = float(self.hours_var.get())
                
                # Call the total hours function with export format selections
                generate_schedule_cli_copy.generate_schedule_total_hours(
                    start_date, total_overall_hours, filename, start_week,
                    self.export_txt.get(), self.export_xlsx.get(), self.export_docx.get()
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