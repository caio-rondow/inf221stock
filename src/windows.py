from src.include.winController import *
from tkinter import *
import sqlite3
from PIL import ImageTk, Image

# ========== DEFAULT WINDOW ==========
winW=800
winH=600
background="#5A5A5A"

class Win(Frame):
    def __init__(self,master):
        # default configs
        super().__init__(master=master, width=winW, height=winH)
        master.geometry(str(winW)+"x"+str(winH))
        master.title("GERENCIADOR DE ESTOQUE RU")
        self.pack_propagate(0)

class StartPage(Win):
    def __init__(self, master):
        super().__init__(master)
        
        # BOTÕES
        button1=Button(self, text="Funcionário", width=20, height=5,command=lambda: master.forward(MenuFunc))
        button2=Button(self, text="Nutricionista", width=20, height=5,command=lambda: master.forward(MenuNutri))
        button3=Button(self, text="login layout",width=20, height=5,command=lambda: master.forward(Login))
        button1.place(relx=0.25, rely=0.5, anchor='e')
        button2.place(relx=0.5, rely=0.5, anchor='center')
        button3.place(relx=0.75, rely=0.5, anchor='w')
        
class Login(Win):
    def __init__(self, master):
        super().__init__(master)

        # BORDA
        lframe=LabelFrame(self,width=winW//3,height=winH//3, background='#ADABAB')
        lframe.place(relx=0.5, rely=0.5, anchor='center')

        # INPUT BARRA DE PESQUISA
        username=Entry(self,width=25,borderwidth=4)
        password=Entry(self,width=25, borderwidth=4)
        username.place(relx=0.5,rely=0.40,anchor='center')
        password.place(relx=0.5,rely=0.55,anchor='center')
        
        usernameLabel=Label(self,text="Login",font=('Arial',12),background='#ADABAB')
        passwordLabel=Label(self,text="Senha",font=('Arial',12),background='#ADABAB')
        usernameLabel.place(relx=0.5,rely=0.36,anchor='center')
        passwordLabel.place(relx=0.5,rely=0.51,anchor='center')

        # BOTÕES
        button=Button(self, text="Voltar",command=lambda:master.backward())


        # --- Place Botões
        button.place(x=winW-100,y=winH-100)

#   ========== FUNC. WINDOWS ==========
class MenuFunc(Win):
    def __init__(self, master):
        super().__init__(master)

        # LABELS
        Label(self, text="MENU FUNCIONÁRIO").pack(side="top", fill="x", pady=10)
        
        # BOTÕES
        button0=Button(self, text="Atualizar Porção",width=20,height=4,command=lambda:master.forward(AtualizaPorcao))
        button1=Button(self, text="Pesquisar",width=20,height=4,command=lambda:master.forward(BuscaItemFunc))
        button2=Button(self, text="Voltar",command=lambda:master.backward())
        # --- Place Botões
        button0.place(x=(winW//2)-200,y=winH-500)
        button1.place(x=(winW//2)-200,y=winH-400)
        button2.place(x=winW-100,y=winH-100)

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
        lframe=LabelFrame(self,text="itens",width=winW-150,height=winH-100)
        lframe.place(x=(winW//4)-190,y=winH-550)

        # BOTÕES
        button0=Button(self, text="Adicionar",width=15,height=3,command=lambda:master.forward(AddItemForm))
        button1=Button(self, text="Remover",width=15,height=3) # Adicionar função de remover item do BD
        button2=Button(self, text="Buscar",width=8,height=1)  # Adicionar função de buscar item no BD
        button3=Button(self, text="Voltar",command=lambda:master.backward())
        query_btn=Button(self,text="Mostrar Estoque",width=15,height=3,command=self.query)
        # --- Place Botões
        button0.place(x=winW-120,y=winH-540)
        button1.place(x=winW-120,y=winH-480)
        button2.place(x=(winW//2)-80,y=15)
        button3.place(x=winW-100,y=winH-100)
        query_btn.place(x=winW-120,y=winH-420)

    def query(self):
        # Create/Connect to database
        conn=sqlite3.connect('misc/test.db')
        cursor=conn.cursor()
    
        cursor.execute("SELECT *, oid FROM addresses")
        records=cursor.fetchall()
        rec=''
        for data in records:
            for item in data:
                rec+=str(item)+" "
            rec+="\n"

        # LABELS
        queryLabel=Label(self,text=rec)
        queryLabel.place(x=(winW//4)-150,y=winH-530)

        conn.commit()
        conn.close()

class AddItemForm(Win):
    def __init__(self, master):
        super().__init__(master)

        # Database connection test
        conn=sqlite3.connect('misc/test.db')
        cursor=conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS addresses(
            first_name text,
            last_name text,
            address text,
            city text,
            state text
        )""")
        conn.commit()
        conn.close()
        
        # INPUT
        self.fname=Entry(self,width=30)
        self.fname.grid(row=0,column=1,padx=20)
        self.lname=Entry(self,width=30)
        self.lname.grid(row=1,column=1)
        self.address=Entry(self,width=30)
        self.address.grid(row=2,column=1)
        self.city=Entry(self,width=30)
        self.city.grid(row=3,column=1)
        self.state=Entry(self,width=30)
        self.state.grid(row=4,column=1)

        # LABELS
        fnameLabel=Label(self,text="Nome")
        fnameLabel.grid(row=0,column=0)
        lnameLabel=Label(self,text="Sobrenome")
        lnameLabel.grid(row=1,column=0)
        addressLabel=Label(self,text="Endereço")
        addressLabel.grid(row=2,column=0)   
        cityLabel=Label(self,text="Cidade")
        cityLabel.grid(row=3,column=0)
        stateLabel=Label(self,text="Estado")
        stateLabel.grid(row=4,column=0)

        # BOTÕES    
        submit_btn=Button(self,text="Cadastrar item", command=self.submit)
        submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
        button=Button(self, text="Voltar",command=lambda:master.backward())
        button.grid(row=8,column=8)

    def submit(self):
        # Create/Connect to database
        conn=sqlite3.connect('misc/test.db')
        cursor=conn.cursor()

        # Insert into table
        cursor.execute("INSERT INTO addresses VALUES (:fname, :lname, :address, :city, :state)",
                    {
                        'fname':self.fname.get(),
                        'lname':self.lname.get(),
                        'address':self.address.get(),
                        'city':self.city.get(),
                        'state':self.state.get()
                    }
        )

        # clear text boxes
        self.fname.delete(0,END)
        self.lname.delete(0,END)
        self.address.delete(0,END)
        self.city.delete(0,END)
        self.state.delete(0,END)

        conn.commit()
        conn.close()

#   ========== NUTRI. WINDOWS ==========
class MenuNutri(Win):
    def __init__(self, master):
        super().__init__(master)
        Label(self, text="MENU NUTRICIONISTA").pack(side="top")

        # BOTÕES
        button0=Button(self,text="Pesquisar",width=20,height=4,command=lambda:master.forward(BuscaItemNutri))
        button1=Button(self,text="Gerar Histórico",width=20,height=4,command=lambda:master.forward(GeraHistorico))
        button2=Button(self,text="Gerar Cardápio",width=20,height=4,command=lambda:master.forward(GeraCardapio))
        button3=Button(self,text="Voltar", command=lambda:master.backward())
        # --- Place Botões
        button0.place(x=(winW//2)-200,y=winH-500)
        button1.place(x=(winW//2)-200,y=winH-400)
        button2.place(x=(winW//2)-200,y=winH-300)
        button3.place(x=(winW-100),y=winH-100)

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