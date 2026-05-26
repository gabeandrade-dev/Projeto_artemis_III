#Autenticação (login)

import streamlit as st
import json

#Funções para o cadastro do usuário
arquivo = "usuarios.json"

def verifica_login(login, senha):
    with open(arquivo, "r") as f:
        usuarios = json.load(f)
        for user in usuarios:

            if user["login"] == login and user["senha"] == senha:
                return True

        return False

def cadastro_usuario(login, senha):
    with open(arquivo, "r") as f:
        usuarios = json.load(f)
        for user in usuarios:
            if user["login"] == login:
                st.error("Usuário já existe.")
                return False
        
        usuarios.append({"login": login, "senha": senha})
    with open(arquivo, "w") as f:
        json.dump(usuarios, f)
    return True



#Funções para o cadastro do robô
arquivo_robos = "robos.json"

def cadastro_robo(nome, ip, senha):
    with open (arquivo_robos, "r") as f:
        robos = json.load(f)
        for robo in robos:
            if robo["nome"] == nome:
                st.error("Este nome já está sendo utilizado. Escolha outro.")
                return False
        
        robos.append({"nome": nome, "ip": ip, "senha": senha})
        with open (arquivo_robos, "w") as f:
            json.dump (robos, f)
        return True

def login_robo(nome, ip, senha):
    with open (arquivo_robos, "r") as f:
        robos = json.load(f)
        for robo in robos:
            if robo["nome"] == nome and robo["ip"] == ip and robo["senha"] == senha:
                return True
        return False



#Interface da streamlit
st.title("Projeto Cold Drive")
menu = st.sidebar.selectbox("Menu", ["Iniciar sessão", "Crie um login", "Cadastrar robô", "Login do robô"])

#Menu de cadastro do usuário
if menu == "Crie um login":
    novo_login = st.text_input("Crie um login: ")
    nova_senha = st.text_input("Crie uma senha:", type="password")
    if st.button("Cadastrar"):
        cadastro_usuario(novo_login, nova_senha)
        st.success("Cadastro realizado com sucesso!")

#Menu de login do usuário
if menu == "Iniciar sessão":
    login = st.text_input("Insira o seu login:")
    senha = st.text_input("Insira a sua senha", type="password")
    if st.button("Login"):
        if verifica_login(login, senha):
            st.success("Login realizado com sucesso!")
            st.switch_page("pages/Carrinho.py")
        else:   
            st.error("Usuário ou senha incorretos. Tente novamente.")

#Menu de cadastro do robô
if menu == "Cadastrar robô":
    novo_ip = st.text_input("Insira o IP do robô")
    novo_nome = st.text_input("Dê um nome ao seu robô")
    nova_senha_robo = st.text_input("Crie uma senha para acessá-lo", type="password")
    if st.button("Cadastrar"):
        if cadastro_robo(novo_nome, novo_ip, nova_senha_robo):
            st.success("Cadastro realizado com sucesso!")

#Menu de login do robô
if menu == "Login do robô":
    nome = st.text_input("Insira o nome do robô:")
    ip = st.text_input("Insira o IP do robô:")
    senha = st.text_input("Insira a senha", type="password")
    if st.button("Login"):
        if login_robo(nome, ip, senha):
            st.session_state["robo_ip"] = ip
            st.session_state["robo_nome"] = nome
            st.switch_page("pages/Carrinho.py")
        else:
            st.error("Dados incorretos. Por favor, tente novamente.")