#Autenticação (login)

import streamlit as st
import json

arquivo = "usuarios.json"
arquivo_robos = "robos.json"

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

def cadastro_robo(nome, ip, senha):
    with open(arquivo_robos, "r") as f:
        robos = json.load(f)
        for robo in robos:
            if robo["nome"] == nome:
                st.error("Este nome já está sendo utilizado. Escolha outro.")
                return False
        robos.append({"nome": nome, "ip": ip, "senha": senha})
    with open(arquivo_robos, "w") as f:
        json.dump(robos, f)
    return True

def login_robo(nome, ip, senha):
    with open(arquivo_robos, "r") as f:
        robos = json.load(f)
        for robo in robos:
            if robo["nome"] == nome and robo["ip"] == ip and robo["senha"] == senha:
                return True
        return False


# Define a aba inicial como login se não houver nada no session_state
if "aba" not in st.session_state:
    st.session_state["aba"] = "login"

st.title("Projeto Artemis III")

#Tela de Login
if st.session_state["aba"] == "login":
    st.subheader("Login")
    login = st.text_input("Insira o seu login:")
    senha = st.text_input("Insira a sua senha", type="password")
    if st.button("Entrar"):
        if verifica_login(login, senha):
            st.success("Login realizado com sucesso!")
            st.session_state["aba"] = "login_robo"
            st.rerun()
        else:
            st.error("Usuário ou senha incorretos. Tente novamente.")
    if st.button("Não tenho um login"):
        st.session_state["aba"] = "cadastro"
        st.rerun()

#Tela de Cadastro
elif st.session_state["aba"] == "cadastro":
    st.subheader("Criar conta")
    novo_login = st.text_input("Crie um login:")
    nova_senha = st.text_input("Crie uma senha:", type="password")
    if st.button("Cadastrar"):
        if not novo_login or not nova_senha:
            st.error("Preencha todos os campos.")
        else:
            if cadastro_usuario(novo_login, nova_senha):
                st.success("Cadastro realizado com sucesso!")
                st.session_state["aba"] = "login"
                st.rerun()

#Tela de Login do Robô
elif st.session_state["aba"] == "login_robo":
    st.subheader("Login do Robô")
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
    if st.button("Não tenho um robô cadastrado"):
        st.session_state["aba"] = "cadastro_robo"
        st.rerun()

#Tela de Cadastro do Robô
elif st.session_state["aba"] == "cadastro_robo":
    st.subheader("Cadastrar Robô")
    novo_ip = st.text_input("Insira o IP do robô")
    novo_nome = st.text_input("Dê um nome ao seu robô")
    nova_senha_robo = st.text_input("Crie uma senha para acessá-lo", type="password")
    if st.button("Cadastrar"):
        if cadastro_robo(novo_nome, novo_ip, nova_senha_robo):
            st.success("Cadastro realizado com sucesso!")
            st.session_state["aba"] = "login_robo"
            st.rerun()