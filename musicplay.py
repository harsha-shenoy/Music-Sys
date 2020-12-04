import sqlite3
from mutagen.id3 import ID3
import pygame
from MiniPro4 import Members
from tkinter import *
import os
from PIL import Image,ImageTk
#from try import Events

index = 0
path = ""

def music_sys():  # languages
	

	
	#name = get_name(uid)
	#textfield = "Welcome" +" "+ name +" "+ "!"
	root = Tk(className='myStudio')
	root.geometry("655x333")
	#root.resizable(width = FALSE, height = FALSE)
	

	frame = Frame(root, bg='grey',borderwidth = 9,relief = SUNKEN,padx = 0,pady = 5)
	frame.pack(side = TOP,fill ='x')
	
	frame5 = Frame(root, bg='grey',borderwidth = 9,relief = SUNKEN,padx = 5,pady = 5)
	frame5.pack(side = LEFT,fill ='y')
	
	Edit_button = Button(frame5,text = "Edit profile",font =("Hellvetica",9),padx = 5,pady = 5)
	Edit_button.pack(side = TOP)

	Change_acc_button = Button(frame5,text = "Change Account",font =("Hellvetica",9),padx = 5,pady = 5)
	Change_acc_button.pack(side = LEFT)
		

	
	frame3 = Frame(root)
	frame3.pack(side = TOP,fill = 'both')
	frame4 = Frame(root)
	frame4.pack(side = TOP,fill = 'both')
	frame1 = Frame(root,bg = "black",pady = 5)
	frame1.pack(side=LEFT,fill = 'both')
	frame2 = Frame(root,bg='yellow')
	frame2.pack(side=LEFT,fill ='both')
	
	WelcomeLabel = Label(frame4,text ="Welcome",font = ('Helvetica',12),padx = 25)
	WelcomeLabel.pack(side = TOP)
	label = Label(frame, text='myStudio',font=('Helvetica',15,'bold'),fg = 'white',bg='grey')
	label.pack(fill ='x')
	
	Search = Label(frame1,text = "Search",font=("Helvetica",10,"bold"))
	Search.pack(side = TOP)

	search_entry = Entry(frame1)
	search_entry.pack(side = TOP)
	
	v = StringVar()
	songlabel = Label(frame1, textvariable=v, width=35, height=2)
	songlabel.pack(side = BOTTOM)

	
	listbox = Listbox(frame1,width = 40,height=8,bg='orange', font=('times', 16)) 
	scrollbar = Scrollbar(frame1)
	listbox.pack(side=LEFT,fill ="both")
	scrollbar.pack(side=RIGHT,fill = "y")
	listbox.config(yscrollcommand=scrollbar.set)
	scrollbar.config(command=listbox.yview)	

	

	realpics = []
	listofpics = []
	listofsongs = []
	realnames = []
	directory_pics = r"C:\Users\Madhavi Shenoy\Desktop\Pics"
	os.chdir(directory_pics)
	for files in os.listdir(directory_pics):		
		if files.endswith(".jpg"):
			realdir_pics = os.path.realpath(files)
		listofpics.append(files) 
	print(listofpics)
	directory = r"C:\Users\Madhavi Shenoy\Desktop\music"
	os.chdir(directory)
	for files in os.listdir(directory):
		if files.endswith(".mp3"):
			realdir = os.path.realpath(files)
			audio = ID3(realdir)
			realnames.append(audio["TIT2"].text[0])
		listofsongs.append(files)
	print(realnames)
	print(listofsongs)

		
	
	realnames.reverse()	
	for items in realnames:
		listbox.insert(0, items)
	realnames.reverse()
	index = 0
	path = ""

	#NextButton = Button(frame2, text='Next Song', width=20,height=2, bg='PeachPuff2')
	#NextButton.pack(side=TOP)

	#PreviousButton = Button(frame2, text='Previous Song',
         #                   width=20, height=2, bg='PeachPuff2')
	#PreviousButton.pack()

	#StopButton = Button(frame2, text='Pause', width=20, height=2,bg='red')
	#StopButton.pack()
     
	def updatelabel():
		global index
		global songname
		v.set(realnames[index])
       	#return songname

	
	


########################################################################################
	def New_Window(event):
		root = Tk()
		path =r"C:\Users\Madhavi Shenoy\Desktop\Pics\Into You.jpg"
		image = Image.open(path)
#image.show()
		img = ImageTk.PhotoImage(image)
		img_label = Label(root,image = img)
		img_label.grid()
#img_label = img
#img.place(x=0,y=0)

		window = Frame(root)
		window.grid(rowspan = 4,columnspan = 4)

		def nextsong(event):
			global index
			index += 1
			listbox.select_set([index])
			pygame.mixer.music.load(listofsongs[index])
			pygame.mixer.music.play()
			updatelabel()
		#window.configure(image = )
	
		def prevsong(event):
			global index
			index -= 1
			listbox.select_set([index])
			pygame.mixer.music.load(listofsongs[index])
			pygame.mixer.music.play()
			updatelabel()
			
	
		def stopsong(event):
			pygame.mixer.music.pause()
 
		def playsong(event):
			pygame.mixer.music.unpause()

		def contplay():
			global index
			index += 1
			pygame.mixer.music.load(listofsongs[index])
			pygame.mixer.music.play()
			updatelabel()
			if (pygame.mixer.music.get_busy) == False:
				contplay()

		

		#img = Image.open('')
		#img.show()
		pygame.mixer.init()
	
				
	
		global index
		w = event.widget
		index = int(w.curselection()[0])
		pygame.mixer.music.load(listofsongs[index])
		pygame.mixer.music.play()
		updatelabel()
#root.minsize(500,500)


		
		path =r"C:\Users\Madhavi Shenoy\Desktop\Pics\Into You.jpg"
		image = Image.open(path)
#image.show()
		img = ImageTk.PhotoImage(image)
		img_label = Label(root,image = img)
		img_label.grid()
#img_label = img
#img.place(x=0,y=0)

		window = Frame(root)
		window.grid(rowspan = 4,columnspan = 4)


		NextButton = Button(window, text='Next Song', width=20,height=2, bg='PeachPuff2')
		NextButton.grid(row = 10 , column = 2)

		PreviousButton = Button(window, text='Previous Song',width=20, height=2, bg='PeachPuff2')
		PreviousButton.grid(row = 10 , column = 1)

		StopButton = Button(window, text='Pause', width=20, height=2,bg='red')
		StopButton.grid(row = 11 , column = 1)
		
		PlayButton = Button(window, text='Resume', width=20, height=2,bg='green')
		PlayButton.grid(row = 11 , column = 2)


		NextButton.bind("<Button-1>", nextsong)
		PreviousButton.bind("<Button-1>", prevsong)
		StopButton.bind("<Button-1>", stopsong)
		PlayButton.bind("<Button-1>",playsong)
		

		root.mainloop()
	


	
##################################################################################
	
	listbox.bind("<<ListboxSelect>>", New_Window)
	
	root.mainloop()
music_sys()