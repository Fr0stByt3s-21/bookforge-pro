[Setup]
AppName=BookForge Pro
AppVersion=1.0
DefaultDirName={pf}\BookForgePro
OutputBaseFilename=BookForgeProInstaller
SetupIconFile=assets\icon.ico

[Files]
Source: "dist\BookForgePro.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\BookForge Pro"; Filename: "{app}\BookForgePro.exe"
