import tkinter
from tkinter import ttk
from tkinter import messagebox
import time

# _______________________________________
#  BACK END FUNCTION FOR BUTTONS
# _______________________________________

def request_quote():
    """Sends a request to microservice to get a quote that can include filters. Will show error if required fields are empty when button is clicked."""
    if option_combobox.get() != "":
        request = option_combobox.get().split()[0]
        advanced_option = None
        if request == "Topic" and topic_combobox.get() != "":
            advanced_option = topic_combobox.get()
        elif request == "Medium" and medium_combobox.get() != "":
            advanced_option = medium_combobox.get()
        elif request == "Random":
            pass
        else:
            tkinter.messagebox.showwarning(title="Error", message=f"You have not selected a specific {request}. Please select a specific option or change your preference to one that doesn't need a specific option.")
        if advanced_option is not None:
            request = request + " " + advanced_option
        with open("quote_request.txt", "w") as quote_request:
            quote_request.write(request)
        time.sleep(1)
        with open("quote_sent.txt", "r+") as quote_returned:
            generated_quote = quote_returned.read()
            if len(generated_quote) == 0:
                generated_quote = "No quote was generated since the microservice is currently down."
            quote_returned.seek(0)
            quote_returned.truncate()
        set_quote(generated_quote)
    else:
        tkinter.messagebox.showwarning(title= "Error", message="You have not selected a quote option. \nAn option and, sometimes, an additional selection are required to generate a quote.")

def show_intro():
    """Displays introduction to Pull-A-Quote! when button is clicked."""
    intro_text = "Welcome to Pull-A-Quote! A random quote will be pulled based on the category that you pick from our curated collection of quotes. You can choose to get a random quote on different topics, such as love, life, success, failure, and more. You can also decide to get a random quote from books or movies specifically. After selecting an option, an additional required dropdown menu will become accessible for you to follow-up to make your request more specific. \n \n *NEW* If you are indecisive and don’t know what type of quote you would like to get, you can now choose random when prompted to get a random quote from our vast library of quotes. This option doesn't have a required additional decision to be made."
    messagebox.showinfo("App Introduction", intro_text)

def enable_specific_options(*args):
    """Makes specific option fields inaccessible if the option that requires them is not selected in the dropdown menu for general options."""
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

def set_quote(quote):
    """Inserts the quote into the Text box and prevents user from interacting with the text inside."""
    generated_quote_text.config(state="normal")
    generated_quote_text.delete("1.0", "end")
    generated_quote_text.insert("1.0", quote)
    generated_quote_text.config(state="disabled")

# _______________________________________
#  FRONT END GUI
# _______________________________________
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
button = tkinter.Button(frame, text="Generate Quote", command=request_quote)
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

# Quote generated Frame
quote_frame = tkinter.LabelFrame(frame, text="Quote Generated")
quote_frame.grid(row=4, column=0, sticky="news", padx=20, pady=5)
generated_quote_text = tkinter.Text(quote_frame, wrap="word", height=5, width=50)
generated_quote_text.grid(row=0, column=0, padx=10, pady=5, sticky="news")
generated_quote_text.config(state="disabled")

app.mainloop()
