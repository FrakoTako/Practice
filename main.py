from tkinter import *
#from PIL import ImageTk, Image
import shutil
import os, re
import easygui
import time, stat
from tkinter import filedialog
from tkinter import messagebox as mb
from datetime import datetime, timedelta
import time
import json

def combine_funcs(*funcs):
	# this function will call the passed functions
	# with the arguments that are passed to the functions
	def inner_combined_func(*args, **kwargs):
		for f in funcs:
			# Calling functions with arguments, if any
			f(*args, **kwargs)
	# returning the reference of inner_combined_func
	# this reference will have the called result of all
	# the functions that are passed to the combined_funcs
	return inner_combined_func

def open_window():
	read = easygui.fileopenbox()
	return read
'''
def open_file():
	string = open_window()
	try:
		os.startfile(string)
	except:
		mb.showinfo('confirmation', "File not found!")

def copy_file():
	source1 = open_window()
	destination1 = filedialog.askdirectory()
	shutil.copy(source1,destination1)
	mb.showinfo('confirmation', "File Copied !")
'''
# delete file function
def delete_file(path):
	if os.path.exists(path):
		os.remove(path)
	else:
		mb.showinfo('confirmation', "File not found !")
'''
def rename_file():
	chosenFile = open_window()
	path1 = os.path.dirname(chosenFile)
	extension=os.path.splitext(chosenFile)[1]
	print("Enter new name for the chosen file")
	newName=input()
	path = os.path.join(path1, newName + extension)
	print(path)
	os.rename(chosenFile, path) 
	mb.showinfo('confirmation', "File Renamed !")

def move_file():
	source = open_window()
	destination = filedialog.askdirectory()
	if(source == destination):
		mb.showinfo('confirmation', "Source and destination are same")
	else:
		shutil.move(source, destination)  
		mb.showinfo('confirmation', "File Moved !")

def make_folder():
	newFolderPath = filedialog.askdirectory()
	print("Enter name of new folder")
	newFolder = input()
	path = os.path.join(newFolderPath, newFolder)  
	os.mkdir(path)
	mb.showinfo('confirmation', "Folder created !")

def remove_folder():
	delFolder = filedialog.askdirectory()
	os.rmdir(delFolder)
	mb.showinfo('confirmation', "Folder Deleted !")
'''

# function to list all the files in folder
def open_folder():
	folder = filedialog.askdirectory()
	return folder

def read_folder(folder):
	file_size = n = 0
	for fname in os.listdir(folder):
		path = '/'.join([folder, fname])
		if os.path.isdir(path):
			read_folder(path)
		else:
			file_size += os.path.getsize(path) 
#			'''
			#modification_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modification_time_sec))
			#Label(root, text = "Last Modified Time for: " + str(fname) + " is " + str(modification_time)).grid(row = n + 4, column = 2)
			
			time_between_insertion = time.time() - os.path.getmtime(path)
			if  time_between_insertion < 1209600: 
				Label(root, text = str(fname)).grid(row = n + 5, column = 2)
#				Button(root, text = "del", command = delete_file(path)).grid(row = n + 4, column = 3)
				Button(root, text = "del", command = lambda: delete_file(path)).grid(row = n + 5, column = 3)
				'''
				json_object = json.dumps(fname, os.path.getmtime(path), os.getlogin(), indent = 4)
				with open("sample.json", "w") as outfile:
					outfile.write(json_object)
				'''

#			'''
			n += 1
	Label(root, text = "trere is " + str(n) + " files in this directory").grid(row = 2, column = 2)
	Label(root, text = "all file size is " + str(file_size) + " bytes").grid(row = 3, column = 2)
	Label(root, text = "modified more than 2 week ago: ").grid(row = 4, column = 2)

# 	sortlist = sorted(os.listdir(folder))
# 	i = 0
# 	print("Files in ", folder, "folder are:")
# 	while(i < len(sortlist)):
#		Button(root, text = sortlist[i]).grid(row = i + 2, column = 2)
# 		print(sortlist[i] + '\n')
# 		i += 1
# 	print(i)

'''
def list_files(startpath):
	for root, dirs, files in os.walk(startpath):
		level = root.replace(startpath, '').count(os.sep)
		indent = ' ' * 4 * (level)
		print('{}{}/'.format(indent, os.path.basename(root)))
		subindent = ' ' * 4 * (level + 1)
		for f in files:
			print('{}{}'.format(subindent, f))
'''

def last_changes():
	path = open_window()
	#час останньої модифікації файлу в секундах
	modTimesinceEpoc = os.path.getmtime(path)
	#Перетворюю секунди в читабельні позначки часу
	modificationTime = 	time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(modTimesinceEpoc))
	#print("Last Modified Time: ", modificationTime)
	Label(root, text = "Last Modified Time: " + str(modificationTime)).grid(row = 5, column = 2)

root = Tk()

Label (root, text = "Практика", font = ("Helvetica", 16), fg = "blue").grid(row = 0, column = 2)
""" 
Button(root, text = "Open a File",		command = open_file).		grid(row = 15, column = 2)
Button(root, text = "Copy a File",		command = copy_file).		grid(row = 25, column = 2)
Button(root, text = "Delete a File",	command = delete_file).		grid(row = 35, column = 2)
Button(root, text = "Rename a File",	command = rename_file).		grid(row = 45, column = 2)
Button(root, text = "Move a File",		command = move_file).		grid(row = 55, column = 2)
Button(root, text = "Make a Folder",	command = make_folder).		grid(row = 75, column = 2)
Button(root, text = "Remove a Folder",	command = remove_folder).	grid(row = 65, column = 2)
Button(root, text = "last changes",		command = last_changes).	grid(row = 4, column = 2)
Button(root, text = "last changes",		command = last_changes).	grid(row = 4, column = 2)
"""
Button(root, text = "Open folder", command = lambda: read_folder(open_folder())).grid(row = 1, column = 2)
root.mainloop()

'''
import os
path = "./test"

for root, d_names, f_names in os.walk(path):
	print(root, d_names, f_names)
'''