import subprocess

APP_NAME = "BookForgePro"
ICON_PATH = "assets/icon.ico"

subprocess.run([
    "pyinstaller", "--onefile", "--noconsole",
    f"--name={APP_NAME}",
    f"--icon={ICON_PATH}",
    "gui_app.py"
])
