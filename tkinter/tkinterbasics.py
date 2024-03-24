from tkinter import *

window = Tk()
window.title("The GUI program")
window.minsize(width=800, height=600)
window.config(padx=20, pady=20) #adds spacong around border window


def buttonclick():
  newtext = input.get() #get input info and use it when button is clicked, this will replace the previosu text
  mylabel.config(text = newtext)
  #mylabel.pack()
button = Button(text ="Click Me",command=buttonclick)
#button.pack()
button.grid(column=1,row=10)
#button2
button = Button(text ="Submit",command=buttonclick)
button.grid(column=2,row=0)

# label
mylabel = Label(text = " I am a label", font=("Ariel", 20, "bold"))

#mylabel.pack(side = "left")
mylabel["text"] = "new text"
mylabel.config(text = "mytext") #this ovrrrides the previous mylabel text
#mylabel.pack(side="bottom")
#mylabel.place(x=0, y=50)
mylabel.grid(column=0,row=0) #need to disable all pack placements before you use grid

entry = Entry(width=20, text="entersomething")
entry.grid(column=4,row=20)

#entry
def inputfunc():
  mylabel.config(text = "input entered")
  #mylabel.pack()
input = Entry(width=10)
#input.pack()

window.mainloop()









