from pygame import *
#crear ventana de juego
window = display.set_mode((700, 500))
#establecer fondo de la escena
display.set_caption("Atrapadas")
#crear 2 objetos y colocarlos en la escena
background =
    transform.scale(
        image.load("background.png"), 
        (700, 500))

x1 = 100
y1 = 300

x2 = 300
y2 = 300

sprite1 = transform.scale(image.load("sprite1.png"), (100, 100))
sprite2 = transform.scale(image.load("sprite2.png"), (100, 100))
speed = 10

#manejo de evento “clic en “Cerrar ventana”
game = True
while game:
    window.blit(background, (0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()

