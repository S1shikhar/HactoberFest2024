import tkinter as tk
import time

# Function to update the time
def update_time():
    current_time = time.strftime("%H:%M:%S %p")  # Get the current time in HH:MM:SS AM/PM format
    clock_label.config(text=current_time)  # Update the label with the current time
    clock_label.after(1000, update_time)  # Schedule the function to run every 1 second (1000ms)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Set the clock label properties
clock_label = tk.Label(root, font=("Arial", 48), bg="black", fg="cyan")
clock_label.pack(pady=20)

# Call the function to update time initially
update_time()

# Start the tkinter event loop
root.mainloop()
