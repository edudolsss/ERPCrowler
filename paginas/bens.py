from customtkinter import CTkFrame, CTkLabel, CTkEntry,CTkButton,LEFT

def start_Bens(master):

    frame_all = CTkFrame(master=master, width=880,height=600)
    frame_all.pack()

    titulo_pagina = CTkLabel(master=master, text="Bens")
    titulo_pagina.pack(ipadx=100)