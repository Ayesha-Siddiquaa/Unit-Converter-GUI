import tkinter as tk

# Function to perform length conversions
def convert_length():
    length_value = float(length_entry.get())
    length_convert = int(length_choice.get())
    if length_convert == 1:
        result_label.config(text=f"{length_value} cm is equal to {length_value / 30.48:.2f} feet.")
    elif length_convert == 2:
        result_label.config(text=f"{length_value} feet is equal to {length_value * 30.48:.2f} cm.")
    elif length_convert == 3:
        result_label.config(text=f"{length_value} feet is equal to {length_value * 12:.2f} inches.")

# Function to perform area conversions
def convert_area():
    area_value = float(area_entry.get())
    area_convert = int(area_choice.get())
    if area_convert == 1:
        result_label_area.config(text=f"{area_value} sqft is equal to {area_value / 10.764:.2f} sqm.")
    elif area_convert == 2:
        result_label_area.config(text=f"{area_value} sqft is equal to {area_value * 0.000247:.2f} acres.")
    elif area_convert == 3:
        result_label_area.config(text=f"{area_value} sqft is equal to {area_value * 0.0929:.2f} hectares.")

# Create the main window
root = tk.Tk()
root.title("Unit Converter")

# Length Conversion Section
length_frame = tk.Frame(root)
length_frame.pack(pady=10)

length_label = tk.Label(length_frame, text="Enter Length:")
length_label.grid(row=0, column=0)

length_entry = tk.Entry(length_frame)
length_entry.grid(row=0, column=1)

length_choice = tk.StringVar()
length_choice.set("1")

length_options = {"Centimeter to Feet": 1, "Feet to Centimeter": 2, "Feet to Inches": 3}

for key, value in length_options.items():
    rb = tk.Radiobutton(length_frame, text=key, variable=length_choice, value=value)
    rb.grid()

convert_button_length = tk.Button(length_frame, text="Convert", command=convert_length)
convert_button_length.grid(row=4, columnspan=2)

result_label = tk.Label(length_frame, text="")
result_label.grid(row=5, columnspan=2)

# Area Conversion Section
area_frame = tk.Frame(root)
area_frame.pack(pady=10)

area_label = tk.Label(area_frame, text="Enter Area (sqft):")
area_label.grid(row=0, column=0)

area_entry = tk.Entry(area_frame)
area_entry.grid(row=0, column=1)

area_choice = tk.StringVar()
area_choice.set("1")

area_options = {"Sqft to Sqm": 1, "Sqft to Acres": 2, "Sqft to Hectares": 3}

for key, value in area_options.items():
    rb = tk.Radiobutton(area_frame, text=key, variable=area_choice, value=value)
    rb.grid()

convert_button_area = tk.Button(area_frame, text="Convert", command=convert_area)
convert_button_area.grid(row=4, columnspan=2)

result_label_area = tk.Label(area_frame, text="")
result_label_area.grid(row=5, columnspan=2)

root.mainloop()
