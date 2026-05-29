# 🤖 Artemis III

Sistema de controle remoto de rover via interface web, desenvolvido como projeto acadêmico do curso de **Análise e Desenvolvimento de Sistemas** do **Centro Universitário Católico Ítalo Brasileiro**.

---

## 📋 Sobre o Projeto

O Artemis III é uma aplicação que permite controlar um rover equipado com microcontrolador **ESP32** através de uma interface web construída com Streamlit. A comunicação entre a interface e o rover é feita via socket, com comandos de movimentação enviados em tempo real pelo teclado.

---

## 👥 Integrantes

- Diego dos Santos Meireles
- Eduardo Gabriel Alves da Silva
- Gabriel Santos Andrade
- Gabriel Pessoa dos Santos
- Gustavo Guilherme Rocha Bernardino

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Streamlit** — interface web
- **Pygame** — janela de controle por teclado
- **Socket TCP** — comunicação com o rover
- **JSON** — armazenamento local de usuários e robôs
- **ESP32** — microcontrolador do rover

---

## 📁 Estrutura do Projeto

```             
Artemis_III/
│
├── Login.py                  # Tela principal: login, cadastro e autenticação
├── pages/
│   ├── Carrinho.py           # Painel de controle do rover
│   └── controle.py           # Janela de controle WASD (pygame)
├── usuarios.json             # Banco de dados de usuários (não versionado)
├── robos.json                # Banco de dados de robôs (não versionado)
├── .gitignore
└── README.md
```

---

## ⚙️ Pré-requisitos

Certifique-se de ter o **Python 3** instalado. Em seguida, instale as dependências:

```bash
pip install streamlit pygame
```

---

## 🚀 Como Executar

**1. Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/artemis-iii.git
cd artemis-iii
```

**2. Crie os arquivos de dados** na raiz do projeto:

`usuarios.json`
```json
[]
```

`robos.json`
```json
[]
```

**3. Inicie a aplicação:**
```bash
streamlit run Login.py
```

**4. Acesse no navegador:**
```
##enter##

```

---

## 🔄 Fluxo de Uso

```
Tela de Login
    │
    ├── Não tem conta? → Cadastro de Usuário → volta para Login
    │
    └── Login realizado → Login do Robô
            │
            ├── Robô não cadastrado? → Cadastro de Robô → volta para Login do Robô
            │
            └── Login do Robô realizado → Painel de Controles
                        │
                        └── Abrir controle WASD → Janela Pygame
                                    │
                                    └── W / A / S / D → comandos enviados ao rover via TCP
```

---

## 🎮 Controles

| Tecla | Comando |
|-------|---------|
| `W`   | Mover para frente |
| `S`   | Mover para trás |
| `A`   | Virar à esquerda |
| `D`   | Virar à direita |
| soltar tecla | Parar |

---

## 🔒 Segurança

Os arquivos `usuarios.json` e `robos.json` contêm dados de acesso e **não se encontram** no repositório. Certifique-se de criá-los manualmente conforme as instruções acima antes de executar o projeto.

---

## 📡 Configuração do Rover

O rover deve estar rodando um servidor TCP na **porta 5000** e acessível na rede local. O IP é informado no momento do cadastro do robô na interface. O microcontrolador utilizado é o **ESP32**, que deve estar programado para receber e interpretar os comandos `w`, `s`, `a`, `d` e `p` via socket.