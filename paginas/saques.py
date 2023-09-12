from customtkinter import CTkFrame, CTkLabel, CTkEntry,CTkButton,LEFT
from apps import cliente as defs


def start_Saques(master):
    # titulo_pagina = CTkLabel(master=master, text="Página Saques")
    # titulo_pagina.pack()

    frame_left = CTkFrame(master=master, width=445, height=450)
    frame_left.pack(side=LEFT,padx=10,ipady=200,ipadx=30)

    frame_right = CTkFrame(master=master, width=655, height=450)
    frame_right.pack(side=LEFT,padx=10,ipady=23)

    realizar_saque = CTkEntry(master=frame_left, placeholder_text="Valor do Saque")
    realizar_saque.pack(pady=10)

    btn_saque = CTkButton(master=frame_left,text="Sacar",width=80)
    btn_saque.pack(pady=10)





