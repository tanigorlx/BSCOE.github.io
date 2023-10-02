import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("1000x850")
root.title("Engineering Economics Calculator")

# Create a frame for the top section (Calculator label, dropdown, and Use button)
top_frame = customtkinter.CTkFrame(master=root)
top_frame.pack(pady=20, padx=60, fill="both")

# Create a frame for the input fields, labels, and result label
calculation_frame = customtkinter.CTkFrame(master=root, height= 250)
calculation_frame.pack(pady=20, padx=60, fill="both")

# Create a frame for displaying the result
result_frame = customtkinter.CTkFrame(master=root, height=100, width=500)
result_frame.pack()

# Define entry widgets as global variables
future_value_entry = None
discount_rate_entry = None
years_entry = None

def PVcalc(f_val, discount_rate, years):
    # Calculate the present value of a future cash flow.
    p_val = f_val / (1 + discount_rate) ** years
    return p_val

# Function to calculate present value and display result for "Present Value of Money"
def calculate_present_value_of_money():
    global future_value_entry, discount_rate_entry, years_entry

    # Get values entered by the user
    f_val = float(future_value_entry.get())
    discount_rate = float(discount_rate_entry.get())
    years = int(years_entry.get())

    # Calculate present value using PVcalc function
    present_value = PVcalc(f_val, discount_rate, years)

    # Display the result in the result_frame
    result_label = customtkinter.CTkLabel(result_frame, text=f"Present Value: {present_value:.2f}", font=("Jetbrains Mono", 18, "bold"))
    result_label.pack()

def update():
    global future_value_entry, discount_rate_entry, years_entry

    # Hide all widgets within calculation_frame
    for widget in calculation_frame.winfo_children():
        widget.pack_forget()

    choice = optionmenu.get()
    if choice == "Future Value of Annuity":
        label1 = customtkinter.CTkLabel(calculation_frame, text="Label 1: Future Value of Annuity")
        label1.pack()

        label2 = customtkinter.CTkLabel(calculation_frame, text="Label 2: Future Value of Annuity")
        label2.pack()

        label3 = customtkinter.CTkLabel(calculation_frame, text="Label 3: Future Value of Annuity")
        label3.pack()

    elif choice == "Present Value of Annuity":
        label1 = customtkinter.CTkLabel(calculation_frame, text="Label 1: Present Value of Annuity")
        label1.pack()

        label2 = customtkinter.CTkLabel(calculation_frame, text="Label 2: Present Value of Annuity")
        label2.pack()

        label3 = customtkinter.CTkLabel(calculation_frame, text="Label 3: Present Value of Annuity")
        label3.pack()

    elif choice == "Future Time Value of Money":
        label1 = customtkinter.CTkLabel(calculation_frame, text="Label 1: Future Time Value of Money")
        label1.pack()

        label2 = customtkinter.CTkLabel(calculation_frame, text="Label 2: Future Time Value of Money")
        label2.pack()

        label3 = customtkinter.CTkLabel(calculation_frame, text="Label 3: Future Time Value of Money")
        label3.pack()

    elif choice == "Present Value of Money":
        global future_value_entry, discount_rate_entry, years_entry
        future_value_label = customtkinter.CTkLabel(calculation_frame, text="Future Value:")
        future_value_label.pack()
        future_value_entry = customtkinter.CTkEntry(calculation_frame)
        future_value_entry.pack()

        discount_rate_label = customtkinter.CTkLabel(calculation_frame, text="Discount Rate (decimal):")
        discount_rate_label.pack()
        discount_rate_entry = customtkinter.CTkEntry(calculation_frame)
        discount_rate_entry.pack()

        years_label = customtkinter.CTkLabel(calculation_frame, text="Years:")
        years_label.pack()
        years_entry = customtkinter.CTkEntry(calculation_frame)
        years_entry.pack()

        calculate_button = customtkinter.CTkButton(calculation_frame, text="Calculate", command=calculate_present_value_of_money)
        calculate_button.pack()

    elif choice == "Price Elasticity":
        label1 = customtkinter.CTkLabel(calculation_frame, text="Label 1: Price Elasticity")
        label1.pack()

        label2 = customtkinter.CTkLabel(calculation_frame, text="Label 2: Price Elasticity")
        label2.pack()

        label3 = customtkinter.CTkLabel(calculation_frame, text="Label 3: Price Elasticity")
        label3.pack()

label = customtkinter.CTkLabel(master=top_frame, text="Calculator", font=("Jetbrains Mono", 24))
label.pack(pady=12, padx=10)

optionmenu = customtkinter.CTkOptionMenu(
    master=top_frame,
    values=[
        "Future Value of Annuity",
        "Present Value of Annuity",
        "Future Time Value of Money",
        "Present Value of Money",
        "Price Elasticity"
    ],
    width=40,
    height=40,
    font=("Jetbrains Mono", 18),
    dropdown_font=("Roboto", 13)
)
optionmenu.pack(pady=10, padx=60)

change_button = customtkinter.CTkButton(master=top_frame, text="Use", command=update)
change_button.pack(pady=5, padx=5)

root.mainloop()
