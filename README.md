# 🗓 Weekly Work Schedule Generator

A powerful tool to generate personalized work schedules with flexible time management and multiple export formats.

## ✨ Features

- **Two Modes**: Weekly hours or total overall hours
- **Smart Time Distribution**: 30-minute increments between 09:00-18:00
- **Multiple Export Formats**: .txt, .xlsx, and .docx with table format
- **User-Friendly Interface**: Both GUI and CLI versions available
- **Flexible Scheduling**: 30-120 minutes per day, max 15 hours per week
- **Professional Output**: Clean, organized schedules ready for use

## 🚀 Quick Start

### Option 1: Launcher (Recommended)
```bash
python3 launcher.py
```
Choose between GUI and CLI interfaces.

### Option 2: Direct Launch
```bash
# GUI Version
python3 schedule_gui.py

# CLI Version
python3 generate_schedule_cli_copy.py
```

## 📋 Requirements

- Python 3.6+
- Required packages:
  - `pandas` (for Excel export)
  - `python-docx` (for Word export)
  - `tkinter` (for GUI - usually included with Python)

### Install Dependencies
```bash
pip3 install pandas python-docx
```

## 🖥️ GUI Interface

The GUI provides an intuitive way to create schedules:

### Mode Selection
- **Mode 1**: Input total weekly hours + number of days
- **Mode 2**: Input total overall hours (auto-distributed across weeks)

### Schedule Parameters
- **Start Date**: Any date within the starting week (YYYY-MM-DD)
- **Starting Week**: Week number to begin with
- **Total Hours**: Weekly hours (Mode 1) or overall hours (Mode 2)
- **Total Days**: Number of days to generate (Mode 1 only)

### Output Settings
- **Filename**: Choose your output filename
- **Export Options**: Select which formats to generate (.txt, .xlsx, .docx)

### Features
- ✅ Input validation
- ✅ Progress indication
- ✅ File browser for save location
- ✅ Clear form functionality
- ✅ Status updates

## 💻 CLI Interface

The command-line interface provides the same functionality:

```bash
python3 generate_schedule_cli_copy.py
```

Follow the prompts to:
1. Choose mode (1 or 2)
2. Enter start date
3. Enter starting week number
4. Enter filename
5. Enter hours and days (if applicable)

## 📊 Output Formats

### 1. Text File (.txt)
```
Week 1: 15 January – 21 January
15 Jan 2024 (Monday) - 1h 30m | 12:30–14:00
16 Jan 2024 (Tuesday) - 1h 0m | 16:00–17:00
...
Total work time: 7.50 hours
```

### 2. Excel File (.xlsx)
Professional spreadsheet with columns:
- Week
- Date
- Day
- Work Time
- Time Slot

### 3. Word Document (.docx)
Professional table format:
| Week | Date | Schedule | Hours |
|------|------|----------|-------|
| Week 1 | 15 Jan 2024 (Monday)<br>16 Jan 2024 (Tuesday) | 12:30–14:00<br>16:00–17:00 | 1h 30m<br>1h 0m |

## ⚙️ Configuration

### Time Settings
- **Working Hours**: 09:00 - 18:00
- **Time Units**: 30-minute increments
- **Daily Range**: 30-120 minutes per day
- **Weekly Maximum**: 15 hours per week

### Schedule Rules
- All times rounded to 30-minute units
- Random time slot assignment within working hours
- Balanced distribution across available days
- Automatic adjustment for partial weeks

## 🔧 Customization

### Modify Time Settings
Edit `generate_schedule_cli_copy.py`:
```python
# Working hours
earliest_start = 9 * 60  # 09:00
latest_start = 18 * 60   # 18:00

# Daily limits
min_day = 30    # Minimum 30 minutes
max_day = 120   # Maximum 120 minutes

# Time units
unit = 30       # 30-minute blocks
```

### Modify Export Formats
The GUI allows you to select which formats to export:
- Check/uncheck the export options
- All formats use the same schedule data
- Files are saved in the current directory

## 🐛 Troubleshooting

### Common Issues

1. **Import Error**: Make sure all files are in the same directory
2. **GUI Not Opening**: Check if tkinter is installed
3. **Export Errors**: Ensure write permissions in the current directory
4. **Invalid Date**: Use YYYY-MM-DD format

### Error Messages
- "Weekly hours cannot exceed 15" - Reduce your hours input
- "Total weekly minutes must be at least 30" - Increase your hours input
- "Duration too long" - The time slot doesn't fit in working hours

## 📁 File Structure

```
schedule-generator/
├── generate_schedule_cli_copy.py  # Main CLI application
├── schedule_gui.py                # GUI interface
├── launcher.py                    # Launcher script
└── README.md                      # This file
```

## 🤝 Contributing

Feel free to enhance the application:
- Add new export formats
- Improve the GUI design
- Add more scheduling options
- Optimize the time distribution algorithm

## 📄 License

This project is open source and available under the MIT License.

---

**Happy Scheduling! 🎉** # Weekly-Work-Schedule-Generator
