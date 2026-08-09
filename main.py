import warnings
warnings.filterwarnings('ignore', category=RuntimeWarning)

import pygame;pygame.init();pygame.font.init()
import random;import time

WIDTH,HEIGHT=800,500
WHITE="#FFFFFF"
BLACK="#000000"

p1points=0
p2points=0

FONT=pygame.font.SysFont('Comic Sans MS',40)

WIN=pygame.display.set_mode((WIDTH,HEIGHT));WIN.fill(BLACK)
pygame.display.set_caption('Pong')
clock=pygame.time.Clock()

lose_message=FONT.render('You Lose!',True,WHITE)
win_message=FONT.render('You Win!',True,WHITE)

pw,ph=20,100
bw,bh=10,10

p1x,p1y=20,(HEIGHT/2)-50
p2x,p2y=WIDTH-40,(HEIGHT/2)-50
bx,by=WIDTH/2,HEIGHT/2

speed=3

def decide_direction():
	direction=random.randint(0,3)

	if direction==0:
		bvx,bvy=3,3
	elif direction==1:
		bvx,bvy=-3,3
	elif direction==2:
		bvx,bvy=3,-3
	elif direction==3:
		bvx,bvy=-3,-3

	return bvx,bvy

bvx,bvy=decide_direction()

run=True
while run:
	clock.tick(60)
	WIN.fill(BLACK)

	paddle1=pygame.Rect(p1x,p1y,pw,ph)
	paddle2=pygame.Rect(p2x,p2y,pw,ph)
	ball=pygame.Rect(bx,by,bw,bh)

	bx+=bvx;by+=bvy

	if by<0 or by>(HEIGHT-bh):
		bvy*=-1

	if paddle1.colliderect(ball):
		bvx*=-1
		bx=p1x+pw
	if paddle2.colliderect(ball):
		bvx*=-1
		bx=p2x-bw

	elif bx<0:
		p2points+=1
		bx,by=WIDTH/2,HEIGHT/2
		bvx,bvy=decide_direction()
	
	elif bx>(WIDTH-bw):
		p1points+=1
		bx,by=WIDTH/2,HEIGHT/2
		bvx,bvy=decide_direction()
	
	if p1points>=5:
		WIN.blit(win_message,((WIDTH/2)-(win_message.get_width()/2),(HEIGHT/2)-(win_message.get_height()/2)))
		run=False
	if p2points>=5:
		WIN.blit(lose_message,((WIDTH/2)-(lose_message.get_width()/2),(HEIGHT/2)-(lose_message.get_height()/2)))
		run=False


	score1=FONT.render('Player 1: {0}'.format(p1points),True,WHITE)
	WIN.blit(score1,((WIDTH/2)-10-score1.get_width(),10))

	score2=FONT.render('Player 2: {0}'.format(p2points),True,WHITE)
	WIN.blit(score2,(((WIDTH/2)+10),10))

	if bx>(WIDTH/2):
		if (by>1.05*(p2y+(ph/2))) and bvx==3:
			p2y+=speed
			if p2y>(HEIGHT-ph):
				p2y=(HEIGHT-ph)
		elif (by<1.05*(p2y+(ph/2))) and bvx==3:
			p2y-=speed
			if p2y<0:
				p2y=0


	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_q:
				run=False
	
	keys=pygame.key.get_pressed()
	if keys[pygame.K_UP]:
		p1y-=speed
		if p1y<0:
			p1y=0
	if keys[pygame.K_DOWN]:
		p1y+=speed
		if p1y>(HEIGHT-ph):
			p1y=(HEIGHT-ph)
	
	pygame.draw.rect(WIN,WHITE,paddle1);pygame.draw.rect(WIN,WHITE,paddle2)
	pygame.draw.rect(WIN,WHITE,ball)

	pygame.display.update()

time.sleep(1)
pygame.quit()
