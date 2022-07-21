 #import modules
 
from tkinter import *
import os
from src.include.winController import WindowController
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Novo usuário")
    register_screen.geometry("300x250")
    register_screen.configure(bg='lightblue')
 
    global username
    global password
    global username_entry
    global password_entry
    global post_entry

    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Por favor, preencha os dados para registrar: ", font=("Verdana", 9), bg="lightblue").pack()
    Label(register_screen, text="", bg='lightblue').pack()
    username_lable = Label(register_screen, text="Login * ", bg='lightblue')
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Senha * ", bg='lightblue')
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()

    post_entry = StringVar(register_screen)
    post_entry.set("Selecione...")
    post_label = Label(register_screen, text="Colaborador * ", bg='lightblue')
    post_label.pack()
    OptionMenu(register_screen, post_entry, "Funcionário", "Nutricionista").pack()
    Label(register_screen, text="", bg='lightblue').pack()
    Button(register_screen, text="Registrar", width=10, height=1, bg="orange", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    login_screen.configure(bg='lightblue')
    Label(login_screen, text="Insira suas credenciais para entrar: ", font=("Verdana", 9), bg='lightblue').pack()
    Label(login_screen, text="", bg='lightblue').pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Login * ", bg='lightblue').pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="", bg='lightblue').pack()
    Label(login_screen, text="Senha * ", bg='lightblue').pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="", bg='lightblue').pack()
    Button(login_screen, text="Login", bg='orange', width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
    post_info = post_entry.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(post_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)
    post_entry.set("Selecione...")
 
    Label(register_screen, text="Registrado com sucesso", bg='lightgreen', fg="green", font=("Verdana", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()

        if password1 == verify[2]:
            if verify[1] == 'Nutricionista':
                WindowController().openMenuNutri()
            else: WindowController().openMenuFunc()
            
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Sucesso")
    login_success_screen.geometry("150x100")
    login_success_screen.configure(bg='lightgreen')
    Label(login_success_screen, text="Entrou com sucesso", bg='lightgreen').pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Sucesso")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Senha inválida").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Sucesso")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="Usuário não encontrado").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Interface")
    main_screen.configure(bg='lightgreen')
    Label(text="Selecione uma opção: ", bg="lightgreen", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text='', bg='lightgreen').pack()
    Button(text="Login", bg='white', height="2", width="30", command = login).pack()
    Label(text="", bg='lightgreen').pack()
    Button(text="Registrar", bg='white', height="2", width="30", command=register).pack()
    main_screen.mainloop()

main_account_screen()