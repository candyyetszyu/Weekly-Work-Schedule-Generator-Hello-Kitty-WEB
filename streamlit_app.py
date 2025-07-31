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

# Custom CSS for smaller cards and wider sidebar
st.markdown("""
<style>
    /* Make sidebar wider */
    section[data-testid="stSidebar"] {
        min-width: 350px !important;
        max-width: 400px !important;
    }
    /* Smaller card styling */
    .card {
        background: linear-gradient(135deg, #fff8fa 0%, #fff0f5 100%);
        padding: 0.75rem 1rem;
        border-radius: 10px;
        border: 2px solid #ffb6c1;
        margin-bottom: 1rem;
        box-shadow: 0 2px 8px rgba(255, 182, 193, 0.10);
        font-size: 1rem;
    }
    .card h3 {
        margin-bottom: 0.5rem;
        font-size: 1.15rem;
    }
    /* Sidebar tips styling */
    .kitty-tips-list {
        color: #c71585;
        font-family: 'Comic Sans MS', cursive;
        font-size: 1.05rem;
        line-height: 1.7;
        margin-left: 0.5rem;
        margin-bottom: 0.5rem;
    }
    .kitty-tips-list li {
        margin-bottom: 0.3rem;
    }
</style>
""", unsafe_allow_html=True)

def main():
    # Main header with Hello Kitty theme
    st.markdown("""
    <div class="main-header">
        <h1 style="text-align: center; color: #ff69b4; font-family: 'Comic Sans MS', cursive; margin-bottom: 0.5rem;">
            🎀 Hello Kitty Schedule Generator 🎀
        </h1>
        <p style="text-align: center; color: #ff1493; font-family: 'Comic Sans MS', cursive; font-size: 1.3rem; margin: 0;">
            ✨ Create magical work schedules with Hello Kitty ✨
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar for navigation and info
    with st.sidebar:
        st.markdown("""
        <div class="card">
            <h3 style="color: #ff69b4; font-family: 'Comic Sans MS', cursive; text-align: center; margin-bottom: 1rem;">
                🌸 Hello Kitty Tips 🌸
            </h3>
            <ul style="color: #c71585; font-family: 'Comic Sans MS', cursive; line-height: 1.6;">
                <li><strong>Mode 1:</strong> Specify weekly hours and total days</li>
                <li><strong>Mode 2:</strong> Specify total overall hours (auto-distributed)</li>
                <li><strong>Time slots:</strong> 30-minute increments between 09:00-18:00</li>
                <li><strong>Daily work:</strong> 30-120 minutes per day</li>
                <li><strong>Maximum:</strong> 15 hours per week</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Add Hello Kitty image if available
        if os.path.exists("hello_kitty.png"):
            st.image("hello_kitty.png", width=150)
        elif os.path.exists("hello_kitty.jpg"):
            st.image("hello_kitty.jpg", width=150)
        
        # Quick start guide
        with st.expander("🚀 Quick Start Guide", expanded=False):
            st.markdown("""
            **1. Choose Mode**: Select between weekly or total hours
            **2. Set Date**: Pick your start date
            **3. Enter Hours**: Specify your work hours
            **4. Choose Format**: Select export options
            **5. Generate**: Click the magic button!
            """)
    
    # Main content area with improved layout
    # Use tabs for better organization
    tab1, tab2, tab3 = st.tabs(["🎀 Schedule Generator", "📊 Preview", "⚙️ Settings"])
    
    with tab1:
        # Mode selection with better visual separation
        st.markdown("""
        <div class="card">
            <h3 style="color: #ff69b4; font-family: 'Comic Sans MS', cursive; text-align: center;">
                🎀 Choose Your Magic Mode 🎀
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        mode = st.radio(
            "Select Generation Mode:",
            ["🌸 Mode 1: Input total weekly hours", "🎀 Mode 2: Input total overall hours"],
            format_func=lambda x: x.split(": ")[1] if ": " in x else x,
            help="Mode 1: Set weekly hours and days. Mode 2: Set total hours (auto-distributed)"
        )
        
        # Schedule parameters in a more organized layout
        st.markdown("""
        <div class="card">
            <h3 style="color: #ff69b4; font-family: 'Comic Sans MS', cursive; text-align: center;">
                🌸 Schedule Parameters 🌸
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        # Use columns for better input organization
        col_date, col_week = st.columns(2)
        
        with col_date:
            start_date = st.date_input(
                "🎀 Start Date:",
                value=datetime.now(),
                format="YYYY-MM-DD",
                help="Choose the starting date for your schedule"
            )
        
        with col_week:
            start_week = st.number_input(
                "🎀 Starting Week Number:",
                min_value=1,
                value=1,
                step=1,
                help="Set the week number to start from"
            )
        
        # Mode-specific inputs with better spacing
        if "weekly" in mode:
            st.markdown("### 📅 Mode 1: Weekly Schedule")
            col_hours, col_days = st.columns(2)
            
            with col_hours:
                total_hours = st.number_input(
                    "🌸 Total Weekly Hours:",
                    min_value=0.5,
                    max_value=15.0,
                    value=10.0,
                    step=0.5,
                    help="Maximum 15 hours per week"
                )
            
            with col_days:
                total_days = st.number_input(
                    "🎀 Total Days:",
                    min_value=1,
                    value=7,
                    step=1,
                    help="Number of days to generate schedule for"
                )
        else:
            st.markdown("### 📅 Mode 2: Total Hours Schedule")
            total_overall_hours = st.number_input(
                "🌸 Total Overall Hours:",
                min_value=0.5,
                value=50.0,
                step=0.5,
                help="Total hours to distribute across weeks"
            )
        
        # Output settings with better organization
        st.markdown("""
        <div class="card">
            <h3 style="color: #ff69b4; font-family: 'Comic Sans MS', cursive; text-align: center;">
                🎀 Output Settings 🎀
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        filename = st.text_input(
            "🌸 Filename:",
            value="hello_kitty_schedule",
            help="Files will be saved with this name (no spaces recommended)"
        )
        
        st.markdown("**📄 Export Formats:**")
        col_export1, col_export2, col_export3 = st.columns(3)
        with col_export1:
            export_txt = st.checkbox("📄 Text File", value=True, help="Human-readable schedule")
        with col_export2:
            export_xlsx = st.checkbox("📊 Excel File", value=True, help="Spreadsheet format")
        with col_export3:
            export_docx = st.checkbox("📝 Word File", value=True, help="Document format")
        
        # Action buttons with better spacing
        st.markdown("---")
        st.markdown("### 🌸 Generate Your Schedule")
        
        col_generate, col_clear, col_exit = st.columns([2, 1, 1])
        
        with col_generate:
            if st.button("🌸 Generate Magic Schedule 🌸", use_container_width=True, type="primary"):
                generate_schedule_web()
        
        with col_clear:
            if st.button("🎀 Clear Form", use_container_width=True, key="clear"):
                st.rerun()
        
        with col_exit:
            if st.button("🌸 Exit", use_container_width=True, key="exit"):
                st.stop()
    
    with tab2:
        st.markdown("""
        <div class="card">
            <h3 style="color: #ff69b4; font-family: 'Comic Sans MS', cursive; text-align: center;">
                📊 Schedule Preview
            </h3>
            <p style="text-align: center; color: #c71585;">
                Generate a schedule first to see the preview here! 🌸
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with tab3:
        st.markdown("""
        <div class="card">
            <h3 style="color: #ff69b4; font-family: 'Comic Sans MS', cursive; text-align: center;">
                ⚙️ App Settings
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.info("🌸 This is the Hello Kitty Schedule Generator - a magical tool for creating work schedules!")
        
        # App information
        st.markdown("### 📋 App Information")
        st.markdown("""
        - **Version**: 2.0 (Web Edition)
        - **Theme**: Hello Kitty Pink
        - **Framework**: Streamlit
        - **Features**: Multiple export formats, responsive design
        """)
        
        # Contact/Support
        st.markdown("### 🎀 Support")
        st.markdown("""
        If you love this app, please give it a ⭐ star on GitHub!
        
        **Repository**: [Weekly-Work-Schedule-Generator-Hello-Kitty-WEB](https://github.com/candyyetszyu/Weekly-Work-Schedule-Generator-Hello-Kitty-WEB)
        """)
    
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
            
            # Show progress with better styling
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
            
            # Success message with better styling
            files_text = ", ".join(created_files) if created_files else "No files"
            st.success(f"""
            🌸 **Hello Kitty schedule created successfully!** 🌸
            
            **Files created:** {files_text}
            **Location:** {os.getcwd()}
            """)
            
            # Display preview in the Preview tab
            if export_txt and os.path.exists(f"{filename.strip()}.txt"):
                with st.expander("📄 Preview Schedule", expanded=True):
                    with open(f"{filename.strip()}.txt", "r") as f:
                        st.text(f.read())
            
            # Display Excel preview if created
            if export_xlsx and os.path.exists(f"{filename.strip()}.xlsx"):
                with st.expander("📊 Preview Excel Data", expanded=False):
                    df = pd.read_excel(f"{filename.strip()}.xlsx")
                    st.dataframe(df, use_container_width=True)
                    
        except Exception as e:
            st.error(f"🌸 Oops! Something went wrong with the magic... 🌸\n\n**Error:** {str(e)}")

if __name__ == "__main__":
    main() 
