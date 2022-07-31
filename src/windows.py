from calendar import c
from src.include.winController import *
from tkinter import *
import time
import mysql.connector
import sqlite3
import os
from PIL import ImageTk, Image
from tkinter.ttk import Treeview

# ========== DEFAULT WINDOW ==========
winW=800
winH=600
background="#5A5A5A"

class Win(Frame):
    def __init__(self,master):
        # default configs
        super().__init__(master=master, width=winW, height=winH)
        master.geometry(str(winW)+"x"+str(winH))
        master.title("Sistema de Estoque RU")
        master.resizable(False, False)
        self.pack_propagate(0)

class FirstPage(Win):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg='lightgreen')
        Label(self, text="Selecione uma opção: ", bg="lightgreen", width="300", height="2", font=("Calibri", 13)).pack()
        Label(self, text='', bg='lightgreen').pack()
        button1=Button(self, text="Login", bg='white', height="2", width="30", command=lambda: master.forward(LoginPage))
        Label(self, text="", bg='lightgreen').pack()
        button2=Button(self, text="Registrar", bg='white', height="2", width="30", command=lambda: master.forward(RegisterPage))
        button1.place(x=winW-700,y=winH-300)
        button2.place(x=winW-300,y=winH-300)

class LoginPage(Win):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg='lightblue')
        Label(self, text="Insira suas credenciais para entrar: ", font=("Verdana", 9), bg='lightblue').pack()
        Label(self, text="", bg='lightblue').pack()
        self.username_verify = StringVar()
        self.password_verify = StringVar()
        Label(self, text="Login * ", bg='lightblue').pack()
        self.username_login_entry = Entry(self, textvariable=self.username_verify)
        self.username_login_entry.pack()
        Label(self, text="", bg='lightblue').pack()
        Label(self, text="Senha * ", bg='lightblue').pack()
        self.password_login_entry = Entry(self, textvariable=self.password_verify, show= '*')
        self.password_login_entry.pack()
        Label(self, text="", bg='lightblue').pack()
        Button(self, text="Login", bg='#4CBB17', width=10, height=1, command = self.login_verify).pack()
        Button(self, text="Voltar", bg='white', width=10, height=1, command=lambda:master.backward()).place(x=winW-100,y=winH-100)

    def login_verify(self):
        username_input = self.username_verify.get()
        password_input = self.password_verify.get()
        self.username_login_entry.delete(0, END)
        self.password_login_entry.delete(0, END)

        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "@RoneCachaca2222@",
            database = "db"
        )
        
        cursor = mydb.cursor()
        cursor.execute(f"SELECT * from users where username = '{username_input}';")
        user = cursor.fetchall() #lista info do usuario

        if len(user) == 0:
            Label(self, text="Usuário não encontrado.", bg='lightblue').pack()
            return

        if password_input != user[0][2]:
            Label(self, text="Senha incorreta. Por favor, tente novamente.", bg='lightblue').pack()
            return
        
        if user[0][3] == 'Funcionário':
            self.master.forward(MenuFunc)
        elif user[0][3] == 'Nutricionista':
            self.master.forward(MenuNutri)

        mydb.commit()
        mydb.close()

class RegisterPage(Win):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg='lightblue')
        self.username = StringVar()
        self.password = StringVar()
        Label(self, text="Por favor, preencha os dados para registrar: ", font=("Verdana", 9), bg="lightblue").pack()
        Label(self, text="", bg='lightblue').pack()
        self.username_lable = Label(self, text="Login * ", bg='lightblue')
        self.username_lable.pack()
        self.username_entry = Entry(self, textvariable=self.username)
        self.username_entry.pack()
        self.password_lable = Label(self, text="Senha * ", bg='lightblue')
        self.password_lable.pack()
        self.password_entry = Entry(self, textvariable=self.password, show='*')
        self.password_entry.pack()
        self.post_entry = StringVar(self)
        self.post_entry.set("Selecione...")
        self.post_label = Label(self, text="Colaborador * ", bg='lightblue')
        self.post_label.pack()
        OptionMenu(self, self.post_entry, "Funcionário", "Nutricionista").pack()
        Label(self, text="", bg='lightblue').pack()
        Button(self, text="Registrar", width=10, height=1, bg="orange", command = self.register_user).pack()
        Button(self, text="Voltar", bg='white', width=10, height=1, command=lambda:master.backward()).place(x=winW-100,y=winH-100)

    def register_user(self):
        username_info = self.username.get()
        password_info = self.password.get()
        post_info = self.post_entry.get()
        
        if (username_info == '' or password_info == '' or post_info == 'Selecione...'):
            Label(self, text="Por favor, preencha todos os campos.", bg='lightblue', fg="red").pack()
            return
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "@RoneCachaca2222@",
            database = "db"
            )
        cursor = mydb.cursor()
        cursor.execute(f"SELECT * from users where username = '{username_info}';")
        user = cursor.fetchall() #lista info do usuario

        if len(user) != 0:
            Label(self, text="Este nome de usuário já está cadastrado.", bg='lightblue').pack()
            return
            
        cursor = mydb.cursor()
        cursor.execute(f"INSERT INTO Users(Username, Password, Tipo) VALUES('{username_info}', '{password_info}', '{post_info}')")
        mydb.commit()
        mydb.close()

#   ========== FUNC. WINDOWS ==========
class MenuFunc(Win):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg='#C4A484')
        # LABELS
        Label(self, text="MENU FUNCIONÁRIO", bg='#C4A484', font='Verdana').pack(side="top", fill="x", pady=10)
        
        # BOTÕES
        button0=Button(self, text="Atualizar Porção",width=20,height=4,command=lambda:master.forward(AtualizaPorcao))
        button1=Button(self, text="Pesquisar",width=20,height=4,command=lambda:master.forward(BuscaItemFunc))
        button2=Button(self, text="Logout", fg='white', bg='red', width=10, height=1, command=lambda:master.backward()).place(x=winW-100,y=winH-100)
        # --- Place Botões
        button0.place(x=(winW//2)-200,y=winH-500)
        button1.place(x=(winW//2)-200,y=winH-400)

class AtualizaPorcao(Win): # MODIFICAR ESSE AQUI
    def __init__(self, master):
        super().__init__(master)

        # BORDA
        lframe=LabelFrame(self,text="Atualiza Porção",width=winW-150,height=winH-100)
        lframe.place(x=(winW//4)-190,y=winH-550)        

        # BOTÕES
        button=Button(self, text="Voltar",command=lambda:master.backward())
        # --- Place Botões
        button.place(x=winW-100,y=winH-100)
        
class BuscaItemFunc(Win):
    def __init__(self, master):
        super().__init__(master)
        
        self.defaultText="sample_text"

        # INPUT BARRA DE PESQUISA
        searchBox=Entry(self,width=50, borderwidth=2)
        searchBox.insert(0,self.defaultText)
        searchBox.place(x=(winW//4)-190,y=20)
        # BORDA
        lframe=LabelFrame(self,text="ESTOQUE",width=winW-150,height=winH-100)
        lframe.place(x=(winW//4)-190,y=winH-550)

        # BOTÕES
        button0=Button(self, text="Adicionar",width=15,height=3,command=lambda:master.forward(AddItemForm))
        button1=Button(self, text="Remover",width=15,height=3,command=lambda:self.remove()) 
        button2=Button(self, text="Buscar",width=8,height=1,command=lambda:self.search(searchBox))  
        button3=Button(self, text="Atualizar",width=15, height=3,command=lambda:self.update(self.query()))
        button4=Button(self, text="Voltar",command=lambda:master.backward())
        # --- Place Botões
        button0.place(x=winW-120,y=winH-540)
        button1.place(x=winW-120,y=winH-480)
        button2.place(x=(winW//2)-80,y=15)
        button3.place(x=winW-120,y=winH-420)
        button4.place(x=winW-100,y=winH-100)

        # LIST BOX
        itemlist=Frame(self)
        scrollbar=Scrollbar(itemlist,orient=VERTICAL)
        self.lbQuery=Treeview(itemlist,column=('c1', 'c2', 'c2'),show='headings', height=22, yscrollcommand=scrollbar.set)
        self.myquery=self.query()

        # LIST BOX HEADINGS
        self.lbQuery.column("# 1",anchor=CENTER)
        self.lbQuery.heading('# 1', text='ID')
        self.lbQuery.column("# 2",anchor=CENTER)
        self.lbQuery.heading('# 2', text='Ingrediente')
        self.lbQuery.column("# 3",anchor=CENTER)
        self.lbQuery.heading('# 3', text='Quantidade')

        # insert into list of itens
        self.update(self.myquery)

        # --- place listbox
        scrollbar.config(command=self.lbQuery.yview)
        scrollbar.pack(side=RIGHT,fill=Y)
        itemlist.place(x=(winW//4)-180,y=winH-530)
        self.lbQuery.pack() 

    def remove(self):
        item=self.lbQuery.selection()
        for i in item:
            self.lbQuery.delete(i)

    def update(self,data):
        self.lbQuery.delete(*self.lbQuery.get_children())
        for item in data:
            self.lbQuery.insert('','end',values=item)

    def search(self,data):
        item='%'+data.get()+'%'
        
        # Create/Connect to database
        conn=mysql.connector.connect(
            host='localhost',
            user='root',
            password='@RoneCachaca2222@',
            database='db'
        )
        cursor=conn.cursor()
        command="select * from estoque where Ingrediente like %s"
        values=(item,)
        cursor.execute(command,values)
        query=cursor.fetchall()

        self.update(query)
        self.lbQuery.pack()

        conn.commit()
        conn.close()


    def query(self):
        # Create/Connect to database
        conn=mysql.connector.connect(
            host='localhost',
            user='root',
            password='@RoneCachaca2222@',
            database='db'
        )
        cursor=conn.cursor()
    
        cursor.execute("select * from estoque")
        query=cursor.fetchall()

        conn.commit()
        conn.close()

        return query

class AddItemForm(Win):
    def __init__(self, master):
        super().__init__(master)

        # Database connection test
        conn=mysql.connector.connect(
            host='localhost',
            user='root',
            password='@RoneCachaca2222@',
            database='db'
        )
        
        cursor=conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS estoque(
            ID int,
            Ingrediente text,
            Quantidade int
        )""")
        conn.commit()
        conn.close()
        
        # INPUT
        self.ingredient=Entry(self,width=30)
        self.ingredient.grid(row=0,column=1)
        self.qntd=Entry(self,width=30)
        self.qntd.grid(row=1,column=1)

        # LABELS
        ingredientLabel=Label(self,text='Ingrediente')
        qntdLabel=Label(self,text='Quantidade')
        ingredientLabel.grid(row=0,column=0)
        qntdLabel.grid(row=1,column=0)

        # BOTÕES    
        submit_btn=Button(self,text="Cadastrar item", command=self.submit)
        submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
        button=Button(self, text="Voltar",command=lambda:master.backward())
        button.grid(row=8,column=8)

    def submit(self):
        # Create/Connect to database
        conn=mysql.connector.connect(
            host='localhost',
            user='root',
            password='@RoneCachaca2222@',
            database='db'
        )
        cursor=conn.cursor()

        # Insert into table
        command="insert into estoque(Ingrediente, Quantidade) values(%s,%s)"
        values=(self.ingredient.get(), self.qntd.get())
        cursor.execute(command,values)

        # clear text boxes
        self.ingredient.delete(0,END)
        self.qntd.delete(0,END)

        conn.commit()
        conn.close()






















#   ========== NUTRI. WINDOWS ==========
class MenuNutri(Win):
    def __init__(self, master):
        super().__init__(master)
        Label(self, text="MENU NUTRICIONISTA", bg='#C3B1E1', font='Verdana').pack(side="top")
        self.configure(bg='#C3B1E1')
        # BOTÕES
        button0=Button(self,text="Pesquisar",width=20,height=4,command=lambda:master.forward(BuscaItemNutri))
        button1=Button(self,text="Gerar Histórico",width=20,height=4,command=lambda:master.forward(GeraHistorico))
        button2=Button(self,text="Gerar Cardápio",width=20,height=4,command=lambda:master.forward(GeraCardapio))
        button3=Button(self, text="Logout", fg='white', bg='red', width=10, height=1, command=lambda:master.backward()).place(x=winW-100,y=winH-100)
        # --- Place Botões
        button0.place(x=(winW//2)-200,y=winH-500)
        button1.place(x=(winW//2)-200,y=winH-400)
        button2.place(x=(winW//2)-200,y=winH-300)

        # Create a Label Widget to display the text or Image

class GeraCardapio(Win):
    def __init__(self, master):
        super().__init__(master)

        cardapio="misc/capi.jpg" # MUDAR PARA FUNÇÃO QUE GERA IMAGEM DO CARDÁPIO
        self.image=ImageTk.PhotoImage(Image.open(cardapio))

        # LABEL
        label=Label(self,image=self.image)
        label.place(anchor='center', relx=0.5, rely=0.5)

        # BOTÕES
        button=Button(self, text="Voltar",command=lambda:master.backward())
        # --- Place Botões
        button.place(x=winW-100,y=winH-100)

class GeraHistorico(Win):
    def __init__(self, master):
        super().__init__(master)

        historico="misc/capi.jpg" # MUDAR PARA FUNÇÃO QUE GERA IMAGEM DO HISTÓRICO
        self.image=ImageTk.PhotoImage(Image.open(historico))

        # LABEL
        label=Label(self,image=self.image)
        label.place(anchor='center', relx=0.5, rely=0.5)

        # BOTÕES
        button=Button(self, text="Voltar",command=lambda:master.backward())
        # --- Place Botões
        button.place(x=winW-100,y=winH-100)

class GeraTabela(Win):
    def __init__(self, master):
        super().__init__(master)

        tabela="misc/capi.jpg" # MUDAR PARA FUNÇÃO QUE GERA IMAGEM DO TABELA
        self.image=ImageTk.PhotoImage(Image.open(tabela))

        # LABEL
        label=Label(self,image=self.image)
        label.place(anchor='center', relx=0.5, rely=0.5)

        # BOTÕES
        button=Button(self, text="Voltar",command=lambda:master.backward())
        # --- Place Botões
        button.place(x=winW-100,y=winH-100)

class BuscaItemNutri(Win):
    def __init__(self, master):
        super().__init__(master)
        
        defaultText="sample_text"

        # INPUT BARRA DE PESQUISA
        searchBox=Entry(self,width=50, borderwidth=2)
        searchBox.insert(0,defaultText)
        searchBox.place(x=(winW//4)-190,y=20)

        # BORDA
        lframe=LabelFrame(self,text="itens",width=winW-150,height=winH-100)
        lframe.place(x=(winW//4)-190,y=winH-550)

        # BOTÕES
        button0=Button(self, text="Buscar",width=8,height=1)  # Adicionar função de buscar item no BD
        button1=Button(self, text="Voltar",command=lambda:master.backward())
        # --- Place Botões
        button0.place(x=(winW//2)-80,y=15)
        button1.place(x=winW-100,y=winH-100)