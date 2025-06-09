import time
from tkinter import *
import customtkinter as ctk
from login.login_alura import login_alura

user_login = ""
pwd_login = ""


# Funcionalidades
def validar_login():
    global user_login, pwd_login
    user_login = entry_app_user.get()
    pwd_login = entry_app_pwd.get()

    if user_login and user_login:
        return_user.configure(
            text="Dados enviados com sucesso para Alura", text_color="green"
        )
        time.sleep(2)
        app.destroy()
    else:
        return_user.configure(
            text="Não podemos enviar os dados em branco para Alura", text_color="yellow"
        )


# Configuração de aparência
ctk.set_appearance_mode("system")

# Janela principal
app = ctk.CTk()
app.title("Login Alura")
app.geometry("300x300")

# Campo Usuário
label_app_user = ctk.CTkLabel(app, text="Usuário")
label_app_user.pack(pady=10)

entry_app_user = ctk.CTkEntry(app, placeholder_text="Informe seu usuário:")
entry_app_user.pack()

# Campo Senha
label_app_pwd = ctk.CTkLabel(app, text="Senha")
label_app_pwd.pack(pady=10)

entry_app_pwd = ctk.CTkEntry(app, placeholder_text="Informe sua senha:", show="*")
entry_app_pwd.pack()

# Botão de login
app_btn = ctk.CTkButton(app, text="Login", command=validar_login)
app_btn.pack(pady=10)

# Label de retorno
return_user = ctk.CTkLabel(app, text="")
return_user.pack(pady=10)


# Iniciar app
def receber_dados():
    app.mainloop()
