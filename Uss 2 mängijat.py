import pygame
from math import sqrt
from random import randrange
import time

try:#Võtame failist highscore ja faili puudumisel oletame, et highscore on 0
    highscore = int(open("highscore.txt").read())
except:
    highscore = 0
alghighscore = highscore

pygame.init()
laius = 520 #Suurused
kõrgus = 520
aken = pygame.display.set_mode((laius,kõrgus)) #Akna pinna tegemine
pygame.display.set_caption("Ussimäng!")
aken.fill((153, 255, 51)) #Värv

#Mäng läbi pilt
mäng_läbi = pygame.image.load("uus_lopp.png")
pildi_laius = 736
pildi_kõrgus = 735
mäng_läbi = pygame.transform.scale(mäng_läbi, (round(pildi_laius * 0.6),round(pildi_kõrgus * 0.6)))

#Kasutajale akna näitamine
pygame.display.flip()

#Uss
x = 35
y = 35
laius_uss = 25
kõrgus_uss = 25
border = 10
surm = 0
x_muutus = 25
y_muutus = 0
keha = []

#kana
kõrgus_kana= 25
laius_kana= 25
x_kana= 35
y_kana= 460
x_kana_muutus = 25
y_kana_muutus = 0
kana_keha = []
kanasurm = 0
usssurm = 0

#Toit
raadius = 10
x1 = randrange(border+raadius, laius-border-raadius, 25)
y1 = randrange(border+raadius, kõrgus-border-raadius, 25)

tõeväärtus = True
while tõeväärtus:
    pygame.time.delay(20)
    for event in pygame.event.get():
        
        #Kui kasutaja paneb aknast kinni
        if event.type == pygame.QUIT:
            tõeväärtus = False
        
    #Uss sööb toitu
    dist_uss = sqrt((x+(laius_uss / 2)-x1)*(x+(laius_uss / 2)-x1) + (y+(kõrgus_uss / 2)-y1)*(y+(kõrgus_uss / 2)-y1))
    dist_kana = sqrt((x_kana+(laius_kana / 2)-x1)*(x_kana+(laius_kana / 2)-x1) + (y_kana+(kõrgus_kana / 2)-y1)*(y_kana+(kõrgus_kana / 2)-y1))
    if dist_uss <= 15:
        skoor_uss += 1
        if skoor_uss > highscore:#Kui skoor suurem kui highscore ss highscore muutub scoreiks
            highscore = skoor_uss
        x1 = randrange(border+raadius, laius-border-raadius, 25)
        y1 = randrange(border+raadius, kõrgus-border-raadius, 25)
        keha.append((x, y, laius_uss, kõrgus_uss))#Sisestame uued kordinaadid kehale

    #Kana sööb toitu
    if dist_kana <= 15:
        x1 = randrange(border+raadius, laius-border-raadius, 25)
        y1 = randrange(border+raadius, kõrgus-border-raadius, 25)
        kana_keha.append((x_kana, y_kana, laius_kana, kõrgus_uss))
    
    #Ussi tagumisest otsast hakkavad kordinaadid ennemaks muutuma, ehk et viimane taguots muutub ruuduks, mis ta ees oli enne jne, kuni selleni mis enne pead on
    for i in range(len(keha)-1, 0, -1):
        keha[i] = keha[i-1]
        pygame.draw.rect(aken, (255,204,204), (keha[i]))
    #kana tagumine ots muutub
    for j in range(len(kana_keha)-1, 0, -1):
        kana_keha[j] = kana_keha[j-1]
        pygame.draw.rect(aken, (200,200,200), (kana_keha[i]))
    #Enne pead ruut liigub pea kohale, sest järgnevalt liigub pea edasi
    if len(keha) > 0:
        keha[0] = (x, y, laius_uss, kõrgus_uss)
        pygame.draw.rect(aken, (255,204,204), (keha[0]))
        
    #kana pea edasi liikumine
    if len(kana_keha) > 0:
        kana_keha[0] = (x_kana, y_kana, laius_kana, kõrgus_kana)
        pygame.draw.rect(aken, (200,200,200), (kana_keha[0]))
        
    #Liikumine ja bordertest mitte välja liikumine  
    keys = pygame.key.get_pressed()
    if keys [pygame.K_LEFT]and x > border and x_muutus != 25 and surm == 0:
        x_muutus = -25
        y_muutus = 0
    elif keys [pygame.K_RIGHT]and x < (laius - laius_uss - border) and x_muutus != -25 and surm == 0:
        x_muutus = 25
        y_muutus = 0
    elif keys [pygame.K_UP] and y > border and y_muutus != 25 and surm == 0:
        y_muutus = -25
        x_muutus = 0
    elif keys [pygame.K_DOWN] and y < (kõrgus - laius_uss - border) and y_muutus != -25 and surm == 0:
        y_muutus = 25
        x_muutus = 0
    x = x + x_muutus
    y = y + y_muutus

    #kana liikumine
    keys_kana = pygame.key.get_pressed()
    if keys_kana [pygame.K_a]and x_kana > border and x_kana_muutus != 25 and surm == 0:
        x_kana_muutus = -25
        y_kana_muutus = 0
    elif keys_kana [pygame.K_d]and x_kana < (laius - laius_kana - border) and x_kana_muutus != -25 and surm == 0:
        x_kana_muutus = 25
        y_kana_muutus = 0
    elif keys_kana [pygame.K_w] and y_kana > border and y_kana_muutus != 25 and surm == 0:
        y_kana_muutus = -25
        x_kana_muutus = 0
    elif keys_kana [pygame.K_s] and y_kana < (kõrgus - laius_kana - border) and y_kana_muutus != -25 and surm == 0:
        y_kana_muutus = 25
        x_kana_muutus = 0
    x_kana = x_kana + x_kana_muutus
    y_kana = y_kana + y_kana_muutus
    
    #Kehasse sõitmine
    for osa in kana_keha:
        dist = sqrt((x+(laius_uss / 2)-(osa[0]+(laius_kana / 2)))*(x+(laius_uss / 2)-(osa[0]+(laius_kana / 2))) + (y+(kõrgus_uss / 2)-(osa[1] +(kõrgus_kana / 2)))*(y+(kõrgus_uss / 2)-(osa[1] +(kõrgus_kana / 2))))
        if dist <= 15 and surm == 0:
            usssurm = 1
    for osa in keha:
        dist = sqrt((x_kana+(laius_uss / 2)-(osa[0]+(laius_kana / 2)))*(x_kana+(laius_uss / 2)-(osa[0]+(laius_kana / 2))) + (y_kana+(kõrgus_uss / 2)-(osa[1] +(kõrgus_kana / 2)))*(y_kana+(kõrgus_uss / 2)-(osa[1] +(kõrgus_kana / 2))))
        if dist <= 15 and surm == 0:
            kanasurm = 1
    
    #Seina kokkupõrge või uued x ja y kordinaadid on juba keha kordinaadi
    if x < border or x > (laius - laius_uss - border) or y < border or y > (laius - laius_uss - border) or (x, y, laius_uss, kõrgus_uss) in keha and surm == 0:
        usssurm = 1
    if x_kana < border or x_kana > (laius - laius_kana - border) or y_kana < border or y_kana > (laius - laius_kana - border) or (x_kana, y_kana, laius_kana, kõrgus_kana) in kana_keha and surm == 0:
        kanasurm = 1
        
    #Peade kokkupõrge
    dist_pead = sqrt(((x+(laius_uss / 2)-(x_muutus/2))-(x_kana+(laius_uss / 2)-(x_kana_muutus/2)))*((x+(laius_uss / 2)-(x_muutus/2))-(x_kana+(laius_uss / 2)-(x_kana_muutus/2))) + ((y+(kõrgus_uss / 2)-(y_muutus/2))-(y_kana+(kõrgus_uss / 2)-(y_kana_muutus/2)))*((y+(kõrgus_uss / 2)-(y_muutus/2))-(y_kana+(kõrgus_uss / 2)-(y_kana_muutus/2))))
    if dist_pead <= 12.5 and surm == 0 and ((x_muutus == -x_kana_muutus != 0 and y == y_kana) or (y_muutus == -y_kana_muutus != 0 and x == x_kana)):
        kanasurm = 1
        usssurm = 1
        
    if surm == 0:
        pygame.draw.circle(aken, (248, 255, 1), (x1, y1), raadius)
        pygame.display.set_caption("""Ussimäng! KANA VS USS""")
        pygame.draw.rect(aken, (252,166,166), (x, y, laius_uss, kõrgus_uss))
        pygame.draw.rect(aken,(200,200,200),(x_kana, y_kana, laius_kana, kõrgus_kana))
        
    #Mäng läbi ja surm  
    if kanasurm == 1 or usssurm == 1:
        surm = 1  
    if surm == 1:
        x = 35
        y = 35
        x_kana = 35
        y_kana = 460
        x_kana_muutus = 0
        y_kana_muutus = 0
        x_muutus = 0
        y_muutus = 0
        lõpp = pygame.display.set_mode((laius,kõrgus))
        if usssurm > kanasurm: #Kontrollime kas saavutati uus highscore ja väljastame vastava sõnumi
            pygame.display.set_caption("Läbi! Kana võitis!")
        if kanasurm > usssurm:
            pygame.display.set_caption("Läbi! Uss võitis!")
        if kanasurm == usssurm:
            pygame.display.set_caption("Läbi! Mäng jäi viiki")    
        aken.blit(mäng_läbi, (39,40))

        
    pygame.display.update()
    aken.fill((153, 255, 51))
    time.sleep (100.0 / 1000.0)

pygame.quit()
