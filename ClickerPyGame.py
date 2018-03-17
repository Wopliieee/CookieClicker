import pygame
import time

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
gray = (100,169,169)
yellow = (255,255,0)

display_width = 800
display_height = 800

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Clicker v2.0")

font = pygame.font.SysFont(None, 30)
count_font = pygame.font.SysFont(None, 60)
clock = pygame.time.Clock()

Cookie = pygame.image.load('cookie.jpg')
gui = pygame.image.load('gui.png')

def GameLoop():

    click = 0
    cookie_position = 0
    fps = 0
    count_upgrade = 0
    cs = 0

    cursor_count = 0
    cursor_price = 50
    cursorSHOP_x = 307
    cursorSHOP_y = 133
    cursorSHOP_position = 0

    grandma_count = 0
    grandma_price = 500
    grandmaSHOP_x = 307
    grandmaSHOP_y = 208
    grandmaSHOP_position = 0

    farm_count = 0
    farm_price = 5000
    farmSHOP_x = 307
    farmSHOP_y = 275
    farmSHOP_position = 0

    mine_count = 0
    mine_price = 50000
    mineSHOP_x = 307
    mineSHOP_y = 345
    mineSHOP_position = 0

    factory_count = 0
    factory_price = 500000
    factorySHOP_x = 307
    factorySHOP_y = 416
    factorySHOP_position = 0

    bank_count = 0
    bank_price = 5000000
    bankSHOP_x = 307
    bankSHOP_y = 488
    bankSHOP_position = 0

    temple_count = 0
    temple_price = 10000000
    templeSHOP_x = 307
    templeSHOP_y = 558
    templeSHOP_position = 0

    tower_count = 0
    tower_price = 50000000
    towerSHOP_x = 307
    towerSHOP_y = 628
    towerSHOP_position = 0

    milk_count = 0
    milk_price = 1000000000
    milkSHOP_x = 307
    milkSHOP_y = 705
    milkSHOP_position = 0

    cookie_x = 30
    cookie_y = 40

    timer = 0
    setna_sekundy = 0
    sekunda = 0
    minuta = 0
    godzina = 0

    setna_sekundy2 = 0
    sekunda2 = 0
    minuta2 = 0
    godzina2 = 0

    restart_x = 10
    restart_y = 635
    quit_x = 10
    quit_y = 715

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if cursorSHOP_position == 1:
                        if click >= cursor_price:
                            click -= cursor_price
                            cursor_count += 1
                            fps += 1
                            count_upgrade += 0.25
                            cursor_price = cursor_price + 75
                            cs += 10
                    elif grandmaSHOP_position == 1:
                        if click >= grandma_price:
                            click -= grandma_price
                            grandma_count += 1
                            fps += 1
                            count_upgrade += 1.25
                            grandma_price = grandma_price + 575
                            cs += 50
                    elif farmSHOP_position == 1:
                        if click >= farm_price:
                            click -= farm_price
                            farm_count += 1
                            fps += 1
                            count_upgrade += 6.25
                            farm_price = farm_price + 5750
                            cs += 250
                    elif mineSHOP_position == 1:
                        if click >= mine_price:
                            click -= mine_price
                            mine_count += 1
                            fps += 1
                            count_upgrade += 31.25
                            mine_price = mine_price + 57500
                            cs += 1250
                    elif factorySHOP_position == 1:
                        if click >= factory_price:
                            click -= factory_price
                            factory_count += 1
                            fps += 1
                            count_upgrade += 156.25
                            factory_price = factory_price + 575000
                            cs += 6250
                    elif bankSHOP_position == 1:
                        if click >= bank_price:
                            click -= bank_price
                            bank_count += 1
                            fps += 1
                            count_upgrade += 775
                            bank_price = bank_price + 1100000
                            cs += 31000
                    elif templeSHOP_position == 1:
                        if click >= temple_price:
                            click -= temple_price
                            temple_count += 1
                            fps += 1
                            count_upgrade += 3750
                            temple_price = temple_price + 10200000
                            cs += 150000
                    elif towerSHOP_position == 1:
                        if click >= tower_price:
                            click -= tower_price
                            tower_count += 1
                            fps += 1
                            count_upgrade += 17500
                            tower_price = tower_price + 50200000
                            cs += 700000
                    elif milkSHOP_position == 1:
                        if click >= milk_price:
                            click -= milk_price
                            milk_count += 1
                            timer = 0

                            setna_sekundy2 = setna_sekundy
                            sekunda2 = sekunda
                            minuta2 = minuta
                            godzina2 = godzina
                    elif restart_position == 1:
                        GameLoop()
                    elif quit_position == 1:
                        gameExit = True
                    if cookie_position == 1:
                        timer += 1
                        click = click + 1

        if timer >= 1:
            setna_sekundy += 1.5
            if setna_sekundy == 60:
                setna_sekundy -= 60
                sekunda += 1
            elif sekunda == 60:
                sekunda -= 60
                minuta += 1
            elif minuta == 60:
                minuta -= 60
                godzina += 1


        if fps >= 1:
            click += count_upgrade

        mouse = pygame.mouse.get_pos()

        if cookie_x + 200 > mouse[0] > cookie_x and cookie_y + 200 > mouse[1] > cookie_y:
            cookie_position = 1
        else:
            cookie_position = 0

        if cursorSHOP_x + 500 > mouse[0] > cursorSHOP_x and cursorSHOP_y + 72 > mouse[1] > cursorSHOP_y:
            cursorSHOP_position = 1
        else:
            cursorSHOP_position = 0

        if grandmaSHOP_x + 500 > mouse[0] > grandmaSHOP_x and grandmaSHOP_y + 72 > mouse[1] > grandmaSHOP_y:
            grandmaSHOP_position = 1
        else:
            grandmaSHOP_position = 0

        if farmSHOP_x + 500 > mouse[0] > farmSHOP_x and farmSHOP_y + 72 > mouse[1] > farmSHOP_y:
            farmSHOP_position = 1
        else:
            farmSHOP_position = 0

        if mineSHOP_x + 500 > mouse[0] > mineSHOP_x and mineSHOP_y + 72 > mouse[1] > mineSHOP_y:
            mineSHOP_position = 1
        else:
            mineSHOP_position = 0

        if factorySHOP_x + 500 > mouse[0] > factorySHOP_x and factorySHOP_y + 72 > mouse[1] > factorySHOP_y:
            factorySHOP_position = 1
        else:
            factorySHOP_position = 0

        if bankSHOP_x + 500 > mouse[0] > bankSHOP_x and bankSHOP_y + 72 > mouse[1] > bankSHOP_y:
            bankSHOP_position = 1
        else:
            bankSHOP_position = 0

        if templeSHOP_x + 500 > mouse[0] > templeSHOP_x and templeSHOP_y + 72 > mouse[1] > templeSHOP_y:
            templeSHOP_position = 1
        else:
            templeSHOP_position = 0

        if towerSHOP_x + 500 > mouse[0] > towerSHOP_x and towerSHOP_y + 72 > mouse[1] > towerSHOP_y:
            towerSHOP_position = 1
        else:
            towerSHOP_position = 0

        if milkSHOP_x + 500 > mouse[0] > milkSHOP_x and milkSHOP_y + 100 > mouse[1] > milkSHOP_y:
            milkSHOP_position = 1
        else:
            milkSHOP_position = 0

        if restart_x + 255 > mouse[0] > restart_x and restart_y + 78 > mouse[1] > restart_y:
            restart_position = 1
        else:
            restart_position = 0

        if quit_x + 255 > mouse[0] > quit_x and quit_y + 78 > mouse[1] > quit_y:
            quit_position = 1
        else:
            quit_position = 0

        gameDisplay.blit(gui, (0, 0))
        screen_text = font.render("Cookie: "+str(click), True, black)
        gameDisplay.blit(screen_text, (50, 280))
        screen_text = font.render("c/s: " + str(cs), True, black)
        gameDisplay.blit(screen_text, (50, 250))
        gameDisplay.blit(Cookie, (cookie_x, cookie_y))

        screen_text = font.render(str(godzina), True, black)
        gameDisplay.blit(screen_text, (50, 400))

        screen_text = font.render(":", True, black)
        gameDisplay.blit(screen_text, (85, 400))

        screen_text = font.render(str(minuta), True, black)
        gameDisplay.blit(screen_text, (100, 400))

        screen_text = font.render(":", True, black)
        gameDisplay.blit(screen_text, (133, 400))

        screen_text = font.render(str(sekunda), True, black)
        gameDisplay.blit(screen_text, (150, 400))

        screen_text = font.render(":", True, black)
        gameDisplay.blit(screen_text, (180, 400))

        screen_text = font.render(str(setna_sekundy), True, black)
        gameDisplay.blit(screen_text, (195, 400))

        ########

        screen_text = font.render(str(godzina2), True, red)
        gameDisplay.blit(screen_text, (50, 430))

        screen_text = font.render(":", True, red)
        gameDisplay.blit(screen_text, (85, 430))

        screen_text = font.render(str(minuta2), True, red)
        gameDisplay.blit(screen_text, (100, 430))

        screen_text = font.render(":", True, red)
        gameDisplay.blit(screen_text, (133, 430))

        screen_text = font.render(str(sekunda2), True, red)
        gameDisplay.blit(screen_text, (150, 430))

        screen_text = font.render(":", True, red)
        gameDisplay.blit(screen_text, (180, 430))

        screen_text = font.render(str(setna_sekundy2), True, red)
        gameDisplay.blit(screen_text, (195, 430))

        ########

        screen_text = count_font.render(str(cursor_count), True, gray)
        gameDisplay.blit(screen_text, (690, 150))
        screen_text = font.render("* "+str(cursor_price), True, yellow)
        gameDisplay.blit(screen_text, (410, 174))

        screen_text = count_font.render(str(grandma_count), True, gray)
        gameDisplay.blit(screen_text, (690, 222))
        screen_text = font.render("* " + str(grandma_price), True, yellow)
        gameDisplay.blit(screen_text, (410, 244))

        screen_text = count_font.render(str(farm_count), True, gray)
        gameDisplay.blit(screen_text, (690, 292))
        screen_text = font.render("* " + str(farm_price), True, yellow)
        gameDisplay.blit(screen_text, (410, 314))

        screen_text = count_font.render(str(mine_count), True, gray)
        gameDisplay.blit(screen_text, (690, 363))
        screen_text = font.render("* " + str(mine_price), True, yellow)
        gameDisplay.blit(screen_text, (410, 384))

        screen_text = count_font.render(str(factory_count), True, gray)
        gameDisplay.blit(screen_text, (690, 433))
        screen_text = font.render("* " + str(factory_price), True, yellow)
        gameDisplay.blit(screen_text, (410, 455))

        screen_text = count_font.render(str(bank_count), True, gray)
        gameDisplay.blit(screen_text, (690, 503))
        screen_text = font.render("* " + str(bank_price), True, yellow)
        gameDisplay.blit(screen_text, (410, 526))

        screen_text = count_font.render(str(temple_count), True, gray)
        gameDisplay.blit(screen_text, (690, 573))
        screen_text = font.render("* " + str(temple_price), True, yellow)
        gameDisplay.blit(screen_text, (410, 597))

        screen_text = count_font.render(str(tower_count), True, gray)
        gameDisplay.blit(screen_text, (690, 643))
        screen_text = font.render("* " + str(tower_price), True, yellow)
        gameDisplay.blit(screen_text, (410, 667))

        screen_text = count_font.render(str(milk_count), True, gray)
        gameDisplay.blit(screen_text, (690, 733))
        screen_text = font.render("* " + str(milk_price), True, blue)
        gameDisplay.blit(screen_text, (410, 757))

        clock.tick(40)
        pygame.display.update()

    pygame.quit()
    quit()

GameLoop()