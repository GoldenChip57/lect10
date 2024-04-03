from tkinter import*
root = Tk()
myInputfeild = Entry(root, fg="red", bg="yellow")
myInputfeild.pack()
myInputfeild.insert(0, "Enter your Name:")

def myClick():
	myLabel1 = Label(root, text = "Hello " + myInputfeild.get())
	myLabel1.pack()
myButton = Button(root, text="Click here",command=myClick, padx = 50, pady = 25, fg ="white", bg = "black")
myButton.pack()
root.mainloop()
