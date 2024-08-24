import tkinter as tk # window library
from pynput import keyboard # keyboard listener lib
import threading # for running listener in a separate thread

# Window Setup
window = tk.Tk()
window.title("Death Counter")
window.geometry("200x200")
window.resizable(False, False)
window.configure(bg="Gray")

window.grid_rowconfigure(0, weight=0)
window.grid_rowconfigure(1, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

# initizilze the death counter
deaths = 0

# Function to do things to the death counter with clicking
def on_click(event):
    global deaths
    deaths += 1
    deathcounter.config(text=deaths)

def on_reset(event):
    global deaths
    deaths = 0
    deathcounter.config(text=deaths)

# Functions to do things with key presses; f9 to increment, f10 to reset
# Note: need to press f10 twice for some reason
def on_press(key):
    global deaths
    match key:
        case keyboard.Key.f9:
            deaths += 1
            deathcounter.config(text=deaths)

# Disabling f10 to reset until I figure out why this doesn't work...
#        case keyboard.Key.f10:
#            deaths = 0
#            deathcounter.config(text=deaths)
#

# Function to start the keyboard listener
def start_listener():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

# Bind the mouse click event to the on_click function, reset on right click
#window.bind("<Button-1>", on_click)
window.bind("<Button-3>", on_reset)

# Start the listener in a separate thread
listener_thread = threading.Thread(target=start_listener)
listener_thread.daemon = True
listener_thread.start()

# Set up Elements
deathcounter = tk.Label(window, text=deaths, font=("Helvetica", 80), height=0, bg="Gray", fg="White")
deathcounter.grid(row=0, column=1, sticky="NSEW", padx=2, pady=2)  # Reduced padding
text = tk.Label(window, text="You died... (right click to reset me)", font=("Helvetica", 8), bg="Gray", fg="White")
text.grid(row=1, column=1, sticky="NSEW", padx=2, pady=2)  # Reduced padding

# Start the main event loop
window.mainloop()