#GUI app with python and tkinter
from tkinter import *
from PIL import ImageTk, Image
from random import choice
from random import shuffle
import os
import pygame
os.system('clear')

root = Tk()
root.title('Heart Companion')

#GUI full screen
width_value=root.winfo_screenwidth()
height_value=root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (width_value, height_value))

#background color
root['background']='Pink'

#corner icon
root.iconbitmap('c:/Users/clari/Downloads/hatouno_9vl_icon.ico')

#page 1 labels and buttons
myLabel = Label(root, text= "Please enter your name.", font= ("Lobster", 18))
myLabel.pack(padx = 200, pady=0)
myTextbox = Entry(root, width = 30)
myTextbox.pack(padx = 200, pady = 10)

def hello():
	global hello_label
	hello_label = Label(root, text= "Hello " +myTextbox.get()+", I am your Heart Companion Hato! Today I will help you de-stress. The next page contains activites to relieve your stress :>", font = ("Lobster", 18))
	hello_label.pack(padx = 200, pady = 35)

myButton = Button(root, text = "Submit", command = hello, fg=('white'), bg= ('turquoise'))
myButton.pack(padx=200, pady= 20)

frame= LabelFrame(root,text="",padx=5,pady=5)
frame.pack(padx=20,pady=20)

#image viewing with forward and back buttons
my_img1 = ImageTk.PhotoImage(Image.open("C:/Users/clari/Pictures/images/hato2.png"))
my_img2 = ImageTk.PhotoImage(Image.open("C:/Users/clari/Pictures/images/hato3.png"))

image_list =[my_img1, my_img2]

my_label =Label(frame,image=my_img1)
my_label.grid(row=0,column=0,columnspan=3)

#forward button functions
def forward(image_number):
	global my_label
	global button_forward
	global button_back
	global myLabel
	global myTextbox
	global myButton


	myLabel.pack_forget()
	myTextbox.pack_forget()
	myButton.pack_forget()
	hello_label.pack_forget()

	my_label.grid_forget()
	my_label = Label(frame,image=image_list[image_number])
	button_forward = Button(frame,text=">>", command=lambda: forward(image_number), bg = 'Misty Rose')
	button_back = Button(frame,text="<<", command=lambda:back(image_number), bg = 'Misty Rose')

#animal word scramble game
	if image_number == 1:
		bframe = Frame(root)
		bframe.pack(pady=20)
		myword = Label(bframe, text = "", font =("Helvetica", 15), fg='Dark slate blue')
		myword.grid(row= 1, column = 0)
		def shuffler():
			animals = ['dolphin', 'bear', 'lobster', 'whale', 'hamster', 'cat', 'dog', 'antelope', 'reindeer', 'giraffe', 'panda', 'deer', 'dinosaur', 'seahorse', 'crocodile', 'alligator', 'turtle', 'jellyfish', 'walrus', 'starfish', 'fish', 'coyote', 'squirrel', 'snake', 'kangaroo', 'hippo', 'cow', 'otter', 'chimpanzee', 'elephant', 'racoon', 'chicken', 'sheep', 'shark', 'turkey', 'gorilla', 'rhino', 'pig']
			global word
			word = choice(animals)
			breakapart = list(word)
			shuffle(breakapart)
	
			global shuffledword
			shuffledword = ''
			for letter in breakapart:
				shuffledword += letter
	
			myword.config(text = shuffledword)

		def answer():
			if word == myentry.get(): 
				answer.config(text =  "Correct!", fg ='Medium Sea Green')
			else:
				answer.config(text = "Incorrect!", fg = 'Red')
		
		buttonframe = Frame(root)
		buttonframe.pack(pady=20)
		description = Label(bframe, text= "This is the Animal Scramble Game! You have to guess the name of the animal that will be scrambled!", font =("Helvetica", 15), fg = 'Dark Cyan')
		description.grid(row=0, column = 0, padx=10)

		myentry = Entry(root, font = ("Helvetica", 15))
		myentry.pack(pady=20)

		button2 = Button(buttonframe, text= "Pick Another Word", command = shuffler, bg = 'sky blue')
		button2.grid(row =0, column=0, padx=10)

		answerbutton = Button(buttonframe, text = "Answer", command = answer, bg = "Coral")
		answerbutton.grid(row=0, column=3, padx=10)

		answer = Label(root, text= '', font = ("Helvetica", 18))
		answer.pack(pady=20)

#music player
	if image_number == 1:
		pygame.mixer.init()

		def play():
			pygame.mixer.music.load("C:/Users/clari/Downloads/meditation.mp3")
			pygame.mixer.music.play(loops=0)

		def stop():
			pygame.mixer.music.stop()

		play_button = Button(root, text="Play Song", font=("Helvetica", 15), command = play, bg='Cornflower Blue')
		play_button.pack(padx = 80, pady=5)

		stop_button = Button(root, text="Stop", command=stop, bg='FireBrick')
		stop_button.pack(padx = 100,pady=10)

#meditation steps
	if image_number == 1:

		myMeditation = Label(root, text= "\n\nMeditation is a great way to relieve stress! I have added a few different poses for meditation and how to do them down below. Pick to your liking. :D\n\n"
		"Yoga Meditation: \n" 
		"1. Child’s Pose: Sit on your knees and have your belly touch your thighs. Lay flat with your arms straight out in front of you and slowly breathe into your belly. Hold for 5 breaths. \n" 
		"2. Single Leg Lifts: Lay flat on your back with arms and legs extended straight outwards. Raise one leg at a 90 degree angle from your other leg, inhaling while raising one leg and exhale while bringing the leg down. Repeat for each leg 10 times. \n"
	  	"3.Inner Peace Meditation: Sit on the floor with your legs crossed and have the back of your hand/wrist rest on your leg. Inhale and exhale with your eyes closed for 10 breaths. \n"
	  	"4. Tree Pose: Stand with your arms raised up, touching each other over your head. Rest one foot on the opposite leg and keep your balance. Slowly inhale and exhale for 5 breaths.\n"
	   	"5.Underdog Pose: Bend down and forward with your arms straight out in front of you. With the floor, create an equilateral triangle shape with your body. Inhale and exhale slowly while holding for 10 breaths.\n\n\n" "Are you satisfied with your care? If so, click the Exit Program Button. If not, continue with the activities. Enjoy!", font= ("Helvetica", 13), fg='Navy')
		myMeditation.pack()

	if image_number == 1:
		button_forward = Button(frame, text=">>",state=DISABLED, bg = 'Misty Rose')


	my_label.grid(row=0,column=0,columnspan=3)
	button_back.grid(row=1000, column=0)
	button_forward.grid(row=1000, column=2)
	
#back button functions
def back(image_number):
	global my_label
	global button_forward
	global button_back


	my_label.grid_forget()
	my_label = Label(frame,image=image_list[image_number])
	button_forward = Button(frame,text=">>", command=lambda: forward(image_number), bg = 'Misty Rose')
	button_back = Button(frame,text="<<", command=lambda:back(image_number), bg = 'Misty Rose')

	my_label.grid(row=0,column=0,columnspan=3)
	button_back.grid(row=1000, column=0)
	button_forward.grid(row=1000, column=2)

button_back = Button(frame,text="<<", command=back, state=DISABLED, bg = 'Misty Rose')
button_back.grid(row=1000, column=0)

button_quit = Button(frame,text="Exit De-stress Machine",command=root.quit, bg = 'Light Salmon')
button_quit.grid(row=1000, column =1)

button_forward = Button(frame,text=">>", command=lambda: forward(1), bg = 'Misty Rose')
button_forward.grid(row=1000, column=2, pady=10)


root.mainloop()
