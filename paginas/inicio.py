from customtkinter import CTkFrame, CTkLabel, CTkEntry,CTkButton,LEFT,RIGHT,TOP
from apps import cliente


def start_Inicio(master):

    frame_left = CTkFrame(master=master, width=445,height=500)
    frame_left.pack(side=LEFT,padx=30,ipady=160)

    frame_right = CTkFrame(master=master, width=445,height=500)
    frame_right.pack(side=LEFT,padx=10,ipady=120)

    # titulo_pagina = CTkLabel(master=master, text="Avisos")
    # titulo_pagina.pack(ipadx=100)

    # Área de Login
    titulo_login = CTkLabel(master=frame_left, text="Login de Conta")
    titulo_login.pack(ipady=20,padx=150)

    entry_login_user = CTkEntry(master=frame_left, placeholder_text="Login")
    entry_login_user.pack(pady=5)

    entry_senha_user = CTkEntry(master=frame_left,placeholder_text="Senha",show="*")
    entry_senha_user.pack(pady=5)

    btn_logar = CTkButton(master=frame_left, text="Entrar")
    btn_logar.pack(pady=5)


    # Área de Cadastro
    titulo_cadastro = CTkLabel(master=frame_right, text="Cadastro de Conta")
    titulo_cadastro.pack(ipady=20,padx=150)

    entry_login = CTkEntry(master=frame_right, placeholder_text="Login")
    entry_login.pack(pady=5)

    entry_senha = CTkEntry(master=frame_right,placeholder_text="Senha",show="*")
    entry_senha.pack(pady=5)

    entry_confirmSenha = CTkEntry(master=frame_right,placeholder_text="Confirmar Senha",show="*")
    entry_confirmSenha.pack(pady=5)

    entry_email = CTkEntry(master=frame_right, placeholder_text="E-mail")
    entry_email.pack(pady=5)

    btn_cadastrar = CTkButton(master=frame_right, text="Cadastrar",command=lambda:cliente.criarConta(entry_login.get(),entry_senha.get(),entry_confirmSenha.get(),entry_email.get()))
    btn_cadastrar.pack(pady=5)


    