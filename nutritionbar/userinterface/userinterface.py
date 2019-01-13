from guizero import App, Text, PushButton, Slider
import csv

valueList = [0, 0, 0]

def generate_csv():
    welcome_message.value = "Saved nutrition requirements. Generating granola!"
    with open("nutrition.csv", 'w', newline='') as myfile:
     wr = csv.writer(myfile)
     wr.writerow(valueList)

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
welcome_message = Text(app, text="Select your macros", size=20, font="Times New Roman", color="darkcyan")

fats = Text(app, text="Fats")
text_size = Slider(app, command=change_fats, start=1, end=100)

carbs = Text(app, text="Carbs")
text_size = Slider(app, command=change_carbs, start=1, end=100)

protein = Text(app, text="Protein")
text_size = Slider(app, command=change_protein, start=1, end=100)

update_text = PushButton(app, command=generate_csv, text="Submit")
app.display()

for x in valueList:
	print(x)