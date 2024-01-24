#Nome: Átila Silvio Carvalho Rocha Melo Oliveira
#Matrícula: 
import turtle
import random
import math
def quadra(): # Aqui é feito aonde a arena onde o jogador, a comida e o veneno anda
    campo = turtle.Turtle()
    campo.color('white')
    campo.shape('classic')
    campo.pensize(3)
    campo.penup()
    campo.speed(0)
    campo.goto(-300, -250) #A arena possui 600px de comprimento e 400px de largura
    campo.pendown()
    campo.setx(300)
    campo.sety(150)
    campo.setx(-300)
    campo.sety(-250)
    campo.hideturtle()


def playerfd(): #Aqui faz o player se movimentar no eixo y (cima)
    y=player.ycor()
    y+=5
    player.sety(y)

def playerbk(): #Aqui faz o player se movimentar no eixo y (baixo)
    y=player.ycor()
    y-=5
    player.sety(y)

def playerrt(): ##Aqui faz o player se movimentar no eixo x (direita)
    x = player.xcor()
    x += 5
    player.setx(x)

def playerlt(): #Aqui faz o player se movimentar no eixo x (esquerda)
    x = player.xcor()
    x -= 5
    player.setx(x)

def pontos(): #Essa função serve para escrever 'Pontuação='
    pont = turtle
    pont.color('blue')
    pont.speed(0)
    pont.penup()
    pont.goto(150, 200)
    pont.write('Pontuação = ', move=False, align='center', font='arial', )
    pont.hideturtle()

def fps(): #aqui faz o joguinho em 30fps
    janela.ontimer(fps(),1000//24)

janela = turtle.Screen() #criação da janela
janela.bgcolor('black')

quadra()
pontos()

soma=000 #Criação da variável soma em número
somatoria = turtle #aqui é a somatória da pontuação quando bate na comida e escrever a soma na tela
somatoria.color('blue')
somatoria.speed(0)
somatoria.penup()
somatoria.goto(225, 200)
somatoria.write(f'{soma} ', move=False, align='center', font='arial', )
somatoria.hideturtle()

vida=turtle.Turtle() # personagem que é a última vida que some
vida.showturtle()
vida.speed(0)
vida.shape('turtle')
vida.color('white')
vida.penup()
vida.goto(-300,200)
vida.left(90)

vidao = turtle.Turtle() #Personagem da segunda vida que some
vidao.showturtle()
vidao.speed(0)
vidao.shape('turtle')
vidao.color('white')
vidao.penup()
vidao.goto(-270, 200)
vidao.left(90)

vidae= turtle.Turtle() #Personagem da primeira vida que some
vidae.showturtle()
vidae.speed(0)
vidae.shape('turtle')
vidae.color('white')
vidae.penup()
vidae.goto(-240, 200)
vidae.left(90)

bem=turtle.Turtle() #Personagem da Comida
bem.color('green')
bem.shape('circle')
bem.penup()
bem.goto(random.randint(-300,300),random.randint(-250,150))
bem.right(random.randint(0,360)) #mover aleatoriamente

mal = turtle.Turtle() #Surgimento do Veneno
mal.color('red')
mal.shape('circle')
mal.penup()
mal.goto(random.randint(-300,300),random.randint(-250,150))
mal.right(random.randint(0, 360))

player = turtle.Turtle() #Personagem do jogador
player.color('white')
player.shape('turtle')
player.left(90)
player.penup()


janela.listen() #atribuição do teclado,serão utilizadas as teclas w,a,s,d
janela.onkeypress(playerfd,'w') #comando para cima
janela.onkeypress(playerbk,'s') #comando para baixo
janela.onkeypress(playerrt,'d')#comando para direita
janela.onkeypress(playerlt,'a')#comando para esquerda

while bem and mal: #laço para movimentar a comida e o veneno simultaneamente
    bem.forward(5)
    mal.forward(7)

    if not bem.xcor() <= 300: #Colisão da comida com a arena (barreira direita)
        bem.speed(0)
        bem.setpos(300, bem.ycor())
        bem.right(random.randint(0,360))

    if not bem.xcor() >= -300: #Colisão da comida com a arena (barreira esquerda)
        bem.speed(0)
        bem.setpos(-300, bem.ycor())
        bem.right(random.randint(0,360))

    if not bem.ycor() <= 150: #Colisão da comida com a arena (barreira superior)
        bem.speed(0)
        bem.setpos(bem.xcor(),150)
        bem.right(random.randint(0,360))

    if not bem.ycor() >= -250: #Colisão da comida com a arena (barreira inferior)
        bem.speed(0)
        bem.setpos(bem.xcor(),-250)
        bem.right(random.randint(0,360))

    if not mal.xcor() <= 300: #Colisão do veneno com a arena (barreira direita)
        mal.speed(0)
        mal.setpos(300, mal.ycor())
        mal.right(random.randint(0,360))

    if not mal.xcor() >= -300: #Colisão do veneno com a arena (barreira esquerda)
        mal.speed(0)
        mal.setpos(-300, mal.ycor())
        mal.right(random.randint(0,360))

    if not mal.ycor() <= 150: #Colisão do veneno com a arena (barreira superior)
        mal.speed(0)
        mal.setpos(mal.xcor(),150)
        mal.right(random.randint(0,360))

    if not mal.ycor() >= -250: #Colisão do veneno com a arena (barreira inferior)
        mal.speed(0)
        mal.setpos(mal.xcor(),-250)
        mal.right(random.randint(0,360))

    if player.xcor()>=300: #Colisão do jogador com a arena (barreira direita)
        player.speed(0)
        player.setpos(300,player.ycor())

    if player.xcor()<=-300: #Colisão do jogador com a arena (barreira esquerda)
        player.speed(0)
        player.setpos(-300, player.ycor())

    if player.ycor()>=150: #Colisão do jogador com a arena (barreira superior)
        player.speed(0)
        player.setpos(player.xcor(), 150)

    if player.ycor()<=-250: #Colisão do jogador com a arena (barreira inferor)
        player.speed(0)
        player.setpos(player.xcor(), -250)

    if player.distance(mal)<=10 and vidae.isvisible()==True: #Interação entre o player e o veneno e a perda da primeira vida
        vidae.hideturtle()
        mal.speed(0)
        mal.goto(random.randint(-300,300),random.randint(-250,150))
        mal.right(random.randint(0,360))

    if player.distance(mal)<=10 and vidae.isvisible()==False and vidao.isvisible()==True: #Interação entre o player e o veneno e a perda da segunda vida
        vidao.hideturtle()
        mal.speed(0)
        mal.goto(random.randint(-300, 300), random.randint(-250, 150))
        mal.right(random.randint(0, 360))

    if player.distance(mal)<=10 and vidao.isvisible()==False: #Interação entre o player e o veneno e a perda da terceira vida
        vida.hideturtle()
    if vida.isvisible()==False: #Após a perda da terceira vida, o jogo é encerrado
        turtle.bye()

    if player.distance(bem)<=10: #Interação entre o jogador e a comida com o fito de aumentar a pontuação
        somatoria.clear()
        pontos()
        bem.speed(0)
        soma+=100
        somatoria.goto(225, 200)
        somatoria.write(f'{soma} ', move=False, align='center', font='arial', )
        bem.goto(random.randint(-300,300),random.randint(-250,150))
        bem.left(random.randint(0,360))


fps()
janela.mainloop()
