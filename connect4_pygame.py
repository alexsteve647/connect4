import pygame

loga_platums = 1280
loga_augstums = 768

zils = (0, 100, 200)

speletajs = "red"

rindas = 7
kolonnas = 6
sunas_platums = 0
sunas_augstums = 0
offsets_y = 100
radiuss = 50
krāsa = "white"

rinda6=[".", ".",".",".",".",".",".",]
rinda5=[".", ".",".",".",".",".",".",]
rinda4=[".", ".",".",".",".",".",".",]
rinda3=[".", ".",".",".",".",".",".",]
rinda2=[".", ".",".",".",".",".",".",]
rinda1=[".", ".",".",".",".",".",".",]

v = []

laukums=[rinda6, rinda5,rinda4,rinda3,rinda2,rinda1]

gajiens = 0
uzvareja = 0

pygame.init()
ekrans = pygame.display.set_mode((loga_platums, loga_augstums))
pygame.display.set_caption("Connect4")
clock = pygame.time.Clock()
running = True
dt = 0

fonts = pygame.font.SysFont("comicsansms", 72)

while running:
    
    gajiens = 0
    
    peles_x, peles_y = pygame.mouse.get_pos()
    
    # pygame.QUIT notikums nozīmē, ka lietotājs noklikšķināja uz X, lai aizvērtu logu
    for pasakums in pygame.event.get():
        if pasakums.type == pygame.QUIT:
            running = False
        elif pasakums.type == pygame.MOUSEBUTTONUP:
            if peles_x >= v[0] - (radiuss) and peles_x <= v[0] + (radiuss):
                gajiens = 1
            elif peles_x >= v[1] - (radiuss) and peles_x <= v[1] + (radiuss):
                gajiens = 2
            elif peles_x >= v[2] - (radiuss) and peles_x <= v[2] + (radiuss):
                gajiens = 3
            elif peles_x >= v[3] - (radiuss) and peles_x <= v[3] + (radiuss):
                gajiens = 4
            elif peles_x >= v[4] - (radiuss) and peles_x <= v[4] + (radiuss):
                gajiens = 5
            elif peles_x >= v[5] - (radiuss) and peles_x <= v[5] + (radiuss):
                gajiens = 6
            elif peles_x >= v[6] - (radiuss) and peles_x <= v[6] + (radiuss):
                gajiens = 7
                
                
    if uzvareja == 0:
        if gajiens >= 1:
            for i in range(6):

                if laukums[5-int(i)][gajiens - 1]==".":
                    laukums[5-int(i)][gajiens - 1]=speletajs
                    z=5-int(i)
                    break
            for iii in range(3):
                for ii in range(4):
                    c1=0
                    c2=0
                    for i in range(4):
                        # No kreisās uz labo dilstošā diognālē
                        if laukums[i+iii][i+ii]==speletajs:
                            c1=c1+1
                        if c1==4: 
                            uzvareja=1
                        # No kreisās uz labo augošā diognālē
                        if laukums[5-i-iii][i+ii]==speletajs:
                            c2=c2+1
                        if c2==4: 
                            uzvareja=1

            for iii in range(6):
                for ii in range(4):
                    c3=0
                    for i in range(4):
                        # Horizontāli no augšas uz leju
                        if laukums[iii][i+ii]==speletajs:
                            c3=c3+1
                        if c3==4: 
                            uzvareja=1
            for iii in range(6):
                for ii in range(3):
                    c4=0
                    for i in range(4):
                        # Vertikāli no augšas uz leju
                        if laukums[i+ii][iii]==speletajs:
                            c4=c4+1
                        if c4==4: 
                            uzvareja=1
            if uzvareja == 0:
                if speletajs == "red": speletajs = "yellow" 
                else: speletajs = "red"
            
    # Aizpildīt ekrānu ar krāsu, lai dzēstu visu no pēdējā kadra
    ekrans.fill(zils)
    
    # Aprēķināt katras režģa šūnas augstumu, pamatojoties uz pieejamo augstumu
    sunas_augstums = (ekrans.get_height() - offsets_y) / kolonnas

    # Aprēķināt katras režģa šūnas platumu, pamatojoties uz cell_height
    sunas_platums = sunas_augstums

    # Aprēķināt kopējo režģa platumu
    kopejais_rezga_platums = sunas_platums * rindas

    # Aprēķināt sānu malas
    sanu_mala = (ekrans.get_width() - kopejais_rezga_platums) / 2

    for rindas_indeks, rinda in enumerate(laukums):
        y = (rindas_indeks * sunas_augstums) + (sunas_augstums / 2) + offsets_y
        for kolonnas_indeks, krasa in enumerate(rinda):
            x = (kolonnas_indeks * sunas_platums) + (sunas_platums / 2) + sanu_mala
            v.append(int(x))
            if krasa == ".":
                pygame.draw.circle(ekrans, "white", (int(x), int(y)), radiuss, 0)
            else: pygame.draw.circle(ekrans, krasa, (int(x), int(y)), radiuss, 0)
            
    if uzvareja == 1:
        if speletajs == "red":
            text = fonts.render("Uzvarēja spēlētājs: sarkans", True, "red")
        else: text = fonts.render("Uzvarēja spēlētājs: dzeltens", True, "yellow")
        
        ekrans.blit(text, ((ekrans.get_width() / 2) - text.get_width() // 2, 50 - text.get_height() // 2))
    else: 
        pygame.draw.circle(ekrans, speletajs, ( peles_x , 52.5), radiuss, 0)

    # flip() apgriezt displeju, lai parādītu savu darbu ekrānā
    pygame.display.flip()

    # Limitē FPS līdz 60
    # dt ir delta laiks sekundēs kopš pēdējā kadra, ko izmanto kadru ātrumam
    # Neatkarīga fizika
    dt = clock.tick(60) / 1000

pygame.quit()