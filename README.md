# Weekly-Work-Schedule-Generator-Hello-Kitty-WEB

🎀 **Hello Kitty Schedule Generator - Web Edition** 🎀

A beautiful, modern web application for generating weekly work schedules with a delightful Hello Kitty theme. Converted from Tkinter GUI to Streamlit for easy web deployment and access.

![Hello Kitty](https://img.shields.io/badge/Hello-Kitty-Pink?style=for-the-badge&logo=heart&color=ff69b4)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-ff4b4b?style=for-the-badge&logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)

## ✨ Live Demo

🌐 **Try it online**: [Hello Kitty Schedule Generator](https://candyyetszyu.streamlit.app/Weekly-Work-Schedule-Generator-Hello-Kitty-WEB)

## 🎯 Features

- 🌸 **Beautiful Hello Kitty Theme**: Pink gradients and cute styling throughout
- 🎀 **Two Generation Modes**: 
  - **Mode 1**: Input total weekly hours and days
  - **Mode 2**: Input total overall hours (auto-distributed across weeks)
- 📄 **Multiple Export Formats**: Text, Excel, and Word documents
- 🌐 **Web-Based Interface**: Access from any browser, anywhere
- 📱 **Responsive Design**: Works perfectly on desktop and mobile devices
- ⬇️ **Direct Downloads**: Download generated files directly from the web app
- 🎨 **Interactive Preview**: Preview your schedule before downloading

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/candyyetszyu/Weekly-Work-Schedule-Generator-Hello-Kitty-WEB.git
   cd Weekly-Work-Schedule-Generator-Hello-Kitty-WEB
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the web app**
   ```bash
   streamlit run streamlit_app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:8501`

## 🎯 How to Use

1. **Choose Your Mode**:
   - **Mode 1**: Specify weekly hours and total number of days
   - **Mode 2**: Specify total overall hours (system auto-distributes)

2. **Set Parameters**:
   - Start date (YYYY-MM-DD format)
   - Starting week number
   - Hours (weekly or total overall)
   - Days (for Mode 1 only)

3. **Configure Output**:
   - Choose your filename
   - Select export formats (Text, Excel, Word)

4. **Generate & Download**:
   - Click "Generate Magic Schedule"
   - Use download buttons to get your files

## 📊 Output Formats

The app generates three types of files:

| Format | Description | Use Case |
|--------|-------------|----------|
| 📄 **Text (.txt)** | Human-readable schedule format | Quick reference, printing |
| 📊 **Excel (.xlsx)** | Structured data in spreadsheet | Data analysis, further editing |
| 📝 **Word (.docx)** | Formatted table in Word document | Professional reports, sharing |

## 🌐 Deployment

### Streamlit Cloud (Recommended)

1. **Fork this repository** or push to your own GitHub repo
2. **Go to [Streamlit Cloud](https://share.streamlit.io)**
3. **Sign in with GitHub**
4. **Click "New app"**
5. **Configure**:
   - **Repository**: Your GitHub repo
   - **Main file path**: `streamlit_app.py`
   - **App URL**: Choose your custom URL
6. **Click "Deploy"**

Your app will be live at: `https://yourusername.streamlit.app/your-app-name`

### Other Deployment Options

- **Heroku**: Use the provided `Procfile` and `setup.sh`
- **Docker**: Build with the included `Dockerfile`
- **Local Server**: Run with `streamlit run streamlit_app.py --server.port 8080`

## 🎨 Customization

### Theme Colors

The app uses a Hello Kitty pink theme:

```css
Primary Pink: #ff69b4
Deep Pink: #ff1493
Light Pink: #ffe6f2
Card Background: #fff8fa
```

### Adding Hello Kitty Images

Place a `hello_kitty.png` or `hello_kitty.jpg` file in the project directory to display the Hello Kitty image in the sidebar.

## 📁 Project Structure

```
├── streamlit_app.py              # Main Streamlit web application
├── generate_schedule_cli_copy.py # Core schedule generation logic
├── requirements.txt              # Python dependencies
├── deploy.sh                     # Deployment helper script
├── hello_kitty.png              # Hello Kitty image (optional)
├── README.md                     # This file
└── schedule_gui.py              # Original Tkinter GUI (reference)
```

## 🔧 Technical Details

### Dependencies

- **Streamlit**: Web framework
- **Pandas**: Data manipulation
- **OpenPyXL**: Excel file generation
- **python-docx**: Word document creation
- **Pillow**: Image processing

### Schedule Generation Logic

- **Time slots**: 30-minute increments between 09:00-18:00
- **Daily work**: 30-120 minutes per day
- **Weekly limit**: Maximum 15 hours per week
- **Random distribution**: Ensures varied and realistic schedules

## 🌟 Features Comparison

| Feature | Tkinter GUI | Streamlit Web App |
|---------|-------------|-------------------|
| Platform | Desktop only | Web (any device) |
| Installation | Local Python | Browser access |
| Deployment | Manual | Streamlit Cloud |
| Sharing | File sharing | URL sharing |
| Updates | Manual | Automatic |
| Mobile | No | Yes |
| Theme | Hello Kitty | Hello Kitty |

## 🤝 Contributing

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **Hello Kitty**: For the adorable theme inspiration
- **Streamlit**: For the amazing web framework
- **Sanrio**: For the Hello Kitty character

## 🎀 Support

If you love this project, please give it a ⭐ star on GitHub!

---

**Made with ❤️ and Hello Kitty magic ✨**

*Happy scheduling with Hello Kitty! 🎀* 