from tkinter import *

root = Tk()
root.title("A.I. with Mario - Search Algorithms")
#root.iconbitmap(PATH)
root.geometry("400x200")

def myClick():
    myLabel = Label(root, text="             After Click                   ")
    myLabel.grid(row=0, column=2)

# creating a label widget and link it to root
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My Name is Mario")

#myButton = Button(root, text="click me!", state="disabled")
#myButton = Button(root, text="click me!", padx=50, pady=50)
myButton = Button(root, text="click me!", command=myClick, bg="#000066", fg="#aadf00")

# put the Label on the screen
#myLabel.pack()

# alterantive way of positioning
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=2)
myButton.grid(row=2, column=1)

c = Canvas(root, height=100, width=100, bg="black")
c.grid(row=3, column=0)
rect = c.create_rectangle(10,10,20,20,fill="yellow")

def move_rect(event):
    if event.keysym=="Up":
        c.move(rect, 0,-5)
    if event.keysym=="Down":
        c.move(rect, 0,5)
    if event.keysym=="Left":
        c.move(rect, -5,0)
    if event.keysym=="Right":
        c.move(rect, 5,0)
c.bind_all("<Key>", move_rect)

root.mainloop()
