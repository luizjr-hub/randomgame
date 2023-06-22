# ------------------ Imports ---------------------- #
import random
from PIL import Image, ImageTk
from tkinter import Button, Frame, Label, PhotoImage, ttk, Tk
# ------------------ Código ---------------------- #

# ------- Criando o código da imagem ------- #
janela = Tk()
janela.title('RandomCars')
janela.geometry('800x600')
janela.resizable(False, False)
janela.configure(background='#00008B')

f1 = Frame(janela, width=700, height=400, background='white')
f1.place(relx=0.5, rely=0.35, anchor="center")

img = ImageTk.PhotoImage(Image.open("img_cars\\login.jpg"))
panel = Label(f1, image = img)
panel.place(relx=0.5, rely=0.50, anchor='center')

l1 = Label(janela, text="NFSU2", font=("Times New Roman bold", 18), background='#00008B', foreground='white')
l1.place(relx=0.5, rely=0.73, anchor="center")


b1 = Button(janela, text="RANDOM", width=11, height=2)
b1.place(relx=0.5, rely=0.95, anchor='center')

l2 = Label(janela, text="ALL CARS \n_______________________________________________________________________"
           "\nACURA RSX - AUDI A3 - AUDI TT - CADILLAC ESCALADE - FORD FOCUS -\nFORD MUSTANG -"
           "HONDA CIVIC - HUMMER H2 - HYUNDAI TIBURON GT - INFINITI GG35 - LEXUS IS300 -\nLINCOLN NAVIGATOR - MAZDA MIATA RX -5 -"
           "MAZDA RX7 - MAZDA RX -8 - MITSUBISHI 3000GT -\nMITSUBISHI ECLIPSE - MITSUBISHI LANCER EVO VIII - NISSAN 240SX - NISSAN 350Z -"
            "NISSAN SENTRA -\nNISSAN SKYLINE - PEUGEOT 106 - PEUGEOT 206 - PONTIAC GTO - SUBARU IMPREZA - TOYOTA CELICA -\nTOYOTA COROLLA -"
            "TOYOTA SUPRA - VAUXRALL CORSA 1.8 - VOLKSWAGEM GOLF GTI.\n_________________________________________________________________________",
            font=("Times New Roman bold", 12), background="#00008B", foreground="white")
l2.place(relx=0.5, rely=0.78, anchor='center')
janela.mainloop()