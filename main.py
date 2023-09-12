from customtkinter import CTk,CTkTabview
from paginas import inicio,saques,depositos,rendimento,relatorios,bens

screenMaster = CTk()
screenMaster.title("Crowler Fin")
screenMaster.geometry("900x600")
screenMaster.resizable(False,False)
screenMaster.iconbitmap("utils/01.ico")

menu = CTkTabview(master=screenMaster,width=890,height=595)
tab_inicio = menu.add("Inicio")
tab_depositos = menu.add("Depositos")
tab_saques = menu.add("Saques")
tab_bens = menu.add("Bens")
tab_relatorios = menu.add("Relatórios")
tab_rendimento = menu.add("Rendimento Financeiro")
menu.pack()


inicio.start_Inicio(tab_inicio)
depositos.start_Depositos(tab_depositos)
saques.start_Saques(tab_saques)
bens.start_Bens(tab_bens)
relatorios.start_Relatorios(tab_relatorios)
rendimento.start_Rendimento(tab_rendimento)


screenMaster.mainloop()