import pygame, sys
pygame.init() #instalira i učitava sve pygame module

#Definiranje displaya
WIDTH, HEIGHT = 1600, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Street-Fighter")

#Clock
clock = pygame.time.Clock()
FPS = 60

#class Borac(pygame.sprite.Group):
#    def __init__(self):
#        super(Borac, self).__init__()

#class BoracNoge(pygame.sprite.Sprite):
#    def __init__(self):
#        super(BoracNoge, self).__init__()
#        noge_surface = pygame.Surface((300,200), pygame.SRCALPHA)
#        noge_rectangle = noge_surface.get_rect()

        
#borac = Borac()

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
        pod_surface = pygame.Surface((1600, 100))
        pod_rectangle = pod_surface.get_rect(topleft = (0,800))
        pygame.draw.rect(SCREEN, "Brown", pod_rectangle)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if escape_screen("Želiš li izaći iz igre?"):
                        run = False

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()