from guizero import App, Text, PushButton, Slider, info
import csv

valueList = [0, 0, 0]

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
	info("Success!", "Your granola pod with " + fatstring + carbstring + proteinstring + "will be in the dispensing area shortly")

def generate_csv():
    #welcome_message.value = "Saved nutrition requirements. Generating granola!"
    fat_slider.value = 0
    carb_slider.value = 0
    protein_slider.value = 0
    with open("nutrition.csv", 'w', newline='') as myfile:
    	wr = csv.writer(myfile)
    	wr.writerow(valueList)
    send_to_controller()

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


app = App(title="GranolaPod")
welcome_message = Text(app, text="Select your macros", size=20, font="Dense", color="darkcyan")

fats = Text(app, text="Fats", size=18, font="Dense", color="black")
fat_slider = Slider(app, command=change_fats, start=1, end=100)
fat_slider.width = 300
fat_slider.height=30

carbs = Text(app, text="Carbs", size=18, font="Dense", color="black")
carb_slider = Slider(app, command=change_carbs, start=1, end=100)
carb_slider.width = 300
carb_slider.height = 30

protein = Text(app, text="Protein", size=18, font="Dense", color="black")
protein_slider = Slider(app, command=change_protein, start=1, end=100)
protein_slider.width = 300
protein_slider.height = 30

update_text = PushButton(app, command=generate_csv, text="Submit")
update_text.width = 40
update_text.height = 100
app.display()

for x in valueList:
	print(x)