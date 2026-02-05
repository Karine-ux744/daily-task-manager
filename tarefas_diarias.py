import tkinter as tk
from tkinter import font

# Paleta de cores
COR_FUNDO = "#f2d5ff"      # Lilás acinzentado
COR_TEXTO = "#4A4A4A"       # Cinza escuro
COR_BOTAO = "#D4A5E8"       # Lavanda
COR_BOTAO_HOVER = "#C088D9" # Lavanda escura

# Configurações gerais da janela
janela = tk.Tk()
logo_janela = tk.PhotoImage(
    file=r"C:\Users\karin\OneDrive\Documentos\Projetos Python\Minhas tarefas diárias\logo to do list.png",master=janela)
janela.iconphoto(False,logo_janela)
janela.title("Tarefas Diárias")
janela.configure(bg=COR_FUNDO)
janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)

# Fonte padrão
fonte_padrao = font.nametofont("TkDefaultFont")
fonte_padrao.configure(family="Segoe UI", size=12)

# Centralizando a janela na tela
largura_janela = 550
altura_janela = 450
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
x = (largura_tela - largura_janela) // 2
y = (altura_tela - altura_janela) // 2
janela.geometry(f"{largura_janela}x{altura_janela}+{x}+{y}")

# Funcionalidades
def add_tarefas():
    '''
    Executada ao clicar no botão "Adicionar tarefas" no frame_principal.

    Ela esconde o frame_principal, mostra o fram_add_tarefas com seus respectivos widgets.
    '''
    frame_principal.grid_forget()
    frame_add_tarefas.grid(row=0,column=0,sticky="nsew")
    frame_add_tarefas.grid_columnconfigure([0,1],weight=1)
    frame_add_tarefas.grid_rowconfigure(3,weight=1)
    msg_caixa_texto_tarefas.grid(row=0,column=0,pady=(0,10),columnspan=2)
    caixa_texto_tarefas.grid(row=1,column=0,pady=5,columnspan=2)
    botaov_adicionar_tarefas.grid(row=3,column=0,pady=10,sticky="s")
    botao_salvar_tarefas.grid(row=3,column=1,pady=10,sticky="s")
def salvar_tarefas():
    '''
    Executada ao clicar no botão "Salvar" no frame_add_tarefas.

    Ela pega o texto inserido pelo usuário na caixa e o transforma em lista, sem espaços em branco sobrando.
    Também transforma cada item da lista em um Checkbutton que será exibido no frame_ver_tarefas, esconde o frame_add_tarefas e
    mostra o frame_tarefas_salvas com seus respectivos widgets.
    '''
    texto_caixa_tarefas = caixa_texto_tarefas.get("1.0",tk.END)
    lista_texto = texto_caixa_tarefas.split("\n")
    lista_texto_tratada = [item for item in lista_texto if item != ""]
    lista_final = [item for item in lista_texto_tratada if item not in tarefas_ja_adicionadas]
    if not lista_texto_tratada:
        aviso_sem_tarefas.grid(row=2,column=0,padx=10,pady=10,columnspan=2)
    for item in lista_final:
        frame_add_tarefas.grid_forget()
        frame_tarefas_salvas.grid(row=0,column=0,sticky="nsew")
        frame_tarefas_salvas.grid_columnconfigure([0,1],weight=1)
        msg_tarefas_salvas.grid(row=0,column=0,pady=10,columnspan=2)
        botaov_tarefas_salvas.grid(row=1,column=0,pady=10,padx=10,sticky="e")
        botao2_ver_tarefas.grid(row=1,column=1,pady=10,padx=10,sticky="w")
        item_lista_final = tk.StringVar(value=item)
        estado = tk.IntVar(value=0)
        tarefa = tk.Checkbutton(frame_ver_tarefas,textvariable=item_lista_final, variable = estado,command=opcoes_tarefas,bg=COR_FUNDO)
        tarefas_ja_adicionadas.append(item)
        dicionario_tarefas[item] = estado
        dicionario_checkbuttons[item] = tarefa    
def ver_tarefas():
    '''
    Executada ao clicar no botão "Ver tarefas" no frame_principal e no frame_tarefas_salvas.

    Ela esconde o frame em que o botão está, mostra o frame_tarefas_salvas com seus respectivos widgets.
    '''
    frame_principal.grid_forget()
    frame_ver_tarefas.grid(row=0,column=0,sticky="nsew")
    frame_ver_tarefas.grid_rowconfigure(99, weight=1)
    frame_ver_tarefas.grid_columnconfigure([0,1,2], weight=1)
    
    opcao_todas_tarefas.grid(row=2,column=0,sticky="n",pady=(20,0))
    opcao_tarefas_pendentes.grid(row=2,column=1,sticky="n",pady=(20,0))
    opcao_tarefas_concluidas.grid(row=2,column=2,sticky="n",pady=(20,0))

    botaov_ver_tarefas.grid(row=99,column=0,sticky="sw",padx=10,pady=10)
    botao_excluir_tarefas.grid(row=99,column=2,sticky="se",padx=10,pady=10)
def opcoes_tarefas():
    '''
    Executada ao clicar nos Radiobuttons "todas","pendentes" e "concluidas" no frame_ver_tarefas.

    Determina a lógica que diz onde cada Checkbotton será exibido no frame_ver_tarefas.
    '''
    opcao = var_opcao_tarefas.get()
    linha = 3
    for tarefa,estado in dicionario_tarefas.items():
        check = dicionario_checkbuttons[tarefa]
        if opcao == "pendentes":
            if estado.get() == 0:
                check.grid(row=linha,column=1)                
                linha += 1
            else:
                check.grid_remove()
        elif opcao == "concluidas":
            if estado.get() == 1:
                check.grid(row=linha,column=2)
                linha += 1
            else:
                check.grid_remove()
        elif opcao == "todas":
            if estado.get() == 0 or estado.get() == 1:
                check.grid(row=linha,column=0)
                linha += 1
            else:
                check.grid_remove()
def voltar_add_tarefas():
    '''
    Executada ao clicar no botão "Voltar" no frame_add_tarefas.

    Ela esconde o frame_add_tarefas e mostra o frame_principal com seus respectivos widgets.
    '''
    frame_add_tarefas.grid_forget()
    frame_principal.grid(row=0,column=0,sticky="nsew")
def voltar_tarefas_salvas():
    '''
    Executada ao clicar no botão "Voltar" no frame_tarefas_salvas.

    Ela esconde o frame_tarefas_salvas e mostra o frame_add_tarefas com seus respectivos widgets.
    '''
    frame_tarefas_salvas.grid_forget()
    frame_add_tarefas.grid(row=0,column=0,sticky="nsew")
def voltar_ver_tarefas():
    '''
    Executada ao clicar no botão "Voltar" no frame_ver_tarefas.

    Ela esconde o frame_ver_tarefas e mostra o frame_principal com seus respectivos widgets.
    '''
    frame_ver_tarefas.grid_forget()
    frame_principal.grid(row=0,column=0,sticky="nsew")
def ver_tarefas2():
    '''
    Executada ao clicar no botão "Ver tarefas" no frame_tarefas_salvas.

    Ela esconde o frame_tarefas_salvas e chama a função ver_tarefas para mostrar o 
    frame_ver_taerfas com seus respectivos widgets.
    '''
    frame_tarefas_salvas.grid_forget()
    ver_tarefas()
def excluir_tarefas():
    '''
    Executada ao clicar no botão "Excluir tarefas" no frame_ver_tarefas.

    Ela apaga todos os Checkbutton criados, limpa dicionario_checkbuttons, dicionario_tarefas e tarefas_ja_adicionadas para que o usuário possa adicionar novas tarefas sem que as antigas apareçam, e apaga o texto colocado pelo usuário na caixa de texto.
    '''
    for tarefa in dicionario_checkbuttons.values():
        tarefa.destroy()
    dicionario_checkbuttons.clear()
    dicionario_tarefas.clear()
    tarefas_ja_adicionadas.clear()
    caixa_texto_tarefas.delete("1.0",tk.END)

# Variáveis globais
tarefas_ja_adicionadas = []
dicionario_tarefas = {}
dicionario_checkbuttons = {}

# Frames
frame_principal = tk.Frame(janela, bg=COR_FUNDO)
frame_principal.grid(row=0,column=0,sticky="nsew")
frame_principal.grid_columnconfigure(0, weight=1)
frame_principal.grid_columnconfigure(1, weight=1)
frame_add_tarefas = tk.Frame(janela,bg=COR_FUNDO)
subframe_add_tarefas = tk.Frame(frame_add_tarefas,bg=COR_FUNDO)
frame_tarefas_salvas = tk.Frame(janela,bg=COR_FUNDO)
frame_ver_tarefas = tk.Frame(janela,bg=COR_FUNDO)


# Definindo widgets
titulo = tk.Label(master=frame_principal,text="Tarefas de hoje",height=4,font=("Segoe UI", 20,"bold"),fg=COR_BOTAO,bg=COR_FUNDO)
botao_add_tarefas = tk.Button(master=frame_principal,text="Adicionar tarefas", command=add_tarefas,bg=COR_BOTAO,fg="white",height=2,width=15,relief="flat",cursor="hand2",font=("Segoe UI", 10,"bold"))
botao_ver_tarefas = tk.Button(master=frame_principal,text="Ver tarefas",command=ver_tarefas,bg=COR_BOTAO,fg="white",height=2,width=15,relief="flat",cursor="hand2",font=("Segoe UI", 10,"bold"))
var_opcao_tarefas = tk.StringVar(value="0")
opcao_todas_tarefas = tk.Radiobutton(frame_ver_tarefas,text="Todas", variable = var_opcao_tarefas, value = "todas",command=opcoes_tarefas,font=("Segoe UI",12,"bold"),fg=COR_TEXTO,bg=COR_FUNDO,selectcolor=COR_BOTAO_HOVER)
opcao_tarefas_pendentes = tk.Radiobutton(frame_ver_tarefas,text="Pendentes", variable = var_opcao_tarefas, value = "pendentes",command=opcoes_tarefas,font=("Segoe UI",12,"bold"),fg=COR_TEXTO,bg=COR_FUNDO,selectcolor=COR_BOTAO_HOVER)
opcao_tarefas_concluidas = tk.Radiobutton(frame_ver_tarefas,text="Concluídas", variable = var_opcao_tarefas, value = "concluidas",command=opcoes_tarefas,font=("Segoe UI",12,"bold"),fg=COR_TEXTO,bg=COR_FUNDO,selectcolor=COR_BOTAO_HOVER)
msg_caixa_texto_tarefas = tk.Label(frame_add_tarefas,text="Digite 1 tarefa por linha:",font=("Segoe UI",12,"bold"),fg=COR_TEXTO,bg=COR_FUNDO)
caixa_texto_tarefas = tk.Text(frame_add_tarefas,height=8,width=35,font=("Songoe UI",11),fg=COR_TEXTO,bg="#ffffff",relief="solid",borderwidth=1,wrap="word")
botao_salvar_tarefas = tk.Button(frame_add_tarefas,text="Salvar",command=salvar_tarefas,font=("Segoe UI", 10,"bold"),bg=COR_BOTAO,fg="white",height=2,width=15,relief="flat",cursor="hand2")
aviso_sem_tarefas = tk.Label(frame_add_tarefas,text="Digite pelo menos 1 tarefa antes de adicionar",font=("Songoe UI",10),fg="#D9534F",bg=COR_FUNDO,wraplength=300)
msg_tarefas_salvas = tk.Label(frame_tarefas_salvas,text="✓ Tarefas salvas com sucesso!",font=("Songoe UI",10,"bold"),fg="#5CB85C",bg=COR_FUNDO)
botaov_adicionar_tarefas = tk.Button(frame_add_tarefas,text="⟵ Voltar",command=voltar_add_tarefas,font=("Segoe UI", 10,"bold"),bg=COR_BOTAO,fg="white",height=2,width=15,relief="flat",cursor="hand2")
botaov_tarefas_salvas = tk.Button(frame_tarefas_salvas,text="⟵ Voltar",command=voltar_tarefas_salvas,font=("Segoe UI", 10,"bold"),bg=COR_BOTAO,fg="white",height=2,width=15,relief="flat",cursor="hand2")
botaov_ver_tarefas = tk.Button(frame_ver_tarefas,text="⟵ Voltar",command=voltar_ver_tarefas,font=("Segoe UI", 10,"bold"),bg=COR_BOTAO,fg="white",height=2,width=15,relief="flat",cursor="hand2")
botao2_ver_tarefas = tk.Button(frame_tarefas_salvas,text="Ver Tarefas",command=ver_tarefas2,font=("Segoe UI", 10,"bold"),bg=COR_BOTAO,fg="white",height=2,width=15,relief="flat",cursor="hand2")
botao_excluir_tarefas = tk.Button(frame_ver_tarefas,text="X Excluir tarefas",font=("Segoe UI", 10,"bold"),bg=COR_BOTAO,fg="white",height=2,width=15,relief="flat",cursor="hand2",command=excluir_tarefas)  

titulo.grid(row=0,column=0,columnspan=2)
botao_add_tarefas.grid(row=1,column=0,padx=(5),pady=10,sticky="e")
botao_ver_tarefas.grid(row=1,column=1,padx=(5),pady=10,sticky="w")

janela.mainloop()