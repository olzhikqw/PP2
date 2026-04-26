import pygame
from datetime import datetime
from tools import draw_shape, flood_fill
pygame.init()
W, H, TH = 900, 650, 50
screen = pygame.display.set_mode((W, H))
canvas = pygame.Surface((W, H - TH))
canvas.fill((255,255,255))
clock = pygame.time.Clock()
fu = pygame.font.SysFont("Arial", 13)
ft = pygame.font.SysFont("Arial", 22)
TOOLS   = ["pencil","line","rect","circle","square","rtriangle","etriangle","rhombus","eraser","fill","text"]
LABELS  = ["Pen","Line","Rect","Circ","Sq","RTri","ETri","Rhom","Era","Fill","Txt"]
COLORS  = [(0,0,0),(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,165,0),(128,0,128),(0,255,255),(165,42,42)]
BSIZES  = [2, 5, 10]
tool, color, bi = "pencil", (0,0,0), 1
drawing, sp, lp, pbuf = False, None, None, None
ta, tp, tb = False, None, "" 
def cp(pos): return (pos[0], pos[1] - TH)
def on_cv(pos): return pos[1] >= TH
def toolbar():
    pygame.draw.rect(screen, (50,50,50), (0,0,W,TH))
    for i,(tn,lb) in enumerate(zip(TOOLS,LABELS)):
        x = 5+i*58
        pygame.draw.rect(screen,(100,100,200) if tool==tn else (80,80,80),(x,5,54,20),border_radius=3)
        screen.blit(fu.render(lb,True,(255,255,255)),(x+4,8))
    for i,sz in enumerate(BSIZES):
        x = 5+i*30+len(TOOLS)*58-160
        pygame.draw.rect(screen,(200,150,50) if bi==i else (80,80,80),(x,28,26,18),border_radius=3)
        screen.blit(fu.render(str(sz),True,(255,255,255)),(x+6,30))
    for i,c in enumerate(COLORS):
        x = W-(len(COLORS)-i)*22-5
        pygame.draw.rect(screen,c,(x,5,18,38),border_radius=2)
        if c==color: pygame.draw.rect(screen,(255,255,255),(x,5,18,38),2,border_radius=2)
    pygame.draw.rect(screen,color,(W-235,10,28,28),border_radius=3)
running = True
while running:
    bs = BSIZES[bi]
    for e in pygame.event.get():
        if e.type == pygame.QUIT: running = False
        elif e.type == pygame.KEYDOWN:
            if ta:
                if e.key == pygame.K_RETURN:
                    canvas.blit(ft.render(tb,True,color),tp); ta=False; tb=""
                elif e.key == pygame.K_ESCAPE: ta=False; tb=""
                elif e.key == pygame.K_BACKSPACE: tb=tb[:-1]
                elif e.unicode: tb+=e.unicode
                continue
            if e.key==pygame.K_ESCAPE: running=False
            if e.key==pygame.K_s and pygame.key.get_mods()&pygame.KMOD_CTRL:
                fname="canvas_"+datetime.now().strftime("%Y%m%d_%H%M%S")+".png"
                pygame.image.save(canvas,fname)
            for k,t in [(pygame.K_p,"pencil"),(pygame.K_l,"line"),(pygame.K_r,"rect"),
                        (pygame.K_c,"circle"),(pygame.K_e,"eraser"),(pygame.K_f,"fill"),(pygame.K_t,"text")]:
                if e.key==k: tool=t
            if e.key==pygame.K_q: bi=0
            if e.key==pygame.K_w: bi=1
            if e.key==pygame.K_F1: bi=2
        elif e.type==pygame.MOUSEBUTTONDOWN and e.button==1:
            mx,my=e.pos
            if my<TH:
                for i,tn in enumerate(TOOLS):
                    if 5+i*58<=mx<=5+i*58+54 and 5<=my<=25: tool=tn
                for i in range(3):
                    if 5+i*30+len(TOOLS)*58-160<=mx<=5+i*30+len(TOOLS)*58-134 and 28<=my<=46: bi=i
                for i,c in enumerate(COLORS):
                    if W-(len(COLORS)-i)*22-5<=mx<=W-(len(COLORS)-i)*22+13 and 5<=my<=43: color=c
                continue
            if not on_cv(e.pos): continue
            p=cp(e.pos)
            if tool=="fill": flood_fill(canvas,p,color)
            elif tool=="text": ta=True; tp=p; tb=""
            else:
                drawing=True; sp=p; lp=p
                if tool not in ("pencil","eraser"): pbuf=canvas.copy()
        elif e.type==pygame.MOUSEBUTTONUP and e.button==1:
            if drawing and on_cv(e.pos) and tool not in ("pencil","eraser"):
                draw_shape(canvas,tool,sp,cp(e.pos),color,bs)
            drawing=False; pbuf=None
        elif e.type==pygame.MOUSEMOTION and drawing and on_cv(e.pos):
            p=cp(e.pos)
            if tool=="pencil": pygame.draw.line(canvas,color,lp,p,bs); lp=p
            elif tool=="eraser": pygame.draw.line(canvas,(255,255,255),lp,p,bs*3); lp=p
            elif pbuf: canvas.blit(pbuf,(0,0)); draw_shape(canvas,tool,sp,p,color,bs)
    screen.fill((0,0,0))
    screen.blit(canvas,(0,TH))
    if ta and tp: screen.blit(ft.render(tb+"|",True,color),(tp[0],tp[1]+TH))
    toolbar()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()