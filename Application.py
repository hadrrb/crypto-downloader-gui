from tkinter import filedialog
import tkinter as tk
import tkinter.ttk as ttk
import subprocess
from tkinter import messagebox
import os
import platform

class Application(tk.Frame):
	def __init__(self, directory, master=None):
		super().__init__(master)
		self.master = master
		self.directory = directory
		self.master.title("CryptoDownloader")
		self.instlist = (subprocess.check_output(['dotnet', self.directory + 'CryptoDownloaderConsole.dll','list'])).split()
		self.cb_value = tk.StringVar()
		self.instrument = ""
		self.actualbatch = int(subprocess.check_output(['dotnet', self.directory + 'CryptoDownloaderConsole.dll','get-batch-number']))
		self.batchval = tk.StringVar()
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		self.hi_there = tk.Label(self)
		self.hi_there["text"] = "Welcome to CryptoDownloader!\n\nPlease choose the pair of instruments for which you want to get the data for.\n"
		#self.hi_there["command"] = self.say_hi
		self.hi_there.grid(row = 0, column = 0, columnspan = 4)
		self.combobox = ttk.Combobox(self, textvariable= self.cb_value , values = self.instlist)
		self.combobox.grid(row = 1, column = 1, columnspan = 1)
		self.combobox.current(1)
		self.combobox.bind("<<ComboboxSelected>>", self.on_select)
		self.batchval.set(self.actualbatch)
		self.batchtext = tk.Label(self, text = "\nChoose the batch number correspnding to the given time interval:\n")
		self.batchtext.grid(row=2, column=0, columnspan=4)
		self.batch = tk.Spinbox(self, from_ = 1, to = self.actualbatch, textvariable = self.batchval, width = 10, command = self.on_batch_change);
		self.batch.grid(row = 3, column = 0, columnspan = 1, sticky = 'EN')
		self.batchinfo = tk.Label(self)
		self.batchinfo["text"] = subprocess.check_output(['dotnet', self.directory + 'CryptoDownloaderConsole.dll','batch-to-date-range', self.batch.get()])
		self.batchinfo.grid(row = 3, column = 1, columnspan = 3, sticky = 'N')
		self.generatebash = tk.Button(self, text="Get Data!", command = self.getins)
		self.generatebash.grid(row = 4, column = 0, columnspan = 2)
		self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
		self.quit.grid(row = 4, column = 2, columnspan = 2)

	def on_select(self, event):
		self.instrument = self.cb_value.get()
		
	def on_batch_change(self):
		self.batchinfo["text"] = subprocess.check_output(['dotnet', self.directory + 'CryptoDownloaderConsole.dll','batch-to-date-range', self.batch.get()])
		
	def getins(self):
		subprocess.run(['dotnet', self.directory + 'CryptoDownloaderConsole.dll','get', '--instruments='+ self.cb_value.get(), '--batch='+self.batch.get(), "--directory=./"])
		if platform.system() == "Windows":
			messagebox.showinfo("Done", "Data saved to " + os.getcwd() +  "\\" + self.batch.get() + "\\" + self.cb_value.get() + ".csv")
		else:
			messagebox.showinfo("Done", "Data saved to " + os.getcwd() + "/" + self.batch.get() + "/" + self.cb_value.get() + ".csv")
		
		
		