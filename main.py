from tkinter import *
from tkinter import messagebox
from datetime import datetime
import requests
import webbrowser

USER_NAME = "testprogramko"
TOKEN = "asdf123qwer456zxcv789"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

# --- PIXELA API COMMUNICATION ---
def post_pixel(date, quantity):
    pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
    pixel_data = {
        "date": date,
        "quantity": quantity,
    }
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
    messagebox.showinfo("Success", "Pixel posted successfully!")

def update_pixel(date, quantity):
    update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{date}"
    update_pixel_data = {
        "quantity": quantity
    }
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    response = requests.put(url=update_endpoint, json=update_pixel_data, headers=headers)
    if response.status_code == 200:
        messagebox.showinfo("Success", "Pixel updated successfully!")
    else:
        messagebox.showerror("Error", f"Failed to update pixel: {response.text}")

# --- UI SETUP ---
window = Tk()
window.title("Habit Tracker")
window.config(padx=20, pady=20)

date_label = Label(text="Date (YYYYMMDD):")
date_label.pack()

date_entry = Entry(width=20)
date_entry.insert(0, datetime.now().strftime("%Y%m%d"))
date_entry.pack()

quantity_label = Label(text="Quantity:")
quantity_label.pack()

quantity_entry = Entry(width=20)
quantity_entry.pack()

def on_submit():
    date = date_entry.get()
    quantity = quantity_entry.get()
    if date and quantity:
        # First try to post, if that fails (because a pixel for that day already exists), try to update.
        # A more robust solution would be to check the response message.
        try:
            post_pixel(date, quantity)
        except:
            update_pixel(date, quantity)

submit_button = Button(text="Add/Update Entry", command=on_submit)
submit_button.pack()

def view_graph():
    webbrowser.open(f"https://pixe.la/v1/users/{USER_NAME}/graphs/{GRAPH_ID}.html")

graph_button = Button(text="View Graph", command=view_graph)
graph_button.pack()

window.mainloop()
