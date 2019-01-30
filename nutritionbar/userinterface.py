from guizero import App, Text, PushButton, Slider, info, Picture
from multiprocessing import Process
import csv
import time

valueList = [0, 0, 0]

def newProcess():
	print("Started new process!")
	# app2 = App(title="motors", layout="grid")
	# info("test", "this is a test")
	# app2.display()
	print("End new process")

def send_to_controller():
	if valueList[0] == 2:
		fatstring = "high fat, " 
	else:
		fatstring = "low fat, "
	if valueList[1] == 2:
		carbstring = "high carb, "  
	else:
		carbstring = "low carb, "
	if valueList[2] == 2:
		proteinstring = "high protein"  
	else:
		proteinstring = "low protein "
	info("Success!", "Your granola pod with " + fatstring + carbstring + proteinstring + " will be in the dispensing area shortly")

def generate_csv():
	#welcome_message.value = "Saved nutrition requirements. Generating granola!"
	fat_slider.value = 0
	carb_slider.value = 0
	protein_slider.value = 0
	with open("nutrition.csv", 'w', newline='') as myfile:
		wr = csv.writer(myfile)
		wr.writerow(valueList)
	send_to_controller()
	disableWidgets()
	p = Process(target=newProcess)
	p.start()
	p.join()
	enableWidgets()


def disableWidgets():
	fat_slider.disable()
	carb_slider.disable()
	protein_slider.disable()
	update_text.disable()
	welcome_message.value = "Please Wait: Granola Pod is in use"

def enableWidgets():
	fat_slider.enable()
	carb_slider.enable()
	protein_slider.enable()
	update_text.enable()
	welcome_message.value = "Select your macros"

def change_fats(slider_value):
	if int(slider_value) < 50:
		valueList[0] = 1
	else:
		valueList[0] = 2

def change_carbs(slider_value):
	if int(slider_value) < 50:
		valueList[1] = 1
	else:
		valueList[1] = 2

def change_protein(slider_value):
	if int(slider_value) < 50:
		valueList[2] = 1
	else:
		valueList[2] = 2

app = App(title="GranolaPod", layout="grid")

picture = Picture(app, image="bg.jpg", grid=[0,0,10,10])

welcome_message = Text(app, text="Select your macros", size=20, font="Dense", color="darkcyan", grid=[2,0])
welcome_message.tk.configure(background="grey")

fats = Text(app, text="Fats", size=18, font="Dense", color="black", grid=[1,1])
fats.tk.configure(background="grey")
fat_slider = Slider(app, command=change_fats, start=1, end=100, grid=[2,1])
fat_slider.width = 300
fat_slider.height=30
fat_slider.tk.configure(background="grey")

carbs = Text(app, text="Carbs", size=18, font="Dense", color="black", grid=[1,2])
carbs.tk.configure(background="grey")
carb_slider = Slider(app, command=change_carbs, start=1, end=100, grid=[2,2])
carb_slider.width = 300
carb_slider.height = 30
carb_slider.tk.configure(background="grey")

protein = Text(app, text="Protein", size=18, font="Dense", color="black", grid=[1,3])
protein.tk.configure(background="grey")
protein_slider = Slider(app, command=change_protein, start=1, end=100, grid=[2,3])
protein_slider.width = 300
protein_slider.height = 30
protein_slider.tk.configure(background="grey")

update_text = PushButton(app, command=generate_csv, text="Submit", grid=[2,4])
update_text.tk.configure(background="grey")
#update_text.width = 30
#update_text.height = 30

app.display()

for x in valueList:
	print(x)