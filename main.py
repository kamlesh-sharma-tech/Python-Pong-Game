import pygame, sys,random


def ball_animation():
    global ball_speed_x, ball_speed_y,score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 50 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x *= -1
        
    if ball.colliderect(player_kamlesh):  
        ball_speed_y *= -1
        score = score + 1
    if ball.bottom >= screen_height: 
        score = 0
        ball_restart()
    
    
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width/2,screen_height/2)
    ball_speed_x = 0
    ball_speed_y = 0
  
def player_kamlesh_animation():
    player_kamlesh.x += player_kamlesh_speed
    if player_kamlesh.left <= 0:
        player_kamlesh.left = 0
    if player_kamlesh.right >= screen_width:
        player_kamlesh.right = screen_width


pygame.init()
clock = pygame.time.Clock()

screen_width = 920
screen_height = 700
light_grey = (200,200,200)
green = (0,255,0)
red = (255,0,0)
white = (255,255,255)
black =(0,0,0)
orange = (255,165,0)
light_blue = (67.8,84.7,90.2)
blue = (0,0,255)
ball_speed_x = 0
ball_speed_y = 0
player_kamlesh_speed = 0
score = 0

screen = pygame.display.set_mode((screen_width,screen_height))
title = pygame.display.set_caption("Ping Pong Game")

ball = pygame.Rect(screen_width/2 - 15,screen_height/2 -15,25,25)
player_kamlesh = pygame.Rect(screen_width/2 - 70,screen_height -25,140,15) 


font = pygame.font.Font('freesansbold.ttf',32)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                player_kamlesh_speed -= 7
            if event.key == pygame.K_RIGHT:
                player_kamlesh_speed += 7
            if event.key == pygame.K_RETURN:
                ball_speed_x = 8 * random.choice((-1,-1))
                ball_speed_y = 8 * random.choice((-1,-1))
               
               
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_RETURN:
                player_kamlesh_speed = 0
               

    screen.fill(light_blue) 
    ball_animation()
      
    text = font.render(f'Score : {score}',True,orange)
  
    screen.blit(text,(10,15))

    player_kamlesh_animation()
    pygame.draw.rect(screen,green,player_kamlesh)
    pygame.draw.ellipse(screen,white,ball)
    pygame.draw.aaline(screen,(255,255,255),(0,screen_height/2 - 300),(screen_width,screen_height/2 - 300))
    pygame.draw.aaline(screen,white,(0,screen_height/2 - 300),(screen_width-920,screen_height))
    
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()