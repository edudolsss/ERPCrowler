from customtkinter import CTkFrame, CTkLabel, CTkEntry


def start_Rendimento(master):
    frame_all = CTkFrame(master=master, width=880,height=600)
    frame_all.pack()

    titulo_pagina = CTkLabel(master=master, text="Página de Rendimento")
    titulo_pagina.pack()