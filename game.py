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
    def __init__(self, poz, odabir):
        super().__init__()
        self.pocetpoz = poz
        self.image = pygame.Surface((416, 590)) 
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = ((self.pocetpoz))
        self.gravitacija = 0
        self.odabir = odabir
        
        #Ovdje radimo rectanglove za svkai dio tijela
        if self.odabir == 1:
            self.legs_rect = pygame.Rect(self.pocetpoz[0] + 3, self.pocetpoz[1], 218, 296)
            self.torso_rect = pygame.Rect(self.pocetpoz[0] + 43, self.pocetpoz[1] - 486, 138, 194)
            self.head_rect = pygame.Rect(self.pocetpoz[0] + 63, self.pocetpoz[1] - 590, 120, 100)
            self.arms_rect = pygame.Rect(self.pocetpoz[0], self.pocetpoz[1] - 493, 270, 158)
        elif self.odabir == 2:
            self.legs_rect = pygame.Rect(self.pocetpoz[0] + (416-218) - 3, self.pocetpoz[1], 218, 296)
            self.torso_rect = pygame.Rect(self.pocetpoz[0] + (416-138) - 43, self.pocetpoz[1] - 486, 138, 194)
            self.head_rect = pygame.Rect(self.pocetpoz[0] + (416-120) - 63, self.pocetpoz[1] - 590, 120, 100)
            self.arms_rect = pygame.Rect(self.pocetpoz[0] + (416-270), self.pocetpoz[1] - 493, 270, 158)

    def draw_hitboxes(self, screen):
        #crtanje tih hitboxeva (samo za testiranje i developanje)
        pygame.draw.rect(screen, (0, 255, 0), self.legs_rect, 2)  
        pygame.draw.rect(screen, (0, 0, 255), self.torso_rect, 2)  
        pygame.draw.rect(screen, (0, 0, 0), self.head_rect, 2)  
        pygame.draw.rect(screen, (255, 255, 0), self.arms_rect, 2)

    def skakanje(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] and self.rect.bottom >= 800:
            self.gravitacija = -17

    def dodajGravitaciju(self):
        self.gravitacija += 1
        self.rect.y += self.gravitacija
        self.legs_rect.y += self.gravitacija
        self.torso_rect.y += self.gravitacija
        self.head_rect.y += self.gravitacija
        self.arms_rect.y += self.gravitacija
        if self.rect.bottom >= 800:
            self.rect.bottom = 800
            self.legs_rect.bottom = 800
            self.torso_rect.top = 800 - 490
            self.head_rect.top = 800 - 595
            self.arms_rect.top = 800 - 475

    def kretanjePrvog(self):
        brzina = 9
        dx = 0
        key = pygame.key.get_pressed()

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

        #Ovo osigurava da ne ispadnemo iz screena
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > WIDTH:
            dx = WIDTH - self.rect.right
        #Ovo zapravo daje brzinu svim rectanglovima
        self.rect.x += dx
        self.legs_rect.x += dx
        self.torso_rect.x += dx
        self.head_rect.x += dx
        self.arms_rect.x += dx

    def update(self):
        self.draw_hitboxes(SCREEN)
        self.skakanje()
        self.dodajGravitaciju()
        self.kretanjePrvog()
        
borac = pygame.sprite.Group()
borac.add(Borac((200,800), 1))

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
    naslov_surface = naslov_font.render("Street-Figther", False, "White")
    naslov_rectangle = naslov_surface.get_rect(center = (WIDTH/2, 150))
    while True:
        SCREEN.fill("Black")
        mouse_position = pygame.mouse.get_pos()
        IGRAJ_GUMB = Button("Igraj", 70, "White", (220, 120), "Grey", "Green", (WIDTH/2, 400))
        IZADI_GUMB = Button("Izađi", 70, "White", (220, 120), "Grey", "Red", (WIDTH/2, 600))
        for gumb in [IGRAJ_GUMB, IZADI_GUMB]:
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
                    #odabir_borca()
                    igranje()
                if IZADI_GUMB.checkForCollision(mouse_position):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        clock.tick(FPS)

def igranje():
    run = True
    while run == True:
        SCREEN.fill("Light Blue")
        pygame.mouse.set_visible(False)
        pod_surface = pygame.Surface((1600, 100))
        pod_rectangle = pod_surface.get_rect(topleft = (0,800))
        pygame.draw.rect(SCREEN, "Brown", pod_rectangle)

        borac.draw(SCREEN)
        borac.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mouse.set_visible(True)
                    if escape_screen("Želiš li izaći u početni zaslon?"):
                        run = False

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()