# IMPORTANTE/ IMPORTANT !!!

# To run the program, use the random and pygame libraries!!!
# To run the program, use the pygame and random libraries!!!

#importar bibliotecas / import libraries
import pygame as pg 
from random import randrange

pg.init() # inicializar o pygame / init pygame
# altura e largura da tela / height and width of the screen
window_height = 800
window_width = 1400
#variaveis de customização da cor da cobra e da fruta / snake and fruit color customization variables
cor_cnova = ''
cor_fnova = ''
txt_usuario_CobraC = ''
txt_usuario_ComidaC = ''
# icones, clock, tela e nome do jogo / icons, clock, screen and game name
icon = pg.image.load('Project5/data/cobrinha.png')
clock = pg.time.Clock()
screen = pg.display.set_mode((window_width, window_height) )
pg.display.set_icon(icon)
pg.display.set_caption('Meu Primeiro Jogo')

# menu principal / main menu
def menu():
    # Fontes, titulos e botoes do menu/ font, title and buttons from menu
    global font_botoes
    font_menu = pg.font.SysFont('Helvetica', 100)
    font_botoes= pg.font.SysFont('Helvetica', 40)
    title_menu = font_menu.render('Digitized Snake', 1, (0, 255, 0))
    Play_button = font_botoes.render('Play', 1, (0,255,0))
    Custom_button = font_botoes.render('Customization', 1, (0,255,0))
    play_button_rect = Play_button.get_rect(topleft=(window_width // 3, window_height * 0.5))
    custom_button_rect = Custom_button.get_rect(topleft=(window_width // 3, window_height * 0.4))
    run = True

    while run:
        # preenchimento da tela com cor, textos e botoes / filling the screen with color, texts and buttons
        screen.fill((0,0,0))
        screen.blit(title_menu, (window_width//3, window_height * 0.15))
        screen.blit(Play_button,(window_width//3, window_height * 0.5))
        screen.blit(Custom_button, (window_width//3, window_height * 0.4))

        for evento in pg.event.get():
            # se clicar no X do jogo, fechar/ if you click on the X in the game, close the game
            if evento.type == pg.QUIT:
                run = False
                pg.quit()
            # se clicar com o mause nos botoes do menu... / if you click on the X in the game...
            if evento.type == pg.MOUSEBUTTONDOWN:
                if evento.button == 1:  # Verifica se é o botão esquerdo do mouse. / Check if it is the left mouse button
                    if play_button_rect.collidepoint(evento.pos): # ...iniciar o jogo... / ... game init...
                        play()
                    if custom_button_rect.collidepoint(evento.pos): # ...customização do jogo./ ... game customization
                        custom(txt_usuario_CobraC, txt_usuario_ComidaC)
        pg.display.update()

# função de customização do jogo / function of game customization
def custom(txt_usuario_CobraC, txt_usuario_ComidaC): # parâmetros do texto da futura cor da cobra e comida / text parameters of the future color of the snake and food
    # botoes de seleção / select buttons
    back_button =  font_botoes.render('Back', 1, (0,255,0))
    snake_colorbutton = font_botoes.render('Snake color', 1, (0,255,0))
    food_colorbutton = font_botoes.render('Food color', 1, (0,255,0))
    # hitbox dos botoes / buttons hitbox
    back_button_rect = back_button.get_rect(topleft=(50, 50))
    snake_button_rect = snake_colorbutton.get_rect(topleft=(50, window_height/2 - 100 ))
    food_button_rect = food_colorbutton.get_rect(topleft=(50, window_height/2))
    d, f = False, False # variaveis para caso acessar cor da cobra, nao acessar a cor da comida virse e versa / 
    # variables for accessing the color of the snake, not accessing the color of the food, same for the another way

    while True:
        # preenchimento dos botoes e fundo / fill the bottons and background
        screen.fill((0,0,0))
        screen.blit(back_button, (50,50))
        screen.blit(snake_colorbutton, snake_button_rect)
        screen.blit(food_colorbutton, food_button_rect)
        global cor_cnova, cor_fnova

        for evento in pg.event.get():
            # fechar ao aperta no X / close if click on the X
            if evento.type == pg.QUIT:
                pg.quit()
                break
            if evento.type == pg.MOUSEBUTTONDOWN:
                if evento.button == 1: # se o click do mause for esquerdo então acessar cor da comida, cobra ou voltar ao menu/
                    # if the left mouse click then acess snake and food color or return to menu
                    if back_button_rect.collidepoint(evento.pos):
                        menu()
                    if snake_button_rect.collidepoint(evento.pos):
                        d = True
                        f = False
                    if food_button_rect.collidepoint(evento.pos):
                        f = True
                        d = False
            # caso tenha clicado no botao de cor de cobra, escrever/ if click on snake color, write
            if evento.type == pg.KEYDOWN and d == True:
                txt_usuario_CobraC += evento.unicode
                if evento.key == pg.K_BACKSPACE: # se pressionar backspace deletar os ultimos 2 caracteres (a letra a se apagar e o caractere do backspace)/
                    # If press backspace it deletes the last 2 characters (the letter to be deleted and the backspace character)
                    txt_usuario_CobraC = txt_usuario_CobraC[:-2] 
                if evento.key == pg.K_RETURN: # se pressionar enter, deletar o ultimo caracter (enter) e considerar a cor_cnova como a cor escrita/
                    # If you press enter, delete the last character (enter) and consider cnova_color as the written color
                    txt_usuario_CobraC = txt_usuario_CobraC[:-1]
                    cor_cnova = txt_usuario_CobraC
                    d = False
            # caso tenha clicado no botao cor comida, escrever / If you clicked on the food color button, write
            if evento.type == pg.KEYDOWN and f == True:
                txt_usuario_ComidaC += evento.unicode
                if evento.key == pg.K_BACKSPACE:
                    txt_usuario_ComidaC = txt_usuario_ComidaC[:-2] # se pressionar backspace deletar os ultimos 2 caracteres (a letra a se apagar e o caractere do backspace)/
                # If you press backspace it deletes the last 2 characters (the letter to be deleted and the backspace character)
                if evento.key == pg.K_RETURN:
                    txt_usuario_ComidaC = txt_usuario_ComidaC[:-1] # se pressionar enter, deletar o ultimo caracter (enter) e considerar a cor_fnova como a cor escrita/
                    # If you press enter, delete the last character (enter) and consider the new_color as the written color
                    cor_fnova = txt_usuario_ComidaC
                    f = False   
        #definindo o texto para exibir na tela / setting text to display on screen
        txt_superficie = font_botoes.render(txt_usuario_CobraC,True,(255,255,255))
        txt_superficie2 = font_botoes.render(txt_usuario_ComidaC,True,(255,255,255))
        # ixibir na tela a escrita caso os botoes tenham sido selecionado / display the writing on the screen if the buttons have been selected
        if d:
            screen.blit(txt_superficie,(window_width/2 - txt_superficie.get_width()/2 , window_height/2)) 
        if f:
            screen.blit(txt_superficie2, (window_width/2 - txt_superficie2.get_width()/2, window_height/2))
        
        pg.display.update()
    
# funçao que ixibe a pontuação final ao perder / function that displays the final score when losing
def scorefinal(score):
    while True:
        screen.fill('black')
        screen.blit(score, (window_width/2 - score.get_width()/2, window_height/2 - score.get_width()/2)) # Posicionar a pontuação no meio da tela/ show the score in the middle of the screen
        pg.display.update()
        pg.time.wait(5000)
        break
        
# função de jogar / play function
def play():
    cubo_size = 50 
    score = 0
    alcance = (cubo_size // 2, window_height - cubo_size // 2, cubo_size) # definindo medidas do alcance da tela / defining screen range measurements
    get_random_position = lambda: [randrange(* alcance), randrange(* alcance)] # definindo o gerador de posições aléatorias na tela com base no alcance / setting random position generator on screen based on range
    cobra_f = pg.rect.Rect([0, 0, cubo_size - 2, cubo_size - 2]) #definindo formato da comida da cobra / setting snake and food format
    cobra_f.center = get_random_position() # definindo que o centro da cobra é a posição gerada aleatoria / setting defining that the center of the snake is the randomly generated position
    length = 1 # tamanho da cobra / snake length
    segments = [cobra_f.copy()] # definindo lista que vai armazenar o tamanho de todos os segmentos da cobra / defining list that will store the size of all segments of the snake
    cobra_dir = (0,0) # direção que a cobra anda / direction the snake walks 
    food = cobra_f.copy() # definindo que a comida é igual a copia da cobra/ defining that food is equal to the snake's copy
    food.center = get_random_position() #pegando posição aleatoria para a comida/ picking random position for food
    tempo, andar = 0, 60 # tempo e passo / time and step
    
   
    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1} # direções para nao permitir que a cobra ande para direção contrária a ela/ directions so as not to allow the snake to walk in the opposite direction   

    # tentar desenhar na tela a comida com a cor_cnova, caso de o Valueerror, definir como cor padrão da cobra verde,...
    # ...caso contrario definir que a cor cobra é a cor_cnova escrita la na customização/
    # try to draw the food on the screen with color_cnova, in case Valueerror sets the green snake as the default color,...
    # ...otherwise define that the snake color is the color_cnova written there in the customization
    try:
        pg.draw.rect(screen, cor_cnova, food)
    except ValueError:
        cor_cobra = 'green'
    else:
        cor_cobra = cor_cnova
    try:
        pg.draw.rect(screen, cor_fnova, food)
    except ValueError:
        cor_fruta = 'red'
    else:
        cor_fruta = cor_fnova

    while True:

        for evento in pg.event.get():
            if evento.type == pg.QUIT: #fechar o jogo ao clicar no X / close the game when click on the X
                pg.quit()

            if evento.type == pg.KEYDOWN:
                #movimentação da cobra / Snake movement
                if evento.key == pg.K_w and dirs[pg.K_w]: #caso pressione W e no dicionario o K_w valer 1 então a cobrar vai passar a ir pra cima/
                    #If you press W and in the dictionary K_w is 1, then the charge will go up
                    cobra_dir = (0, -cubo_size)
                    dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1} 
                if evento.key == pg.K_s and dirs[pg.K_s]: #caso pressione S e o valor da lista de k_s for 1 então seguir para baixo/
                    #if you press S and the value of the list of k_s is 1 then go down
                    cobra_dir = (0, cubo_size)
                    dirs = {pg.K_w: 0, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}
                if evento.key == pg.K_a and dirs[pg.K_a]:
                    cobra_dir = (-cubo_size, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 0}
                if evento.key == pg.K_d and dirs[pg.K_d]:
                    cobra_dir = (cubo_size, 0)
                    dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 0, pg.K_d: 1}
                if evento.key == pg.K_ESCAPE:
                    cobra_dir = (0, 0)
        # esse mecanismo serve pra impossibilitar da cobra ir para direção oposta a qual esta indo
        #This mechanism serves to make it impossible for the snake to go in the opposite direction to which it is going.
        screen.fill('black')
        # controle de espaço da cobra
        if cobra_f.left < 0 or cobra_f.right > window_width or cobra_f.top < 0 or cobra_f.bottom > window_height:
            scorefinal(txt_score) #caso saia da tela chamar a função score e menu / if you leave the screen, call the score function and menu
            break
        if cobra_f.center == segments[1:]:
            print('deu')
        # controle de crescimento da cobra / snake growth control
        if cobra_f.center == food.center:
            food.center = get_random_position()
            length += 1
            score += 1

        txt_score = font_botoes.render(f'Score: {score}', 1, (0,255,0))
        # desenhar a cobra e comida / draw the snake and food
        [pg.draw.rect(screen, cor_cobra, segment) for segment in segments]
        pg.draw.rect(screen, cor_fruta, food)
        screen.blit(txt_score, (window_width - 200 , 20)) # pontuação / score
        tempo_agora = pg.time.get_ticks() # pegar o fps atual / get current FPS
        if tempo_agora - tempo > andar: #se o fps atual - o tempo for maior que o passo então/ if current fps - time is greater than step then
            tempo = tempo_agora #tempo passa a ser o fps atual / time becomes the current fps
            cobra_f.move_ip(cobra_dir) # cobra vai movimentar/ snake will move
            segments.append(cobra_f.copy())# adicionar as parte do corpo da cobra a lista de segmentos / add snake body parts to segment list
            segments = segments[-length:]# definir o segmento com base no tamanho (length) /  define the segment based on length

        pg.display.flip() # atualizar o display do pygame / update pygame display
        clock.tick(60)# definindo o fps do jogo / setting game fps
menu() #chamar a função menu / calling the menu function