import pygame
from math import sqrt
from random import randint
import time

pygame.init()
laius = 500 #Suurused
kõrgus = 500
aken = pygame.display.set_mode((laius,kõrgus)) #Akna pinna tegemine
pygame.display.set_caption("Ussimäng")
aken.fill((153, 255, 51)) #Värv

#Mäng läbi pilt
mäng_läbi = pygame.image.load("game-over.png")
pildi_laius = 528
pildi_kõrgus = 528
mäng_läbi = pygame.transform.scale(mäng_läbi, (round(pildi_laius * 0.35),round(pildi_kõrgus * 0.35)))

#Kasutajale akna näitamine
pygame.display.flip()

#Uss
x = 250
y = 250
laius_uss = 25
kõrgus_uss = 25
border = 10
surm = 0
x_muutus = 25
y_muutus = 0
keha = []

#Toit
raadius = 10
x1 = randint(border*1.5+raadius, laius-border*1.5-raadius)
y1 = randint(border*1.5+raadius, kõrgus-border*1.5-raadius)


tõeväärtus = True
while tõeväärtus:
    pygame.time.delay(20)
    for event in pygame.event.get():
        
        #Kui kasutaja paneb aknast kinni
        if event.type == pygame.QUIT:
            tõeväärtus = False
    #Uss sööb toitu
    dist = sqrt((x+(laius_uss / 2)-x1)*(x+(laius_uss / 2)-x1) + (y+(kõrgus_uss / 2)-y1)*(y+(kõrgus_uss / 2)-y1))
    if dist <= 15:
        x1 = randint(border*1.5+raadius, laius-border*1.5-raadius)
        y1 = randint(border*1.5+raadius, kõrgus-border*1.5-raadius)
        keha.insert(0, (x, y, laius_uss, kõrgus_uss))#Sisestame uued kordinaadid kehale
    
    #Ussi tagumisest otsast hakkavad kordinaadid ennemaks muutuma, ehk et viimane taguots muutub ruuduks, mis ta ees oli enne jne, kuni selleni mis enne pead on
    for i in range(len(keha)-1, 0, -1):
        keha[i] = keha[i-1]
        pygame.draw.rect(aken, (199,0,157), (keha[i]))
        
    #Enne pead ruut liigub pea kohale, sest järgnevalt liigub pea edasi
    if len(keha) > 0:
        keha[0] = (x, y, laius_uss, kõrgus_uss)
        pygame.draw.rect(aken, (199,0,157), (keha[0]))
        
    #Liikumine ja bordertest mitte välja liikumine  
    keys = pygame.key.get_pressed()
    if keys [pygame.K_LEFT]and x > border:
        x_muutus = -25
        y_muutus = 0
    elif keys [pygame.K_RIGHT]and x < (laius - laius_uss - border) :
        x_muutus = 25
        y_muutus = 0
    elif keys [pygame.K_UP] and y > border:
        y_muutus = -25
        x_muutus = 0
    elif keys [pygame.K_DOWN] and y < (kõrgus - laius_uss - border):
        y_muutus = 25
        x_muutus = 0
    x = x + x_muutus
    y = y + y_muutus
    
    #Seina kokkupõrge ja mäng läbi
    if x < border or x > (laius - laius_uss - border) or y < border or y > (laius - laius_uss - border) or (x, y, laius_uss, kõrgus_uss) in keha:
        surm = 1
        x_muutus = 0
        y_muutus = 0
    if surm == 1:
        lõpp = pygame.display.set_mode((laius,kõrgus))
        pygame.display.set_caption("Läbi")
        aken.blit(mäng_läbi, (250-(round(pildi_laius*0.35/2)),250-(round(pildi_kõrgus*0.35/2))))
           
    pygame.draw.rect(aken, (199,0,157), (x, y, laius_uss, kõrgus_uss))
    if surm == 0:
        pygame.draw.circle(aken, (255, 0, 0), (x1, y1), raadius)
    pygame.display.update()
    aken.fill((153, 255, 51))
    time.sleep (100.0 / 1000.0)

pygame.quit()