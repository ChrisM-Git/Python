from tkinter import *

window = Tk()
window.title("Miles converter to Km")
window.minsize(width=400, height=200)
window.config(padx=20, pady=20)

def convert():
  miles = float(milesentry.get())
  km = round(miles * 1.60934)
  kmentry.config(text=f"{km}")

miles = Label(text="Miles")
miles.grid(row=0, column=3)
equalto = Label(text="is equal to")
equalto.grid(row=2, column=0)

milesentry = Entry(width=10)
milesentry.grid(row=0, column=2)

kmentry = Entry(width=10)
kmentry.grid(row=2, column=2)
kmlabel = Label(text="Km")
kmlabel.grid(row=2, column=3)


button = Button(text="Convert",command=convert)
button.grid(row=3, column=2)


window.mainloop()