import pandas as pd
from tkinter import *

data = pd.read_csv("2023-06-09_-_Worker_and_Temporary_Worker.csv")

county = data["County"]
oxfordshire_sponsors = data[county == "Oxfordshire"]

print(oxfordshire_sponsors)

route = oxfordshire_sponsors["Route"]
organisation_name = oxfordshire_sponsors["Organisation Name"]

city = data["Town/City"]
oxford_sponsors = data[city == "Oxford"]
#Data frame
print(type(oxford_sponsors))

ox_list = []
with open("Oxford_sponsor_names.txt", mode="a") as names_data:
    for (key, value) in oxford_sponsors.iterrows():
        sponsor_names_STR = value["Organisation Name"]

        ox_list.append(sponsor_names_STR)

        names_data.write(sponsor_names_STR + "\n\n")

# ox_list = oxford_sponsors.values.tolist()

print(ox_list)


window = Tk()
window.title("Sponsors")
window.minsize(width=600, height=500)

label = Label(text="Ashley's List of Sponsors", font=("Arial", 24, "bold"))
label.pack()

#calls action() when pressed
button = Button(text="Click Me", width=15)
button.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=100, width=50)

for company in ox_list:
    listbox.insert(ox_list.index(company), company)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()







window.mainloop()


#Looping through the data frame

# data.to_csv("C:/Users/Ashley/PycharmProjects/Registered_Sponsors/oxford_sponsors.csv", index=False)


# print(f" Oxford sponsors {oxford_sponsors}")

# sponsor_CVS = oxford_sponsors.to_csv("new_data.cvs")
#
# print(sponsor_CVS)
#
# data = pandas.DataFrame(sponsor_CVS)


# print(organisation_name)
#
# data_dict  = {"Organisation Name": [organisation_name],
#               "Route": [route]
#
#
# }
#
#
# final_data = pandas.DataFrame(data_dict)
#
# print(final_data)


