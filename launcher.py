#!/usr/bin/env python3
"""
Launcher for Weekly Work Schedule Generator
Choose between GUI and CLI versions
"""

import sys
import os

def main():
    print("🗓 Weekly Work Schedule Generator Launcher")
    print("=" * 50)
    print("Choose your preferred interface:")
    print("1. GUI (Graphical User Interface) - Recommended")
    print("2. CLI (Command Line Interface)")
    print("3. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            print("\n🚀 Launching GUI version...")
            try:
                import schedule_gui
                schedule_gui.main()
            except ImportError as e:
                print(f"❌ Error: Could not import GUI module: {e}")
                print("Make sure schedule_gui.py is in the same directory.")
            except Exception as e:
                print(f"❌ Error launching GUI: {e}")
            break
            
        elif choice == "2":
            print("\n🚀 Launching CLI version...")
            try:
                import generate_schedule_cli_copy
                # The CLI version will start automatically when imported
            except ImportError as e:
                print(f"❌ Error: Could not import CLI module: {e}")
                print("Make sure generate_schedule_cli_copy.py is in the same directory.")
            except Exception as e:
                print(f"❌ Error launching CLI: {e}")
            break
            
        elif choice == "3":
            print("\n👋 Goodbye!")
            sys.exit(0)
            
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main() 