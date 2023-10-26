import pygame, sys
pygame.init()

width, height = 1600, 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Street-Fighter")
clock = pygame.time.Clock()
FPS = 30

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
        

def main():
    naslov_font = pygame.font.Font(None, 100)
    naslov_surface = naslov_font.render("Street-Figther", False, "White")
    naslov_rectangle = naslov_surface.get_rect(center = (width/2, 150))
    while True:
        mouse_position = pygame.mouse.get_pos()
        igraj_gumb = Button(text_input = "Igraj", text_size = 70, text_color = "White", rectangle_width_and_height = (220, 120), rectangle_color = "Grey", rectangle_hovering_color = "Green", position = (width/2, 400))
        izađi_gumb = Button(text_input = "Izađi", text_size = 70, text_color = "White", rectangle_width_and_height = (220, 120), rectangle_color = "Grey", rectangle_hovering_color = "Red", position = (width/2, 600))
        for gumb in [igraj_gumb, izađi_gumb]:
            if gumb.checkForCollision(mouse_position):
                gumb.changeButtonColor()
            gumb.update(screen)
        
        screen.blit(naslov_surface, naslov_rectangle)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if igraj_gumb.checkForCollision(mouse_position):
                    #odabir_borca()
                    pass
                if izađi_gumb.checkForCollision(mouse_position):
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        clock.tick(FPS)

main()