import streamlit as st
import subprocess

st.set_page_config(page_title="Painel de Controles")
st.title("Painel de Controles")

if st.sidebar.button("Sair"):
    st.session_state.clear()
    st.switch_page("Login.py")

# Verifica se tem um robô logado
if "robo_ip" not in st.session_state:
    st.error("Nenhum robô conectado. Volte e faça login.")
    st.stop()

st.success(f"Robô conectado: {st.session_state['robo_nome']} ({st.session_state['robo_ip']})")

st.write("Clique no botão abaixo para abrir o controle por teclado.")

if st.button("🎮 Abrir controle WASD"):
    import sys, os
    caminho = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "controle.py"))
    subprocess.Popen([sys.executable, caminho])
    st.info("Janela aberta! Use W A S D para controlar.")