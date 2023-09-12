from customtkinter import CTkFrame, CTkLabel, CTkEntry,CTkButton,LEFT
from apps import cliente as defs


def start_Depositos(master):
    # titulo_pagina = CTkLabel(master=master, text="Página Depositos")
    # titulo_pagina.pack()

    frame_left = CTkFrame(master=master, width=445, height=450)
    frame_left.pack(side=LEFT,padx=10,ipady=200,ipadx=30)

    frame_right = CTkFrame(master=master, width=655, height=450)
    frame_right.pack(side=LEFT,padx=10,ipady=23)

    realizar_deposito = CTkEntry(master=frame_left, placeholder_text="Valor do Deposito")
    realizar_deposito.pack(pady=10)

    btn_depositar = CTkButton(master=frame_left,text="Depositar",width=80)
    btn_depositar.pack(pady=10)