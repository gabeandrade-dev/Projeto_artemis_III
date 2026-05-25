#Redirecionamento para o controle do carrinho
import streamlit as st
import socket 

st.set_page_config(page_title="Painel de Controles")
st.title("Painel de Controles")

if st.sidebar.button("Sair"):
    st.session_state.clear()
    st.switch_page("Login.py")



# if "socket" not in st.session_state:
#     s = socket.socket()
#     s.connect(("10.151.185.105", 5000))
#     st.session_state.socket = s

# if st.button("Frente"):
#     st.session_state.socket.send(b'w')

# if st.button("Esquerda"):
#     st.session_state.socket.send(b'a')

# if st.button("Ré"):
#     st.session_state.socket.send(b's')

# if st.button("Direita"):
#     st.session_state.socket.send(b'd')

# if st.button("Parar"):
#     st.session_state.socket.send(b'p')