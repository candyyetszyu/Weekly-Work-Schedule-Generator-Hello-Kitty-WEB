#!/usr/bin/env python3
"""
Streamlit Web Application for Weekly Work Schedule Generator
Converted from Tkinter GUI to modern web interface
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import generate_schedule_cli_copy
import os
import io
import base64

# Page configuration
st.set_page_config(
    page_title="🎀 Hello Kitty Schedule Generator 🎀",
    page_icon="🎀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Hello Kitty theme
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #ffe6f2 0%, #fff0f5 100%);
        padding: 1rem;
        border-radius: 10px;
        border: 2px solid #ff69b4;
        margin-bottom: 2rem;
    }
    
    .card {
        background: #fff8fa;
        padding: 1.5rem;
        border-radius: 10px;
        border: 2px solid #ffb6c1;
        margin-bottom: 1rem;
    }
    
    .success-message {
        background: #e8f5e8;
        padding: 1rem;
        border-radius: 10px;
        border: 2px solid #90ee90;
        margin: 1rem 0;
    }
    
    .error-message {
        background: #ffe6e6;
        padding: 1rem;
        border-radius: 10px;
        border: 2px solid #ff6b6b;
        margin: 1rem 0;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #ff1493 0%, #ff69b4 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        font-size: 1.1rem;
    }
    
    .stButton > button:hover {
        background: linear-gradient(90deg, #dc143c 0%, #ff1493 100%);
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(255, 20, 147, 0.3);
    }
    
    .secondary-button {
        background: linear-gradient(90deg, #98fb98 0%, #90ee90 100%) !important;
        color: #006400 !important;
    }
    
    .secondary-button:hover {
        background: linear-gradient(90deg, #90ee90 0%, #7cfc00 100%) !important;
    }
    
    .exit-button {
        background: linear-gradient(90deg, #87ceeb 0%, #87cefa 100%) !important;
        color: #000080 !important;
    }
    
    .exit-button:hover {
        background: linear-gradient(90deg, #87cefa 0%, #00bfff 100%) !important;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Main header with Hello Kitty theme
    st.markdown("""
    <div class="main-header">
        <h1 style="text-align: center; color: #ff69b4; font-family: 'Comic Sans MS', cursive;">
            🎀 Hello Kitty Schedule Generator 🎀
        </h1>
        <p style="text-align: center; color: #ff1493; font-family: 'Comic Sans MS', cursive; font-size: 1.2rem;">
            ✨ Create magical work schedules with Hello Kitty ✨
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar for navigation and info
    with st.sidebar:
        st.markdown("""
        <div class="card">
            <h3 style="color: #ff69b4; font-family: 'Comic Sans MS', cursive;">🌸 Hello Kitty Tips 🌸</h3>
            <ul style="color: #c71585; font-family: 'Comic Sans MS', cursive;">
                <li>Mode 1: Specify weekly hours and total days</li>
                <li>Mode 2: Specify total overall hours (auto-distributed)</li>
                <li>Time slots: 30-minute increments between 09:00-18:00</li>
                <li>Daily work: 30-120 minutes per day</li>
                <li>Maximum: 15 hours per week</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Add Hello Kitty image if available
        if os.path.exists("hello_kitty.png"):
            st.image("hello_kitty.png", width=150)
        elif os.path.exists("hello_kitty.jpg"):
            st.image("hello_kitty.jpg", width=150)
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Mode selection
        st.markdown("""
        <div class="card">
            <h3 style="color: #ff69b4; font-family: 'Comic Sans MS', cursive;">🎀 Choose Your Magic Mode 🎀</h3>
        </div>
        """, unsafe_allow_html=True)
        
        mode = st.radio(
            "Select Mode:",
            ["🌸 Mode 1: Input total weekly hours", "🎀 Mode 2: Input total overall hours"],
            format_func=lambda x: x.split(": ")[1] if ": " in x else x
        )
        
        # Schedule parameters
        st.markdown("""
        <div class="card">
            <h3 style="color: #ff69b4; font-family: 'Comic Sans MS', cursive;">🌸 Schedule Parameters 🌸</h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Input fields
        start_date = st.date_input(
            "🎀 Start Date:",
            value=datetime.now(),
            format="YYYY-MM-DD"
        )
        
        start_week = st.number_input(
            "🎀 Starting Week Number:",
            min_value=1,
            value=1,
            step=1
        )
        
        if "weekly" in mode:
            # Mode 1 inputs
            total_hours = st.number_input(
                "🌸 Total Weekly Hours:",
                min_value=0.5,
                max_value=15.0,
                value=10.0,
                step=0.5,
                help="Maximum 15 hours per week"
            )
            
            total_days = st.number_input(
                "🎀 Total Days:",
                min_value=1,
                value=7,
                step=1
            )
        else:
            # Mode 2 inputs
            total_overall_hours = st.number_input(
                "🌸 Total Overall Hours:",
                min_value=0.5,
                value=50.0,
                step=0.5
            )
        
        # Output settings
        st.markdown("""
        <div class="card">
            <h3 style="color: #ff69b4; font-family: 'Comic Sans MS', cursive;">🎀 Output Settings 🎀</h3>
        </div>
        """, unsafe_allow_html=True)
        
        filename = st.text_input(
            "🌸 Filename:",
            value="hello_kitty_schedule",
            help="Files will be saved with this name"
        )
        
        col_export1, col_export2, col_export3 = st.columns(3)
        with col_export1:
            export_txt = st.checkbox("📄 Text", value=True)
        with col_export2:
            export_xlsx = st.checkbox("📊 Excel", value=True)
        with col_export3:
            export_docx = st.checkbox("📝 Word", value=True)
    
    with col2:
        # Action buttons
        st.markdown("""
        <div class="card">
            <h3 style="color: #ff69b4; font-family: 'Comic Sans MS', cursive;">🌸 Generate Schedule 🌸</h3>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🌸 Generate Magic Schedule 🌸", use_container_width=True):
            generate_schedule_web()
        
        if st.button("🎀 Clear Form", use_container_width=True, key="clear"):
            st.rerun()
        
        if st.button("🌸 Exit", use_container_width=True, key="exit"):
            st.stop()
    
    # Function to generate schedule
    def generate_schedule_web():
        try:
            # Validate inputs
            if not filename.strip():
                st.error("Please enter a filename")
                return
            
            if "weekly" in mode:
                if total_hours <= 0 or total_hours > 15:
                    st.error("Weekly hours must be between 0.5 and 15")
                    return
                if total_days < 1:
                    st.error("Total days must be at least 1")
                    return
            else:
                if total_overall_hours <= 0:
                    st.error("Total overall hours must be greater than 0")
                    return
            
            # Show progress
            with st.spinner("🌸 Creating your magical Hello Kitty schedule... 🌸"):
                start_date_str = start_date.strftime("%Y-%m-%d")
                
                if "weekly" in mode:
                    # Mode 1
                    generate_schedule_cli_copy.generate_schedule(
                        start_date_str, total_hours, int(total_days), filename.strip(), start_week,
                        export_txt, export_xlsx, export_docx
                    )
                else:
                    # Mode 2
                    generate_schedule_cli_copy.generate_schedule_total_hours(
                        start_date_str, total_overall_hours, filename.strip(), start_week,
                        export_txt, export_xlsx, export_docx
                    )
            
            # Check which files were created and provide download links
            created_files = []
            download_links = []
            
            if export_txt and os.path.exists(f"{filename.strip()}.txt"):
                created_files.append(".txt")
                with open(f"{filename.strip()}.txt", "r") as f:
                    txt_content = f.read()
                    st.download_button(
                        label="📄 Download Text File",
                        data=txt_content,
                        file_name=f"{filename.strip()}.txt",
                        mime="text/plain"
                    )
            
            if export_xlsx and os.path.exists(f"{filename.strip()}.xlsx"):
                created_files.append(".xlsx")
                with open(f"{filename.strip()}.xlsx", "rb") as f:
                    st.download_button(
                        label="📊 Download Excel File",
                        data=f.read(),
                        file_name=f"{filename.strip()}.xlsx",
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    )
            
            if export_docx and os.path.exists(f"{filename.strip()}.docx"):
                created_files.append(".docx")
                with open(f"{filename.strip()}.docx", "rb") as f:
                    st.download_button(
                        label="📝 Download Word File",
                        data=f.read(),
                        file_name=f"{filename.strip()}.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    )
            
            # Success message
            files_text = ", ".join(created_files) if created_files else "No files"
            st.success(f"""
            🌸 Hello Kitty schedule created successfully! 🌸
            
            Files created: {files_text}
            Location: {os.getcwd()}
            """)
            
            # Display preview if text file was created
            if export_txt and os.path.exists(f"{filename.strip()}.txt"):
                with st.expander("📄 Preview Schedule"):
                    with open(f"{filename.strip()}.txt", "r") as f:
                        st.text(f.read())
            
            # Display Excel preview if created
            if export_xlsx and os.path.exists(f"{filename.strip()}.xlsx"):
                with st.expander("📊 Preview Excel Data"):
                    df = pd.read_excel(f"{filename.strip()}.xlsx")
                    st.dataframe(df, use_container_width=True)
                    
        except Exception as e:
            st.error(f"🌸 Oops! Something went wrong with the magic... 🌸\n\nError: {str(e)}")

if __name__ == "__main__":
    main() 