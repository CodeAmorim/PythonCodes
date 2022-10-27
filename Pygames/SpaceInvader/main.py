import pygame
import math
import random


from pygame import mixer
# Inicialize o pygame
pygame.init()

# Crie o tamanho da tela
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.png')

# Tema do inicio
# Para a musica tocar em loop é só colocar 'mixer.music.play(-1)'
mixer.music.load('theme.wav')
mixer.music.play()

# Titulo e ícone
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('ufo (32px).png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(1)
    enemyY_change.append(40)

# Bullet
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 8
bullet_state = 'ready'

# Score
# Para adicionar outras fontes é só ir no dafont.com e baixar a fonte desejada com a extensão .ttf e colocá-la dento
# da pasta do projeto
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font('freesansbold.ttf', 64)
# O método .blit "desenha" na tela
""" Nele colocamos a imagem para ser desenhada na tela e os pontos de intersecção de X e Y
# Como queremos que ele apareça todo tempo, chamamos a função dentro do while"""


def show_score(x, y):
    score = font.render('Score: ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


# Tornamos a variável global para ser acessada fora da função
def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# Crie o game loop
"""
O programa roda dentro desse loop
pygame.event.get(): associado à "event" roda o programa até que o usuário clique no x de sair.
Se o usuário clicar no x ele testa se esse evento é igual ao pygame.QUIT (SAIR).
Caso seja igual, running se torna FALSO e o loop while acaba, encerrando o programa
"""

running = True
while running:
    # RGB - Red, Green, Blue
    # Controlando esses tres valores, controla-se a cor. Limite de 255 para cada cord
    screen.fill((0, 0, 0))
    # Background
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # KEYDOWN - Verifica se alguma tecla está sendo pressionada
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:  # Se for a tecla <-
                playerX_change = -5  # Controla a velocidade de movimento da nave para a esquerda
            if event.key == pygame.K_RIGHT:  # Se for a tecla ->
                playerX_change = 5  # Controla a velocidade de movimento da nave para a direita
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bullet_Sound = mixer.Sound('shoot.wav')
                    bullet_Sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        # KEYUP - Verifica se a tecla foi solta
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0  # Caso o botão seja solto a nave para

    # Controle de movimentação na janela do jogo (fronteiras)
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound('explosion.wav')
            explosion_Sound.play()
            bulletY = 480
            bullet_state = 'ready'
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    """
    Tudo o que deseja que continue aparecendo na tela durante o jogo (cor de fundo por exemplo),
    deve estar dentro do while loop
    """

    # Chamamos a função abaixo da cor da janela para ele aparecer acima da cor e assim ficar no primeiro Layer
    player(playerX, playerY)
    show_score(textX, textY)
    # Para o programa continuar atualizando e mostrando o que está acontecendo na tela,
    # precisamos usar um comando para ele atualizar tudo o que acontecer no loop
    pygame.display.update()
