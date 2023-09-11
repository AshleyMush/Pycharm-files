from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Mile to KM converter")
window.minsize(width=300, height=150)
window.config(padx=40,pady=40)


result = 0
kilometer = 1.609344

# def button_clicked():
#     new_text = input.get()
#
#     my_label.config(text= result)
#Buttons
def action():
    miles = int(entry.get())
    answer = round(miles * kilometer)
    output.config(text=f"{answer}")



# #calls action() when pressed
button = Button(text="Click Me", command=action)
button.grid(column=2, row=3)

#Entry

entry = Entry(width=10)
entry.grid(column=2, row=1)
entry.insert(END, string=f"{result}")

miles = Label(text="Miles", font=("Arial", 10, "bold"))
miles.grid(column=3,row=1)
miles.config(pady=5, padx=5)

km = Label(text="Km", font=("Arial", 10, "bold"))
km.grid(column=3,row=2)
km.config(pady=5, padx=5)

output = Label(text=f"{result}")
output.grid(column=2,row=2)

is_equal_to = Label(text="is equal to", font=("Arial", 10, "bold"))
is_equal_to.grid(column=1, row=2)
is_equal_to.config(pady=5, padx=5)

#TODO ADD 0 to input Entry Bar
#Define a function to calculate the conversion












window.mainloop()