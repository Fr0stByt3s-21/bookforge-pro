import subprocess, webbrowser

print("Launching BookForge Pro GUI...")
subprocess.Popen(["streamlit", "run", "gui_app_main.py", "--server.headless", "true"])
webbrowser.open("http://localhost:8501")
