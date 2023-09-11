from tkinter import *



window = Tk()
window.title("My_first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)
def button_clicked():
    new_text = input.get()

    my_label.config(text= new_text)

#Label
my_label =Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)
my_label.config(text="New Text")

#Creating Buttons



button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)



new_button = Button(text="Click me 2")
new_button.grid(column=2, row=0)


#Entry

input = Entry(width=10)
input.grid(column=3,row=2)
# input.pack()
# input.get()

print(type(input))






















window.mainloop()