ZippOpener
A simple zip file compression and extraction tool built with Python and tkinter.
Features
Compress files into zip archives
Extract files from zip archives
Optional password protection for zip files
User-friendly graphical interface
Installation
Clone the repository:
bash
git clone https://github.com/Shogund21/ZippOpener.git

Navigate to the project directory:
bash
cd ZippOpener

Install the required dependencies:
bash
pip install -r requirements.txt

Usage
Run the application:
bash
python zip_app.py

To create an executable:
Install PyInstaller:
bash
pip install pyinstaller

Create the executable:
bash
pyinstaller --onefile --windowed zip_app.py

Find the executable in the dist folder.
Dependencies
Python 3.x
tkinter (included with Python)
pyzipper
Deployment
Create the executable using PyInstaller.
Distribute the .exe file found in the dist folder to your team.
Provide instructions for running the executable.
