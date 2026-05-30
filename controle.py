# ============================================================
# controle.py — Cliente de controle do Rover via teclado
# Envia comandos WASD para o servidor do Rover via socket TCP
# Código fornecido pelo professor Lucas
# ============================================================

import pygame   # Biblioteca para criar a janela e capturar teclas
import socket   # Biblioteca para comunicação via rede (TCP/IP)
import sys

# ── Conexão com o servidor (Rover) ──────────────────────────
cliente = socket.socket()
cliente.connect((sys.argv[1], 5000))

# Inicializa todos os módulos do pygame
pygame.init()

# Cria a janela gráfica com tamanho 300x300 pixels
tela = pygame.display.set_mode((300, 300))

# Define a fonte de texto padrão do sistema com tamanho 40
fonte = pygame.font.SysFont(None, 40)

# ── Loop principal do programa ───────────────────────────────
while True:

    tela.fill((30, 30, 30))
    texto = fonte.render("Use W A S D", True, (255, 255, 255))
    tela.blit(texto, (60, 130))
    pygame.display.update()

    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            cliente.close()
            pygame.quit()
            sys.exit()

        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_w:
                cliente.send(b"w")
            if e.key == pygame.K_s:
                cliente.send(b"s")
            if e.key == pygame.K_a:
                cliente.send(b"a")
            if e.key == pygame.K_d:
                cliente.send(b"d")

        if e.type == pygame.KEYUP:
            cliente.send(b"p")