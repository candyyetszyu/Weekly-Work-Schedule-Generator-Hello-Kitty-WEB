# 🎀 Weekly Work Schedule Generator - Hello Kitty Edition 🌸

A magical and adorable schedule generator that creates personalized work schedules with a beautiful Hello Kitty theme! This application helps you generate weekly work schedules with customizable hours, time slots, and multiple export formats.

## ✨ Features

### 🎯 Core Functionality
- **Two Generation Modes**:
  - **Mode 1**: Weekly hours + total days
  - **Mode 2**: Total overall hours (automatically calculates weeks needed)
- **Smart Time Distribution**: Automatically splits hours across days and weeks
- **30-Minute Units**: All calculations use 30-minute increments for precision
- **Time Constraints**: 
  - Maximum 15 hours per week
  - 30-120 minutes per day
  - Work hours: 09:00-18:00

### 🎨 Beautiful Hello Kitty GUI
- **Adorable Pink Theme**: Complete Hello Kitty styling with pink color palette
- **Background Image**: Custom Hello Kitty background with hearts and stars
- **User-Friendly Interface**: Easy-to-use form with clear sections
- **Real-time Validation**: Input validation with helpful error messages
- **Progress Indicators**: Visual feedback during schedule generation

### 📁 Multiple Export Formats
- **Text (.txt)**: Simple text format for easy reading
- **Excel (.xlsx)**: Structured spreadsheet with formatting
- **Word (.docx)**: Professional table format with weekly summaries

### 🚀 Dual Interface Options
- **GUI Version**: Beautiful Hello Kitty themed graphical interface
- **CLI Version**: Command-line interface for quick automation

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Required Packages
```bash
pip install pandas openpyxl python-docx Pillow
```

### Quick Setup
1. Clone the repository:
```bash
git clone https://github.com/candyyetszyu/Weekly-Work-Schedule-Generator-Hello-Kitty.git
cd Weekly-Work-Schedule-Generator-Hello-Kitty
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Quick Start

### Option 1: Launcher (Recommended)
```bash
python3 launcher.py
```
Choose between GUI and CLI versions from the menu.

### Option 2: Direct GUI Launch
```bash
python3 schedule_gui.py
```

### Option 3: Direct CLI Launch
```bash
python3 generate_schedule_cli_copy.py
```

## 📖 Usage Guide

### GUI Interface

#### 🎀 Hello Kitty GUI Features
- **Mode Selection**: Choose between weekly hours or total hours mode
- **Input Fields**: 
  - Start Date (YYYY-MM-DD format)
  - Starting Week Number
  - Total Hours (Mode 2) or Weekly Hours + Days (Mode 1)
- **Output Settings**:
  - Custom filename
  - Export format selection (TXT, XLSX, DOCX)
  - Browse button for save location
- **Action Buttons**:
  - Generate Magic Schedule
  - Clear Form
  - Exit

#### 🌸 GUI Styling
- **Color Palette**: Pink theme (#ff69b4, #ff1493, #c71585, #ffb6c1)
- **Font**: Comic Sans MS for that cute Hello Kitty feel
- **Background**: Custom Hello Kitty image with decorative elements
- **Icons**: Emojis throughout the interface (🌸, 🎀, ✨)

### CLI Interface

#### Mode 1: Weekly Hours + Days
```bash
Enter mode (1 for weekly hours + days, 2 for total overall hours): 1
Enter start date (YYYY-MM-DD): 2024-01-01
Enter weekly hours: 10
Enter total days: 7
Enter starting week number: 1
Enter output filename: my_schedule
```

#### Mode 2: Total Overall Hours
```bash
Enter mode (1 for weekly hours + days, 2 for total overall hours): 2
Enter start date (YYYY-MM-DD): 2024-01-01
Enter total overall hours: 25
Enter starting week number: 1
Enter output filename: my_schedule
```

## 📊 Output Formats

### Text (.txt) Format
```
Week 1 (January 1 - January 7)
Monday, January 1: 1h 30m | 09:00-10:30
Tuesday, January 2: 1h 30m | 14:00-15:30
Wednesday, January 3: 1h 30m | 10:00-11:30
...
Total work time: 10.00 hours
```

### Excel (.xlsx) Format
- **Sheet 1**: Daily schedule with columns for Date, Day, Time, Hours
- **Sheet 2**: Weekly summary with total hours per week
- **Formatting**: Clean table layout with borders and headers

### Word (.docx) Format
- **Table Structure**: 
  - Week column
  - Date column (with daily dates on new lines)
  - Schedule column (with daily times on new lines)
  - Hours column (with daily hours on new lines)
- **Professional Layout**: Formatted table with proper spacing
- **Summary**: Total work time at the bottom

## ⚙️ Configuration

### Time Constraints
- **Maximum Weekly Hours**: 15 hours
- **Daily Time Range**: 30-120 minutes
- **Work Hours**: 09:00-18:00
- **Time Unit**: 30-minute increments

### File Locations
- **Default Save Location**: Current directory
- **Custom Location**: Use browse button in GUI or specify path in CLI
- **File Naming**: Customizable filename with automatic format extensions

## 🎨 Customization

### Hello Kitty Theme
The GUI uses a custom Hello Kitty theme with:
- **Background Image**: `hello_kitty_bg.png` (generated programmatically)
- **Color Scheme**: Various shades of pink
- **Font**: Comic Sans MS for that cute aesthetic
- **Icons**: Emojis and decorative elements

### Background Image
The Hello Kitty background is generated using `create_hello_kitty_bg.py`:
- **Size**: 800x900 pixels
- **Elements**: Hello Kitty face, bow, whiskers, hearts, stars
- **Colors**: Pink background with white and pink Hello Kitty elements

## 📁 Project Structure

```
Weekly-Work-Schedule-Generator-Hello-Kitty/
├── generate_schedule_cli_copy.py    # Core schedule generation logic
├── schedule_gui.py                  # Hello Kitty themed GUI
├── launcher.py                      # Interface launcher
├── create_hello_kitty_bg.py        # Background image generator
├── hello_kitty_bg.png              # Hello Kitty background image
├── README.md                        # This documentation
├── .gitignore                       # Git ignore rules
└── requirements.txt                 # Python dependencies
```

## 🔧 Technical Details

### Core Functions
- `generate_schedule()`: Main schedule generation logic
- `generate_schedule_total_hours()`: Mode 2 implementation
- `split_weekly_minutes()`: Time distribution algorithm
- `generate_random_time_slots()`: Random time slot generation

### GUI Components
- `ScheduleGeneratorGUI`: Main GUI class
- `setup_background()`: Background image loading
- `setup_styles()`: Hello Kitty theme configuration
- `create_widgets()`: Interface layout creation

### Export Functions
- **Text Export**: Simple string formatting
- **Excel Export**: Using pandas and openpyxl
- **Word Export**: Using python-docx with table formatting

## 🐛 Troubleshooting

### Common Issues

#### GUI Not Starting
```bash
# Check Python version
python3 --version

# Install missing dependencies
pip install pandas openpyxl python-docx Pillow

# Check file permissions
chmod +x schedule_gui.py
```

#### Background Image Not Loading
- Ensure `hello_kitty_bg.png` exists in the project directory
- Run `python3 create_hello_kitty_bg.py` to regenerate the image
- Check PIL/Pillow installation

#### Export Errors
- Ensure all required packages are installed
- Check write permissions in the target directory
- Verify filename doesn't contain invalid characters

### Error Messages
- **"Total overall hours must be at least 0.5 hours"**: Increase the minimum hours
- **"Invalid date format"**: Use YYYY-MM-DD format
- **"File not found"**: Check file paths and permissions

## 🤝 Contributing

We welcome contributions to make the Hello Kitty Schedule Generator even more magical!

### How to Contribute
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Development Setup
```bash
git clone https://github.com/candyyetszyu/Weekly-Work-Schedule-Generator-Hello-Kitty.git
cd Weekly-Work-Schedule-Generator-Hello-Kitty
pip install -r requirements.txt
```

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- **Hello Kitty**: For the adorable inspiration and theme
- **Python Community**: For the amazing libraries and tools
- **Open Source Contributors**: For making this project possible

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review the error messages carefully
3. Ensure all dependencies are installed
4. Try both GUI and CLI versions

---

**Made with ❤️ and lots of 🌸 Hello Kitty magic! 🎀✨**

*Enjoy creating your magical work schedules!*
