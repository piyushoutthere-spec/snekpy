import pygame
import random
pygame.init()
window=pygame.display.set_mode((800,600))
window.fill((0,0,0))
pygame.display.set_caption("Write your caption here!")
player=pygame.image.load("imgs/player.png.png").convert_alpha()
player=pygame.transform.scale(player,(100,100))
player_x=0
player_y=450
player_vel_x=0
player_vel_y=0
falling_object=pygame.image.load("imgs/falling.png.png").convert_alpha()
falling_object=pygame.transform.scale(falling_object,(100,100))
falling_object_x=400
falling_object_y=0
falling_object_vel_x=0
falling_object_vel_y=0.2
game_state=1
S=0
HS=0
F=pygame.font.Font(None,50)
def collision_detection():
    player_rect=player.get_rect(topleft=(player_x,player_y))
    falling_rect=falling_object.get_rect(topleft=(falling_object_x,falling_object_y))
    return player_rect.colliderect(falling_rect)    
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit(0)
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_r and game_state==2:
                player_x=0
                player_y=450
                falling_object_x=random.randint(0,window.width-falling_object.width)
                falling_object_y=0
                player_vel_x=0
                player_vel_y=0
                falling_object_vel_x=0
                falling_object_vel_y=0.2
                S=0
                game_state=1
            if event.key==pygame.K_LEFT:
                player_vel_x=-1
            if event.key==pygame.K_RIGHT:
                player_vel_x=1
        if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    player_vel_x=0        
    window.fill((255,255,255))
    if game_state==1:    
     player_x +=player_vel_x
     player_y +=player_vel_y
     player_x=max(0,min(player_x,window.width-player.width))
     falling_object_x +=falling_object_vel_x
     falling_object_y +=falling_object_vel_y
     if collision_detection():
         S+=1
         if S>HS:
             HS=S
         falling_object_x=random.randint(0,window.width-falling_object.width)
         falling_object_y=0
     elif falling_object_y+falling_object.height>=600:
         game_state=2    
     window.blit(player,(player_x,player_y))
     ST=F.render("Score:"+str(S),True,(0,0,0))
     window.blit(ST,(10,10))
     HT=F.render("High score:"+str(HS),True,(0,0,0))
     window.blit(HT,(10,50))
     window.blit(falling_object,(falling_object_x,falling_object_y))
    elif game_state==2:
        GOT=F.render("GAME OVERR",True,(255,0,0))
        ST=F.render("Score: "+ str(S),True,(0,0,0))
        RT=F.render("Press R to restart",True,(0,0,0))
        window.blit(GOT,(300,200))
        window.blit(ST,(330,260))
        window.blit(RT,(280,320))
    pygame.display.flip()    
