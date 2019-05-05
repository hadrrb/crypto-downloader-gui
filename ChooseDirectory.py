from tkinter import filedialog
import tkinter as tk
import subprocess
global directory 
class ChooseDirectory(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.master.title("CryptoDownloader")
		self.directory = ''
		self.grid()
		self.create_widgets()
		
	def create_widgets(self):
		self.hi = tk.Label(self, text = "CryptoDownloader", font = ('Arial', 15))
		self.hi.grid(column=0, row = 0)
		self.hi1 = tk.Label(self, text = "\nWelcome to CryptoDownloader.\n Please indicate the executable CryptoDownloaderConsole.dll file\n or let the program download the executable from github\n")
		self.hi1.grid(column=0, row = 1)		
		self.button2 = tk.Button(self, text="Choose CryptoDownloaderConsole.dll location", command= self.browse_button)
		self.button2.grid(column=0, row = 2)
		self.button2 = tk.Button(self, text="Download (git and dotnet required)", command= self.download)
		self.button2.grid(column=0, row = 3)

		
	def browse_button(self):
		# Allow user to select a directory and store it in global var
		# called folder_path
		self.directory  = filedialog.askdirectory()
		self.master.destroy()
		
	def download(self):
		subprocess.run(['git','clone','https://github.com/xmik/crypto-downloader'])
		subprocess.run(['dotnet', 'build', 'crypto-downloader', '--configuration=Release'])
		self.directory  = "./crypto-downloader/src/CryptoDownloaderConsole/bin/Release/netcoreapp2.1/"
		self.master.destroy()