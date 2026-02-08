
from tkinter import *
import customtkinter

# Okno
window = customtkinter.CTk()
window.title("Úkolníček")
window.geometry("600x430")
window.resizable(False, False)
window.iconbitmap('icon.ico')
customtkinter.set_appearance_mode("dark")

# Definujeme fonty a barvy
main_font = ("Arial", 20)
main_color = "#dd7f00"
button_color = "#e2cff4"


# Funkce
def add_text(): # přidání textového pole
    list_box.insert(END, user_input.get())
    user_input.delete(0, END)

def remove_text_item(): # Odstraní jednu položku seznamu
    list_box.delete(ANCHOR)

def clear_all_list(): # Ostraní všechny položky ze seznamu
    list_box.delete(0, END)

def save_list(): # Uložení seznamu úkolů
    with open('tasks.txt', 'w') as file:
        my_tasks = list_box.get(0, END)
        for one_task in my_tasks:
            if one_task.endswith("\n"):
                file.write(f"{one_task}")
            else:
                file.write(f"{one_task}\n")

def open_tasks(): # zkouška otevření souboru Task
    try:
        with open('tasks.txt', 'r') as file:
            for one_line in file:
                list_box.insert(END, one_line)
    except:
        print("Chyba načtení.")


# Framy
input_frame = customtkinter.CTkFrame(window)
text_frame = customtkinter.CTkFrame(window)
button_frame = customtkinter.CTkFrame(window)
input_frame.pack(pady = 5)
text_frame.pack(pady = 5)
button_frame.pack()

# Input_frame - obsah
user_input = customtkinter.CTkEntry(input_frame, width=400)
user_input.grid(row=0, column=0, padx= 5, pady= 5)
add_button = customtkinter.CTkButton(input_frame, text = "Přidat", command = add_text)
add_button.grid(row=0, column=1, padx= 5, pady= 5)

# Scrollbar
text_scrollbar = customtkinter.CTkScrollbar(text_frame)
text_scrollbar.grid(row=0, column=1, padx=5, sticky= N + S)

# Text frame - obsah
list_box = Listbox(text_frame, height = 10, width= 35, borderwidth= 3, font = main_font, yscrollcommand = text_scrollbar.set)
list_box.grid(row=0, column=0)
# Propojení scrollbar s list_boxem
#text_scrollbar.config(command=list_box.yview)

# Button frame obsah - spodní tlačítka
remove_button = customtkinter.CTkButton(button_frame, text="Remove", command = remove_text_item)
remove_button.grid(row=0, column=0, padx= 5, pady= 5)

clear_button = customtkinter.CTkButton(button_frame, text="Clear all", command = clear_all_list)
clear_button.grid(row=0, column=1, padx= 5, pady= 5)

save_button = customtkinter.CTkButton(button_frame, text="Save", command = save_list)
save_button.grid(row=0, column=2, padx= 5, pady= 5)

quit_button = customtkinter.CTkButton(button_frame, text="Quit", command = window.destroy)
quit_button.grid(row=0, column=3, padx= 5, pady= 5)


# Načtení seznamu úkolů do Text_frame
open_tasks()

# Hlavní cyklus
window.mainloop()
