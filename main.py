import tkinter
from tkinter import ttk
from tkinter import messagebox
import os
import openpyxl
import random
import time

# WIP
# def generate_quote():
    
#     if not option_combobox.get().isEmpty():
#         # User info
#         firstname = first_name_entry.get()
#         lastname = last_name_entry.get()
        
#         if firstname and lastname:
#             title = title_combobox.get()
#        
#         else:
#             tkinter.messagebox.showwarning(title="Error", message="You have not selected a specific option. Please select a specific option or change your preference to one that doesn't need a specific option.")
#     else:
#         tkinter.messagebox.showwarning(title= "Error", message="You have not selected an option. An option and, sometimes, additional selections are required to generate a quote.")

def show_intro():
    intro_text = "Welcome to Pull-A-Quote! A random quote will be pulled based on the category that you pick from our curated collection of quotes. You can choose to get a random quote on different topics, such as love, life, success, failure, and more. You can also decide to get a random quote from books or movies specifically. After selecting an option, an additional required dropdown menu will become accessible for you to follow-up to make your request more specific. \n \n *NEW* If you are indecisive and don’t know what type of quote you would like to get, you can now choose random when prompted to get a random quote from our vast library of quotes. This option doesn't have a required additional decision to be made."
    messagebox.showinfo("App Introduction", intro_text)

def enable_specific_options(*args):
    selection = option_var.get()
    if selection == "Topic":
        topic_combobox.config(state="readonly")
        medium_combobox.config(state="disabled")
    elif selection == "Medium":
        medium_combobox.config(state="readonly")
        topic_combobox.config(state="disabled")
    else:
        topic_combobox.config(state="disabled")
        medium_combobox.config(state="disabled")

def set_quote():
    generated_quote_text.config(state="normal")
    generated_quote_text.delete("1.0", "end")
    generated_quote_text.insert("1.0", str(random.randint(1, 10000)))
    tkinter.messagebox.showwarning(title= "Error", message="You have not selected a specific option. Please select a specific option or change your preference to one that doesn't need a specific option.")
    generated_quote_text.config(state="disabled")

app = tkinter.Tk()
app.title("Pull-A-Quote!")

frame = tkinter.Frame(app)
frame.pack()

# Create a Label widget for the introduction message
intro_label = ttk.Label(app, text="", wraplength=400)  # Adjust wraplength as needed

# Add a button to trigger the introduction
intro_button = tkinter.Button(frame, text="Introduction", command=show_intro)
intro_button.grid(row= 0, column=0, padx=10, pady=10)

# Quote Options
option_frame = tkinter.LabelFrame(frame, text="Quote Options")
option_frame.grid(row= 1, column=0, padx=20, pady=10)
option_var = tkinter.StringVar()
option_var.trace("w", enable_specific_options)

option_label = tkinter.Label(option_frame, text="Pick a preference for the type of quote")
option_combobox = ttk.Combobox(option_frame, textvariable=option_var,values=["", "Topic", "Medium", "Random *NEW*"])
option_label.grid(row=0, column=0, padx=10, pady=5)
option_combobox.grid(row=1, column=0, padx=10, pady=5)

# Frame for Topics/Mediums
specific_frame = tkinter.LabelFrame(frame, text="Select a specific option if needed.")
specific_frame.grid(row=2, column=0, padx=10, pady=10)

# Options for Topic Combobox
topic_label = ttk.Label(specific_frame, text="Select a specific topic:")
topic_combobox = ttk.Combobox(specific_frame, values=["", "Success", "Failure", "Growth", "Family", "War", "Death", "Love", "Life", "Inspiration"])
topic_label.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")  
topic_combobox.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")  
topic_combobox.config(state="disabled")

# Options for Medium Combobox
medium_label = ttk.Label(specific_frame, text="Select a specific medium:")
medium_combobox = ttk.Combobox(specific_frame, values=["", "Book", "Movie"])
medium_label.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")  
medium_combobox.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")  
medium_combobox.config(state="disabled")

# Button 
button = tkinter.Button(frame, text="Generate Quote", command=set_quote)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

# Quote generated Frame
quote_frame = tkinter.LabelFrame(frame, text="Quote Generated")
quote_frame.grid(row=4, column=0, sticky="news", padx=20, pady=5)
generated_quote_text = tkinter.Text(quote_frame, height=5, width=50)
generated_quote_text.grid(row=0, column=0, padx=10, pady=5, sticky="news")
generated_quote_text.config(state="disabled")

app.mainloop()