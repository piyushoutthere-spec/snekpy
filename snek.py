import pygame
import random
pygame.init()
window=pygame.display.set_mode((800,600))
window.fill((0,0,0))
pygame.display.set_caption("Write your caption here!")
player=pygame.image.load("imgs/player.png.png").convert_alpha()
player=pygame.transform.scale(player,(300,300))
player_x=0
player_y=0
player_vel_x=0
player_vel_y=0
falling_object=pygame.surface.Surface((50,50))
falling_object.fill((255,255,255))
falling_object_x=0
falling_object_y=0
falling_object_vel_x=0
falling_object_vel_y=0
game_state=1
def collision_detection():
        return(player_x<=(falling_object_x + int(falling_object.width)) and
            (player_x + player.width)>=falling_object_x and
            player_y <=(falling_object_y+falling_object.height+5) and
            (player_y +player.height)>= falling_object_y)
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit(0)
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                player_vel_x=-0.2
            if event.key==pygame.K_RIGHT:
                player_vel_x=0.2
        else:
            player_vel_x=0
            player_vel_y=0            
    window.fill((255,255,255))
    if collision_detection():
        falling_object_y=0
        falling_object_x=random.randint(0,window.width-50)
    if falling_object_y>=600:
        player_x,player_y=1000,1000 
        player_vel_x,player_vel_y=0,0
        falling_object_x,falling_objects_y=1000,1000
        falling_object_vel_x,falling_object_vel_y=0,0
        game_state=2   
    if game_state==1:    
     player_x +=player_vel_x
     player_y +=player_vel_y
     window.blit(player,(player_x,player_y))
     falling_object_x +=falling_object_vel_x
     falling_object_y +=falling_object_vel_y
     window.blit(falling_object,(falling_object_x,falling_object_y))
    elif game_state==2:
     pass
    pygame.display.flip()
