import subprocess
from tkinter import filedialog
import tkinter as tk
import ChooseDirectory as cd
from Application import Application
from pathlib import Path

myfile = Path(".config")
directory = ''
if myfile.is_file():
	f=open(".config", "r")
	directory = f.read()
	f.close()
else:
	#first run
	root = tk.Tk()
	app = cd.ChooseDirectory(master=root)
	app.mainloop()
	directory = app.directory
	f = open(".config","w+")
	f.write(directory)
	f.close()

root = tk.Tk()
app= Application(directory, master=root)
app.mainloop()
#print(directory)
#print(subprocess.check_output(['dotnet', directory + 'CryptoDownloaderConsole.dll','--help']))