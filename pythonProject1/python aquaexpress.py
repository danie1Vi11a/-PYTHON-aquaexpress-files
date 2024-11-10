import tkinter as tk
from tkinter import messagebox

# Global variables for entry fields
name_entry = None
address_entry = None
gallons_entry = None
delivery_date_entry = None
delivery_time_entry = None

# In-memory order storage (dictionary to store orders)
orders = {}

# Function to place an order
def place_order():
    global name_entry, address_entry, gallons_entry, delivery_date_entry, delivery_time_entry

    # Get values from entry fields
    name = name_entry.get()
    address = address_entry.get()
    gallons = gallons_entry.get()
    delivery_date = delivery_date_entry.get()
    delivery_time = delivery_time_entry.get()

    # Check if any field is empty
    if not name or not address or not gallons or not delivery_date or not delivery_time:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    # Validate that the number of gallons is an integer
    try:
        gallons = int(gallons)
    except ValueError:
        messagebox.showerror("Error", "Number of gallons must be a valid integer.")
        return

    # Generate a new order ID
    order_id = len(orders) + 1

    # Create a new order dictionary
    order = {
        'order_id': order_id,
        'name': name,
        'address': address,
        'gallons': gallons,
        'delivery_date': delivery_date,
        'delivery_time': delivery_time,
        'status': 'Processing'
    }

    # Store the order in the orders dictionary
    orders[order_id] = order

    # Clear the form entries after placing order
    clear_form_entries()

    # Switch to the receipt page to show the order details
    show_receipt(order)

# Function to clear form entries
def clear_form_entries():
    name_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    gallons_entry.delete(0, tk.END)
    delivery_date_entry.delete(0, tk.END)
    delivery_time_entry.delete(0, tk.END)

# Function to show order receipt
def show_receipt(order):
    # Hide the form frame
    form_frame.grid_forget()

    # Create receipt frame
    receipt_frame = tk.Frame(root, padx=20, pady=20, bg="#e0f7fa")
    receipt_frame.grid(row=0, column=0, sticky="nsew")

    # Display receipt details
    tk.Label(receipt_frame, text="Order Receipt", font=("Arial", 20, "bold"), bg="#e0f7fa", fg="#1565c0").grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")

    tk.Label(receipt_frame, text="Order ID:", font=("Arial", 12, "bold"), bg="#e0f7fa").grid(row=1, column=0, sticky="w")
    tk.Label(receipt_frame, text=order['order_id'], font=("Arial", 12), bg="#e0f7fa").grid(row=1, column=1, sticky="w")

    tk.Label(receipt_frame, text="Name:", font=("Arial", 12, "bold"), bg="#e0f7fa").grid(row=2, column=0, sticky="w")
    tk.Label(receipt_frame, text=order['name'], font=("Arial", 12), bg="#e0f7fa").grid(row=2, column=1, sticky="w")

    tk.Label(receipt_frame, text="Address:", font=("Arial", 12, "bold"), bg="#e0f7fa").grid(row=3, column=0, sticky="w")
    tk.Label(receipt_frame, text=order['address'], font=("Arial", 12), bg="#e0f7fa").grid(row=3, column=1, sticky="w")

    tk.Label(receipt_frame, text="Number of Gallons:", font=("Arial", 12, "bold"), bg="#e0f7fa").grid(row=4, column=0, sticky="w")
    tk.Label(receipt_frame, text=order['gallons'], font=("Arial", 12), bg="#e0f7fa").grid(row=4, column=1, sticky="w")

    tk.Label(receipt_frame, text="Delivery Date:", font=("Arial", 12, "bold"), bg="#e0f7fa").grid(row=5, column=0, sticky="w")
    tk.Label(receipt_frame, text=order['delivery_date'], font=("Arial", 12), bg="#e0f7fa").grid(row=5, column=1, sticky="w")

    tk.Label(receipt_frame, text="Delivery Time:", font=("Arial", 12, "bold"), bg="#e0f7fa").grid(row=6, column=0, sticky="w")
    tk.Label(receipt_frame, text=order['delivery_time'], font=("Arial", 12), bg="#e0f7fa").grid(row=6, column=1, sticky="w")

    tk.Label(receipt_frame, text="Status:", font=("Arial", 12, "bold"), bg="#e0f7fa").grid(row=7, column=0, sticky="w")
    tk.Label(receipt_frame, text=order['status'], font=("Arial", 12), bg="#e0f7fa").grid(row=7, column=1, sticky="w")

    # Back button to return to order form
    back_button = tk.Button(receipt_frame, text="Back to Order Form", font=("Arial", 14, "bold"), command=show_form, bg="#1565c0", fg="white", padx=20, pady=10)
    back_button.grid(row=8, columnspan=2, pady=20)

    # Center the receipt frame content
    for i in range(9):
        receipt_frame.grid_rowconfigure(i, weight=1)
    receipt_frame.grid_columnconfigure(0, weight=1)
    receipt_frame.grid_columnconfigure(1, weight=1)

# Function to show order form
def show_form():
    # Destroy all widgets in root window
    for widget in root.winfo_children():
        widget.destroy()

    # Recreate form frame
    global form_frame
    form_frame = tk.Frame(root, padx=20, pady=20, bg="#e0f7fa")
    form_frame.grid(row=0, column=0, sticky="nsew")

    # Custom font for headers
    header_font = ("Arial", 20, "bold")

    # Centered title
    title_label = tk.Label(form_frame, text="AquaExpress Water Delivery", font=header_font, bg="#e0f7fa", fg="#1565c0")
    title_label.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")

    # Labels and entries in form_frame
    labels = ["Name:", "Address:", "Number of Gallons:", "Delivery Date:", "Delivery Time:"]
    entries = [tk.Entry(form_frame, font=("Arial", 12)) for _ in range(len(labels))]

    for i, label in enumerate(labels):
        tk.Label(form_frame, text=label, font=("Arial", 14, "bold"), bg="#e0f7fa").grid(row=i + 1, column=0, sticky="e", pady=5)
        entries[i].grid(row=i + 1, column=1, pady=5, sticky="w")

        # Assign entries to global variables
        if i == 0:
            global name_entry
            name_entry = entries[i]
        elif i == 1:
            global address_entry
            address_entry = entries[i]
        elif i == 2:
            global gallons_entry
            gallons_entry = entries[i]
        elif i == 3:
            global delivery_date_entry
            delivery_date_entry = entries[i]
        elif i == 4:
            global delivery_time_entry
            delivery_time_entry = entries[i]

    # Submit button
    submit_button = tk.Button(form_frame, text="Place Order", font=("Arial", 14, "bold"), command=place_order, bg="#1565c0", fg="white", padx=20, pady=10)
    submit_button.grid(row=len(labels) + 1, columnspan=2, pady=20)

    # Center the form frame content
    for i in range(len(labels) + 2):
        form_frame.grid_rowconfigure(i, weight=1)
    form_frame.grid_columnconfigure(0, weight=1)
    form_frame.grid_columnconfigure(1, weight=1)

    # Configure root grid to center form_frame
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)

# Create main application window
root = tk.Tk()
root.title("AquaExpress Water Delivery")

# Set background color
root.configure(bg="#e0f7fa")  # Light blue background

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size and position it in the center of the screen
window_width = int(screen_width * 0.8)  # 80% of screen width
window_height = int(screen_height * 0.8)  # 80% of screen height

# Calculate the position of the window
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set geometry and position
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Show the order form initially
show_form()

# Run the Tkinter main loop
root.mainloop()
