import pygame, sys
pygame.init() #instalira i učitava sve pygame module

#Definiranje displaya
WIDTH, HEIGHT = 1600, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Street-Fighter")

#Clock
clock = pygame.time.Clock()
FPS = 60

#Borac
class Borac(pygame.sprite.Sprite):
    def __init__(self, poz):
        super().__init__()
        self.pocetpoz = poz
        self.image = pygame.Surface((416, 590)) 
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = ((self.pocetpoz))
        self.gravitacija = 0
        self.zadnji_skok = pygame.time.get_ticks()
        self.zadnji_punch = pygame.time.get_ticks()
        self.jump_cooldown = 1000
        self.punch_cooldown = 500
        self.health = 100
        self.blokiranje = False
        self.blok_pocetak = 0
        self.blok_health = 4
        self.blok_health_regeneracija = 10000
        self.blok_health_oduzet = pygame.time.get_ticks()
        self.ziv = True
        self.keybind = 0
        
        #Pozicioniranje rectangleova dijelova tijela
        if self.pocetpoz[0] < 800:
            self.legs_rect = pygame.Rect(self.pocetpoz[0] + 3, self.pocetpoz[1], 218, 296)
            self.torso_rect = pygame.Rect(self.pocetpoz[0] + 43, self.pocetpoz[1], 138, 194)
            self.head_rect = pygame.Rect(self.pocetpoz[0] + 63, self.pocetpoz[1], 120, 100)
            self.arms_rect = pygame.Rect(self.pocetpoz[0], self.pocetpoz[1], 270, 158)
        elif self.pocetpoz[0] >= 800:
            self.legs_rect = pygame.Rect(self.pocetpoz[0] + (416-218) - 3, self.pocetpoz[1] - 296, 218, 296)
            self.torso_rect = pygame.Rect(self.pocetpoz[0] + (416-138) - 43, self.pocetpoz[1] - 486, 138, 194)
            self.head_rect = pygame.Rect(self.pocetpoz[0] + (416-120) - 63, self.pocetpoz[1] - 590, 120, 100)
            self.arms_rect = pygame.Rect(self.pocetpoz[0] + (416-270), self.pocetpoz[1] - 493, 270, 158)
    
    #Rectangleovi se vraćaju na početnu poziciju
    def reset(self):
        if self.pocetpoz[0] < 800:
            self.rect.bottomleft = ((self.pocetpoz))
            self.legs_rect = pygame.Rect(self.pocetpoz[0] + 3, self.pocetpoz[1] - 296, 218, 296)
            self.torso_rect = pygame.Rect(self.pocetpoz[0] + 43, self.pocetpoz[1] - 486, 138, 194)
            self.head_rect = pygame.Rect(self.pocetpoz[0] + 63, self.pocetpoz[1] - 590, 120, 100)
            self.arms_rect = pygame.Rect(self.pocetpoz[0], self.pocetpoz[1] - 493, 270, 158)
            self.health = 100
            self.blok_health = 4
        elif self.pocetpoz[0] >= 800:
            self.rect.bottomleft = ((self.pocetpoz))
            self.legs_rect = pygame.Rect(self.pocetpoz[0] + (416-218) - 3, self.pocetpoz[1] - 296, 218, 296)
            self.torso_rect = pygame.Rect(self.pocetpoz[0] + (416-138) - 43, self.pocetpoz[1] - 486, 138, 194)
            self.head_rect = pygame.Rect(self.pocetpoz[0] + (416-120) - 63, self.pocetpoz[1] - 590, 120, 100)
            self.arms_rect = pygame.Rect(self.pocetpoz[0] + (416-270), self.pocetpoz[1] - 493, 270, 158)
            self.health = 100
            self.blok_health = 4


    def draw_hitboxes(self):
        pygame.draw.rect(SCREEN, (0, 255, 0), self.legs_rect, 2)  
        pygame.draw.rect(SCREEN, (0, 0, 255), self.torso_rect, 2)  
        pygame.draw.rect(SCREEN, (0, 0, 0), self.head_rect, 2)  
        pygame.draw.rect(SCREEN, (255, 255, 0), self.arms_rect, 2)


    def blok(self):
        trenutacno_vrijeme = pygame.time.get_ticks()
        key = pygame.key.get_pressed()

        if self.keybind == 1:
            if key[pygame.K_e] and not self.blokiranje:
                self.blokiranje = True

        if self.keybind == 2:
            if key[pygame.K_i] and not self.blokiranje:
                self.blokiranje = True

        if self.blok_health <= 0:
            if trenutacno_vrijeme - self.blok_health_oduzet > self.blok_health_regeneracija:
                self.blok_health = 4
                self.blok_health_oduzet = trenutacno_vrijeme
            else:
                self.blokiranje = False
                self.blok_pocetak = trenutacno_vrijeme


    #Dodaje se punch attack, i oduzima se health na uspješnom udarcu
    def punch(self, protivnik):
        if self.pocetpoz[0] < 800:
            self.punch_rect = pygame.Rect(self.rect.left + 266, self.rect.bottom - 502, 130, 78)
        elif self.pocetpoz[0] >= 800:
            self.punch_rect = pygame.Rect(self.rect.left + (416 - 130) - 266, self.rect.bottom - 502, 130, 78)
        if self.pocetpoz[0] < 800 and self.rect.right < protivnik.rect.right:
            self.punch_rect.left = (self.rect.x + 266)
        elif self.pocetpoz[0] < 800 and self.rect.right > protivnik.rect.right:
            self.punch_rect.left = (self.rect.x + (416 - 130) - 266)
        elif self.pocetpoz[0] >= 800 and self.rect.left > protivnik.rect.left:
            self.punch_rect.left = (self.rect.x + (416 - 130) - 266)
        elif self.pocetpoz[0] >= 800 and self.rect.left < protivnik.rect.left:
            self.punch_rect.left = (self.rect.x + 266)
        pygame.draw.rect(SCREEN, (255, 255, 255), self.punch_rect, 2)
        if protivnik.blokiranje:
            protivnik.blok_health -= 1
            print(protivnik.blok_health)
            return
        elif self.punch_rect.colliderect(protivnik.legs_rect) or self.punch_rect.colliderect(protivnik.torso_rect) or self.punch_rect.colliderect(protivnik.head_rect) or self.punch_rect.colliderect(protivnik.arms_rect):
            protivnik.health -= 5
            print(protivnik.health)
            print(protivnik.blok_health)
           

    def kick(self, protivnik):
        if self.pocetpoz[0] < 800:
            self.kick_rect = pygame.Rect(self.rect.left + 256, self.rect.bottom - 349, 160, 105)
        elif self.pocetpoz[0] >= 800:
            self.kick_rect = pygame.Rect(self.rect.left + (416 - 160) - 256, self.rect.bottom - 349, 160, 105)
        if self.pocetpoz[0] < 800 and self.rect.right < protivnik.rect.right:
            self.kick_rect.left = (self.rect.x + 256)
        elif self.pocetpoz[0] < 800 and self.rect.right > protivnik.rect.right:
            self.kick_rect.left = (self.rect.x + (416 - 160) - 256)
        elif self.pocetpoz[0] >= 800 and self.rect.left > protivnik.rect.left:
            self.kick_rect.left = (self.rect.x + (416 - 160) - 256)
        elif self.pocetpoz[0] >= 800 and self.rect.left < protivnik.rect.left:
            self.kick_rect.left = (self.rect.x + 256)
        pygame.draw.rect(SCREEN, (255, 255, 255), self.kick_rect, 2)
        if protivnik.blokiranje:
            protivnik.blok_health -= 1
            print(protivnik.blok_health)
            return
        elif self.kick_rect.colliderect(protivnik.legs_rect) or self.kick_rect.colliderect(protivnik.torso_rect) or self.kick_rect.colliderect(protivnik.head_rect) or self.kick_rect.colliderect(protivnik.arms_rect):
            protivnik.health -= 10
            print(protivnik.health)
            print(protivnik.blok_health)


    #Funkcija koja omogućava kretanje lika, pali punch metodu
    def kretanje(self, protivnik):
        global brzina
        brzina = 9
        dx = 0
        key = pygame.key.get_pressed()
        self.gravitacija += 1

        self.blok()

        if self.pocetpoz[0] < 800 and self.rect.right < protivnik.rect.right:
            self.legs_rect.left = (self.rect.x + 3)
            self.torso_rect.left = (self.rect.x + 43)
            self.head_rect.left = (self.rect.x + 63)
            self.arms_rect.left = (self.rect.x)
        elif self.pocetpoz[0] < 800 and self.rect.right > protivnik.rect.right:
            self.legs_rect.left = (self.rect.x + (416-219) - 3)
            self.torso_rect.left = (self.rect.x + (416-139) - 43)
            self.head_rect.left = (self.rect.x + (416-121) - 63)
            self.arms_rect.left = (self.rect.x + (416-271))
        elif self.pocetpoz[0] >= 800 and self.rect.left > protivnik.rect.left:
            self.legs_rect.left = (self.rect.x + (416-219) - 3)
            self.torso_rect.left = (self.rect.x + (416-139) - 43)
            self.head_rect.left = (self.rect.x + (416-121) - 63)
            self.arms_rect.left = (self.rect.x + (416-271))
        elif self.pocetpoz[0] >= 800 and self.rect.left < protivnik.rect.left:
            self.legs_rect.left = (self.rect.x + 3)
            self.torso_rect.left = (self.rect.x + 43)
            self.head_rect.left = (self.rect.x + 63)
            self.arms_rect.left = (self.rect.x)

        
        self.rect.y += self.gravitacija
        self.legs_rect.y += self.gravitacija
        self.torso_rect.y += self.gravitacija
        self.head_rect.y += self.gravitacija
        self.arms_rect.y += self.gravitacija
        if self.rect.bottom >= 800:
            self.rect.bottom = 800
            self.legs_rect.bottom = 800
            self.torso_rect.top = 800 - 486
            self.head_rect.top = 800 - 590
            self.arms_rect.top = 800 - 493

        trenutacno_vrijeme = pygame.time.get_ticks()

        #Movement
        if self.keybind == 1:
            if self.ziv == False:
                return
            else:
                if key[pygame.K_w] and self.rect.bottom >= 800 and trenutacno_vrijeme - self.zadnji_skok >= self.jump_cooldown:
                    self.gravitacija = -17
                    self.zadnji_skok = trenutacno_vrijeme

                if self.rect.bottom == 800:
                    if key[pygame.K_a]:
                        dx = -brzina
                    if key[pygame.K_d]:
                        dx = brzina
                elif self.rect.bottom < 800:
                    if key[pygame.K_a]:
                        dx = -brzina/2
                    if key[pygame.K_d]:
                        dx = brzina/2
                if self.blokiranje:
                    if key[pygame.K_a]:
                        dx = -brzina/2
                    if key[pygame.K_d]:
                        dx = brzina/2

                if self.rect.left + dx < 0:
                    dx = -self.rect.left
                if self.rect.right + dx > WIDTH:
                    dx = WIDTH - self.rect.right

                #Punch
                if key[pygame.K_r] and trenutacno_vrijeme - self.zadnji_punch >= self.punch_cooldown:
                    self.punch(protivnik)

                    self.zadnji_punch = trenutacno_vrijeme
                    self.punch_rect.y += self.gravitacija
                    if self.rect.bottom >= 800:
                        self.punch_rect.top = 800 - 503
                    self.punch_rect.x += dx

                if key[pygame.K_f] and trenutacno_vrijeme - self.zadnji_punch >= self.punch_cooldown:
                    self.kick(protivnik)

                    self.zadnji_punch = trenutacno_vrijeme
                    self.kick_rect.y += self.gravitacija
                    if self.rect.bottom >= 800:
                        self.kick_rect.top = 800 - 349
                    self.kick_rect.x += dx

            self.rect.x += dx
            self.legs_rect.x += dx
            self.torso_rect.x += dx
            self.head_rect.x += dx
            self.arms_rect.x += dx

        if self.keybind == 2:
            if self.ziv == False:
                return
            else:
                if key[pygame.K_u] and self.rect.bottom >= 800 and trenutacno_vrijeme - self.zadnji_skok >= self.jump_cooldown:
                    self.gravitacija = -17
                    self.zadnji_skok = trenutacno_vrijeme

                if self.rect.bottom == 800:
                    if key[pygame.K_h]:
                        dx = -brzina
                    if key[pygame.K_k]:
                        dx = brzina
                elif self.rect.bottom < 800:
                    if key[pygame.K_h]:
                        dx = -brzina/2
                    if key[pygame.K_k]:
                        dx = brzina/2

                if self.rect.left + dx < 0:
                    dx = -self.rect.left
                if self.rect.right + dx > WIDTH:
                    dx = WIDTH - self.rect.right

                #Punch
                if key[pygame.K_o] and trenutacno_vrijeme - self.zadnji_punch >= self.punch_cooldown:
                    self.punch(protivnik)

                    self.zadnji_punch = trenutacno_vrijeme
                    self.punch_rect.y += self.gravitacija
                    if self.rect.bottom >= 800:
                        self.punch_rect.top = 800 - 503
                    self.punch_rect.x += dx

                if key[pygame.K_l] and trenutacno_vrijeme - self.zadnji_punch >= self.punch_cooldown:
                    self.kick(protivnik)

                    self.zadnji_punch = trenutacno_vrijeme
                    self.kick_rect.y += self.gravitacija
                    if self.rect.bottom >= 800:
                        self.kick_rect.top = 800 - 349
                    self.kick_rect.x += dx

            self.rect.x += dx
            self.legs_rect.x += dx
            self.torso_rect.x += dx
            self.head_rect.x += dx
            self.arms_rect.x += dx
    
    #Provjerava životni status lika
    def update(self):
        self.draw_hitboxes()
        if self.health <= 0:
            self.ziv = False

class Player:
    def __init__(self, ime):
        self.ime = ime
        self.Ws = 0
        self.Ls = 0

    def zapis(self, igrac, protivnik):
        if protivnik.health <= 0:
            self.Ws += 1
        elif igrac.health <= 0:
            self.Ls += 1

    def postotak(self):
        ukupno_igara = self.Ws + self.Ls
        return (self.Ws / ukupno_igara) * 100 if ukupno_igara > 0 else 0

    #def achievements()

#Definiranje objekata (likova) iz klase Borac i dodavanje u Sprite Grupu        
borac = pygame.sprite.Group()

#Definira se klasa gumb sa svojim metodama
class Button:
    def __init__(self, text_input, text_size, text_color, rectangle_width_and_height, rectangle_color, rectangle_hovering_color, position):
        #rectangle ispod teksta
        self.rectangle = pygame.Rect((position[0]-(rectangle_width_and_height[0]/2), position[1]-(rectangle_width_and_height[1]/2)), rectangle_width_and_height)
        self.rectangle_color, self.rectangle_hovering_color = rectangle_color, rectangle_hovering_color
        #tekst u gumbu
        self.font = pygame.font.Font(None, text_size)
        self.text_surface = self.font.render(text_input, False, text_color)
        self.text_rectangle = self.text_surface.get_rect(center = self.rectangle.center)

    def update(self, screen):
        pygame.draw.rect(screen, self.rectangle_color, self.rectangle)
        screen.blit(self.text_surface, self.text_rectangle)

    def checkForCollision(self, mouse_position):
        if mouse_position[0] in range(self.rectangle.left, self.rectangle.right) and mouse_position[1] in range(self.rectangle.top, self.rectangle.bottom):
            return True
        return False
    
    def changeButtonColor(self):
        self.rectangle_color = self.rectangle_hovering_color
        

def escape_screen(tekst):
    transparent_background = pygame.Surface((WIDTH, HEIGHT))
    transparent_background.fill("Black")
    transparent_background.set_alpha(100)
    SCREEN.blit(transparent_background, (0,0))

    plava_pozadina = pygame.Surface((640,360))
    plava_pozadina.fill("Navy")
    plava_pozadina_rectangle = plava_pozadina.get_rect(center = (WIDTH/2, HEIGHT/2))

    okvir_surface = pygame.Surface((600,320))
    okvir_rectangle = okvir_surface.get_rect(center = (WIDTH/2, HEIGHT/2))

    font = pygame.font.Font(None, 30)
    tekst_surface = font.render(tekst, False, "White")
    tekst_rectangle = tekst_surface.get_rect(midtop = (WIDTH/2, 380))
    while True:
        mouse_position = pygame.mouse.get_pos()
        SCREEN.blit(plava_pozadina, plava_pozadina_rectangle)
        pygame.draw.rect(SCREEN,'Black', okvir_rectangle, 6)
        SCREEN.blit(tekst_surface, tekst_rectangle)

        CANCEL_GUMB = Button('Ne', 30, 'Black', (70, 40), '#475F77', '#D74B4B', (650, 500))
        CONFIRM_GUMB = Button('Da', 30, 'Black', (70, 40), '#475F77', '#77dd77', (950, 500))
        for gumb in [CANCEL_GUMB, CONFIRM_GUMB]:
            if gumb.checkForCollision(mouse_position):
                gumb.changeButtonColor()
            gumb.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if CONFIRM_GUMB.checkForCollision(mouse_position):
                    return True
                if CANCEL_GUMB.checkForCollision(mouse_position):
                    return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        pygame.display.update()
        clock.tick(FPS)

#Glavna funkcija koja se počinje vrtjeti čim se program starta i hijerarhijski je najviša
def main():
    naslov_font = pygame.font.Font(None, 100)
    naslov_surface = naslov_font.render("Podzemne borbe", False, "White")
    naslov_rectangle = naslov_surface.get_rect(center = (WIDTH/2, 100))
    while True:
        SCREEN.fill("Black")
        mouse_position = pygame.mouse.get_pos()
        IGRAJ_GUMB = Button("Igraj", 70, "White", (220, 120), "Grey", "Green", (WIDTH/2, 300))
        ACHIEVEMENTS_GUMB = Button("Achievements", 70, "White", (350, 120), "Grey", "Yellow", (WIDTH/2, 500))
        IZADI_GUMB = Button("Izađi", 70, "White", (220, 120), "Grey", "Red", (WIDTH/2, 700))
        for gumb in [IGRAJ_GUMB, IZADI_GUMB, ACHIEVEMENTS_GUMB]:
            if gumb.checkForCollision(mouse_position):
                gumb.changeButtonColor()
            gumb.update(SCREEN)
        
        SCREEN.blit(naslov_surface, naslov_rectangle)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if escape_screen("Želiš li izaći iz igre?"):
                        pygame.quit()
                        sys.exit()
                    pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                if IGRAJ_GUMB.checkForCollision(mouse_position):
                    imenovanje_profila()
                if IZADI_GUMB.checkForCollision(mouse_position):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        clock.tick(FPS)

PLAYERI_SELEKTIRANI = {}
PLAYERI_IMENA = {}
PLAYERI_LISTA_GUMBOVA = []

selektirani_profili = []
with open("Podzemne borbe\profili.txt",encoding="utf-8") as datoteka:
        profili = datoteka.readlines()

imenovanje_profila_bool = True
biranje_profila_bool = True

def imenovanje_profila(): #upisivanje imena igrača/profila za pamćenje rezultata
    global profili
    global PLAYERI_IMENA
    global PLAYERI_SELEKTIRANI
    global biranje_profila_bool
    global imenovanje_profila_bool
    global trenutno_ime_upis
    global Player1, Player2, Player3, Player4, Player5, Player6, Player7, Player8
    imenovanje_profila_bool = True
    naslov_font = pygame.font.Font(None, 100)
    naslov_surface = naslov_font.render("Odabir igraca", False, "White")
    naslov_rectangle = naslov_surface.get_rect(center = (250, 50))
    trenutno_ime_upis = ""
    for i in range(1,9):
        PLAYERI_SELEKTIRANI.update({f"player_{i}":False})
        PLAYERI_IMENA.update({f"player{i}": profili[i-1][:-1]})
    
    while imenovanje_profila_bool == True:
        SCREEN.fill("Black")
        mouse_position = pygame.mouse.get_pos()
        SCREEN.blit(naslov_surface, naslov_rectangle)


        PLAYER_BUTTON1 = Button(PLAYERI_IMENA.get("player1"), 70, "White", (480, 120), "Grey", "Green", (350, 175))
        PLAYER_BUTTON2 = Button(PLAYERI_IMENA.get("player2"), 70, "White", (480, 120), "Grey", "Green", (350, 175 + 200))
        PLAYER_BUTTON3 = Button(PLAYERI_IMENA.get("player3"), 70, "White", (480, 120), "Grey", "Green", (350, 175 + 200*2))
        PLAYER_BUTTON4 = Button(PLAYERI_IMENA.get("player4"), 70, "White", (480, 120), "Grey", "Green", (350, 175 + 200*3))
        
        PLAYER_BUTTON5 = Button(PLAYERI_IMENA.get("player5"), 70, "White", (480, 120), "Grey", "Green", (1000, 175)) 
        PLAYER_BUTTON6 = Button(PLAYERI_IMENA.get("player6"), 70, "White", (480, 120), "Grey", "Green", (1000, 175 + 200))        
        PLAYER_BUTTON7 = Button(PLAYERI_IMENA.get("player7"), 70, "White", (480, 120), "Grey", "Green", (1000, 175 + 200*2))
        PLAYER_BUTTON8 = Button(PLAYERI_IMENA.get("player8"), 70, "White", (480, 120), "Grey", "Green", (1000, 175 + 200*3))


        Player1 = Player(PLAYERI_IMENA.get("player1")) 
        Player2 = Player(PLAYERI_IMENA.get("player2"))
        Player3 = Player(PLAYERI_IMENA.get("player3"))
        Player4 = Player(PLAYERI_IMENA.get("player4"))

        Player5 = Player(PLAYERI_IMENA.get("player5")) 
        Player6 = Player(PLAYERI_IMENA.get("player6"))
        Player7 = Player(PLAYERI_IMENA.get("player7"))
        Player8 = Player(PLAYERI_IMENA.get("player8"))

        
        PLAYERI_LISTA_GUMBOVA = [PLAYER_BUTTON1,PLAYER_BUTTON2,PLAYER_BUTTON3,PLAYER_BUTTON4,PLAYER_BUTTON5,PLAYER_BUTTON6,PLAYER_BUTTON7,PLAYER_BUTTON8]
        
        
        NAZAD_GUMB = Button("Nazad", 35, "White", (120, 60), "Grey", "Red", (1500, 50))
        NAZAD_GUMB.update(SCREEN)
        if NAZAD_GUMB.checkForCollision(mouse_position):
            NAZAD_GUMB.changeButtonColor()
        NAZAD_GUMB.update(SCREEN)
        for gumb in PLAYERI_LISTA_GUMBOVA:
            if gumb.checkForCollision(mouse_position):
                gumb.changeButtonColor()
            gumb.update(SCREEN)                    
        if list(PLAYERI_IMENA.values()).count("Napravi profil") <= 6:
            DALJE_GUMB = Button("Dalje", 35, "White", (120, 60), "Grey", "Green", (1500, 850))
        else:
            DALJE_GUMB = Button("Dalje", 35, "White", (120, 60), "Grey", "Green", (1500, 850))
        DALJE_GUMB.update(SCREEN)
        if DALJE_GUMB.checkForCollision(mouse_position):
            DALJE_GUMB.changeButtonColor()
        DALJE_GUMB.update(SCREEN)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range (8):
                    PLAYERI_SELEKTIRANI.update({f"player_{i+1}":False})
                    if PLAYERI_IMENA.get(f"player{i+1}") == "":
                        PLAYERI_IMENA.update({f"player{i+1}":"Napravi profil"})
                    if PLAYERI_IMENA.get(f"player{i+1}") + "\n" == profili[i]:
                        pass


                if NAZAD_GUMB.checkForCollision(mouse_position):
                    imenovanje_profila_bool = False
                    main()
                    
                for i in range(8):
                    
                    if PLAYERI_LISTA_GUMBOVA[i].checkForCollision(mouse_position):
                        
                        for k in range (8):
                            if PLAYERI_IMENA.get(f"player{k+1}") == "" and PLAYERI_SELEKTIRANI.get(f"player{k+1}") == False:
                                PLAYERI_IMENA.update({f"player{k+1}":"Napravi profil"})
                            PLAYERI_SELEKTIRANI.update({f"player_{k+1}":False})

                        
                        PLAYERI_SELEKTIRANI.update({f"player_{i+1}":True})
                        trenutno_ime_upis = ""                    
                        PLAYERI_IMENA.update({f"player{i+1}":""})
                    if DALJE_GUMB.checkForCollision(mouse_position):
                        if list(PLAYERI_IMENA.values()).count("Napravi profil") <= 6:
                            if PLAYERI_IMENA.get(f"player{i+1}")+"\n"== profili[i]:
                                biranje_profila()
                                biranje_profila_bool = True
                            
                            with open("Podzemne borbe\profili.txt", encoding="utf-8") as datoteka:
                                profili = []
                                profili = datoteka.readlines()
                                for z in range (8):
                                    profili[z] = PLAYERI_IMENA.get(f"player{z+1}") + "\n"
                            with open("Podzemne borbe\profili.txt","wt",encoding="utf-8",) as datoteka:
                                datoteka.writelines(profili)      
                            imenovanje_profila_bool = False
                        
                        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    escape_screen('Želiš li se vratiti nazad?')
                    imenovanje_profila_bool = False


                for i in range(8):
                    if PLAYERI_SELEKTIRANI.get(f"player_{i+1}") == True:
                        
                        if event.key == pygame.K_BACKSPACE:
                            trenutno_ime_upis = PLAYERI_IMENA.get(f"player{i+1}")
                            trenutno_ime_upis = trenutno_ime_upis[:-1]
                            PLAYERI_IMENA.update({f"player{i+1}": trenutno_ime_upis})
                        elif event.key == pygame.K_RETURN:
                            PLAYERI_SELEKTIRANI.update({f"player_{i+1}":False})
                            if PLAYERI_IMENA.get(f"player{i+1}") == "" :
                                PLAYERI_IMENA.update({f"player{i+1}":"Napravi profil"})
                            trenutno_ime_upis = ""
                        else:
                            if len(trenutno_ime_upis) < 8:
                                trenutno_ime_upis = PLAYERI_IMENA.get(f"player{i+1}")
                                trenutno_ime_upis += event.unicode
                                if trenutno_ime_upis not in list(PLAYERI_IMENA.values()):
                                    PLAYERI_IMENA.update({f"player{i+1}": trenutno_ime_upis})

        pygame.display.update()
        clock.tick(FPS)

def biranje_profila():
    global selektirani_profili
    global PLAYERI_IMENA
    global PLAYERI_SELEKTIRANI
    global PLAYERI_LISTA_GUMBOVA
    global Player1, Player2, Player3, Player4, Player5, Player6, Player7, Player8
    global LISTA_IGRACA
    biranje_profila_bool = True
    SCREEN.fill('Black')

    PLAYER_BUTTON1 = Button(PLAYERI_IMENA.get("player1"), 70, "White", (480, 120), "Grey", "Green", (350, 175))
    PLAYER_BUTTON2 = Button(PLAYERI_IMENA.get("player2"), 70, "White", (480, 120), "Grey", "Green", (350, 175 + 200))
    PLAYER_BUTTON3 = Button(PLAYERI_IMENA.get("player3"), 70, "White", (480, 120), "Grey", "Green", (350, 175 + 200*2))
    PLAYER_BUTTON4 = Button(PLAYERI_IMENA.get("player4"), 70, "White", (480, 120), "Grey", "Green", (350, 175 + 200*3))
         
    PLAYER_BUTTON5 = Button(PLAYERI_IMENA.get("player5"), 70, "White", (480, 120), "Grey", "Green", (1000, 175)) 
    PLAYER_BUTTON6 = Button(PLAYERI_IMENA.get("player6"), 70, "White", (480, 120), "Grey", "Green", (1000, 175 + 200))        
    PLAYER_BUTTON7 = Button(PLAYERI_IMENA.get("player7"), 70, "White", (480, 120), "Grey", "Green", (1000, 175 + 200*2))
    PLAYER_BUTTON8 = Button(PLAYERI_IMENA.get("player8"), 70, "White", (480, 120), "Grey", "Green", (1000, 175 + 200*3))

    LISTA_IGRACA = [Player1, Player2, Player3, Player4, Player5, Player6, Player7, Player8]
  
    font = pygame.font.Font(None, 60)
    
    GUMBOVI_POZICIJE = [(350, 175),(350, 175+200),(350, 175+200*2),((350, 175+200*3)),((1000, 175)),(1000, 175+200),(1000, 175+200*2),(1000, 175+200*3)]
    PLAYERI_LISTA_GUMBOVA=[PLAYER_BUTTON1,PLAYER_BUTTON2,PLAYER_BUTTON3,PLAYER_BUTTON4,PLAYER_BUTTON5,PLAYER_BUTTON6,PLAYER_BUTTON7,PLAYER_BUTTON8]
    GUMBOVI_METAMORFOZA = {PLAYER_BUTTON1:0, PLAYER_BUTTON2:0, PLAYER_BUTTON3:0, PLAYER_BUTTON4:0 ,PLAYER_BUTTON5:0 ,PLAYER_BUTTON6:0 ,PLAYER_BUTTON7:0 ,PLAYER_BUTTON8:0}
    SCREEN.fill('Black')

    while biranje_profila_bool == True:
        SCREEN.fill('Black')
        mouse_position = pygame.mouse.get_pos()
        Choose_profile = font.render("Izaberi profile",1,'White')
        Choose_profile_rect = Choose_profile.get_rect(center=(630,45))
        SCREEN.blit(Choose_profile,Choose_profile_rect)
        for gumb in PLAYERI_LISTA_GUMBOVA:
            if GUMBOVI_METAMORFOZA.get(gumb) == 0:
                if PLAYERI_IMENA.get(f"player{PLAYERI_LISTA_GUMBOVA.index(gumb)+1}") == "Napravi profil":
                    gumb = Button("N/A", 70, 'Black', (480, 120), '#475F77', '#77dd77', GUMBOVI_POZICIJE[PLAYERI_LISTA_GUMBOVA.index(gumb)])
                    gumb.update(SCREEN)         
                else:
                    gumb = Button(PLAYERI_IMENA.get(f"player{PLAYERI_LISTA_GUMBOVA.index(gumb)+1}"), 70, 'Black', (480, 120), '#DADBDD', '#77dd77',GUMBOVI_POZICIJE[PLAYERI_LISTA_GUMBOVA.index(gumb)])
                    gumb.update(SCREEN)
                    if gumb.checkForCollision(mouse_position):
                        gumb.changeButtonColor()
                    gumb.update(SCREEN)
            else:
                gumb = Button(PLAYERI_IMENA.get(f"player{PLAYERI_LISTA_GUMBOVA.index(gumb)+1}"), 70, 'Black', (480, 120), '#D74B4B', '#D74B4B',GUMBOVI_POZICIJE[PLAYERI_LISTA_GUMBOVA.index(gumb)])
                gumb.update(SCREEN) 

        NAZAD_GUMB = Button("Nazad", 35, "White", (120, 60), "Grey", "Red", (1500, 50))
        NAZAD_GUMB.update(SCREEN)
        if NAZAD_GUMB.checkForCollision(mouse_position):
            NAZAD_GUMB.changeButtonColor()
        NAZAD_GUMB.update(SCREEN)
        DALJE_GUMB = Button("Dalje", 35, "White", (120, 60), "Grey", "Green", (1500, 850))        
        DALJE_GUMB.update(SCREEN)
        if DALJE_GUMB.checkForCollision(mouse_position):
            DALJE_GUMB.changeButtonColor()
        DALJE_GUMB.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    escape_screen('Želiš li izaći iz igre?', SCREEN)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if DALJE_GUMB.checkForCollision(mouse_position):
                    if len(selektirani_profili) == 2:
                        odabir_borca()
                        biranje_profila_bool = False
                if NAZAD_GUMB.checkForCollision(mouse_position):
                    imenovanje_profila()
                if len(selektirani_profili) <= 2:
                    for i in range(8):
                        if PLAYERI_LISTA_GUMBOVA[i].checkForCollision(mouse_position):
                            if PLAYERI_IMENA.get(f"player{i+1}") == "Napravi profil":
                                pass
                            else:
                                if len(selektirani_profili)<2:
                                    PLAYERI_LISTA_GUMBOVA[i] = Button(PLAYERI_IMENA.get(f"player{i+1}"), 70, 'Black', (480, 120), '#D74B4B', '#77dd77',GUMBOVI_POZICIJE[i])
                                    PLAYERI_LISTA_GUMBOVA[i].update(SCREEN)
                                    GUMBOVI_METAMORFOZA.update({PLAYERI_LISTA_GUMBOVA[i]:1})
                                if PLAYERI_IMENA.get(f"player{i+1}") in selektirani_profili:
                                    selektirani_profili.remove(PLAYERI_IMENA.get(f"player{i+1}")) 
                                    PLAYERI_LISTA_GUMBOVA[i] = Button(PLAYERI_IMENA.get(f"player{i+1}"), 35, 'Black', (480, 120), '#475F77', '#77dd77',GUMBOVI_POZICIJE[i])
                                    PLAYERI_LISTA_GUMBOVA[i].update(SCREEN)
                                    GUMBOVI_METAMORFOZA.update({PLAYERI_LISTA_GUMBOVA[i]:0})
                                elif PLAYERI_IMENA.get(f"player{i+1}") not in selektirani_profili:
                                    selektirani_profili.append(PLAYERI_IMENA.get(f"player{i+1}"))
                                if len(selektirani_profili) == 3:
                                    selektirani_profili.remove(selektirani_profili[2])
                    
                
                            
        pygame.display.update()

brojac = 0
borcici = []

def odabir_borca():
    global brojac
    global borcici
    global borac1l
    global borac1r
    global borac2l
    global borac2r
    global LISTA_IGRACA
    naslov_font = pygame.font.Font(None, 100)
    naslov_surface = naslov_font.render("Odabir Borca", False, "White")
    naslov_rectangle = naslov_surface.get_rect(center = (250, 50))
    run = True
    while run == True:
        SCREEN.fill("Black")
        mouse_position = pygame.mouse.get_pos()
        NAZAD_GUMB = Button("Nazad", 35, "White", (120, 60), "Grey", "Red", (1500, 50))
        BORAC1_GUMB = Button("Borac1", 70, "White", (220, 120), "Grey", "Green", (WIDTH/2, 400))
        BORAC2_GUMB = Button("Borac2", 70, "White", (220, 120), "Grey", "Blue", (WIDTH/2, 600))
        for gumb in [NAZAD_GUMB, BORAC1_GUMB, BORAC2_GUMB]:
            if gumb.checkForCollision(mouse_position):
                gumb.changeButtonColor()
            gumb.update(SCREEN)

        SCREEN.blit(naslov_surface, naslov_rectangle)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if escape_screen("Želiš li se vratiti na početnu stranicu?"):
                        main()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if NAZAD_GUMB.checkForCollision(mouse_position):
                    main()
                if BORAC1_GUMB.checkForCollision(mouse_position):
                    if brojac == 0:
                        borac1l = Borac((200, 800))
                        borac1l.keybind = 1
                        borac.add(borac1l)
                        borcici.append(borac1l)
                        brojac += 1
                    elif brojac == 1:
                        borac1r = Borac((900, 800))
                        borac1r.keybind = 2
                        borac.add(borac1r)
                        borcici.append(borac1r)
                        brojac -= 1
                        odabir_rundi()
                if BORAC2_GUMB.checkForCollision(mouse_position):
                    if brojac == 0:
                        borac2l = Borac((200, 800))
                        borac2l.keybind = 1
                        borac.add(borac2l)
                        borcici.append(borac2l)
                        brojac += 1
                    elif brojac == 1:
                        borac2r = Borac((900, 800))
                        borac2r.keybind = 2
                        borac.add(borac2r)
                        borcici.append(borac2r)
                        brojac -= 1
                        odabir_rundi()
                
        pygame.display.update()
        clock.tick(FPS)

def odabir_rundi():
    naslov_font = pygame.font.Font(None, 100)
    naslov_surface = naslov_font.render("Na koliko rundi se igra?", False, "White")
    naslov_rectangle = naslov_surface.get_rect(center = (WIDTH/2, 100))
    while True:
        SCREEN.fill("Black")
        mouse_position = pygame.mouse.get_pos()
        JEDNA_GUMB = Button("1", 70, "White", (220, 120), "Grey", "Green", (WIDTH/2, 300))
        TRI_GUMB = Button("3", 70, "White", (220, 120), "Grey", "Green", (WIDTH/2, 500))
        SEDAM_GUMB = Button("7", 70, "White", (220, 120), "Grey", "Green", (WIDTH/2, 700))
        NAZAD_GUMB = Button("Nazad", 35, "White", (120, 60), "Grey", "Red", (1500, 50))
        for gumb in [JEDNA_GUMB, SEDAM_GUMB, TRI_GUMB, NAZAD_GUMB]:
            if gumb.checkForCollision(mouse_position):
                gumb.changeButtonColor()
            gumb.update(SCREEN)

        SCREEN.blit(naslov_surface, naslov_rectangle)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if escape_screen("Želiš li se vratiti na početnu stranicu?"):
                        main()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if JEDNA_GUMB.checkForCollision(mouse_position):
                    igranje()
                if TRI_GUMB.checkForCollision(mouse_position):
                    #igranje3()
                    pass
                if SEDAM_GUMB.checkForCollision(mouse_position):
                    #igranje7()
                    pass
                if NAZAD_GUMB.checkForCollision(mouse_position):
                    odabir_borca()
                
        pygame.display.update()
        clock.tick(FPS)


#Funkcija u kojoj se odvija sama igra
def igranje():
    global borac1l, borac1r, borac2l, borac2r, borcici
    run = True
    while run == True:
        SCREEN.fill("Light Blue")
        pygame.mouse.set_visible(False)
        pod_surface = pygame.Surface((1600, 100))
        pod_rectangle = pod_surface.get_rect(topleft = (0,800))
        pygame.draw.rect(SCREEN, "Brown", pod_rectangle)
        borac.update()
        borac.draw(SCREEN)

        for i in range(0, len(borcici), 2):
            borcici[i].kretanje(borcici[i + 1])
            borcici[i + 1].kretanje(borcici[i])

            borcici[i].draw_hitboxes()
            borcici[i + 1].draw_hitboxes()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mouse.set_visible(True)
                    if escape_screen("Želiš li izaći u početni zaslon?"):
                        for i in range(0, len(borcici), 2):
                            borcici[i].reset()
                            borcici[i + 1].reset()
                            
                        main()
                        run = False

        pygame.display.update()
        clock.tick(FPS)

def winscreen():
    pygame.mouse.set_visible(True)
    transparent_background = pygame.Surface((WIDTH, HEIGHT))
    transparent_background.fill("Light Blue")
    transparent_background.set_alpha(100)
    SCREEN.blit(transparent_background, (0,0))
    run = True
    while run == True:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if escape_screen("Želiš li izaći u početni zaslon?"):
                        run = False
                        main()

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()