import pygame, sys, time, random
from pygame.locals import *
from datetime import datetime
pygame.init()
play_surface = pygame.display.set_mode((500,500))
fps = pygame.time.Clock()

def notocar_spawm():
    bad_pos = [random.randint(0,49)*10, random.randint(0,49)*10]
    return bad_pos
def comida_spawm():
    food_pos = [random.randint(0,49)*10, random.randint(0,49)*10]
    return food_pos
def main():
    
    snake_pos = [100,50]
    snake_body = [[100,50],[90,50],[80,50]]
    direction = "RIGHT"
    change = direction
    food_pos = comida_spawm()
    bad_pos1 = notocar_spawm()
    bad_pos2 = notocar_spawm()
    bad_pos3 = notocar_spawm()
    score = 0
    contador = 0
    contador2 = 0
    
    run = True
    while run:
        contador += 1
        if contador >= 59:
            contador = 1
            bad_pos1 = notocar_spawm()
            bad_pos2 = notocar_spawm()
            bad_pos3 = notocar_spawm()
            contador2 +=1
        if contador2 >= 2: 
            if contador >= 20 and contador <= 33:
                bad_pos1 = notocar_spawm()
                bad_pos2 = notocar_spawm()
                bad_pos3 = notocar_spawm()

            if contador >= 35 and contador <= 39:
                bad_pos1 = notocar_spawm()
                bad_pos2 = notocar_spawm()
                bad_pos3 = notocar_spawm()
            if contador >= 40 and contador <= 49:
                bad_pos1 = notocar_spawm()
                bad_pos2 = notocar_spawm()
                bad_pos3 = notocar_spawm() 
            
                   
        """print(contador)"""
        """tiempo = datetime.now()
        print(tiempo.strftime("%S"))"""
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    change = "RIGHT"
                if event.key == pygame.K_LEFT:
                    change = "LEFT"
                if event.key == pygame.K_UP:
                    change = "UP"
                if event.key == pygame.K_DOWN:
                    change = "DOWN"
        """Aqui le damos la direccion a la culebra"""
        if change == "RIGHT" and direction != "LEFT":
            direction = "RIGHT"
        if change == "LEFT" and direction != "RIGHT":
            direction = "LEFT"
        if change == "UP" and direction != "DOWN":
            direction = "UP"
        if change == "DOWN" and direction != "UP":
            direction = "DOWN"
            
        if direction == "RIGHT":
            snake_pos[0] += 10
        if direction == "LEFT":
            snake_pos[0] -= 10
        if direction == "UP":
            snake_pos[1] -= 10
        if direction == "DOWN":
            snake_pos[1] += 10
            
        snake_body.insert(0,list(snake_pos))

        if snake_pos == food_pos:
            food_pos = comida_spawm()
            score += 1
            print(f"Puntuacion: {score}")
        else:
            snake_body.pop()
        
        play_surface.fill((0,0,0))
        
        for pos in snake_body:
            pygame.draw.rect(play_surface,(200,200,200), pygame.Rect((pos[0],pos[1], 10, 10)))
            pygame.draw.rect(play_surface,(255,160,20), pygame.Rect((food_pos[0],food_pos[1], 10, 10)))
            pygame.draw.rect(play_surface,(255,0,0), pygame.Rect((bad_pos1[0],bad_pos1[1], 10, 10)))
            pygame.draw.rect(play_surface,(255,0,0), pygame.Rect((bad_pos2[0],bad_pos2[1], 10, 10)))
            pygame.draw.rect(play_surface,(255,0,0), pygame.Rect((bad_pos3[0],bad_pos3[1], 10, 10)))

        if snake_pos[0] >= 500 or snake_pos[0] <= 0:
            print(f"Game Over: {score}")
            run = False
        if snake_pos[1] >= 500 or snake_pos[1] <= 0:
            print(f"Game Over: {score}")
            run = False

        if snake_pos in snake_body[1:]:
            print(f"Game Over: {score}")
            run = False
            
        if snake_pos == bad_pos1:
            print(f"Game Over: {score}")
            run = False
        if snake_pos == bad_pos2:
            print(f"Game Over: {score}")
            run = False
        if snake_pos == bad_pos3:
            print(f"Game Over: {score}")
            run = False
        pygame.display.flip()
        fps.tick(10)

main()
pygame.quit()
