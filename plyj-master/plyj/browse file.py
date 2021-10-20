# Python program to create
# a file explorer in Tkinter

# import all components
# from the tkinter library
from re import split
from PAR.model import CompilationUnit, VariableDeclaration
from tkinter import *
from PAR import parser
from PAR import model as m
<<<<<<< HEAD
import os
import sys

# import filedialog module
from tkinter import filedialog

# Function for opening the
# file explorer window
def browseFiles():
	
	## To save time change initialdir to a directory with a java file.
	filename = filedialog.askopenfilename(initialdir = "/",
										title = "Select a File",
										filetypes = (("Java files",
														"*.java*"),
													("all files",
														"*.*")))
	writeFile = open(os.path.expanduser("~/Desktop/repos/SourceCodeChecker/ParsedDataInFile.txt","a"))
	# Change label contents
	label_file_explorer.configure(text="File Opened: "+filename)

	p = parser.Parser()
	tree = p.parse_file(filename)
	for type_decl in tree.type_declarations:
		writeFile.write(type_decl.name)
		if type_decl.extends is not None:
			writeFile.write(' -> extending ' + type_decl.extends.name.value)
		if len(type_decl.implements) is not 0:
			writeFile.write(' -> implementing ' + ', '.join([type.name.value for type in type_decl.implements]))
		writeFile.write

		writeFile.write('fields:')
		for field_decl in [decl for decl in type_decl.body if type(decl) is m.FieldDeclaration]:
			for var_decl in field_decl.variable_declarators:
				if type(field_decl.type) is str:
					type_name = field_decl.type
				else:
					type_name = field_decl.type.name.value
				writeFile.write('    ' + type_name + ' ' + var_decl.variable.name)

		writeFile.write
		writeFile.write('methods:')
		for method_decl in [decl for decl in type_decl.body if type(decl) is m.MethodDeclaration]:
			param_strings = []
			for param in method_decl.parameters:
				if type(param.type) is str:
					param_strings.append(param.type + ' ' + param.variable.name)
				else:
					param_strings.append(param.type.name.value + ' ' + param.variable.name)
			writeFile.write('    ' + method_decl.name + '(' + ', '.join(param_strings) + ')')

			if method_decl.body is not None:
				for statement in method_decl.body:
					# note that this misses variables in inner blocks such as for loops
					# see symbols_visitor.py for a better way of handling this
					if type(statement) is m.VariableDeclaration:
						for var_decl in statement.variable_declarators:
							if type(statement.type) is str:
								type_name = statement.type
							else:
								type_name = statement.type.name.value
							writeFile.write('        ' + type_name + ' ' + var_decl.variable.name)
		

		

		
		
		
		


								
			
			

		

		
		
		
		
		
			
		




		
		
		
		

		
		


		
		
		


		return filename
		
	
																								
# Create the root window
window = Tk()

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("500x500")

#Set window background color
window.config(background = "white")

# Create a File Explorer label
label_file_explorer = Label(window,
							text = "File Explorer using Tkinter",
							width = 100, height = 4,
							fg = "blue")

	
button_explore = Button(window,
						text = "Browse Files",
						command = browseFiles)


button_exit = Button(window,
					text = "Exit",
					command = exit)

# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)

button_explore.grid(column = 1, row = 2)

button_exit.grid(column = 1,row = 3)

# Let the window wait for any events
window.mainloop()
