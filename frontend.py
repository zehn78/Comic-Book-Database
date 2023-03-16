"""
Fields:
 A progam that stores book information: 
  Title     Author
  Year      ISBN
Buttons
 User can:
  View all records
  Search an entry
  Add entry
  Update entry
  Delete
  Close
"""
from tkinter import *
import sqlite3

# we're going to create a separate file for the backend
from backend import Database

database = Database("comics.db")

# we use this to populate the entry fields with info from a listbox selection
def get_selected_row(event):
  global selected_tuple
  index=list1.curselection()[0]
  selected_tuple=list1.get(index)
  # return selected_tuple
  e1.delete(0,END)
  e1.insert(END,selected_tuple[1])
  e2.delete(0,END)
  e2.insert(END,selected_tuple[2])
  e3.delete(0,END)
  e3.insert(END,selected_tuple[3])
  e4.delete(0,END)
  e4.insert(END,selected_tuple[4])
  e5.delete(0,END)
  e5.insert(END,selected_tuple[5])
  e6.delete(0,END)
  e6.insert(END,selected_tuple[6])

def view_command():
  # outputs to tuple
  list1.delete(0,END)
  for row in database.view():
    list1.insert(END,row)

def search_command():
  # def search(title="",author="",year="",isbn=""):
  list1.delete(0,END)
  for row in database.search(title_text.get(),publisher_text.get(),issue_text.get(),print_text.get(),month_text.get(),year_text.get()):
    list1.insert(END,row)

def add_command():
  database.insert(title_text.get(),publisher_text.get(),issue_text.get(),print_text.get(),month_text.get(),year_text.get())
  list1.delete(0,END)
  list1.insert(END,(title_text.get(),publisher_text.get(),issue_text.get(),print_text.get(),month_text.get(),year_text.get()))
  view_command()

def update_command():
  # use insert
  database.update(selected_tuple[0],title_text.get(),publisher_text.get(),issue_text.get(),print_text.get(),month_text.get(),year_text.get())
  view_command()

def delete_command():
  database.delete(selected_tuple[0])
  view_command()

window = Tk()
window.wm_title("Comic Books")

# start by making the labels
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)
l2 = Label(window, text="Publisher")
l2.grid(row=0, column=2)
l3 = Label(window, text="Issue")
l3.grid(row=0, column=4)
l4 = Label(window, text="Print")
l4.grid(row=1, column=0)
l5 = Label(window, text="Month")
l5.grid(row=1, column=2)
l5 = Label(window, text="Year")
l5.grid(row=1, column=4)
# data entry fields
title_text = StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)
publisher_text = StringVar()
e2=Entry(window,textvariable=publisher_text)
e2.grid(row=0,column=3)
issue_text = StringVar()
e3=Entry(window,textvariable=issue_text)
e3.grid(row=0,column=5)
print_text = StringVar()
e4=Entry(window,textvariable=print_text)
e4.grid(row=1,column=1)
month_text = StringVar()
e5=Entry(window,textvariable=month_text)
e5.grid(row=1,column=3)
year_text = StringVar()
e6=Entry(window,textvariable=year_text)
e6.grid(row=1,column=5)
# data results fields 
list1=Listbox(window, height=10, width=50)
list1.grid(row=2,column=0,rowspan=6,columnspan=5)
list1.bind('<<ListboxSelect>>',get_selected_row)
# scrollbar to scroll the listbox
sb1=Scrollbar(window)
sb1.grid(row=2,column=4,rowspan=6)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)
# buttons on the right side
# b1 = Button(window, text="View All",command=km_to_miles)
b1 = Button(window, text="View all", width=12,command=view_command)
b1.grid(row=2,column=5)
b2 = Button(window, text="Search entry", width=12,command=search_command)
b2.grid(row=3,column=5)
b3 = Button(window, text="Add entry", width=12,command=add_command)
b3.grid(row=4,column=5)
b4 = Button(window, text="Update", width=12,command=update_command)
b4.grid(row=5,column=5)
b5 = Button(window, text="Delete", width=12,command=delete_command)
b5.grid(row=6,column=5)
b6 = Button(window, text="Close", width=12,command=window.destroy)
b6.grid(row=7,column=5)
# generate window
window.mainloop() 