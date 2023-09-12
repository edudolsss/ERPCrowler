from customtkinter import CTkFrame, CTkLabel, CTkEntry


def start_Relatorios(master):

    frame_all = CTkFrame(master=master, width=880,height=600)
    frame_all.pack()

    titulo_pagina = CTkLabel(master=master, text="Página de Relatórios")
    titulo_pagina.pack()