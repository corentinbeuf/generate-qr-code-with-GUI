# Import modules to generate QR-code
from ensurepip import version
from pickle import TRUE
from turtle import fillcolor
import qrcode
from qrcode.constants import ERROR_CORRECT_L

# Import Tkinter for GUI
from tkinter import *
from tkinter import messagebox

import os

def create_folder():
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def generate_qrcode(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_L,
        box_size=3,
        border=5
    )
    qr.add_data(url)
    qr.make(fit=TRUE)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

def check_entries(*args):
    if url_var.get().strip() and filename_var.get().strip():
        bouton_generate.place(x=200, y=450)
    else:
        bouton_generate.place_forget()

def generate():
    try:
        path = create_folder()
        filename = os.path.join(path, user_filename.get().strip() + '.png')
        generate_qrcode(user_url.get().strip(), filename)
        messagebox.showinfo("Succès", "Le QR-code a été généré avec succès.")
        messagebox.showinfo("Succès", "Le QR-code a été enregitré dans le dossier : " + folder_path)
    except Exception as e:
        messagebox.showerror("Erreur", f"Échec de la génération : {e}")

def save():
    try:
        messagebox.showinfo("Succès", "Le QR-code a été enregitré dans le dossier : " + folder_path)
    except Exception as e:
        messagebox.showerror("Erreur", f"Échec de la génération : {e}")

def save_and_notify():
    save()

# Create Tkinter window
fenetre = Tk()
fenetre.title("Generate QR-code")
fenetre.configure(bg="#000033")
canvas=Canvas(fenetre, width=800, height=600)
canvas.pack()

# Declaration of global variables
url_var = StringVar()
filename_var = StringVar()
url_var.trace_add("write", check_entries)
filename_var.trace_add("write", check_entries)

# Check OS to declare the good path
if os.name == 'nt':  # For Windows
    folder_path = os.path.join(os.environ['USERPROFILE'], 'Documents', 'qrcode')
    print(folder_path)
else:  # For Linux & MacOS
    folder_path = os.path.join(os.environ['HOME'], 'Documents', 'qrcode')
    print(folder_path)

# Create label to write URL
label_url = Label(fenetre, text="URL de la page web :")
label_url.place(x=200, y=200)
user_url = Entry(fenetre, textvariable=url_var)
user_url.configure(width=30, bg="white", fg="black")
user_url.place(x=350, y=200)

# Create label to write name of the file of QR-code generated
label_url = Label(fenetre, text="Nom du fichier sauvegardé :")
label_url.place(x=160, y=300)
user_filename = Entry(fenetre, textvariable=filename_var)
user_filename.configure(width=30, bg="white", fg="black")
user_filename.place(x=350, y=300)

# Create button to generate QR-code
bouton_generate = Button(fenetre, text="Générer", command=generate)
bouton_generate.pack(side="right", padx=5, pady=5)
bouton_generate.configure(width=10, height=2, bg="gray", fg="black")
bouton_generate.place(x=200, y= 450)
bouton_generate.place_forget()

# Create button to quit app
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.quit)
bouton_quitter.pack(side="right", padx=5, pady=5)
bouton_quitter.configure(width=10, height=2, bg="gray", fg="black")
bouton_quitter.place(x=500, y= 450)

fenetre.mainloop()