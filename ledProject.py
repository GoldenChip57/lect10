from tkinter import *
#import RPi.GPIO as GPIO
#GPIO.setwarnings(Flase)
#LED = 21
#GPIO.setup(LED, GPIO.OUT)
root = Tk()
root.title("LED PROJECT")
root.geometry("600x400")
Count = 0
def greenClicked():
	global Count
	Count = Count + 1
	CountReminder = Count % 2
	if CountReminder == 1:
		greenLabel1 = Label(root, text="LED ON", fg="white",bg="green")
		#GPIO.output(LED, GPIO.HIGH)

	else:
		greenLabel1 = Label(root, text="LED OFF",fg="white",bg="green")
		#GPIO.output(LED, GPIO.LOW)
	greenLabel1.grid(row=5, column=5)

greenButton = Button(root,text="GREEN",fg="white",bg="green",padx=25,command=greenClicked)
greenLabel = Label(root,text="LED is off",fg="white",bg="green")

root.columnconfigure(5, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(7,weight=1)

greenButton.grid(row=3,column=5)
greenLabel.grid(row=7,column=5)

root.mainloop()


