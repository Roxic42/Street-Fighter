import pygame, sys, os, warnings, time #,pygamepopup
warnings.filterwarnings("ignore", category=UserWarning, message=".*iCCP.*")
pygame.init() #instalira i učitava sve pygame module
#pygamepopup.init()

#Definiranje displaya
WIDTH, HEIGHT = 1600, 900
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Street-Fighter")

#Clock
clock = pygame.time.Clock()
FPS = 60

#Zvukovi opći
pogodeniudaraczvuk=pygame.mixer.Sound(os.path.join("audio","punch zvuk.wav"))
chooseyourcharacterzvuk=pygame.mixer.Sound(os.path.join("audio","choose your character.wav"))
VRATI_NAZAD_ZVUK = pygame.mixer.Sound(os.path.join("audio", "vrati_nazad_zvuk.ogg"))
EXIT_GUMB_ZVUK = pygame.mixer.Sound(os.path.join("audio", "exit_gumb_zvuk.wav"))
TUPI_GUMB_ZVUK = pygame.mixer.Sound(os.path.join("audio", "tupi_gumb_zvuk.ogg"))
KLIK_GUMB_ZVUK = pygame.mixer.Sound(os.path.join("audio", "klik_gumb_zvuk.ogg"))

#Loading screen
LOGO = pygame.image.load(os.path.join("Assets", "MLKJR_LOGO.png")).convert_alpha()
INTRO = pygame.mixer.Sound(os.path.join("audio", "INTRO.ogg"))

def LOADING_SCREEN():
    SCREEN.fill('White')
    SCREEN.blit(LOGO,(300,50))
    pygame.mixer.Sound.play(INTRO).set_volume(0.75)
    pygame.display.update()
    time.sleep(5.7)                
    SCREEN.fill('White')
LOADING_SCREEN()
class SlikeGumbi:
    def __init__(self, slika, hover_slika, x, y):
        self.slika = slika
        self.hover_slika = hover_slika
        self.poz = (x, y)
        self.slika_rect = self.slika.get_rect(topleft = self.poz)
    def provjeraSudara(self, pozicija_misa):
        if pozicija_misa[0] in range(self.slika_rect.left, self.slika_rect.right) and pozicija_misa[1] in range(self.slika_rect.top, self.slika_rect.bottom):
            return True
        return False
    def crtanjeGumba(self, pozicija_misa):
        if pozicija_misa[0] in range(self.slika_rect.left, self.slika_rect.right) and pozicija_misa[1] in range(self.slika_rect.top, self.slika_rect.bottom):
            SCREEN.blit(self.hover_slika, self.poz)
        else:
            SCREEN.blit(self.slika, self.slika_rect)

#Slike za main ekran
main_background = []
for image in range(3):
    main_background.append(pygame.image.load(os.path.join("Assets", "MainScreen", f"main_bg{image +1 }.png")).convert_alpha())
naslov = pygame.image.load(os.path.join("Assets", "MainScreen", "naslov.png")).convert_alpha()
igraj_gumb = pygame.image.load(os.path.join("Assets", "MainScreen", "igraj_gumb.png")).convert_alpha()
igraj_gumb_hover = pygame.image.load(os.path.join("Assets", "MainScreen", "igraj_gumb_hover.png")).convert_alpha()
postignuca_gumb = pygame.image.load(os.path.join("Assets", "MainScreen", "postignuca_gumb.png")).convert_alpha()
postignuca_gumb_hover = pygame.image.load(os.path.join("Assets", "MainScreen", "postignuca_gumb_hover.png")).convert_alpha()
izadi_gumb = pygame.image.load(os.path.join("Assets", "MainScreen", "izadi_gumb.png")).convert_alpha()
izadi_gumb_hover = pygame.image.load(os.path.join("Assets", "MainScreen", "izadi_gumb_hover.png")).convert_alpha()

#Slike za escape ekran
da_gumb = pygame.image.load(os.path.join("Assets", "EscapeScreen", "da.png")).convert_alpha()
da_gumb_hover = pygame.image.load(os.path.join("Assets", "EscapeScreen", "da_hover.png")).convert_alpha()
ne_gumb = pygame.image.load(os.path.join("Assets", "EscapeScreen", "ne.png")).convert_alpha()
ne_gumb_hover = pygame.image.load(os.path.join("Assets", "EscapeScreen", "ne_hover.png")).convert_alpha()
prozor = pygame.image.load(os.path.join("Assets", "EscapeScreen", "escape_okvir.png")).convert_alpha()

#Slike za achievemente
ACHV_BG = pygame.image.load(os.path.join("Assets", "Achievements", "achievement_bg.png")).convert_alpha()
ACHV_NASLOV = pygame.image.load(os.path.join("Assets", "Achievements", "achievement_naslov.png")).convert_alpha()
A_ACHV = pygame.image.load(os.path.join("Assets", "Achievements", "andrej_achvmnt.png")).convert_alpha()
A_OPIS = pygame.image.load(os.path.join("Assets", "Achievements", "andrej_opis.png")).convert_alpha()
BACK_GUMB_OKVIR = pygame.image.load(os.path.join("Assets", "Achievements", "back_gumb_hover_bijelo.png")).convert_alpha()
BACK_GUMB_HOVER = pygame.image.load(os.path.join("Assets", "Achievements", "back_gumb_hover.png")).convert_alpha()
BACK_GUMB = pygame.image.load(os.path.join("Assets", "Achievements", "back_gumb.png")).convert_alpha()
B_ACHV = pygame.image.load(os.path.join("Assets", "Achievements", "broz_achvmnt.png")).convert_alpha()
B_OPIS = pygame.image.load(os.path.join("Assets", "Achievements", "broz_opis.png")).convert_alpha()
COLLEC_ACHV = pygame.image.load(os.path.join("Assets", "Achievements", "collector_achvmnt.png")).convert_alpha()
COLLEC_OPIS = pygame.image.load(os.path.join("Assets", "Achievements", "collector_opis.png")).convert_alpha()
ONEHP_ACHV = pygame.image.load(os.path.join("Assets", "Achievements", "onehp_achvmnt.png")).convert_alpha()
ONEHP_OPIS = pygame.image.load(os.path.join("Assets", "Achievements", "onehp_opis.png")).convert_alpha()
SEVKE_ACHV = pygame.image.load(os.path.join("Assets", "Achievements", "severina_achvmnt.png")).convert_alpha()
SEVKE_OPIS = pygame.image.load(os.path.join("Assets", "Achievements", "severina_opis.png")).convert_alpha()
SUPER_ACHV = pygame.image.load(os.path.join("Assets", "Achievements", "superhero_achvmnt.png")).convert_alpha()
SUPER_OPIS = pygame.image.load(os.path.join("Assets", "Achievements", "superhero_opis.png")).convert_alpha()
UNKNOWN_ACHV = pygame.image.load(os.path.join("Assets", "Achievements", "unkown_achvmnt.png")).convert_alpha()
UNKNOWN_HOVER = pygame.image.load(os.path.join("Assets", "Achievements", "unkown_achvmnt_hover.png")).convert_alpha()
ZAKLJUCANO = pygame.image.load(os.path.join("Assets", "Achievements", "zakljucano.png")).convert_alpha()
NEPOSTOJI_PROFIL = pygame.image.load(os.path.join("Assets", "Achievements", "nepostoji_profil.png")).convert_alpha()
NEP_IZADJI = pygame.image.load(os.path.join("Assets", "Achievements", "nepostojeci_izadi_gumb.png")).convert_alpha()
NEP_IZADJI_HOVER = pygame.image.load(os.path.join("Assets", "Achievements", "nepostojeci_izadi_gumb_hover.png")).convert_alpha()

#Slike za odabir preseta
preset1_bg = pygame.image.load(os.path.join("Assets", "OdabirPreseta", "background_preset1.png")).convert_alpha()
preset2_bg = pygame.image.load(os.path.join("Assets", "OdabirPreseta", "background_preset2.png")).convert_alpha()
builder_elim = pygame.image.load(os.path.join("Assets", "OdabirPreseta", "builder_pro_eliminiran.png")).convert_alpha()
builder_hover = pygame.image.load(os.path.join("Assets", "OdabirPreseta", "builder_pro_hover.png")).convert_alpha()
builder_gumb = pygame.image.load(os.path.join("Assets", "OdabirPreseta", "builder_pro.png")).convert_alpha()
builder_selekt = pygame.image.load(os.path.join("Assets", "OdabirPreseta", "builder_pro_selektiran.png")).convert_alpha()
builder_info = pygame.image.load(os.path.join("Assets", "OdabirPreseta", "builder_pro_info.png")).convert_alpha()
combat_elim = pygame.image.load(os.path.join("Assets", "OdabirPreseta", "combat_pro_eliminiran.png")).convert_alpha()
combat_hover = pygame.image.load(os.path.join("Assets", "OdabirPreseta", "combat_pro_hover.png")).convert_alpha()
combat_gumb = pygame.image.load(os.path.join("Assets", "OdabirPreseta", "combat_pro.png")).convert_alpha()
combat_selekt = pygame.image.load(os.path.join("Assets", "OdabirPreseta", "combat_pro_selektiran.png")).convert_alpha()
combat_info = pygame.image.load(os.path.join("Assets", "OdabirPreseta", "combat_pro_info.png")).convert_alpha()
old_school_elim = pygame.image.load(os.path.join("Assets", "OdabirPreseta", "old_school_eliminiran.png")).convert_alpha()
old_school_hover = pygame.image.load(os.path.join("Assets", "OdabirPreseta", "old_school_hover.png")).convert_alpha()
old_school_gumb = pygame.image.load(os.path.join("Assets", "OdabirPreseta", "old_school.png")).convert_alpha()
old_school_selekt = pygame.image.load(os.path.join("Assets", "OdabirPreseta", "old_school_selektiran.png")).convert_alpha()
old_school_info = pygame.image.load(os.path.join("Assets", "OdabirPreseta", "old_school_info.png")).convert_alpha()
savjet = pygame.image.load(os.path.join("Assets", "OdabirPreseta", "savjet.png")).convert_alpha()
dalje_hover = pygame.image.load(os.path.join("Assets", "OdabirPreseta", "gumb_dalje_hover.png")).convert_alpha()
dalje_hover_invalid = pygame.image.load(os.path.join("Assets", "OdabirPreseta", "gumb_dalje_hover_invalid.png")).convert_alpha()
dalje_invalid = pygame.image.load(os.path.join("Assets", "OdabirPreseta", "gumb_dalje_invalid.png")).convert_alpha()
dalje = pygame.image.load(os.path.join("Assets", "OdabirPreseta", "gumb_dalje.png")).convert_alpha()

#Slike za odabir heroja
odabir_bg = pygame.image.load(os.path.join("Assets", "OdabirHeroja", "background.png")).convert_alpha()
andrej_gumb_hover = pygame.image.load(os.path.join("Assets", "OdabirHeroja", "andrej_gumb_hover.png")).convert_alpha()
andrej_gumb_selektiran = pygame.image.load(os.path.join("Assets", "OdabirHeroja", "andrej_gumb_selektiran.png")).convert_alpha()
andrej_gumb = pygame.image.load(os.path.join("Assets", "OdabirHeroja", "andrej_gumb.png")).convert_alpha()
andrej_selektiran = pygame.image.load(os.path.join("Assets", "OdabirHeroja", "andrej_selektiran.png")).convert_alpha()
andrej = pygame.image.load(os.path.join("Assets", "OdabirHeroja", "andrej.png")).convert_alpha()
broz_gumb_hover = pygame.image.load(os.path.join("Assets", "OdabirHeroja", "broz_gumb_hover.png")).convert_alpha()
broz_gumb_selektiran = pygame.image.load(os.path.join("Assets", "OdabirHeroja", "broz_gumb_selektiran.png")).convert_alpha()
broz_gumb = pygame.image.load(os.path.join("Assets", "OdabirHeroja", "broz_gumb.png")).convert_alpha()
broz_selektiran = pygame.image.load(os.path.join("Assets", "OdabirHeroja", "broz_selektiran.png")).convert_alpha()
broz = pygame.image.load(os.path.join("Assets", "OdabirHeroja", "broz.png")).convert_alpha()

#Slike za igranje
publika = pygame.image.load(os.path.join("Assets", "Igranje", "background.png")).convert_alpha()
arena = pygame.image.load(os.path.join("Assets", "Igranje", "arena.png")).convert_alpha()
health = pygame.image.load(os.path.join("Assets", "Igranje", "health.png")).convert_alpha()

#Slike za winscreen
bekigrunt = pygame.image.load(os.path.join("Assets", "WinScreen", "background.png")).convert_alpha()
andrew = pygame.image.load(os.path.join("Assets", "WinScreen", "andrejtejt.png")).convert_alpha()
bruce = pygame.image.load(os.path.join("Assets", "WinScreen", "brozli.png")).convert_alpha()


class SpriteRectangle(pygame.sprite.Sprite):
    def __init__(self, color, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))
        self.position = (x, y)
        #self.image = pygame.Surface((width, height))
        #self.image.fill(color)
        self.rect = self.image.get_rect(topleft = self.position)


def flip_image_horizontally(image):
    return pygame.transform.flip(image, True, False)


class Andrej(pygame.sprite.Sprite):
    def __init__(self, igrac):
        super().__init__()

        if igrac == "prvi":
            self.pozicija_borca = "lijevo"
        elif igrac == "drugi":
            self.pozicija_borca = "desno"

        self.borac = "Andrej"

        self.varijable = {"jumping" : False, "crouching" : False, "blocking" : False, "stunned" : False, "defeated" : False, "kicking" : False, "punching" : False, "jumpingpunch" : False, "jumpingkick" : False, "crouchingpunch" : False}

        self.dictionary = {"left":0, "right":0, "up":0, "down":0, "punch":0, "kick":0, "block":0}

        self.rectangles = pygame.sprite.Group()

        self.health = 10
        self.stamina = 5
        self.promjena_stamine = time.time()
        self.udario_u_blok = False

        self.score = 0

        self.udarci = 0
        self.hit = 0
        self.blokirano = 0

        self.pocetak_skoka = False

        self.pocinjen_damage = False
        self.stunned_timer_start = "kreiran eto da postoji"

        self.punch_timer_start = "kreiran eto da postoji"
        self.superman_timer_start = "kreiran eto da postoji"
        self.aperkat_timer_start = "kreiran eto da postoji"
        self.kick_timer_start = "kreiran eto da postoji"
        self.windmill_timer_start = "kreiran eto da postoji"
        self.opcenito_attack_timer_start = "kreiran eto da postoji"

        self.pocetak_skok_animacije = False
        self.hodanje_animacija = False
        self.crouch_hodanje_animacija = False
        self.pocetak_airkick_animacija = False
        self.airkick_animacija = False
        self.pocetak_airpunch_animacija = False
        self.airpunch_animacija = False
        self.pocetak_punch_animacija = False
        self.punch_animacija = False
        self.pocetak_kick_animacija = False
        self.kick_animacija = False
        self.pocetak_crouchpunch_animacija = False
        self.crouchpunch_animacija = False

        self.airkick = []
        self.promjena_airkick = 0
        self.airpunch = []
        self.promjena_airpunch = 0
        self.crouchpunch = []
        self.promjena_crouch_punch = 0
        self.crouchwalk = []
        self.promjena_crouchwalk = 0
        self.idle = []
        self.promjena_idle = 0
        self.jump = []
        self.promjena_jump = 0
        self.kick = []
        self.promjena_kick = 0
        self.punch = []
        self.promjena_punch = 0
        self.walk = []
        self.promjena_walk = 0

        self.skokzvuk=pygame.mixer.Sound(os.path.join("audio","andrej_jump.wav"))
        self.punchzvuk=pygame.mixer.Sound(os.path.join("audio", "andrej_punch.wav"))
        self.kickzvuk=pygame.mixer.Sound(os.path.join("audio", "andrej_kick.wav"))
        self.primakickzvuk=pygame.mixer.Sound(os.path.join("audio", "andrej_prima_punch.wav"))
        self.primaudaracblokzvuk=pygame.mixer.Sound(os.path.join("audio", "andrej blok prima punch.wav"))
        self.mrtavzvuk=pygame.mixer.Sound(os.path.join("audio","andrej mrtav.wav"))
        self.kadapobijedizvuk=pygame.mixer.Sound(os.path.join("audio", "andrej kada pobijedi.wav"))

        if self.pozicija_borca == "lijevo":
            for image in range(3):
                self.airkick.append(pygame.image.load(os.path.join("Assets", "andrej_animacije", "airkick", f"airkick{image + 1}.png")).convert_alpha())
            for image in range(3):
                self.airpunch.append(pygame.image.load(os.path.join("Assets", "andrej_animacije", "airpunch", f"airpunch{image + 1}.png")).convert_alpha())
            for image in range(3):
                self.crouchpunch.append(pygame.image.load(os.path.join("Assets", "andrej_animacije", "crouchpunch", f"crouchpunch{image + 1}.png")).convert_alpha())
            for image in range(2):
                self.crouchwalk.append(pygame.image.load(os.path.join("Assets", "andrej_animacije", "crouchwalk", f"crouchwalk{image + 1}.png")).convert_alpha())
            for image in range(4):
                self.idle.append(pygame.image.load(os.path.join("Assets", "andrej_animacije", "idle", f"idle{image + 1}.png")).convert_alpha())
            for image in range(2):
                self.jump.append(pygame.image.load(os.path.join("Assets", "andrej_animacije", "jump", f"jump{image + 1}.png")).convert_alpha())
            for image in range(4):
                self.kick.append(pygame.image.load(os.path.join("Assets", "andrej_animacije", "kick", f"kick{image + 1}.png")).convert_alpha())
            for image in range(3):
                self.punch.append(pygame.image.load(os.path.join("Assets", "andrej_animacije", "punch", f"punch{image + 1}.png")).convert_alpha())
            for image in range(3):
                self.walk.append(pygame.image.load(os.path.join("Assets", "andrej_animacije", "walk", f"walk{image + 1}.png")).convert_alpha())
            self.block = pygame.image.load(os.path.join("Assets", "andrej_animacije", "block.png")).convert_alpha()
            self.crouch = pygame.image.load(os.path.join("Assets", "andrej_animacije", "crouch.png")).convert_alpha()
            self.fatality = pygame.image.load(os.path.join("Assets", "andrej_animacije", "fatality.png")).convert_alpha()
            self.stun = pygame.image.load(os.path.join("Assets", "andrej_animacije", "stun.png")).convert_alpha()
        elif self.pozicija_borca == "desno":
            for image in range(3):
                self.airkick.append(pygame.transform.flip(pygame.image.load(os.path.join("Assets", "andrej_animacije", "airkick", f"airkick{image + 1}.png")).convert_alpha(), True, False))
            for image in range(3):
                self.airpunch.append(pygame.transform.flip(pygame.image.load(os.path.join("Assets", "andrej_animacije", "airpunch", f"airpunch{image + 1}.png")).convert_alpha(), True, False))
            for image in range(3):
                self.crouchpunch.append(pygame.transform.flip(pygame.image.load(os.path.join("Assets", "andrej_animacije", "crouchpunch", f"crouchpunch{image + 1}.png")).convert_alpha(), True, False))
            for image in range(2):
                self.crouchwalk.append(pygame.transform.flip(pygame.image.load(os.path.join("Assets", "andrej_animacije", "crouchwalk", f"crouchwalk{image + 1}.png")).convert_alpha(), True, False))
            for image in range(4):
                self.idle.append(pygame.transform.flip(pygame.image.load(os.path.join("Assets", "andrej_animacije", "idle", f"idle{image + 1}.png")).convert_alpha(), True, False))
            for image in range(2):
                self.jump.append(pygame.transform.flip(pygame.image.load(os.path.join("Assets", "andrej_animacije", "jump", f"jump{image + 1}.png")).convert_alpha(), True, False))
            for image in range(4):
                self.kick.append(pygame.transform.flip(pygame.image.load(os.path.join("Assets", "andrej_animacije", "kick", f"kick{image + 1}.png")).convert_alpha(), True, False))
            for image in range(3):
                self.punch.append(pygame.transform.flip(pygame.image.load(os.path.join("Assets", "andrej_animacije", "punch", f"punch{image + 1}.png")).convert_alpha(), True, False))
            for image in range(3):
                self.walk.append(pygame.transform.flip(pygame.image.load(os.path.join("Assets", "andrej_animacije", "walk", f"walk{image + 1}.png")).convert_alpha(), True, False))
            self.block = pygame.transform.flip(pygame.image.load(os.path.join("Assets", "andrej_animacije", "block.png")).convert_alpha(), True, False)
            self.crouch = pygame.transform.flip(pygame.image.load(os.path.join("Assets", "andrej_animacije", "crouch.png")).convert_alpha(), True, False)
            self.fatality = pygame.transform.flip(pygame.image.load(os.path.join("Assets", "andrej_animacije", "fatality.png")).convert_alpha(), True, False)
            self.stun = pygame.transform.flip(pygame.image.load(os.path.join("Assets", "andrej_animacije", "stun.png")).convert_alpha(), True, False)


    def resetBeforeGame(self):
        for key in self.varijable:
            self.varijable[key] = False
        self.health = 10
        self.stamina = 5
        if self.pozicija_borca == "lijevo":
            self.baseRectX = 200
            self.baseRectY = 290
        elif self.pozicija_borca == "desno":
            self.baseRectX = 984
            self.baseRectY = 290

    def idleRectangles(self):
        self.rectangles.empty()
        if (self.pozicija_borca == "lijevo" and obrnuto == False) or (self.pozicija_borca == "desno" and obrnuto == True):
            self.headRect = SpriteRectangle("Blue", self.baseRect.topleft[0] + 84, self.baseRect.topleft[1] + 1, 80, 93)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topleft[0] + 22, self.baseRect.topleft[1] + 76, 126, 161)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topleft[0] + 16, self.baseRect.topleft[1] + 85, 182, 119)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topleft[0] + 11, self.baseRect.topleft[1] + 237, 187, 353)
        else:
            self.headRect = SpriteRectangle("Blue", self.baseRect.topright[0] - 164, self.baseRect.topleft[1] + 1, 80, 93)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topright[0] - 148, self.baseRect.topleft[1] + 76, 126, 161)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topright[0] - 198, self.baseRect.topleft[1] + 85, 182, 119)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topright[0] - 198, self.baseRect.topleft[1] + 237, 187, 353)
        self.rectangles.add(self.headRect)
        self.rectangles.add(self.torsoRect)
        self.rectangles.add(self.handsRect)
        self.rectangles.add(self.legsRect)

    def jumpRectangles(self):
        self.rectangles.empty()
        if (self.pozicija_borca == "lijevo" and obrnuto == False) or (self.pozicija_borca == "desno" and obrnuto == True):
            self.headRect = SpriteRectangle("Blue", self.baseRect.topleft[0] + 99, self.baseRect.topleft[1] + 25, 78, 99)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topleft[0] + 24, self.baseRect.topleft[1] + 85, 128, 170)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topleft[0] + 34, self.baseRect.topleft[1] + 110, 151, 123)
            self.leg1Rect = SpriteRectangle("Pink", self.baseRect.topleft[0] + 26, self.baseRect.topleft[1] + 230, 103, 351)
            self.leg2Rect = SpriteRectangle("Purple", self.baseRect.topleft[0] + 120, self.baseRect.topleft[1] + 221, 83, 231)
        else:
            self.headRect = SpriteRectangle("Blue", self.baseRect.topright[0] - 177, self.baseRect.topright[1] + 25, 78, 99)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topright[0] - 152, self.baseRect.topright[1] + 85, 128, 170)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topright[0] - 185, self.baseRect.topright[1] + 110, 151, 123)
            self.leg1Rect = SpriteRectangle("Pink", self.baseRect.topright[0] - 129, self.baseRect.topright[1] + 230, 103, 351)
            self.leg2Rect = SpriteRectangle("Purple", self.baseRect.topright[0] - 203, self.baseRect.topright[1] + 221, 83, 231)
        self.rectangles.add(self.headRect)
        self.rectangles.add(self.torsoRect)
        self.rectangles.add(self.handsRect)
        self.rectangles.add(self.leg1Rect)
        self.rectangles.add(self.leg2Rect)

    def crouchRectangles(self):
        self.rectangles.empty()
        if (self.pozicija_borca == "lijevo" and obrnuto == False) or (self.pozicija_borca == "desno" and obrnuto == True):
            self.headRect = SpriteRectangle("Blue", self.baseRect.topleft[0] + 66, self.baseRect.topleft[1] + 169, 71, 91)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topleft[0] + 18, self.baseRect.topleft[1] + 241, 174, 129)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topleft[0] + 12, self.baseRect.topleft[1] + 369, 217, 221)
        else:
            self.headRect = SpriteRectangle("Blue", self.baseRect.topright[0] - 137, self.baseRect.topleft[1] + 169, 71, 91)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topright[0] - 192, self.baseRect.topleft[1] + 241, 174, 129)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topright[0] - 229, self.baseRect.topleft[1] + 369, 217, 221)
        self.rectangles.add(self.headRect)
        self.rectangles.add(self.handsRect)
        self.rectangles.add(self.legsRect)


    def blockRectangles(self):
        self.rectangles.empty()
        if (self.pozicija_borca == "lijevo" and obrnuto == False) or (self.pozicija_borca == "desno" and obrnuto == True):
            self.headRect = SpriteRectangle("Blue", self.baseRect.topleft[0] + 75, self.baseRect.topleft[1] + 26, 77, 81)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topleft[0] + 30, self.baseRect.topleft[1] + 73, 113, 180)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topleft[0] + 17, self.baseRect.topleft[1] + 250, 163, 336)
            self.blockRect = SpriteRectangle("Cyan", self.baseRect.topleft[0] + 89, self.baseRect.topleft[1] + 52, 84, 221)
        else:
            self.headRect = SpriteRectangle("Blue", self.baseRect.topright[0] - 152, self.baseRect.topleft[1] + 26, 77, 81)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topright[0] - 143, self.baseRect.topleft[1] + 73, 113, 180)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topright[0] - 180, self.baseRect.topleft[1] + 250, 163, 336)
            self.blockRect = SpriteRectangle("Cyan", self.baseRect.topright[0] - 173, self.baseRect.topleft[1] + 52, 84, 221)
        self.rectangles.add(self.headRect)
        self.rectangles.add(self.torsoRect)
        self.rectangles.add(self.legsRect)
        self.rectangles.add(self.blockRect)

    def stunnedRectangles(self):
        self.rectangles.empty()
        if (self.pozicija_borca == "lijevo" and obrnuto == False) or (self.pozicija_borca == "desno" and obrnuto == True):
            self.headRect = SpriteRectangle("Blue", self.baseRect.topleft[0] + 15, self.baseRect.topleft[1] + 9, 76, 73)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topleft[0] + 6, self.baseRect.topleft[1] + 82, 162, 166)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topleft[0] + 20, self.baseRect.topleft[1] + 248, 166, 324)
        else:
            self.headRect = SpriteRectangle("Blue", self.baseRect.topright[0] - 91, self.baseRect.topleft[1] + 9, 76, 73)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topright[0] - 168, self.baseRect.topleft[1] + 82, 162, 166)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topright[0] - 186, self.baseRect.topleft[1] + 248, 166, 324)
        self.rectangles.add(self.headRect)
        self.rectangles.add(self.torsoRect)
        self.rectangles.add(self.legsRect)

    def crouchPunchRectangles(self):
        self.rectangles.empty()
        if (self.pozicija_borca == "lijevo" and obrnuto == False) or (self.pozicija_borca == "desno" and obrnuto == True):
            self.headRect = SpriteRectangle("Blue", self.baseRect.topleft[0] + 108, self.baseRect.topleft[1] + 56, 77, 80)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topleft[0] + 60, self.baseRect.topleft[1] + 111, 132, 163)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topleft[0] + 54, self.baseRect.topleft[1] + 274, 153, 297)
            self.damageRect = SpriteRectangle("Red", self.baseRect.topleft[0] + 167, self.baseRect.topleft[1] + 0, 73, 230)
        else:
            self.headRect = SpriteRectangle("Blue", self.baseRect.topright[0] - 185, self.baseRect.topleft[1] + 56, 77, 80)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topright[0] - 192, self.baseRect.topleft[1] + 111, 132, 163)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topright[0] - 207, self.baseRect.topleft[1] + 274, 153, 297)
            self.damageRect = SpriteRectangle("Red", self.baseRect.topright[0] - 240, self.baseRect.topleft[1] + 0, 73, 230)
        self.rectangles.add(self.headRect)
        self.rectangles.add(self.torsoRect)
        self.rectangles.add(self.legsRect)
        self.rectangles.add(self.damageRect)

    def jumpPunchRectangles(self):
        self.rectangles.empty()
        if (self.pozicija_borca == "lijevo" and obrnuto == False) or (self.pozicija_borca == "desno" and obrnuto == True):
            self.headRect = SpriteRectangle("Blue", self.baseRect.topleft[0] + 127, self.baseRect.topleft[1] + 71, 94, 95)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topleft[0] + 73, self.baseRect.topleft[1] + 117, 107, 174)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topleft[0] + 112, self.baseRect.topleft[1] + 94, 120, 186)
            self.leg1Rect = SpriteRectangle("Pink", self.baseRect.topleft[0] + 38, self.baseRect.topleft[1] + 273, 88, 213)
            self.leg2Rect = SpriteRectangle("Purple", self.baseRect.topleft[0] + 126, self.baseRect.topleft[1] + 272, 66, 83)
            self.damageRect = SpriteRectangle("Red", self.baseRect.topleft[0] + 192, self.baseRect.topleft[1] + 236, 92, 168)
        else:
            self.headRect = SpriteRectangle("Blue", self.baseRect.topright[0] - 221, self.baseRect.topleft[1] + 71, 94, 95)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topright[0] - 180, self.baseRect.topleft[1] + 117, 107, 174)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topright[0] - 232, self.baseRect.topleft[1] + 94, 120, 186)
            self.leg1Rect = SpriteRectangle("Pink", self.baseRect.topright[0] - 126, self.baseRect.topleft[1] + 273, 88, 213)
            self.leg2Rect = SpriteRectangle("Purple", self.baseRect.topright[0] - 192, self.baseRect.topleft[1] + 272, 66, 83)
            self.damageRect = SpriteRectangle("Red", self.baseRect.topright[0] - 284, self.baseRect.topleft[1] + 236, 92, 168)
        self.rectangles.add(self.headRect)
        self.rectangles.add(self.torsoRect)
        self.rectangles.add(self.handsRect)
        self.rectangles.add(self.leg1Rect)
        self.rectangles.add(self.leg2Rect)
        self.rectangles.add(self.damageRect)

    def jumpKickRectangles(self):
        self.rectangles.empty()
        if (self.pozicija_borca == "lijevo" and obrnuto == False) or (self.pozicija_borca == "desno" and obrnuto == True):
            self.headRect = SpriteRectangle("Blue", self.baseRect.topleft[0] + 98, self.baseRect.topleft[1] + 45, 104, 100)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topleft[0] + 47, self.baseRect.topleft[1] + 111, 124, 125)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topleft[0] + 41, self.baseRect.topleft[1] + 121, 165, 106)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topleft[0] + 18, self.baseRect.topleft[1] + 256, 174, 232)
            self.damageRect = SpriteRectangle("Red", self.baseRect.topleft[0] + 192, self.baseRect.topleft[1] + 167, 140, 329)
        else:
            self.headRect = SpriteRectangle("Blue", self.baseRect.topright[0] - 202, self.baseRect.topleft[1] + 45, 104, 100)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topright[0] - 171, self.baseRect.topleft[1] + 111, 124, 125)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topright[0] - 206, self.baseRect.topleft[1] + 121, 165, 106)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topright[0] - 192, self.baseRect.topleft[1] + 256, 174, 232)
            self.damageRect = SpriteRectangle("Red", self.baseRect.topright[0] - 332, self.baseRect.topleft[1] + 167, 140, 329)
        self.rectangles.add(self.headRect)
        self.rectangles.add(self.torsoRect)
        self.rectangles.add(self.handsRect)
        self.rectangles.add(self.legsRect)
        self.rectangles.add(self.damageRect)

    def punchRectangles(self):
        self.rectangles.empty()
        if (self.pozicija_borca == "lijevo" and obrnuto == False) or (self.pozicija_borca == "desno" and obrnuto == True):
            self.headRect = SpriteRectangle("Blue", self.baseRect.topleft[0] + 98, self.baseRect.topleft[1] + 13, 74, 78)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topleft[0] + 45, self.baseRect.topleft[1] + 88, 105, 158)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topleft[0] + 21, self.baseRect.topleft[1] + 91, 256, 49)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topleft[0] + 21, self.baseRect.topleft[1] + 242, 159, 348)
            self.damageRect = SpriteRectangle("Red", self.baseRect.topleft[0] + 268, self.baseRect.topleft[1] + 82, 73, 57)
        else:
            self.headRect = SpriteRectangle("Blue", self.baseRect.topright[0] - 172, self.baseRect.topleft[1] + 13, 74, 78)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topright[0] - 150, self.baseRect.topleft[1] + 88, 105, 158)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topright[0] - 277, self.baseRect.topleft[1] + 91, 256, 49)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topright[0] - 180, self.baseRect.topleft[1] + 242, 159, 348)
            self.damageRect = SpriteRectangle("Red", self.baseRect.topright[0] - 341, self.baseRect.topleft[1] + 82, 73, 57)
        self.rectangles.add(self.headRect)
        self.rectangles.add(self.torsoRect)
        self.rectangles.add(self.handsRect)
        self.rectangles.add(self.legsRect)
        self.rectangles.add(self.damageRect)

    def kickRectangles(self):
        self.rectangles.empty()
        if (self.pozicija_borca == "lijevo" and obrnuto == False) or (self.pozicija_borca == "desno" and obrnuto == True):
            self.headRect = SpriteRectangle("Blue", self.baseRect.topleft[0] + 90, self.baseRect.topleft[1] + 10, 93, 103)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topleft[0] + 42, self.baseRect.topleft[1] + 82, 106, 163)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topleft[0] + 48, self.baseRect.topleft[1] + 104, 181, 105)
            self.leg1Rect = SpriteRectangle("Pink", self.baseRect.topleft[0] + 30, self.baseRect.topleft[1] + 244, 92, 346)
            self.leg2Rect = SpriteRectangle("Purple", self.baseRect.topleft[0] + 121, self.baseRect.topleft[1] + 235, 223, 56)
            self.damageRect = SpriteRectangle("Red", self.baseRect.topleft[0] + 293, self.baseRect.topleft[1] + 210, 76, 105)
        else:
            self.headRect = SpriteRectangle("Blue", self.baseRect.topright[0] - 183, self.baseRect.topleft[1] + 10, 93, 103)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topright[0] - 148, self.baseRect.topleft[1] + 82, 106, 163)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topright[0] - 229, self.baseRect.topleft[1] + 104, 181, 105)
            self.leg1Rect = SpriteRectangle("Pink", self.baseRect.topright[0] - 122, self.baseRect.topleft[1] + 244, 92, 346)
            self.leg2Rect = SpriteRectangle("Purple", self.baseRect.topright[0] - 344, self.baseRect.topleft[1] + 235, 223, 56)
            self.damageRect = SpriteRectangle("Red", self.baseRect.topright[0] - 369, self.baseRect.topleft[1] + 210, 76, 105)
        self.rectangles.add(self.headRect)
        self.rectangles.add(self.torsoRect)
        self.rectangles.add(self.handsRect)
        self.rectangles.add(self.leg1Rect)
        self.rectangles.add(self.leg2Rect)
        self.rectangles.add(self.damageRect)

    def crtanjeRectangleova(self):
        self.rectangles.draw(SCREEN)

    def postavljanjeRectangleova(self):
        self.baseRect = pygame.Rect(self.baseRectX, self.baseRectY, 416, 590)
        if self.varijable["defeated"] == True:
            pass
        elif self.varijable["stunned"] == True:
            self.stunnedRectangles()
        elif self.varijable["blocking"] == True:
            self.blockRectangles()
        elif self.varijable["kicking"] == True:
            self.kickRectangles()
        elif self.varijable["crouchingpunch"] == True:
            self.crouchPunchRectangles()
        elif self.varijable["crouching"] == True:
            self.crouchRectangles()
        elif self.varijable["jumpingpunch"] == True:
            self.jumpPunchRectangles()
        elif self.varijable["jumpingkick"] == True:
            self.jumpKickRectangles()
        elif self.varijable["jumping"] == True:
            self.jumpRectangles()
        elif self.varijable["punching"] == True:
            self.punchRectangles()
        else:
            self.idleRectangles()

    def animacije(self):
        if self.varijable["defeated"] == True:
            SCREEN.blit(self.fatality, (self.baseRectX, self.baseRectY))
        elif self.varijable["stunned"] == True:
            SCREEN.blit(self.stun, (self.baseRectX, self.baseRectY))
        elif self.varijable["blocking"] == True:
            SCREEN.blit(self.block, (self.baseRectX, self.baseRectY))
        elif self.crouchpunch_animacija == True:
            if self.pocetak_crouchpunch_animacija == True:
                self.pocetak_crouchpunch_animacija = False
                self.promjena_crouch_punch = 0
            if self.promjena_crouch_punch >= 2:
                self.promjena_crouch_punch = 2
            else:
                self.promjena_crouch_punch += 0.15
            SCREEN.blit(self.crouchpunch[int(self.promjena_crouch_punch)], (self.baseRectX, self.baseRectY))
        elif self.crouch_hodanje_animacija == True:
            self.promjena_crouchwalk += 0.1
            if self.promjena_crouchwalk > 2:
                self.promjena_crouchwalk = 0
            SCREEN.blit(self.crouchwalk[int(self.promjena_crouchwalk)], (self.baseRectX, self.baseRectY))
        elif self.varijable["crouching"] == True:
            SCREEN.blit(self.crouch, (self.baseRectX, self.baseRectY))
        elif self.airkick_animacija == True:
            if self.pocetak_airkick_animacija == True:
                self.pocetak_airkick_animacija = False
                self.promjena_airkick = 0
            if self.promjena_airkick >= 2:
                self.promjena_airkick = 2
            else:
                self.promjena_airkick += 0.115
            SCREEN.blit(self.airkick[int(self.promjena_airkick)], (self.baseRectX, self.baseRectY))
        elif self.airpunch_animacija == True:
            if self.pocetak_airpunch_animacija == True:
                self.pocetak_airpunch_animacija = False
                self.promjena_airpunch = 0
            if self.promjena_airpunch >= 2:
                self.promjena_airpunch = 2
            else:
                self.promjena_airpunch += 0.17
            SCREEN.blit(self.airpunch[int(self.promjena_airpunch)], (self.baseRectX, self.baseRectY))
        elif self.varijable["jumping"] == True:
            if self.pocetak_skok_animacije == True:
                self.pocetak_skok_animacije = False
                self.promjena_jump = 0
            if self.promjena_jump >= 1:
                self.promjena_jump = 1
            else:
                self.promjena_jump += 0.15
            SCREEN.blit(self.jump[int(self.promjena_jump)], (self.baseRectX, self.baseRectY))
        elif self.kick_animacija == True:
            if self.pocetak_kick_animacija == True:
                self.pocetak_kick_animacija = False
                self.promjena_kick = 0
            if self.promjena_kick >= 3:
                self.promjena_kick = 3
            else:
                self.promjena_kick += 0.1
            SCREEN.blit(self.kick[int(self.promjena_kick)], (self.baseRectX, self.baseRectY))
        elif self.punch_animacija == True:
            if self.pocetak_punch_animacija == True:
                self.pocetak_punch_animacija = False
                self.promjena_punch = 0
            if self.promjena_punch >= 2:
                self.promjena_punch = 2
            else:
                self.promjena_punch += 0.17
            SCREEN.blit(self.punch[int(self.promjena_punch)], (self.baseRectX, self.baseRectY))
        elif self.hodanje_animacija == True:
            self.promjena_walk += 0.1
            if self.promjena_walk > 3:
                self.promjena_walk = 0
            SCREEN.blit(self.walk[int(self.promjena_walk)], (self.baseRectX, self.baseRectY))
        else:
            self.promjena_idle += 0.1
            if self.promjena_idle > 4:
                self.promjena_idle = 0
            SCREEN.blit(self.idle[int(self.promjena_idle)], (self.baseRectX, self.baseRectY))


    def flipanje_slika(self):
        for i in range(len(self.airkick)):
            self.airkick[i] = flip_image_horizontally(self.airkick[i])
        for i in range(len(self.airpunch)):
            self.airpunch[i] = flip_image_horizontally(self.airpunch[i])
        for i in range(len(self.crouchpunch)):
            self.crouchpunch[i] = flip_image_horizontally(self.crouchpunch[i])   
        for i in range(len(self.crouchwalk)):
            self.crouchwalk[i] = flip_image_horizontally(self.crouchwalk[i])
        for i in range(len(self.idle)):
            self.idle[i] = flip_image_horizontally(self.idle[i])
        for i in range(len(self.jump)):
            self.jump[i] = flip_image_horizontally(self.jump[i])
        for i in range(len(self.kick)):
            self.kick[i] = flip_image_horizontally(self.kick[i])
        for i in range(len(self.punch)):
            self.punch[i] = flip_image_horizontally(self.punch[i])
        for i in range(len(self.walk)):
            self.walk[i] = flip_image_horizontally(self.walk[i])
        self.block = flip_image_horizontally(self.block)
        self.crouch = flip_image_horizontally(self.crouch)
        self.fatality = flip_image_horizontally(self.fatality)
        self.stun = flip_image_horizontally(self.stun)


    def gravitacija(self):
        if self.varijable["jumping"] == True:
            if self.pocetak_skoka == True:
                self.deltaY = 22
                self.pocetak_skoka = False
            if self.baseRectY > 290:
                self.baseRectY = 290
                self.varijable["jumping"] = False
            else:
                self.baseRectY -= self.deltaY
                self.deltaY -= 1
        else:
            pass

    def move(self, strana):
        self.smjer = strana
        if self.baseRectX <= 0 and self.smjer == "left":
            pass
        elif self.smjer == "left":
            self.pomak = -9
            self.hodanje_animacija = True
            if self.varijable["crouching"] == True:
                self.pomak = self.pomak/2
                self.crouch_hodanje_animacija = True
            self.baseRectX += self.pomak
        if (self.baseRectX + 416) >= 1600 and self.smjer == "right":
            pass
        elif self.smjer == "right":
            self.pomak = 9
            self.hodanje_animacija = True
            if self.varijable["crouching"] == True:
                self.pomak = self.pomak/2
                self.crouch_hodanje_animacija = True
            self.baseRectX += self.pomak


class Broz(Andrej):
    def __init__(self, igrac):
        super().__init__(igrac)

        if igrac == "prvi":
            self.pozicija_borca = "lijevo"
        elif igrac == "drugi":
            self.pozicija_borca = "desno"

        self.borac = "Broz"

        self.varijable = {"jumping" : False, "crouching" : False, "blocking" : False, "stunned" : False, "defeated" : False, "kicking" : False, "punching" : False, "jumpingpunch" : False, "jumpingkick" : False, "crouchingpunch" : False}

        self.dictionary = {"left":0, "right":0, "up":0, "down":0, "punch":0, "kick":0, "block":0}

        self.rectangles = pygame.sprite.Group()

        self.health = 10
        self.stamina = 5
        self.promjena_stamine = time.time()
        self.udario_u_blok = False

        self.score = 0

        self.udarci = 0
        self.hit = 0
        self.blokirano = 0

        self.pocetak_skoka = False

        self.pocinjen_damage = False
        self.stunned_timer_start = "kreiran eto da postoji"

        self.punch_timer_start = "kreiran eto da postoji"
        self.superman_timer_start = "kreiran eto da postoji"
        self.aperkat_timer_start = "kreiran eto da postoji"
        self.kick_timer_start = "kreiran eto da postoji"
        self.windmill_timer_start = "kreiran eto da postoji"
        self.opcenito_attack_timer_start = "kreiran eto da postoji"

        self.pocetak_skok_animacije = False
        self.hodanje_animacija = False
        self.crouch_hodanje_animacija = False
        self.pocetak_airkick_animacija = False
        self.airkick_animacija = False
        self.pocetak_airpunch_animacija = False
        self.airpunch_animacija = False
        self.pocetak_punch_animacija = False
        self.punch_animacija = False
        self.pocetak_kick_animacija = False
        self.kick_animacija = False
        self.pocetak_crouchpunch_animacija = False
        self.crouchpunch_animacija = False

        self.airkick = []
        self.promjena_airkick = 0
        self.airpunch = []
        self.promjena_airpunch = 0
        self.crouchpunch = []
        self.promjena_crouch_punch = 0
        self.crouchwalk = []
        self.promjena_crouchwalk = 0
        self.idle = []
        self.promjena_idle = 0
        self.kick = []
        self.promjena_kick = 0
        self.punch = []
        self.promjena_punch = 0
        self.walk = []
        self.promjena_walk = 0
        self.skokzvuk=pygame.mixer.Sound(os.path.join("audio","broz li jump.wav"))
        self.punchzvuk=pygame.mixer.Sound(os.path.join("audio", "broz li punch.wav"))
        self.kickzvuk=pygame.mixer.Sound(os.path.join("audio", "broz li kick.wav"))
        self.primakickzvuk=pygame.mixer.Sound(os.path.join("audio", "broz li prima punch.wav"))
        self.primaudaracblokzvuk=pygame.mixer.Sound(os.path.join("audio", "broz li blok prima punch.wav"))
        self.mrtavzvuk=pygame.mixer.Sound(os.path.join("audio","broz li mrtav.wav"))
        self.kadapobijedizvuk=pygame.mixer.Sound(os.path.join("audio", "broz li kada pobijedi.wav"))

        self.promjena_stamine = time.time()

        if self.pozicija_borca == "lijevo":
            for image in range(3):
                self.airkick.append(pygame.image.load(os.path.join("Assets", "brozli", f"jumpkickpunch{image + 1}.png")).convert_alpha())
            for image in range(3):
                self.airpunch.append(pygame.image.load(os.path.join("Assets", "brozli", f"jumpkickpunch{image + 1}.png")).convert_alpha())
            for image in range(2):
                self.crouchwalk.append(pygame.image.load(os.path.join("Assets", "brozli", f"crouchmove{image + 1}.png")).convert_alpha())
            for image in range(2):
                self.idle.append(pygame.image.load(os.path.join("Assets", "brozli", f"idle{image + 1}.png")).convert_alpha())
            for image in range(3):
                self.kick.append(pygame.image.load(os.path.join("Assets", "brozli", f"kick{image + 1}.png")).convert_alpha())
            for image in range(3):
                self.punch.append(pygame.image.load(os.path.join("Assets", "brozli", f"punch{image + 1}.png")).convert_alpha())
            for image in range(2):
                self.walk.append(pygame.image.load(os.path.join("Assets", "brozli", f"move{image + 1}.png")).convert_alpha())
            for image in range(3):
                self.crouchpunch.append(pygame.image.load(os.path.join("Assets", "brozli", f"crouchpunch{image + 1}.png")).convert_alpha())
            self.stun = pygame.image.load(os.path.join("Assets", "brozli", "stunned.png")).convert_alpha()
            self.jump = pygame.image.load(os.path.join("Assets", "brozli", "jump.png")).convert_alpha()
            self.block = pygame.image.load(os.path.join("Assets", "brozli", "blok.png")).convert_alpha()
            self.crouch = pygame.image.load(os.path.join("Assets", "brozli", "crouchmove1.png")).convert_alpha()
            self.fatality = pygame.image.load(os.path.join("Assets", "brozli", "fatality.png")).convert_alpha()
        elif self.pozicija_borca == "desno":
            for image in range(3):
                self.airkick.append(pygame.transform.flip(pygame.image.load(os.path.join("Assets", "brozli", f"jumpkickpunch{image + 1}.png")).convert_alpha(), True, False))
            for image in range(3):
                self.airpunch.append(pygame.transform.flip(pygame.image.load(os.path.join("Assets", "brozli", f"jumpkickpunch{image + 1}.png")).convert_alpha(), True, False))
            for image in range(2):
                self.crouchwalk.append(pygame.transform.flip(pygame.image.load(os.path.join("Assets", "brozli", f"crouchmove{image + 1}.png")).convert_alpha(), True, False))
            for image in range(2):
                self.idle.append(pygame.transform.flip(pygame.image.load(os.path.join("Assets", "brozli", f"idle{image + 1}.png")).convert_alpha(), True, False))
            for image in range(3):
                self.kick.append(pygame.transform.flip(pygame.image.load(os.path.join("Assets", "brozli", f"kick{image + 1}.png")).convert_alpha(), True, False))
            for image in range(3):
                self.punch.append(pygame.transform.flip(pygame.image.load(os.path.join("Assets", "brozli", f"punch{image + 1}.png")).convert_alpha(), True, False))
            for image in range(2):
                self.walk.append(pygame.transform.flip(pygame.image.load(os.path.join("Assets", "brozli", f"move{image + 1}.png")).convert_alpha(), True, False))
            for image in range(3):
                self.crouchpunch.append(pygame.transform.flip(pygame.image.load(os.path.join("Assets", "brozli", f"crouchpunch{image + 1}.png")).convert_alpha(), True, False))
            self.stun = pygame.transform.flip(pygame.image.load(os.path.join("Assets", "brozli", "stunned.png")).convert_alpha(), True, False)
            self.jump = pygame.transform.flip(pygame.image.load(os.path.join("Assets", "brozli", "jump.png")).convert_alpha(), True, False)
            self.block = pygame.transform.flip(pygame.image.load(os.path.join("Assets", "brozli", "blok.png")).convert_alpha(), True, False)
            self.crouch = pygame.transform.flip(pygame.image.load(os.path.join("Assets", "brozli", "crouchmove1.png")).convert_alpha(), True, False)
            self.fatality = pygame.transform.flip(pygame.image.load(os.path.join("Assets", "brozli", "fatality.png")).convert_alpha(), True, False)

    def idleRectangles(self):
        self.rectangles.empty()
        if (self.pozicija_borca == "lijevo" and obrnuto == False) or (self.pozicija_borca == "desno" and obrnuto == True):
            self.headRect = SpriteRectangle("Blue", self.baseRect.topleft[0] + 110, self.baseRect.topleft[1] + 46, 75, 103)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topleft[0] + 76, self.baseRect.topleft[1] + 143, 117, 136)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topleft[0] + 158, self.baseRect.topleft[1] + 152, 178, 88)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topleft[0] + 52, self.baseRect.topleft[1] + 279, 247, 300)
        else:
            self.headRect = SpriteRectangle("Blue", self.baseRect.topright[0] - 185, self.baseRect.topleft[1] + 46, 75, 103)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topright[0] - 193, self.baseRect.topleft[1] + 143, 117, 136)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topright[0] - 336, self.baseRect.topleft[1] + 152, 178, 88)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topright[0] - 299, self.baseRect.topleft[1] + 279, 247, 300)
        self.rectangles.add(self.headRect)
        self.rectangles.add(self.torsoRect)
        self.rectangles.add(self.handsRect)
        self.rectangles.add(self.legsRect)

    def jumpRectangles(self):
        self.rectangles.empty()
        if (self.pozicija_borca == "lijevo" and obrnuto == False) or (self.pozicija_borca == "desno" and obrnuto == True):
            self.headRect = SpriteRectangle("Blue", self.baseRect.topleft[0] + 184, self.baseRect.topleft[1] + 103, 73, 99)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topleft[0] + 75, self.baseRect.topleft[1] + 112, 143, 144)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topleft[0] + 0, self.baseRect.topleft[1] + 129, 75, 108)
            self.leg1Rect = SpriteRectangle("Pink", self.baseRect.topleft[0] + 107, self.baseRect.topleft[1] + 254, 104, 316)
            self.leg2Rect = SpriteRectangle("Pink", self.baseRect.topleft[0] + 211, self.baseRect.topleft[1] + 267, 103, 118)
        else:
            self.headRect = SpriteRectangle("Blue", self.baseRect.topright[0] - 257, self.baseRect.topleft[1] + 103, 73, 99)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topright[0] - 218, self.baseRect.topleft[1] + 112, 143, 144)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topright[0] - 75, self.baseRect.topleft[1] + 129, 75, 108)
            self.leg1Rect = SpriteRectangle("Pink", self.baseRect.topright[0] - 211, self.baseRect.topleft[1] + 254, 104, 316)
            self.leg2Rect = SpriteRectangle("Pink", self.baseRect.topright[0] - 314, self.baseRect.topleft[1] + 267, 103, 118)
        self.rectangles.add(self.headRect)
        self.rectangles.add(self.torsoRect)
        self.rectangles.add(self.handsRect)
        self.rectangles.add(self.leg1Rect)
        self.rectangles.add(self.leg2Rect)
        

    def crouchRectangles(self):
        self.rectangles.empty()
        if (self.pozicija_borca == "lijevo" and obrnuto == False) or (self.pozicija_borca == "desno" and obrnuto == True):
            self.headRect = SpriteRectangle("Blue", self.baseRect.topleft[0] + 141, self.baseRect.topleft[1] + 234, 65, 78)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topleft[0] + 52, self.baseRect.topleft[1] + 296, 135, 106)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topleft[0] + 32, self.baseRect.topleft[1] + 402, 211, 178)
        else:
            self.headRect = SpriteRectangle("Blue", self.baseRect.topright[0] - 206, self.baseRect.topleft[1] + 234, 65, 78)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topright[0] - 187, self.baseRect.topleft[1] + 296, 135, 106)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topright[0] - 243, self.baseRect.topleft[1] + 402, 211, 178)
        self.rectangles.add(self.headRect)
        self.rectangles.add(self.handsRect)
        self.rectangles.add(self.legsRect)


    def blockRectangles(self):
        self.rectangles.empty()
        if (self.pozicija_borca == "lijevo" and obrnuto == False) or (self.pozicija_borca == "desno" and obrnuto == True):
            self.headRect = SpriteRectangle("Blue", self.baseRect.topleft[0] + 120, self.baseRect.topleft[1] + 27, 61, 107)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topleft[0] + 54, self.baseRect.topleft[1] + 94, 130, 127)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topleft[0] + 46, self.baseRect.topleft[1] + 221, 200, 356)
            self.blockRect = SpriteRectangle("Light blue", self.baseRect.topleft[0] + 155, self.baseRect.topleft[1] + 84, 127, 261)
        else:
            self.headRect = SpriteRectangle("Blue", self.baseRect.topright[0] - 181, self.baseRect.topleft[1] + 27, 61, 107)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topright[0] - 184, self.baseRect.topleft[1] + 94, 130, 127)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topright[0] - 246, self.baseRect.topleft[1] + 221, 200, 356)
            self.blockRect = SpriteRectangle("Light blue", self.baseRect.topright[0] - 282, self.baseRect.topleft[1] + 84, 127, 261)
        self.rectangles.add(self.headRect)
        self.rectangles.add(self.torsoRect)
        self.rectangles.add(self.legsRect)
        self.rectangles.add(self.blockRect)

    def stunnedRectangles(self):
        self.rectangles.empty()
        if (self.pozicija_borca == "lijevo" and obrnuto == False) or (self.pozicija_borca == "desno" and obrnuto == True):
            self.headRect = SpriteRectangle("Blue", self.baseRect.topleft[0] + 151, self.baseRect.topleft[1] + 71, 65, 88)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topleft[0] + 70, self.baseRect.topleft[1] + 106, 156, 121)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topleft[0] + 61, self.baseRect.topleft[1] + 227, 165, 341)
        else:
            self.headRect = SpriteRectangle("Blue", self.baseRect.topright[0] - 216, self.baseRect.topleft[1] + 71, 65, 88)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topright[0] - 226, self.baseRect.topleft[1] + 106, 156, 121)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topright[0] - 226, self.baseRect.topleft[1] + 227, 165, 341)
        self.rectangles.add(self.headRect)
        self.rectangles.add(self.torsoRect)
        self.rectangles.add(self.legsRect)

    def crouchPunchRectangles(self):
        self.rectangles.empty()
        if (self.pozicija_borca == "lijevo" and obrnuto == False) or (self.pozicija_borca == "desno" and obrnuto == True):
            self.headRect = SpriteRectangle("Blue", self.baseRect.topleft[0] + 46, self.baseRect.topleft[1] + 378, 78, 67)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topleft[0] + 95, self.baseRect.topleft[1] + 303, 133, 163)
            self.handsRect = SpriteRectangle("Yellow", self.baseRect.topleft[0] + 93, self.baseRect.topleft[1] + 206, 78, 380)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topleft[0] + 177, self.baseRect.topleft[1] + 178, 123, 171)
            self.damageRect = SpriteRectangle("Red", self.baseRect.topleft[0] + 258, self.baseRect.topleft[1] + 98, 99, 144)
        else:
            self.headRect = SpriteRectangle("Blue", self.baseRect.topright[0] - 124, self.baseRect.topleft[1] + 378, 78, 67)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topright[0] - 228, self.baseRect.topleft[1] + 303, 133, 163)
            self.handsRect = SpriteRectangle("Yellow", self.baseRect.topright[0] - 171, self.baseRect.topleft[1] + 206, 78, 380)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topright[0] - 300, self.baseRect.topleft[1] + 178, 123, 171)
            self.damageRect = SpriteRectangle("Red", self.baseRect.topright[0] - 357, self.baseRect.topleft[1] + 98, 99, 144)
        self.rectangles.add(self.headRect)
        self.rectangles.add(self.torsoRect)
        self.rectangles.add(self.handsRect)
        self.rectangles.add(self.legsRect)
        self.rectangles.add(self.damageRect)

    def jumpPunchRectangles(self):
        self.rectangles.empty()
        if (self.pozicija_borca == "lijevo" and obrnuto == False) or (self.pozicija_borca == "desno" and obrnuto == True):
            self.headRect = SpriteRectangle("Blue", self.baseRect.topleft[0] + 81, self.baseRect.topleft[1] + 52, 73, 97)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topleft[0] + 8, self.baseRect.topleft[1] + 99, 99, 141)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topleft[0] + 104, self.baseRect.topleft[1] + 126, 176, 46)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topleft[0] + 17, self.baseRect.topleft[1] + 240, 197, 103)
            self.damageRect = SpriteRectangle("Red", self.baseRect.topleft[0] + 214, self.baseRect.topleft[1] + 242, 160, 110)
        else:
            self.headRect = SpriteRectangle("Blue", self.baseRect.topright[0] - 154, self.baseRect.topleft[1] + 52, 73, 97)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topright[0] - 107, self.baseRect.topleft[1] + 99, 99, 141)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topright[0] - 280, self.baseRect.topleft[1] + 126, 176, 46)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topright[0] - 214, self.baseRect.topleft[1] + 240, 197, 103)
            self.damageRect = SpriteRectangle("Red", self.baseRect.topright[0] - 374, self.baseRect.topleft[1] + 242, 160, 110)
        self.rectangles.add(self.headRect)
        self.rectangles.add(self.torsoRect)
        self.rectangles.add(self.handsRect)
        self.rectangles.add(self.legsRect)
        self.rectangles.add(self.damageRect)

    def jumpKickRectangles(self):
        self.rectangles.empty()
        if (self.pozicija_borca == "lijevo" and obrnuto == False) or (self.pozicija_borca == "desno" and obrnuto == True):
            self.headRect = SpriteRectangle("Blue", self.baseRect.topleft[0] + 81, self.baseRect.topleft[1] + 52, 73, 97)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topleft[0] + 8, self.baseRect.topleft[1] + 99, 99, 141)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topleft[0] + 104, self.baseRect.topleft[1] + 126, 176, 46)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topleft[0] + 17, self.baseRect.topleft[1] + 240, 197, 103)
            self.damageRect = SpriteRectangle("Red", self.baseRect.topleft[0] + 214, self.baseRect.topleft[1] + 242, 160, 110)
        else:
            self.headRect = SpriteRectangle("Blue", self.baseRect.topright[0] - 154, self.baseRect.topleft[1] + 52, 73, 97)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topright[0] - 107, self.baseRect.topleft[1] + 99, 99, 141)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topright[0] - 280, self.baseRect.topleft[1] + 126, 176, 46)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topright[0] - 214, self.baseRect.topleft[1] + 240, 197, 103)
            self.damageRect = SpriteRectangle("Red", self.baseRect.topright[0] - 374, self.baseRect.topleft[1] + 242, 160, 110)
        self.rectangles.add(self.headRect)
        self.rectangles.add(self.torsoRect)
        self.rectangles.add(self.handsRect)
        self.rectangles.add(self.legsRect)
        self.rectangles.add(self.damageRect)

    def punchRectangles(self):
        self.rectangles.empty()
        if (self.pozicija_borca == "lijevo" and obrnuto == False) or (self.pozicija_borca == "desno" and obrnuto == True):
            self.headRect = SpriteRectangle("Blue", self.baseRect.topleft[0] + 167, self.baseRect.topleft[1] + 62, 67, 67)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topleft[0] + 132, self.baseRect.topleft[1] + 125, 86, 173)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topleft[0] + 203, self.baseRect.topleft[1] + 109, 113, 49)
            self.leg1Rect = SpriteRectangle("Green", self.baseRect.topleft[0] + 182, self.baseRect.topleft[1] + 298, 116, 86)
            self.leg2Rect = SpriteRectangle("Pink", self.baseRect.topleft[0] + 294, self.baseRect.topleft[1] + 360, 49, 191)
            self.damageRect = SpriteRectangle("Red", self.baseRect.topleft[0] + 316, self.baseRect.topleft[1] + 102, 62, 53)
        else:
            self.headRect = SpriteRectangle("Blue", self.baseRect.topright[0] - 234, self.baseRect.topleft[1] + 62, 67, 67)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topright[0] - 218, self.baseRect.topleft[1] + 125, 86, 173)
            self.handsRect = SpriteRectangle("Green", self.baseRect.topright[0] - 316, self.baseRect.topleft[1] + 109, 113, 49)
            self.leg1Rect = SpriteRectangle("Green", self.baseRect.topright[0] - 298, self.baseRect.topleft[1] + 298, 116, 86)
            self.leg2Rect = SpriteRectangle("Pink", self.baseRect.topright[0] - 343, self.baseRect.topleft[1] + 360, 49, 191)
            self.damageRect = SpriteRectangle("Red", self.baseRect.topright[0] - 378, self.baseRect.topleft[1] + 102, 62, 53)
        self.rectangles.add(self.headRect)
        self.rectangles.add(self.torsoRect)
        self.rectangles.add(self.handsRect)
        self.rectangles.add(self.leg1Rect)
        self.rectangles.add(self.leg2Rect)
        self.rectangles.add(self.damageRect)

    def kickRectangles(self):
        self.rectangles.empty()
        if (self.pozicija_borca == "lijevo" and obrnuto == False) or (self.pozicija_borca == "desno" and obrnuto == True):
            self.headRect = SpriteRectangle("Blue", self.baseRect.topleft[0] + 5, self.baseRect.topleft[1] + 102, 72, 80)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topleft[0] + 11, self.baseRect.topleft[1] + 136, 134, 132)
            self.leg1Rect = SpriteRectangle("Pink", self.baseRect.topleft[0] + 109, self.baseRect.topleft[1] + 268, 104, 318)
            self.leg2Rect = SpriteRectangle("Pink", self.baseRect.topleft[0] + 147, self.baseRect.topleft[1] + 147, 136, 120)
            self.damageRect = SpriteRectangle("Red", self.baseRect.topleft[0] + 283, self.baseRect.topleft[1] + 81, 100, 116)
        else:
            self.headRect = SpriteRectangle("Blue", self.baseRect.topright[0] - 78, self.baseRect.topleft[1] + 102, 72, 80)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topright[0] - 145, self.baseRect.topleft[1] + 136, 134, 132)
            self.leg1Rect = SpriteRectangle("Pink", self.baseRect.topright[0] - 213, self.baseRect.topleft[1] + 268, 104, 318)
            self.leg2Rect = SpriteRectangle("Pink", self.baseRect.topright[0] - 283, self.baseRect.topleft[1] + 147, 136, 120)
            self.damageRect = SpriteRectangle("Red", self.baseRect.topright[0] - 383, self.baseRect.topleft[1] + 81, 100, 116)
        self.rectangles.add(self.headRect)
        self.rectangles.add(self.torsoRect)
        self.rectangles.add(self.leg1Rect)
        self.rectangles.add(self.leg2Rect)
        self.rectangles.add(self.damageRect)

    def moveRectangles(self):
        self.rectangles.empty()
        if (self.pozicija_borca == "lijevo" and obrnuto == False) or (self.pozicija_borca == "desno" and obrnuto == True):
            self.headRect = SpriteRectangle("Blue", self.baseRect.topleft[0] + 180, self.baseRect.topleft[1] + 35, 65, 85)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topleft[0] + 145, self.baseRect.topleft[1] + 109, 86, 180)
            self.handsRect = SpriteRectangle("Yellow", self.baseRect.topleft[0] + 87, self.baseRect.topleft[1] + 128, 174, 125)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topleft[0] + 17, self.baseRect.topleft[1] + 289, 240, 283)
        else:
            self.headRect = SpriteRectangle("Blue", self.baseRect.topright[0] - 245, self.baseRect.topleft[1] + 35, 65, 85)
            self.torsoRect = SpriteRectangle("Yellow", self.baseRect.topright[0] - 231, self.baseRect.topleft[1] + 109, 86, 180)
            self.handsRect = SpriteRectangle("Yellow", self.baseRect.topright[0] - 261, self.baseRect.topleft[1] + 128, 174, 125)
            self.legsRect = SpriteRectangle("Pink", self.baseRect.topright[0] - 257, self.baseRect.topleft[1] + 289, 240, 283)
        self.rectangles.add(self.headRect)
        self.rectangles.add(self.torsoRect)
        self.rectangles.add(self.handsRect)
        self.rectangles.add(self.legsRect)


    def postavljanjeRectangleova(self):
        self.baseRect = pygame.Rect(self.baseRectX, self.baseRectY, 416, 590)
        if self.varijable["defeated"] == True:
            pass
        elif self.varijable["stunned"] == True:
            self.stunnedRectangles()
        elif self.varijable["blocking"] == True:
            self.blockRectangles()
        elif self.varijable["kicking"] == True:
            self.kickRectangles()
        elif self.varijable["crouchingpunch"] == True:
            self.crouchPunchRectangles()
        elif self.varijable["crouching"] == True:
            self.crouchRectangles()
        elif self.varijable["jumpingpunch"] == True:
            self.jumpPunchRectangles()
        elif self.varijable["jumpingkick"] == True:
            self.jumpKickRectangles()
        elif self.varijable["jumping"] == True:
            self.jumpRectangles()
        elif self.varijable["punching"] == True:
            self.punchRectangles()
        else:
            self.idleRectangles()

    def animacije(self):
        if self.varijable["defeated"] == True:
            SCREEN.blit(self.fatality, (self.baseRectX, self.baseRectY))
        elif self.varijable["stunned"] == True:
            SCREEN.blit(self.stun, (self.baseRectX, self.baseRectY))
        elif self.varijable["blocking"] == True:
            SCREEN.blit(self.block, (self.baseRectX, self.baseRectY))
        elif self.crouchpunch_animacija == True:
            if self.pocetak_crouchpunch_animacija == True:
                self.pocetak_crouchpunch_animacija = False
                self.promjena_crouch_punch = 0
            if self.promjena_crouch_punch >= 2:
                self.promjena_crouch_punch = 2
            else:
                self.promjena_crouch_punch += 0.15
            SCREEN.blit(self.crouchpunch[int(self.promjena_crouch_punch)], (self.baseRectX, self.baseRectY))
        elif self.crouch_hodanje_animacija == True:
            self.promjena_crouchwalk += 0.1
            if self.promjena_crouchwalk > 2:
                self.promjena_crouchwalk = 0
            SCREEN.blit(self.crouchwalk[int(self.promjena_crouchwalk)], (self.baseRectX, self.baseRectY))
        elif self.varijable["crouching"] == True:
            SCREEN.blit(self.crouch, (self.baseRectX, self.baseRectY))
        elif self.airkick_animacija == True:
            if self.pocetak_airkick_animacija == True:
                self.pocetak_airkick_animacija = False
                self.promjena_airkick = 0
            if self.promjena_airkick >= 2:
                self.promjena_airkick = 2
            else:
                self.promjena_airkick += 0.115
            SCREEN.blit(self.airkick[int(self.promjena_airkick)], (self.baseRectX, self.baseRectY))
        elif self.airpunch_animacija == True:
            if self.pocetak_airpunch_animacija == True:
                self.pocetak_airpunch_animacija = False
                self.promjena_airpunch = 0
            if self.promjena_airpunch >= 2:
                self.promjena_airpunch = 2
            else:
                self.promjena_airpunch += 0.115
            SCREEN.blit(self.airpunch[int(self.promjena_airpunch)], (self.baseRectX, self.baseRectY))
        elif self.varijable["jumping"] == True:
            SCREEN.blit(self.jump, (self.baseRectX, self.baseRectY))
        elif self.kick_animacija == True:
            if self.pocetak_kick_animacija == True:
                self.pocetak_kick_animacija = False
                self.promjena_kick = 0
            if self.promjena_kick >= 2:
                self.promjena_kick = 2
            else:
                self.promjena_kick += 0.1
            SCREEN.blit(self.kick[int(self.promjena_kick)], (self.baseRectX, self.baseRectY))
        elif self.punch_animacija == True:
            if self.pocetak_punch_animacija == True:
                self.pocetak_punch_animacija = False
                self.promjena_punch = 0
            if self.promjena_punch >= 2:
                self.promjena_punch = 2
            else:
                self.promjena_punch += 0.17
            SCREEN.blit(self.punch[int(self.promjena_punch)], (self.baseRectX, self.baseRectY))
        elif self.hodanje_animacija == True:
            self.promjena_walk += 0.1
            if self.promjena_walk > 2:
                self.promjena_walk = 0
            self.moveRectangles()
            SCREEN.blit(self.walk[int(self.promjena_walk)], (self.baseRectX, self.baseRectY))
        else:
            self.promjena_idle += 0.1
            if self.promjena_idle > 2:
                self.promjena_idle = 0
            SCREEN.blit(self.idle[int(self.promjena_idle)], (self.baseRectX, self.baseRectY))


    def flipanje_slika(self):
        for i in range(len(self.airkick)):
            self.airkick[i] = flip_image_horizontally(self.airkick[i])
        for i in range(len(self.airpunch)):
            self.airpunch[i] = flip_image_horizontally(self.airpunch[i])
        for i in range(len(self.crouchpunch)):
            self.crouchpunch[i] = flip_image_horizontally(self.crouchpunch[i])   
        for i in range(len(self.crouchwalk)):
            self.crouchwalk[i] = flip_image_horizontally(self.crouchwalk[i])
        for i in range(len(self.idle)):
            self.idle[i] = flip_image_horizontally(self.idle[i])
        for i in range(len(self.kick)):
            self.kick[i] = flip_image_horizontally(self.kick[i])
        for i in range(len(self.punch)):
            self.punch[i] = flip_image_horizontally(self.punch[i])
        for i in range(len(self.walk)):
            self.walk[i] = flip_image_horizontally(self.walk[i])
        self.block = flip_image_horizontally(self.block)
        self.crouch = flip_image_horizontally(self.crouch)
        self.fatality = flip_image_horizontally(self.fatality)
        self.stun = flip_image_horizontally(self.stun)
        self.jump = flip_image_horizontally(self.jump)


def crtanjeHealthaIImena(igrac, pozicija):
    transparent_back = pygame.Surface((406, 46))
    transparent_back.fill("Black")
    transparent_back.set_alpha(100)
    if pozicija == "lijevo":
        x = 30
        ime = selektirani_profili[0]
    elif pozicija == "desno":
        x = 1167
        ime = selektirani_profili[1]
    SCREEN.blit(transparent_back, (x, 52))
    if igrac.health < 4:
        boja = "Red"
    elif igrac.health < 8:
        boja = "Yellow"
    else:
        boja = "Green"
    health_bar = pygame.Surface(((0.1 * igrac.health * 406), 46))
    health_bar.fill(boja)
    SCREEN.blit(health_bar, (x, 52))
    ime_font = pygame.font.Font(None, 40)
    ime_surface = ime_font.render(ime, True, "White")
    ime_rectangle = ime_surface.get_rect(midtop = (x + 203, 5))
    SCREEN.blit(ime_surface, ime_rectangle)
    if igrac.stamina < 0:
        igrac.stamina = 0
    transparent_back = pygame.Surface((406, 22))
    transparent_back.fill("Black")
    transparent_back.set_alpha(100)
    SCREEN.blit(transparent_back, (x, 114))
    stamina_bar = pygame.Surface((((igrac.stamina / 5) * 406), 22))
    stamina_bar.fill("Blue")
    SCREEN.blit(stamina_bar, (x, 114))

def crtanjeRunde(igrac1, igrac2):
    global broj_runde
    runda_font = pygame.font.Font(None, 100)
    runda_surface = runda_font.render(f"Runda {broj_runde}", True, "White")
    runda_rectangle = runda_surface.get_rect(midtop = (WIDTH/2, 5))
    SCREEN.blit(runda_surface, runda_rectangle)
    score_font = pygame.font.Font(None, 40)
    score_surface = score_font.render(f"{igrac1.score}  -  {igrac2.score}", True, "White")
    score_rectangle = score_surface.get_rect(midtop = (WIDTH/2, 70))
    SCREEN.blit(score_surface, score_rectangle)

def provjeraPozicijeZaObrnuto(left, right):
    global obrnuto
    global promjena_obrnuto
    if obrnuto == False:
        if (left.baseRectX - 150) > right.baseRectX:
            obrnuto = True
            promjena_obrnuto = True
    elif obrnuto == True:
        if (right.baseRectX - 150) > left.baseRectX:
            obrnuto = False
            promjena_obrnuto = True

keybind_preset1 = {"left": pygame.K_a, "right" : pygame.K_d, "up" : pygame.K_w, "down" : pygame.K_s, "punch" : pygame.K_LSHIFT, "kick" : pygame.K_LCTRL, "block" : pygame.K_SPACE}
keybind_preset2 = {"left": pygame.K_LEFT, "right" : pygame.K_RIGHT, "up" : pygame.K_UP, "down" : pygame.K_DOWN, "punch" : pygame.K_m, "kick" : pygame.K_n, "block" : pygame.K_b}
keybind_preset3 = {"left": pygame.K_KP4, "right" : pygame.K_KP6, "up" : pygame.K_KP8, "down" : pygame.K_KP5, "punch" : pygame.K_p, "kick" : pygame.K_i, "block" : pygame.K_o}

def provjeraTrajanjaUdaraca(igrac):
    if igrac.varijable["punching"] == True:
        if (time.time() - igrac.punch_timer_start) >= 0.45:
            igrac.varijable["punching"] = False
            igrac.punch_animacija = False
    elif igrac.varijable["jumpingpunch"] == True:
        if (time.time() - igrac.superman_timer_start) >= 0.65:
            igrac.varijable["jumpingpunch"] = False
            igrac.airpunch_animacija = False
    elif igrac.varijable["crouchingpunch"] == True:
        if (time.time() - igrac.aperkat_timer_start) >= 0.57:
            igrac.varijable["crouchingpunch"] = False
            igrac.crouchpunch_animacija = False
    elif igrac.varijable["kicking"] == True:
        if (time.time() - igrac.kick_timer_start) >= 0.6:
            igrac.varijable["kicking"] = False
            igrac.kick_animacija = False
    elif igrac.varijable["jumpingkick"] == True:
        if (time.time() - igrac.windmill_timer_start) >= 0.6:
            igrac.varijable["jumpingkick"] = False
            igrac.airkick_animacija = False

def provjeraCrouchanja(igrac, pritisnuta_tipka, trazena_tipka):
    igrac.varijable["crouching"] = False
    if pritisnuta_tipka[trazena_tipka]:
        if igrac.varijable["jumping"] == True:
            pass
        elif igrac.varijable["defeated"] == True:
            pass
        elif igrac.varijable["stunned"] == True:
            pass
        elif igrac.varijable["punching"] == True:
            pass
        elif igrac.varijable["kicking"] == True:
            pass
        elif igrac.varijable["jumpingpunch"] == True:
            pass
        elif igrac.varijable["jumpingkick"] == True:
            pass
        elif igrac.varijable["crouchingpunch"] == True:
            pass
        else:
            igrac.varijable["crouching"] = True

def provjeraBlokiranja(igrac, pritisnuta_tipka, trazena_tipka):
    igrac.varijable["blocking"] = False
    if pritisnuta_tipka[trazena_tipka]:
        if igrac.varijable["jumping"] == True:
            pass
        elif igrac.varijable["defeated"] == True:
            pass
        elif igrac.varijable["stunned"] == True:
            pass
        elif igrac.varijable["punching"] == True:
            pass
        elif igrac.varijable["kicking"] == True:
            pass
        elif igrac.varijable["jumpingpunch"] == True:
            pass
        elif igrac.varijable["jumpingkick"] == True:
            pass
        elif igrac.varijable["crouchingpunch"] == True:
            pass
        elif igrac.varijable["crouching"] == True:
            pass
        elif igrac.stamina <= 0:
            pass
        else:
            igrac.varijable["blocking"] = True
            igrac.stamina -= 0.01
            igrac.promjena_stamine = time.time()

def provjeraKretanjaIKretanje(igrac, pritisnuta_tipka, tipka_za_lijevo, tipka_za_desno):
    igrac.hodanje_animacija = False
    igrac.crouch_hodanje_animacija = False
    if pritisnuta_tipka[tipka_za_lijevo] and pritisnuta_tipka[tipka_za_desno]:
        pass
    else:
        if pritisnuta_tipka[tipka_za_lijevo]:
            if igrac.varijable["defeated"] == True:
                pass
            elif igrac.varijable["blocking"] == True:
                pass
            else:
                igrac.move("left")
        if pritisnuta_tipka[tipka_za_desno]:
            if igrac.varijable["defeated"] == True:
                pass
            elif igrac.varijable["blocking"] == True:
                pass
            else:
                igrac.move("right")

def provjeraSkokaISkakanje(igrac, pritisnuta_tipka, trazena_tipka):
    if pritisnuta_tipka == trazena_tipka:
        if igrac.varijable["jumping"] == True:
            pass
        elif igrac.varijable["defeated"] == True:
            pass
        elif igrac.varijable["stunned"] == True:
            pass
        elif igrac.varijable["punching"] == True:
            pass
        elif igrac.varijable["kicking"] == True:
            pass
        elif igrac.varijable["jumpingpunch"] == True:
            pass
        elif igrac.varijable["jumpingkick"] == True:
            pass
        elif igrac.varijable["crouchingpunch"] == True:
            pass
        else:
            for key in igrac.varijable:
                igrac.varijable[key] = False
            igrac.varijable["jumping"] = True
            igrac.pocetak_skoka = True
            igrac.pocetak_skok_animacije = True
            pygame.mixer.Sound.play(igrac.skokzvuk)

def provjeraUdarcaIUdaranje(igrac, pritisnuta_tipka, trazena_tipka):
    if pritisnuta_tipka == trazena_tipka:
        if igrac.varijable["punching"] == True:
            pass
        elif igrac.varijable["jumpingpunch"] == True:
            pass
        elif igrac.varijable["jumpingkick"] == True:
            pass
        elif igrac.varijable["crouchingpunch"] == True:
            pass
        elif igrac.varijable["kicking"] == True:
            pass
        elif igrac.varijable["defeated"] == True:
            pass
        elif igrac.varijable["stunned"] == True:
            pass
        elif igrac.varijable["blocking"] == True:
            pass
        elif igrac.stamina < 1:
            pass
        else:
            pygame.mixer.Sound.play(igrac.punchzvuk)
            if igrac.varijable["crouching"] == True:
                igrac.varijable["crouchingpunch"] = True
                igrac.aperkat_timer_start = time.time()
                igrac.pocetak_crouchpunch_animacija = True
                igrac.crouchpunch_animacija = True
                igrac.pocinjen_damage = False
                igrac.opcenito_attack_timer_start = time.time()
            elif igrac.varijable["jumping"] == True:
                igrac.varijable["jumpingpunch"] = True
                igrac.superman_timer_start = time.time()
                igrac.airpunch_animacija = True
                igrac.pocetak_airpunch_animacija = True
                igrac.pocinjen_damage = False
                igrac.opcenito_attack_timer_start = time.time()
            else:
                igrac.varijable["punching"] = True
                igrac.punch_timer_start = time.time()
                igrac.punch_animacija = True
                igrac.pocetak_punch_animacija = True
                igrac.pocinjen_damage = False
                igrac.opcenito_attack_timer_start = time.time()
            igrac.stamina -= 1
            igrac.udarci += 1
            igrac.promjena_stamine = time.time()
            igrac.udario_u_blok = False

def provjeraNogeINogatanje(igrac, pritisnuta_tipka, trazena_tipka):
    if pritisnuta_tipka == trazena_tipka:
        if igrac.varijable["punching"] == True:
            pass
        elif igrac.varijable["jumpingpunch"] == True:
            pass
        elif igrac.varijable["jumpingkick"] == True:
            pass
        elif igrac.varijable["crouchingpunch"] == True:
            pass
        elif igrac.varijable["kicking"] == True:
            pass
        elif igrac.varijable["defeated"] == True:
            pass
        elif igrac.varijable["stunned"] == True:
            pass
        elif igrac.varijable["blocking"] == True:
            pass
        elif igrac.stamina < 1:
            pass
        else:
            pygame.mixer.Sound.play(igrac.kickzvuk)
            if igrac.varijable["jumping"] == True:
                igrac.varijable["jumpingkick"] = True
                igrac.windmill_timer_start = time.time()
                igrac.airkick_animacija = True
                igrac.pocetak_airkick_animacija = True
                igrac.pocinjen_damage = False
                igrac.opcenito_attack_timer_start = time.time()
            else:
                igrac.varijable["kicking"] = True
                igrac.kick_timer_start = time.time()
                igrac.kick_animacija = True
                igrac.pocetak_kick_animacija = True
                igrac.pocinjen_damage = False
                igrac.opcenito_attack_timer_start = time.time()
            igrac.stamina -= 1
            igrac.promjena_stamine = time.time()
            igrac.udario_u_blok = False
            igrac.udarci += 1

def provjeraDamagea(igrac1, igrac2):
    if findDamageRectangle(igrac1) == True:
        if igrac1.pocinjen_damage == True:
            pass
        elif findDamageRectangle(igrac2) == True:
            if pygame.sprite.spritecollide(igrac1.damageRect, igrac2.rectangles, False, pygame.sprite.collide_rect):
                vrijeme = time.time()
                if (vrijeme - igrac1.opcenito_attack_timer_start) >= (vrijeme - igrac2.opcenito_attack_timer_start):
                    igrac2.varijable["stunned"] = True
                    igrac2.stunned_timer_start = time.time()
                    igrac2.health -= 1
                    pygame.mixer.Sound.play(igrac2.primakickzvuk)
                    pygame.mixer.Sound.play(pogodeniudaraczvuk)
                    igrac1.pocinjen_damage = True
            else:
                pass
        elif igrac2.varijable["blocking"] == True:
            if igrac1.udario_u_blok == True:
                pass
            else:
                igrac1.udario_u_blok = True
                igrac2.blokirano += 1
                pygame.mixer.Sound.play(igrac2.primaudaracblokzvuk)
                pygame.mixer.Sound.play(pogodeniudaraczvuk)
                igrac2.stamina -= 0.5
                igrac2.promjena_stamine = time.time()
        elif igrac2.varijable["defeated"] == True:
            pass
        elif pygame.sprite.spritecollide(igrac1.damageRect, igrac2.rectangles, False, pygame.sprite.collide_rect):
            igrac2.varijable["stunned"] = True
            igrac2.stunned_timer_start = time.time()
            pygame.mixer.Sound.play(igrac2.primakickzvuk)
            pygame.mixer.Sound.play(pogodeniudaraczvuk)
            igrac2.health -= 1
            igrac1.pocinjen_damage = True
            igrac1.hit += 1
        else:
            pass
    if findDamageRectangle(igrac2) == True:
        if igrac2.pocinjen_damage == True:
            pass
        elif findDamageRectangle(igrac1) == True:
            if pygame.sprite.spritecollide(igrac2.damageRect, igrac1.rectangles, False, pygame.sprite.collide_rect):
                vrijeme = time.time()
                if (vrijeme - igrac2.opcenito_attack_timer_start) >= (vrijeme - igrac1.opcenito_attack_timer_start):
                    igrac1.varijable["stunned"] = True
                    igrac1.stunned_timer_start = time.time()
                    igrac1.health -= 1
                    pygame.mixer.Sound.play(igrac1.primakickzvuk)
                    pygame.mixer.Sound.play(pogodeniudaraczvuk)
                    igrac2.pocinjen_damage = True
            else:
                pass
        elif igrac1.varijable["blocking"] == True:
            if igrac2.udario_u_blok == True:
                pass
            else:
                igrac2.udario_u_blok = True
                igrac1.blokirano += 1
                igrac1.stamina -= 0.5
                pygame.mixer.Sound.play(igrac1.primaudaracblokzvuk)
                pygame.mixer.Sound.play(pogodeniudaraczvuk)
                igrac1.promjena_stamine = time.time()
        elif igrac1.varijable["defeated"] == True:
            pass
        elif pygame.sprite.spritecollide(igrac2.damageRect, igrac1.rectangles, False, pygame.sprite.collide_rect):
            igrac1.varijable["stunned"] = True
            igrac1.stunned_timer_start = time.time()
            igrac1.health -= 1
            pygame.mixer.Sound.play(igrac1.primakickzvuk)
            pygame.mixer.Sound.play(pogodeniudaraczvuk)
            igrac2.pocinjen_damage = True
            igrac2.hit += 1
        else:
            pass

def provjeraJeLiStunned(igrac):
    if igrac.varijable["stunned"] == True:
        if (time.time() - igrac.stunned_timer_start) >= 0.4:
            igrac.varijable["stunned"] = False
            igrac.airkick_animacija = False
            igrac.airpunch_animacija = False
            igrac.crouchpunch_animacija = False
            igrac.kick_animacija = False
            igrac.punch_animacija = False
            igrac.varijable["punching"] = False
            igrac.varijable["kicking"] = False
            igrac.varijable["jumpingpunch"] = False
            igrac.varijable["jumpingkick"] = False
            igrac.varijable["crouchingpunch"] = False
        else:
            pass
    else:
        pass

def provjeraZaRegeneriranjeStamine(igrac):
    if igrac.stamina >= 5:
        igrac.stamina = 5
    elif (time.time() - igrac.promjena_stamine) < 1.25:
        pass
    else:
        igrac.stamina += 0.08

class Player:
    def __init__(self, ime, Ws, Ls, achievements, profil_broj):
        self.ime = ime                       
        self.Ws = Ws
        self.Ls = Ls
        self.achievements = achievements
        self.profil_broj = profil_broj

IGRACI = []
def read_data():
    global selektirani_profili
    global IGRACI

    with open("Podzemne borbe\profili.txt", 'r') as names_file:
        imena = names_file.read().splitlines()

    with open("Podzemne borbe\score.txt", 'r') as stats_file:
        score_lines = stats_file.read().splitlines()

    with open("Podzemne borbe\Achievements.txt", 'r', encoding="utf-8") as achievements_file:
        achievements_line = achievements_file.readline().strip().split(',')

    for i, (ime, score_line) in enumerate(zip(imena, score_lines), start=1):
        if ime in selektirani_profili:
            ws, ls = map(int, score_line.split(','))
            achievements = achievements_line
            igrac = Player(ime, ws, ls, achievements, i)
            IGRACI.append(igrac)

    return IGRACI

SVI_IGRACI = []
def read_data_sve():
    global SVI_IGRACI

    with open("Podzemne borbe\profili.txt", 'r') as names_file:
        imena = names_file.read().splitlines()

    with open("Podzemne borbe\score.txt", 'r') as stats_file:
        score_lines = stats_file.read().splitlines()

    with open("Podzemne borbe\Achievements.txt", 'r', encoding="utf-8") as achievements_file:
        achievements_line = achievements_file.readline().strip().split(',')

    for i, (ime, score_line) in enumerate(zip(imena, score_lines), start=1):
        if ime != "Napravi profil":
            ws, ls = map(int, score_line.split(','))
            achievements = achievements_line
            igrac = Player(ime, ws, ls, achievements, i)
            SVI_IGRACI.append(igrac)

    return SVI_IGRACI

def poredak():
    global IGRACI, selektirani_profili
    if selektirani_profili[0] == IGRACI[1].ime:
        IGRACI[0], IGRACI[1] = IGRACI[1], IGRACI[0]
    return IGRACI


def update_achievementa(igrac_broj, broj_achievementa):
    with open("Podzemne borbe\Achievements.txt", 'r', encoding="utf-8") as achievements_file:
        lines = achievements_file.read().splitlines()

    line_index = igrac_broj - 1

    if 0 <= line_index < len(lines):
        achievements_line = list(lines[line_index].split(','))
        achievements_line[broj_achievementa - 1] = "da"
        lines[line_index] = ",".join(achievements_line)

        with open("Podzemne borbe\Achievements.txt", 'wt', encoding="utf-8") as achievements_file:
            achievements_file.write("\n".join(lines))

def zadnji_achievement():
    for igrac_broj in range(1,9):
        with open("Podzemne borbe\Achievements.txt", 'r', encoding="utf-8") as achievements_file:
            lines = achievements_file.read().splitlines()

        line_index = igrac_broj - 1

        if 0 <= line_index < len(lines):
            achievements_line = list(lines[line_index].split(','))
            if all(achievement == "da" for achievement in achievements_line[:5]):
                achievements_line[-1] = "da"
                lines[line_index] = ",".join(achievements_line)

        with open("Podzemne borbe\Achievements.txt", 'wt', encoding="utf-8") as achievements_file:
                achievements_file.write("\n".join(lines))
    
def update_score(igrac_broj, wins, losses):
    with open("Podzemne borbe\score.txt", 'r') as score_file:
        lines = score_file.read().splitlines()

    line_index = igrac_broj - 1 

    if 0 <= line_index < len(lines):
        score_line = list(map(int, lines[line_index].split(',')))
        score_line[0] = wins
        score_line[1] = losses
        lines[line_index] = ",".join(map(str, score_line))

        with open("Podzemne borbe\score.txt", 'wt') as score_file:
            score_file.write("\n".join(lines))

#Definira se klasa gumb sa svojim metodama
class Button:
    def __init__(self, text_input, text_size, text_color, rectangle_width_and_height, rectangle_color, rectangle_hovering_color, position):
        #rectangle ispod teksta
        self.rectangle = pygame.Rect((position[0]-(rectangle_width_and_height[0]/2), position[1]-(rectangle_width_and_height[1]/2)), rectangle_width_and_height)
        self.rectangle_color, self.rectangle_hovering_color = rectangle_color, rectangle_hovering_color
        #tekst u gumbu
        self.text_input = text_input
        self.font = pygame.font.Font(None, text_size)
        self.text_surface = self.font.render(text_input, False, text_color)
        self.text_rectangle = self.text_surface.get_rect(center = self.rectangle.center)
        self.player_number = 0
    
    def dodaj(self, IGRAC):
        self.player_number = IGRAC.profil_broj

    def update(self, screen):
        pygame.draw.rect(screen, self.rectangle_color, self.rectangle)
        screen.blit(self.text_surface, self.text_rectangle)

    def checkForCollision(self, mouse_position):
        if mouse_position[0] in range(self.rectangle.left, self.rectangle.right) and mouse_position[1] in range(self.rectangle.top, self.rectangle.bottom):
            return True
        return False
    
    def changeButtonColor(self):
        self.rectangle_color = self.rectangle_hovering_color
        

def escape_screen():
    transparent_background = pygame.Surface((WIDTH, HEIGHT))
    transparent_background.fill("Black")
    transparent_background.set_alpha(120)
    SCREEN.blit(transparent_background, (0,0))

    SCREEN.blit(prozor, (0, 0))
    da = SlikeGumbi(da_gumb, da_gumb_hover, 620, 540)
    ne = SlikeGumbi(ne_gumb, ne_gumb_hover, 815, 540)
    while True:
        SCREEN.blit(prozor, (0, 0))
        mouse_position = pygame.mouse.get_pos()

        for gumb in [da, ne]:
            gumb.crtanjeGumba(mouse_position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if da.provjeraSudara(mouse_position):
                    pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                    return True
                if ne.provjeraSudara(mouse_position):
                    pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                    return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
        pygame.display.update()
        clock.tick(FPS)

#Glavna funkcija koja se počinje vrtjeti čim se program starta i hijerarhijski je najviša
def main():
    global selektirani_profili, IGRACI, PLAYERI_IMENA, PLAYERI_SELEKTIRANI, SVI_IGRACI
    IGRAJ_GUMB = SlikeGumbi(igraj_gumb, igraj_gumb_hover, 200, 293)
    ACHIEVEMENTS_GUMB = SlikeGumbi(postignuca_gumb, postignuca_gumb_hover, 200, 483)
    IZADI_GUMB = SlikeGumbi(izadi_gumb, izadi_gumb_hover, 200, 673)
    promjena = 0
    while True:
        selektirani_profili.clear()
        PLAYERI_SELEKTIRANI.clear()
        PLAYERI_IMENA.clear()
        IGRACI.clear()
        SVI_IGRACI.clear()
        zadnji_achievement()
        SCREEN.fill("Black")
        mouse_position = pygame.mouse.get_pos()
        if promjena >= 2.9:
            promjena = 0
        else:
            promjena += 0.012
        SCREEN.blit(main_background[int(promjena)], (0, 0))
        SCREEN.blit(naslov, (250, 0))
        for gumb in [IGRAJ_GUMB, ACHIEVEMENTS_GUMB, IZADI_GUMB]:
            gumb.crtanjeGumba(mouse_position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.Sound.play(EXIT_GUMB_ZVUK)
                time.sleep(2)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if escape_screen():
                        pygame.mixer.Sound.play(EXIT_GUMB_ZVUK)
                        time.sleep(2)
                        pygame.quit()
                        sys.exit()
                    pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                if IGRAJ_GUMB.provjeraSudara(mouse_position):
                    pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                    if imenovanje_profila():
                        break
                    if biranje_profila():
                        break
                    if odabir_borca1():
                        break
                    if odabir_borca2():
                        break
                    if keybind_screen1():
                        break
                    if keybind_screen2():
                        break
                    if odabir_rundi():
                        break
                    if igranje():
                        break
                    winscreen()
                if ACHIEVEMENTS_GUMB.provjeraSudara(mouse_position):
                    pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                    if postignuca_nema_profila():
                        break
                    if prije_postignuca():
                        break
                    if postignuca():
                        break
                if IZADI_GUMB.provjeraSudara(mouse_position):
                    pygame.mixer.Sound.play(EXIT_GUMB_ZVUK)
                    time.sleep(2)
                    pygame.quit()
                    sys.exit()
        pygame.display.update()
        clock.tick(FPS)

def crtajAchievemente(mouse_pos, player_number):
    with open("Podzemne borbe\Achievements.txt", 'r', encoding="utf-8") as achievements_file:
        achievements_lines = achievements_file.read().splitlines()

    if achievements_lines and player_number - 1 < len(achievements_lines):
        achievements = achievements_lines[player_number - 1].split(',')

        achievements_info = [{"ikona": SEVKE_ACHV, "opis": SEVKE_OPIS},{"ikona": A_ACHV, "opis": A_OPIS},{"ikona": B_ACHV, "opis": B_OPIS},{"ikona": ONEHP_ACHV, "opis": ONEHP_OPIS},{"ikona": SUPER_ACHV, "opis": SUPER_OPIS},{"ikona": COLLEC_ACHV, "opis": COLLEC_OPIS}]

        for i, achievement in enumerate(achievements_info):
            x = 25 if i % 2 == 0 else 850
            y = 170 + (i // 2) * 230

            if achievements[i] == "da":
                SCREEN.blit(achievement["ikona"], (x, y))
                SCREEN.blit(achievement["opis"], (x + 225, y))
            else:
                unknown_achv_gumb = SlikeGumbi(UNKNOWN_ACHV, UNKNOWN_HOVER, x, y)
                unknown_achv_gumb.crtanjeGumba(mouse_pos)
                SCREEN.blit(ZAKLJUCANO, (x + 225, y))

def imali():
    global nema_profila, ima_profila2, ima_profila1, SVI_IGRACI
    read_data_sve()
    ima_profila1 = False
    ima_profila2 = False
    nema_profila = False
    if len(SVI_IGRACI) == 0:
        nema_profila = True
    else:
        ima_profila1 = True
        ima_profila2 = True

    return nema_profila, ima_profila2, ima_profila1

def postignuca_nema_profila():
    global nema_profila, SVI_IGRACI
    SVI_IGRACI.clear()
    imali()
    NEPOSTOJECI_GUMB = SlikeGumbi(NEP_IZADJI, NEP_IZADJI_HOVER, 625, 550)
    while nema_profila == True:
        mouse_position = pygame.mouse.get_pos()
        SCREEN.fill("White")
        SCREEN.blit(ACHV_BG, (0,0))
        SCREEN.blit(NEPOSTOJI_PROFIL, (0,0))
        NEPOSTOJECI_GUMB.crtanjeGumba(mouse_position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.Sound.play(EXIT_GUMB_ZVUK)
                time.sleep(2)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if escape_screen():
                        return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NEPOSTOJECI_GUMB.provjeraSudara(mouse_position):
                    pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                    nema_profila = False
                    
        pygame.display.update()
        clock.tick(FPS)

def draw_buttons():
    global SVI_IGRACI
    buttons = []
    buttons = []
    button_width = 380
    button_height = 120
    button_spacing = 50
    x_offset_increase = 300
    start_position = (900, 200)

    for i, igrac in enumerate(SVI_IGRACI):
        x_offset = -button_width / 2 - button_spacing / 2 - x_offset_increase if i % 2 == 0 else button_spacing / 2 + x_offset_increase
        x = start_position[0] + x_offset
        y = start_position[1] + (i // 2) * (button_height + button_spacing)
        button = Button(f"{igrac.ime}, W{igrac.Ws}-L{igrac.Ls}", 70, "#E1E193", (button_width, button_height), "#0A0A09", "#064719", (x, y))
        button.dodaj(igrac)
        buttons.append(button)

    return buttons

def prije_postignuca():
    global ima_profila1, SVI_IGRACI, broj
    broj = 0
    SVI_IGRACI.clear()
    imali()
    BACK_GUMBIC = SlikeGumbi(BACK_GUMB, BACK_GUMB_HOVER, 10, 10)
    gumbici = draw_buttons()
    naslov_font = pygame.font.Font(None, 100)
    naslov_surface = naslov_font.render("ODABERI PROFIL:", False, "#0A0A09")
    naslov_rectangle = naslov_surface.get_rect(topleft = (150, 20))
    while ima_profila1 == True:
        mouse_position = pygame.mouse.get_pos()
        SCREEN.fill("White")
        SCREEN.blit(ACHV_BG, (0,0))
        SCREEN.blit(naslov_surface, naslov_rectangle)

        for gumb in gumbici:
            gumb.update(SCREEN)

        BACK_GUMBIC.crtanjeGumba(mouse_position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.Sound.play(EXIT_GUMB_ZVUK)
                time.sleep(2)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if escape_screen():
                        return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(SVI_IGRACI)):
                    if gumbici[i].checkForCollision(mouse_position):
                        pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                        broj = gumbici[i].player_number
                        ima_profila1 = False
                if BACK_GUMBIC.provjeraSudara(mouse_position):
                    pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                    ima_profila1 = False
                    return True

        pygame.display.update()
        clock.tick(FPS)

def postignuca():
    global ima_profila2, ima_profila1, SVI_IGRACI, broj
    BACK_GUMBIC = SlikeGumbi(BACK_GUMB, BACK_GUMB_HOVER, 10, 10)
    while ima_profila2 == True:
        mouse_position = pygame.mouse.get_pos()
        SCREEN.fill("White")
        SCREEN.blit(ACHV_BG, (0,0))
        SCREEN.blit(ACHV_NASLOV, (WIDTH/4, 10))

        crtajAchievemente(mouse_position, broj)

        BACK_GUMBIC.crtanjeGumba(mouse_position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.Sound.play(EXIT_GUMB_ZVUK)
                time.sleep(2)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if escape_screen():
                        return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_GUMBIC.provjeraSudara(mouse_position):
                    pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                    ima_profila1 = True
                    ima_profila2 = False
                    

        pygame.display.update()
        clock.tick(FPS)

PLAYERI_SELEKTIRANI = {}
PLAYERI_IMENA = {}
PLAYERI_LISTA_GUMBOVA = []

selektirani_profili = []


imenovanje_profila_bool = True
biranje_profila_bool = True

def imenovanje_profila(): #upisivanje imena igrača/profila za pamćenje rezultata
    global score
    global profili
    global postignucici
    global PLAYERI_IMENA
    global PLAYERI_SELEKTIRANI
    global biranje_profila_bool
    global imenovanje_profila_bool
    global trenutno_ime_upis
    imenovanje_profila_bool = True
    naslov_font = pygame.font.Font(None, 100)
    naslov_surface = naslov_font.render("NAPRAVI PROFIL", False, "#0A0A09")
    naslov_rectangle = naslov_surface.get_rect(topleft = (50, 20))
    trenutno_ime_upis = ""
    with open("Podzemne borbe\profili.txt",encoding="utf-8") as datoteka:
        profili = datoteka.readlines()
    with open("Podzemne borbe\score.txt",encoding="utf-8") as datoteka:
        score = datoteka.readlines()
    with open("Podzemne borbe\Achievements.txt",encoding="utf-8") as datoteka:
        postignucici = datoteka.readlines()
    for i in range(1,9):
        PLAYERI_SELEKTIRANI.update({f"player_{i}":False})
        PLAYERI_IMENA.update({f"player{i}": profili[i-1][:-1]})
    while imenovanje_profila_bool == True:
        SCREEN.fill("#d0d0d0")
        mouse_position = pygame.mouse.get_pos()
        SCREEN.blit(naslov_surface, naslov_rectangle)


        PLAYER_BUTTON1 = Button(PLAYERI_IMENA.get("player1"), 70, "#E1E193", (480, 120), "#0A0A09", "#444443", (350, 175))
        PLAYER_BUTTON2 = Button(PLAYERI_IMENA.get("player2"), 70, "#E1E193", (480, 120), "#0A0A09", "#444443", (350, 175 + 200))
        PLAYER_BUTTON3 = Button(PLAYERI_IMENA.get("player3"), 70, "#E1E193", (480, 120), "#0A0A09", "#444443", (350, 175 + 200*2))
        PLAYER_BUTTON4 = Button(PLAYERI_IMENA.get("player4"), 70, "#E1E193", (480, 120), "#0A0A09", "#444443", (350, 175 + 200*3))
        
        PLAYER_BUTTON5 = Button(PLAYERI_IMENA.get("player5"), 70, "#E1E193", (480, 120), "#0A0A09", "#444443", (1000, 175)) 
        PLAYER_BUTTON6 = Button(PLAYERI_IMENA.get("player6"), 70, "#E1E193", (480, 120), "#0A0A09", "#444443", (1000, 175 + 200))        
        PLAYER_BUTTON7 = Button(PLAYERI_IMENA.get("player7"), 70, "#E1E193", (480, 120), "#0A0A09", "#444443", (1000, 175 + 200*2))
        PLAYER_BUTTON8 = Button(PLAYERI_IMENA.get("player8"), 70, "#E1E193", (480, 120), "#0A0A09", "#444443", (1000, 175 + 200*3))


        PLAYERI_LISTA_GUMBOVA = [PLAYER_BUTTON1,PLAYER_BUTTON2,PLAYER_BUTTON3,PLAYER_BUTTON4,PLAYER_BUTTON5,PLAYER_BUTTON6,PLAYER_BUTTON7,PLAYER_BUTTON8]
        
        
        for gumb in PLAYERI_LISTA_GUMBOVA:
            if gumb.checkForCollision(mouse_position):
                gumb.changeButtonColor()
            gumb.update(SCREEN)                    
        if list(PLAYERI_IMENA.values()).count("Napravi profil") <= 6:
            DALJE_GUMB = Button("Dalje", 70, "#E1E193", (240, 120), "#0A0A09", "#064719", (1425, 775))
        else:
            DALJE_GUMB = Button("Dalje", 70, "#E1E193", (240, 120), "#0A0A09", "#470606", (1425, 775))
        DALJE_GUMB.update(SCREEN)
        if DALJE_GUMB.checkForCollision(mouse_position):
            DALJE_GUMB.changeButtonColor()
        DALJE_GUMB.update(SCREEN)
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.Sound.play(EXIT_GUMB_ZVUK)
                time.sleep(2)
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range (8):
                    PLAYERI_SELEKTIRANI.update({f"player_{i+1}":False})
                    if PLAYERI_IMENA.get(f"player{i+1}") == "":
                        PLAYERI_IMENA.update({f"player{i+1}":"Napravi profil"})
                    if PLAYERI_IMENA.get(f"player{i+1}") + "\n" == profili[i]:
                        pass
                    else:
                        score[i] = "0,0\n"
                        postignucici[i] = "ne,ne,ne,ne,ne,ne\n"
                      
                for i in range(8):
                    
                    if PLAYERI_LISTA_GUMBOVA[i].checkForCollision(mouse_position):
                        pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                        for k in range (8):
                            if PLAYERI_IMENA.get(f"player{k+1}") == "" and PLAYERI_SELEKTIRANI.get(f"player{k+1}") == False:
                                PLAYERI_IMENA.update({f"player{k+1}":"Napravi profil"})
                            PLAYERI_SELEKTIRANI.update({f"player_{k+1}":False})

                        
                        PLAYERI_SELEKTIRANI.update({f"player_{i+1}":True})
                        trenutno_ime_upis = ""                    
                        PLAYERI_IMENA.update({f"player{i+1}":""})
                    if DALJE_GUMB.checkForCollision(mouse_position):
                        pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                        if list(PLAYERI_IMENA.values()).count("Napravi profil") <= 6:
                            if PLAYERI_IMENA.get(f"player{i+1}")+"\n"== profili[i]:
                                pass
                            else:
                                score[i] = "0,0\n"
                                postignucici[i] = "ne,ne,ne,ne,ne,ne\n"
                            
                            with open("Podzemne borbe\profili.txt", encoding="utf-8") as datoteka:
                                profili = []
                                profili = datoteka.readlines()
                                for z in range (8):
                                    profili[z] = PLAYERI_IMENA.get(f"player{z+1}") + "\n"
                            with open("Podzemne borbe\profili.txt","wt",encoding="utf-8",) as datoteka:
                                datoteka.writelines(profili)
                            with open("Podzemne borbe\score.txt","wt",encoding="utf-8",) as datoteka:
                                datoteka.writelines(score)
                            imenovanje_profila_bool = False
                        
                        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if escape_screen():
                        return True

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
    biranje_profila_bool = True
    naslov_font = pygame.font.Font(None, 100)
    naslov_surface = naslov_font.render("ODABIR IGRACA", False, "#0A0A09")
    naslov_rectangle = naslov_surface.get_rect(topleft = (50, 20))

    PLAYER_BUTTON1 = Button(PLAYERI_IMENA.get("player1"), 70, "#E1E193", (480, 120), "#0A0A09", "#064719", (350, 175))
    PLAYER_BUTTON2 = Button(PLAYERI_IMENA.get("player2"), 70, "#E1E193", (480, 120), "#0A0A09", "#064719", (350, 175 + 200))
    PLAYER_BUTTON3 = Button(PLAYERI_IMENA.get("player3"), 70, "#E1E193", (480, 120), "#0A0A09", "#064719", (350, 175 + 200*2))
    PLAYER_BUTTON4 = Button(PLAYERI_IMENA.get("player4"), 70, "#E1E193", (480, 120), "#0A0A09", "#064719", (350, 175 + 200*3))
        
    PLAYER_BUTTON5 = Button(PLAYERI_IMENA.get("player5"), 70, "#E1E193", (480, 120), "#0A0A09", "#064719", (1000, 175)) 
    PLAYER_BUTTON6 = Button(PLAYERI_IMENA.get("player6"), 70, "#E1E193", (480, 120), "#0A0A09", "#064719", (1000, 175 + 200))        
    PLAYER_BUTTON7 = Button(PLAYERI_IMENA.get("player7"), 70, "#E1E193", (480, 120), "#0A0A09", "#064719", (1000, 175 + 200*2))
    PLAYER_BUTTON8 = Button(PLAYERI_IMENA.get("player8"), 70, "#E1E193", (480, 120), "#0A0A09", "#064719", (1000, 175 + 200*3))
  
    
    GUMBOVI_POZICIJE = [(350, 175),(350, 175+200),(350, 175+200*2),((350, 175+200*3)),((1000, 175)),(1000, 175+200),(1000, 175+200*2),(1000, 175+200*3)]
    PLAYERI_LISTA_GUMBOVA=[PLAYER_BUTTON1,PLAYER_BUTTON2,PLAYER_BUTTON3,PLAYER_BUTTON4,PLAYER_BUTTON5,PLAYER_BUTTON6,PLAYER_BUTTON7,PLAYER_BUTTON8]
    GUMBOVI_METAMORFOZA = {PLAYER_BUTTON1:0, PLAYER_BUTTON2:0, PLAYER_BUTTON3:0, PLAYER_BUTTON4:0 ,PLAYER_BUTTON5:0 ,PLAYER_BUTTON6:0 ,PLAYER_BUTTON7:0 ,PLAYER_BUTTON8:0}

    while biranje_profila_bool == True:
        SCREEN.fill('#d0d0d0')
        SCREEN.blit(naslov_surface, naslov_rectangle)
        mouse_position = pygame.mouse.get_pos()
        for gumb in PLAYERI_LISTA_GUMBOVA:
            if GUMBOVI_METAMORFOZA.get(gumb) == 0:
                if PLAYERI_IMENA.get(f"player{PLAYERI_LISTA_GUMBOVA.index(gumb)+1}") == "Napravi profil":
                    gumb = Button("N/A", 70, '#E1E193', (480, 120), '#300000', '#77dd77', GUMBOVI_POZICIJE[PLAYERI_LISTA_GUMBOVA.index(gumb)])
                    gumb.update(SCREEN)         
                else:
                    gumb = Button(PLAYERI_IMENA.get(f"player{PLAYERI_LISTA_GUMBOVA.index(gumb)+1}"), 70, '#E1E193', (480, 120), '#0A0A09', '#444443',GUMBOVI_POZICIJE[PLAYERI_LISTA_GUMBOVA.index(gumb)])
                    gumb.update(SCREEN)
                    if gumb.checkForCollision(mouse_position):
                        gumb.changeButtonColor()
                    gumb.update(SCREEN)
            else:
                gumb = Button(PLAYERI_IMENA.get(f"player{PLAYERI_LISTA_GUMBOVA.index(gumb)+1}"), 70, '#E1E193', (480, 120), '#064719', '#064719',GUMBOVI_POZICIJE[PLAYERI_LISTA_GUMBOVA.index(gumb)])
                gumb.update(SCREEN) 

        DALJE_GUMB = Button("Dalje", 70, "#E1E193", (240, 120), "#0A0A09", "#064719", (1425, 775))        
        DALJE_GUMB.update(SCREEN)
        if DALJE_GUMB.checkForCollision(mouse_position):
            DALJE_GUMB.changeButtonColor()
        DALJE_GUMB.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.Sound.play(EXIT_GUMB_ZVUK)
                time.sleep(2)
                pygame.quit()
                sys.exit()   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if escape_screen():
                        return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if DALJE_GUMB.checkForCollision(mouse_position):
                    pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                    if len(selektirani_profili) == 2:
                        biranje_profila_bool = False
                if len(selektirani_profili) <= 2:
                    for i in range(8):
                        if PLAYERI_LISTA_GUMBOVA[i].checkForCollision(mouse_position):
                            pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
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


BORCI = {"igrac1":0, "igrac2":0}
def odabir_borca1():
    global odabran_borac, andrej_odabran, broz_odabran
    global IGRACI
    global BORCI
    read_data()
    poredak()
    update_achievementa(IGRACI[0].profil_broj, 1)
    update_achievementa(IGRACI[1].profil_broj, 1)
    naslov_font = pygame.font.Font(None, 100)
    naslov_surface = naslov_font.render(f"{selektirani_profili[0]}, izaberi borca!", False, "Black")
    naslov_rectangle = naslov_surface.get_rect(center = (WIDTH/2, 50))
    odabran_borac = False
    andrej_odabran = False
    broz_odabran = False
    run = True
    pygame.mixer.Sound.play(chooseyourcharacterzvuk)
    while run == True:
        SCREEN.fill("Black")
        mouse_position = pygame.mouse.get_pos()
        SCREEN.blit(odabir_bg, (0,0))
        SCREEN.blit(naslov_surface, naslov_rectangle)
        SCREEN.blit(andrej, (0,0))
        SCREEN.blit(broz, (0,0))

        A_GUMB = SlikeGumbi(andrej_gumb, andrej_gumb_hover, 425, 400)
        A_SELEKT_GUMB = SlikeGumbi(andrej_gumb_selektiran, andrej_gumb_selektiran, 425, 400)

        B_GUMB = SlikeGumbi(broz_gumb, broz_gumb_hover, 600, 175)
        B_SELEKT_GUMB = SlikeGumbi(broz_gumb_selektiran, broz_gumb_selektiran, 600, 175)

        DALJE_GUMB = SlikeGumbi(dalje, dalje_hover, 710, 650)
        DALJE_GUMB_NEMOZE = SlikeGumbi(dalje_invalid, dalje_invalid, 710, 650)

        if andrej_odabran:
            A_SELEKT_GUMB.crtanjeGumba(mouse_position)
            SCREEN.blit(andrej_selektiran, (0,0))
        else:
            A_GUMB.crtanjeGumba(mouse_position)
            if A_GUMB.provjeraSudara(mouse_position):
                SCREEN.blit(andrej_selektiran, (0,0))

        if broz_odabran:
            B_SELEKT_GUMB.crtanjeGumba(mouse_position)
            SCREEN.blit(broz_selektiran, (0,0))
        else:
            B_GUMB.crtanjeGumba(mouse_position)
            if B_GUMB.provjeraSudara(mouse_position):
                SCREEN.blit(broz_selektiran, (0,0))

        if odabran_borac == False:
            DALJE_GUMB_NEMOZE.crtanjeGumba(mouse_position)
        else:
            DALJE_GUMB.crtanjeGumba(mouse_position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.Sound.play(EXIT_GUMB_ZVUK)
                time.sleep(2)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if escape_screen():
                        return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if odabran_borac == False:
                    pass
                else:
                    if DALJE_GUMB.provjeraSudara(mouse_position):
                        pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                        run = False
                if A_GUMB.provjeraSudara(mouse_position):
                    pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                    BORCI["igrac1"] = 0
                    odabran_borac = True
                    andrej_odabran = True
                    broz_odabran = False
                    BORCI["igrac1"] = Andrej("prvi")
                if B_GUMB.provjeraSudara(mouse_position):
                    pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                    BORCI["igrac1"] = 0
                    odabran_borac = True
                    andrej_odabran = False
                    broz_odabran = True
                    BORCI["igrac1"] = Broz("prvi")
                
        pygame.display.update()
        clock.tick(FPS)

def odabir_borca2():
    global odabran_borac, andrej_odabran, broz_odabran
    global IGRACI
    global BORCI
    naslov_font = pygame.font.Font(None, 100)
    naslov_surface = naslov_font.render(f"{selektirani_profili[1]}, izaberi borca!", False, "Black")
    naslov_rectangle = naslov_surface.get_rect(center = (WIDTH/2, 50))
    odabran_borac = False
    andrej_odabran = False
    broz_odabran = False
    run = True
    while run == True:
        SCREEN.fill("Black")
        mouse_position = pygame.mouse.get_pos()
        SCREEN.blit(odabir_bg, (0,0))
        SCREEN.blit(naslov_surface, naslov_rectangle)
        SCREEN.blit(andrej, (0,0))
        SCREEN.blit(broz, (0,0))

        A_GUMB = SlikeGumbi(andrej_gumb, andrej_gumb_hover, 425, 400)
        A_SELEKT_GUMB = SlikeGumbi(andrej_gumb_selektiran, andrej_gumb_selektiran, 425, 400)

        B_GUMB = SlikeGumbi(broz_gumb, broz_gumb_hover, 600, 175)
        B_SELEKT_GUMB = SlikeGumbi(broz_gumb_selektiran, broz_gumb_selektiran, 600, 175)

        DALJE_GUMB = SlikeGumbi(dalje, dalje_hover, 710, 650)
        DALJE_GUMB_NEMOZE = SlikeGumbi(dalje_invalid, dalje_invalid, 710, 650)

        if andrej_odabran:
            A_SELEKT_GUMB.crtanjeGumba(mouse_position)
            SCREEN.blit(andrej_selektiran, (0,0))
        else:
            A_GUMB.crtanjeGumba(mouse_position)
            if A_GUMB.provjeraSudara(mouse_position):
                SCREEN.blit(andrej_selektiran, (0,0))

        if broz_odabran:
            B_SELEKT_GUMB.crtanjeGumba(mouse_position)
            SCREEN.blit(broz_selektiran, (0,0))
        else:
            B_GUMB.crtanjeGumba(mouse_position)
            if B_GUMB.provjeraSudara(mouse_position):
                SCREEN.blit(broz_selektiran, (0,0))

        if odabran_borac == False:
            DALJE_GUMB_NEMOZE.crtanjeGumba(mouse_position)
        else:
            DALJE_GUMB.crtanjeGumba(mouse_position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.Sound.play(EXIT_GUMB_ZVUK)
                time.sleep(2)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if escape_screen():
                        return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if odabran_borac == False:
                    pass
                else:
                    if DALJE_GUMB.provjeraSudara(mouse_position):
                        pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                        run = False
                if A_GUMB.provjeraSudara(mouse_position):
                    pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                    BORCI["igrac2"] = 0
                    odabran_borac = True
                    andrej_odabran = True
                    broz_odabran = False
                    BORCI["igrac2"] = Andrej("drugi")
                if B_GUMB.provjeraSudara(mouse_position):
                    pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                    BORCI["igrac2"] = 0
                    odabran_borac = True
                    andrej_odabran = False
                    broz_odabran = True
                    BORCI["igrac2"] = Broz("drugi")
                
        pygame.display.update()
        clock.tick(FPS)

       
        pygame.display.update()
        clock.tick(FPS)

def keybind_screen1():
    global selektirani_profili, odabrano, preset1, preset2, preset3, otprije1, otprije2, otprije3, hover
    global BORCI, IGRACI
    odabrano = False
    preset1 = False
    preset2 = False
    preset3 = False
    otprije1 = False
    otprije2  = False
    otprije3 = False
    hover = False
    naslov_font = pygame.font.Font(None, 100)
    naslov_surface = naslov_font.render(f"{selektirani_profili[0]}, odaberi svoje kontrole ", False, "Black")
    naslov_rectangle = naslov_surface.get_rect(topleft = (10, 10))
    run = True
    print(BORCI["igrac1"].borac)
    print(BORCI["igrac2"].borac)
    if BORCI["igrac1"].borac == "Broz":
        update_achievementa(IGRACI[0].profil_broj, 3)
    else:
        update_achievementa(IGRACI[0].profil_broj, 2)
    if BORCI["igrac2"].borac == "Broz":
        update_achievementa(IGRACI[1].profil_broj, 3)
    else:
        update_achievementa(IGRACI[1].profil_broj, 2)
    while run == True:
        SCREEN.fill("Black")
        mouse_position = pygame.mouse.get_pos()
        SCREEN.blit(preset1_bg, (0,0))
        SCREEN.blit(naslov_surface, naslov_rectangle)
        SCREEN.blit(savjet, (0,0))

        PRESET1 = SlikeGumbi(old_school_gumb, old_school_hover, 80, 750)
        PRESET1_CLICK = SlikeGumbi(old_school_selekt, old_school_selekt, 80, 750)

        PRESET2 = SlikeGumbi(builder_gumb, builder_hover, 580, 750)
        PRESET2_CLICK = SlikeGumbi(builder_selekt, builder_selekt, 580, 750)

        PRESET3 = SlikeGumbi(combat_gumb, combat_hover, 1080, 750)
        PRESET3_CLICK = SlikeGumbi(combat_selekt, combat_selekt, 1080, 750)

        DALJE_GUMB = SlikeGumbi(dalje, dalje_hover, 710, 650)
        DALJE_GUMB_NEMOZE = SlikeGumbi(dalje_invalid, dalje_invalid, 710, 650)

        if odabrano == False:
            DALJE_GUMB_NEMOZE.crtanjeGumba(mouse_position)
        else:
            DALJE_GUMB.crtanjeGumba(mouse_position)

        if preset1 == True and hover == True:
            PRESET1_CLICK.crtanjeGumba(mouse_position)
            hover = False
        elif preset1 == True:
            PRESET1_CLICK.crtanjeGumba(mouse_position)
            SCREEN.blit(old_school_info, (0,0))
        else:
            PRESET1.crtanjeGumba(mouse_position)
            if PRESET1.provjeraSudara(mouse_position):
                SCREEN.blit(old_school_info, (0,0))
                hover = True


        if preset2 == True and hover == True:
            PRESET2_CLICK.crtanjeGumba(mouse_position)
            hover = False
        elif preset2 == True:
            PRESET2_CLICK.crtanjeGumba(mouse_position)
            SCREEN.blit(builder_info, (0,0))
        else:
            PRESET2.crtanjeGumba(mouse_position)
            if PRESET2.provjeraSudara(mouse_position):
                SCREEN.blit(builder_info, (0,0))
                hover = True

        if preset3 == True and hover == True:
            PRESET3_CLICK.crtanjeGumba(mouse_position)
            hover = False
        elif preset3 == True:
            PRESET3_CLICK.crtanjeGumba(mouse_position)
            SCREEN.blit(combat_info, (0,0))
        else:
            PRESET3.crtanjeGumba(mouse_position)
            if PRESET3.provjeraSudara(mouse_position):
                SCREEN.blit(combat_info, (0,0))
                hover = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.Sound.play(EXIT_GUMB_ZVUK)
                time.sleep(2)
                pygame.quit()
                sys.exit()   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if escape_screen():
                        return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if odabrano == False:
                    pass
                else:
                    if DALJE_GUMB.provjeraSudara(mouse_position):
                        pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                        run = False

                if PRESET1.provjeraSudara(mouse_position):
                    pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                    preset1 = True
                    preset2 = False
                    preset3 = False
                    odabrano = True
                    otprije1 = True
                    otprije2 = False
                    otprije3 = False
                    BORCI["igrac1"].dictionary = {key: keybind_preset1[key] for key in BORCI["igrac1"].dictionary}

                if PRESET2.provjeraSudara(mouse_position):
                    pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                    preset1 = False
                    preset3 = False
                    preset2 = True
                    odabrano = True
                    otprije1 = False
                    otprije2 = True
                    otprije3 = False
                    BORCI["igrac1"].dictionary = {key: keybind_preset2[key] for key in BORCI["igrac1"].dictionary}

                if PRESET3.provjeraSudara(mouse_position):
                    pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                    preset3 = True
                    preset1 = False
                    preset2 = False
                    odabrano = True
                    otprije1 = False
                    otprije2 = False
                    otprije3 = True
                    BORCI["igrac1"].dictionary = {key: keybind_preset3[key] for key in BORCI["igrac1"].dictionary}

        pygame.display.update()
        clock.tick(FPS)

def keybind_screen2():
    global selektirani_profili, odabrano, preset1, preset2, preset3, otprije1, otprije2, otprije3, hover
    global BORCI
    odabrano = False
    preset1 = False
    preset2 = False
    preset3 = False
    naslov_font = pygame.font.Font(None, 100)
    naslov_surface = naslov_font.render(f"{selektirani_profili[1]}, odaberi svoje kontrole ", False, "Black")
    naslov_rectangle = naslov_surface.get_rect(topleft = (10, 10))
    run = True
    hover = False
    while run == True:
        SCREEN.fill("Black")
        mouse_position = pygame.mouse.get_pos()
        SCREEN.blit(preset2_bg, (0,0))
        SCREEN.blit(naslov_surface, naslov_rectangle)
        SCREEN.blit(savjet, (0,0))

        PRESET1 = SlikeGumbi(old_school_gumb, old_school_hover, 80, 750)
        PRESET1_CLICK = SlikeGumbi(old_school_selekt, old_school_selekt, 80, 750)
        PRESET1_ELIM = SlikeGumbi(old_school_elim, old_school_elim, 80, 750)

        PRESET2 = SlikeGumbi(builder_gumb, builder_hover, 580, 750)
        PRESET2_CLICK = SlikeGumbi(builder_selekt, builder_selekt, 580, 750)
        PRESET2_ELIM = SlikeGumbi(builder_elim, builder_elim, 580, 750)
        
        PRESET3 = SlikeGumbi(combat_gumb, combat_hover, 1080, 750)
        PRESET3_CLICK = SlikeGumbi(combat_selekt, combat_selekt, 1080, 750)
        PRESET3_ELIM = SlikeGumbi(combat_elim, combat_elim, 1080, 750)

        DALJE_GUMB = SlikeGumbi(dalje, dalje_hover, 710, 650)
        DALJE_GUMB_NEMOZE = SlikeGumbi(dalje_invalid, dalje_invalid, 710, 650)

        if odabrano == False:
            DALJE_GUMB_NEMOZE.crtanjeGumba(mouse_position)
        else:
            DALJE_GUMB.crtanjeGumba(mouse_position)

        if preset1 == True and hover == True:
            PRESET1_CLICK.crtanjeGumba(mouse_position)
            hover = False
        elif preset1 == True:
            PRESET1_CLICK.crtanjeGumba(mouse_position)
            SCREEN.blit(old_school_info, (0,0))
        elif otprije1 == True:
            PRESET1_ELIM.crtanjeGumba(mouse_position)
        else:
            PRESET1.crtanjeGumba(mouse_position)
            if PRESET1.provjeraSudara(mouse_position):
                SCREEN.blit(old_school_info, (0,0))
                hover = True

        if preset2 == True and hover == True:
            PRESET2_CLICK.crtanjeGumba(mouse_position)
            hover = False
        elif preset2 == True:
            PRESET2_CLICK.crtanjeGumba(mouse_position)
            SCREEN.blit(builder_info, (0,0))
        elif otprije2 == True:
            PRESET2_ELIM.crtanjeGumba(mouse_position)
        else:
            PRESET2.crtanjeGumba(mouse_position)
            if PRESET2.provjeraSudara(mouse_position):
                SCREEN.blit(builder_info, (0,0))
                hover = True

        if preset3 == True and hover == True:
            PRESET3_CLICK.crtanjeGumba(mouse_position)
            hover = False
        elif preset3 == True:
            PRESET3_CLICK.crtanjeGumba(mouse_position)
            SCREEN.blit(combat_info, (0,0))
        elif otprije3 == True:
            PRESET3_ELIM.crtanjeGumba(mouse_position)
        else:
            PRESET3.crtanjeGumba(mouse_position)
            if PRESET3.provjeraSudara(mouse_position):
                SCREEN.blit(combat_info, (0,0))
                hover = True


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.Sound.play(EXIT_GUMB_ZVUK)
                time.sleep(2)
                pygame.quit()
                sys.exit()   
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if escape_screen():
                        return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if odabrano == False:
                    pass
                else:
                    if DALJE_GUMB.provjeraSudara(mouse_position):
                        pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                        run = False

                if otprije1 == True:
                    if PRESET1.provjeraSudara(mouse_position):
                        pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                        pass
                else:      
                    if PRESET1.provjeraSudara(mouse_position):
                        odabrano = True
                        preset1 = True
                        preset2 = False
                        preset3 = False
                        BORCI["igrac2"].dictionary = {key: keybind_preset1[key] for key in BORCI["igrac2"].dictionary}
                    
                if otprije2 == True:
                    if PRESET2.provjeraSudara(mouse_position):
                        pass
                else:      
                    if PRESET2.provjeraSudara(mouse_position):
                        pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                        odabrano = True
                        preset1 = False
                        preset2 = True
                        preset3 = False
                        BORCI["igrac2"].dictionary = {key: keybind_preset2[key] for key in BORCI["igrac2"].dictionary}

                if otprije3 == True:
                    if PRESET3.provjeraSudara(mouse_position):
                        pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                        pass
                else:      
                    if PRESET3.provjeraSudara(mouse_position):
                        pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                        preset1 = False
                        preset2 = False
                        preset3 = True
                        odabrano = True
                        BORCI["igrac2"].dictionary = {key: keybind_preset3[key] for key in BORCI["igrac2"].dictionary}                

        pygame.display.update()
        clock.tick(FPS)

def odabir_rundi():
    global broj_rundi
    naslov_font = pygame.font.Font(None, 100)
    naslov_surface = naslov_font.render("Na koliko rundi se igra?", False, "#0A0A09")
    naslov_rectangle = naslov_surface.get_rect(center = (WIDTH/2, 100))
    run = True
    while run == True:
        SCREEN.fill('#d0d0d0')
        mouse_position = pygame.mouse.get_pos()
        JEDNA_GUMB = Button("1", 70, "#E1E193", (220, 120), "#0A0A09", "#064719", (WIDTH/2, 300))
        TRI_GUMB = Button("3", 70, "#E1E193", (220, 120), "#0A0A09", "#064719", (WIDTH/2, 500))
        SEDAM_GUMB = Button("7", 70, "#E1E193", (220, 120), "#0A0A09", "#064719", (WIDTH/2, 700))
        NAZAD_GUMB = Button("Nazad", 35, "#E1E193", (120, 60), "#0A0A09", "#470606", (1500, 50))
        for gumb in [JEDNA_GUMB, SEDAM_GUMB, TRI_GUMB, NAZAD_GUMB]:
            if gumb.checkForCollision(mouse_position):
                gumb.changeButtonColor()
            gumb.update(SCREEN)

        SCREEN.blit(naslov_surface, naslov_rectangle)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.Sound.play(EXIT_GUMB_ZVUK)
                time.sleep(2)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if escape_screen():
                        return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if JEDNA_GUMB.checkForCollision(mouse_position):
                    pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                    run = False
                    broj_rundi = 1
                if TRI_GUMB.checkForCollision(mouse_position):
                    pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                    run = False
                    broj_rundi = 3
                if SEDAM_GUMB.checkForCollision(mouse_position):
                    pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                    run = False
                    broj_rundi = 7
                if NAZAD_GUMB.checkForCollision(mouse_position):
                    pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                    run = False
                    return True
                
        pygame.display.update()
        clock.tick(FPS)

def findDamageRectangle(igrac):
    if igrac.varijable["punching"] == True:
        return True
    elif igrac.varijable["kicking"] == True:
        return True
    elif igrac.varijable["crouchingpunch"] == True:
        return True
    elif igrac.varijable["jumpingpunch"] == True:
        return True
    elif igrac.varijable["jumpingkick"] == True:
        return True
    else:
        return False
    
def provjeraJeLiTkoDefeated(igrac1, igrac2):
    global pocetak_kraja, krajnji_counter
    if (igrac1.health == 0) and (igrac2.health == 1):
        igrac1.varijable["defeated"] = True
        update_achievementa(IGRACI[1].profil_broj, 4)
        if pocetak_kraja == False:
            igrac2.score += 1
            pygame.mixer.Sound.play(igrac1.mrtavzvuk)
            pygame.mixer.Sound.play(igrac2.kadapobijedizvuk)
            pocetak_kraja = True
            krajnji_counter = time.time()
    if (igrac1.health == 0) and (igrac2.health == 10):
        igrac1.varijable["defeated"] = True
        update_achievementa(IGRACI[1].profil_broj, 5)
        if pocetak_kraja == False:
            igrac2.score += 1
            pygame.mixer.Sound.play(igrac1.mrtavzvuk)
            pygame.mixer.Sound.play(igrac2.kadapobijedizvuk)
            pocetak_kraja = True
            krajnji_counter = time.time()
    if igrac1.health == 0:
        igrac1.varijable["defeated"] = True
        if pocetak_kraja == False:
            igrac2.score += 1
            pygame.mixer.Sound.play(igrac1.mrtavzvuk)
            pygame.mixer.Sound.play(igrac2.kadapobijedizvuk)
            pocetak_kraja = True
            krajnji_counter = time.time()
        ime_font = pygame.font.Font(None, 100)
        ime_surface = ime_font.render(f"{selektirani_profili[1]} je pobjedio/la rundu!", True, "White")
        ime_rectangle = ime_surface.get_rect(center = (WIDTH/2, 400))
        SCREEN.blit(ime_surface, ime_rectangle)
        if (time.time() - krajnji_counter) >= 5:
            reset_igre(igrac1, igrac2)
    if (igrac2.health == 0) and (igrac1.health == 1):
        igrac2.varijable["defeated"] = True
        update_achievementa(IGRACI[0].profil_broj, 4)
        if pocetak_kraja == False:
            igrac1.score += 1
            pygame.mixer.Sound.play(igrac2.mrtavzvuk)
            pygame.mixer.Sound.play(igrac1.kadapobijedizvuk)
            pocetak_kraja = True
            krajnji_counter = time.time()
    if (igrac2.health == 0) and (igrac1.health == 10):
        igrac2.varijable["defeated"] = True
        update_achievementa(IGRACI[0].profil_broj, 5)
        if pocetak_kraja == False:
            igrac1.score += 1
            pygame.mixer.Sound.play(igrac2.mrtavzvuk)
            pygame.mixer.Sound.play(igrac1.kadapobijedizvuk)
            pocetak_kraja = True
            krajnji_counter = time.time()
    if igrac2.health == 0:
        igrac2.varijable["defeated"] = True
        if pocetak_kraja == False:
            igrac1.score += 1
            pygame.mixer.Sound.play(igrac2.mrtavzvuk)
            pygame.mixer.Sound.play(igrac1.kadapobijedizvuk)
            pocetak_kraja = True
            krajnji_counter = time.time()
        ime_font = pygame.font.Font(None, 100)
        ime_surface = ime_font.render(f"{selektirani_profili[0]} je pobjedio/la rundu!", True, "White")
        ime_rectangle = ime_surface.get_rect(center = (WIDTH/2, 400))
        SCREEN.blit(ime_surface, ime_rectangle)
        if (time.time() - krajnji_counter) >= 5:
            reset_igre(igrac1, igrac2)

def reset_igre(igrac1, igrac2):
    global kraj_igre, pobjednik, shef, luzer, pocetak_runde, broj_runde, IGRACI, pob_score, luz_score
    if broj_rundi == 1:
        if igrac1.score == 1:
            kraj_igre = True
            pobjednik = selektirani_profili[0]
            shef = BORCI["igrac1"]
            luzer = BORCI["igrac2"]
            IGRACI[0].Ws += 1
            update_score(IGRACI[0].profil_broj, IGRACI[0].Ws, IGRACI[0].Ls)
            IGRACI[1].Ls += 1
            update_score(IGRACI[1].profil_broj, IGRACI[1].Ws, IGRACI[1].Ls)
            pob_score = IGRACI[0]
            luz_score = IGRACI[1]
        elif igrac2.score == 1:
            kraj_igre = True
            pobjednik = selektirani_profili[1]
            shef = BORCI["igrac2"]
            luzer = BORCI["igrac1"]
            IGRACI[1].Ws += 1
            update_score(IGRACI[1].profil_broj, IGRACI[1].Ws, IGRACI[1].Ls)
            IGRACI[0].Ls += 1
            update_score(IGRACI[0].profil_broj, IGRACI[0].Ws, IGRACI[0].Ls)
            pob_score = IGRACI[1]
            luz_score = IGRACI[0]

    elif broj_rundi == 3:
        if igrac1.score == 2:
            kraj_igre = True
            pobjednik = selektirani_profili[0]
            shef = BORCI["igrac1"]
            luzer = BORCI["igrac2"]
            IGRACI[0].Ws += 1
            update_score(IGRACI[0].profil_broj, IGRACI[0].Ws, IGRACI[0].Ls)
            IGRACI[1].Ls += 1
            update_score(IGRACI[1].profil_broj, IGRACI[1].Ws, IGRACI[1].Ls)
            pob_score = IGRACI[0]
            luz_score = IGRACI[1]
        elif igrac2.score == 2:
            kraj_igre = True
            pobjednik = selektirani_profili[1]
            shef = BORCI["igrac2"]
            luzer = BORCI["igrac1"]
            IGRACI[1].Ws += 1
            update_score(IGRACI[1].profil_broj, IGRACI[1].Ws, IGRACI[1].Ls)
            IGRACI[0].Ls += 1
            update_score(IGRACI[0].profil_broj, IGRACI[0].Ws, IGRACI[0].Ls)
            pob_score = IGRACI[1]
            luz_score = IGRACI[0]
        else:
            broj_runde += 1
            pocetak_runde = True
    elif broj_rundi == 7:
        if igrac1.score == 4:
            kraj_igre = True
            pobjednik = selektirani_profili[0]
            shef = BORCI["igrac1"]
            luzer = BORCI["igrac2"]
            IGRACI[0].Ws += 1
            update_score(IGRACI[0].profil_broj, IGRACI[0].Ws, IGRACI[0].Ls)
            IGRACI[1].Ls += 1
            update_score(IGRACI[1].profil_broj, IGRACI[1].Ws, IGRACI[1].Ls)
            pob_score = IGRACI[0]
            luz_score = IGRACI[1]
        elif igrac2.score == 4:
            kraj_igre = True
            pobjednik = selektirani_profili[1]
            shef = BORCI["igrac2"]
            luzer = BORCI["igrac1"]
            IGRACI[1].Ws += 1
            update_score(IGRACI[1].profil_broj, IGRACI[1].Ws, IGRACI[1].Ls)
            IGRACI[0].Ls += 1
            update_score(IGRACI[0].profil_broj, IGRACI[0].Ws, IGRACI[0].Ls)
            pob_score = IGRACI[1]
            luz_score = IGRACI[0]
        else:
            broj_runde += 1
            pocetak_runde = True
    

#Funkcija u kojoj se odvija sama igra
def igranje():
    global BORCI
    global IGRACI
    global promjena_obrnuto, obrnuto
    global pocetak_kraja, kraj_igre, pocetak_runde, broj_runde
    pocetak_runde = True
    igranje = True
    obrnuto = False
    promjena_obrnuto = False
    kraj_igre = False
    broj_runde = 1
    BORCI["igrac1"].score = 0
    BORCI["igrac2"].score = 0
    while igranje:
        SCREEN.fill("Black")
        pygame.mouse.set_visible(False)
        SCREEN.blit(publika, (0, 0))
        SCREEN.blit(arena, (0, 0))
        if pocetak_runde == True:
            pocetak_kraja = False
            BORCI["igrac1"].resetBeforeGame()
            BORCI["igrac2"].resetBeforeGame()
            pocetak_runde = False

        provjeraJeLiTkoDefeated(BORCI["igrac1"], BORCI["igrac2"])
        if kraj_igre == True:
            return
        
        provjeraZaRegeneriranjeStamine(BORCI["igrac1"])
        provjeraZaRegeneriranjeStamine(BORCI["igrac2"])

        BORCI["igrac1"].gravitacija()
        BORCI["igrac2"].gravitacija()

        provjeraPozicijeZaObrnuto(BORCI["igrac1"], BORCI["igrac2"])

        if promjena_obrnuto == True:
            promjena_obrnuto = False
            BORCI["igrac1"].flipanje_slika()
            BORCI["igrac2"].flipanje_slika()

        provjeraJeLiStunned(BORCI["igrac1"])
        provjeraJeLiStunned(BORCI["igrac2"])

        provjeraTrajanjaUdaraca(BORCI["igrac1"])
        provjeraTrajanjaUdaraca(BORCI["igrac2"])
            
        BORCI["igrac1"].postavljanjeRectangleova()
        BORCI["igrac2"].postavljanjeRectangleova()

        BORCI["igrac1"].crtanjeRectangleova()
        BORCI["igrac2"].crtanjeRectangleova()

        BORCI["igrac1"].animacije()
        BORCI["igrac2"].animacije()

        provjeraDamagea(BORCI["igrac1"], BORCI["igrac2"])

        crtanjeHealthaIImena(BORCI["igrac1"], "lijevo")
        crtanjeHealthaIImena(BORCI["igrac2"], "desno")
        SCREEN.blit(health, (0, 0))
        crtanjeRunde(BORCI["igrac1"], BORCI["igrac2"])

        keys_pressed = pygame.key.get_pressed()

        provjeraCrouchanja(BORCI["igrac1"], keys_pressed, BORCI["igrac1"].dictionary["down"])
        provjeraBlokiranja(BORCI["igrac1"], keys_pressed, BORCI["igrac1"].dictionary["block"])
        provjeraKretanjaIKretanje(BORCI["igrac1"], keys_pressed, BORCI["igrac1"].dictionary["left"], BORCI["igrac1"].dictionary["right"])

        provjeraCrouchanja(BORCI["igrac2"], keys_pressed, BORCI["igrac2"].dictionary["down"])
        provjeraBlokiranja(BORCI["igrac2"], keys_pressed, BORCI["igrac2"].dictionary["block"])
        provjeraKretanjaIKretanje(BORCI["igrac2"], keys_pressed, BORCI["igrac2"].dictionary["left"], BORCI["igrac2"].dictionary["right"])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.Sound.play(EXIT_GUMB_ZVUK)
                time.sleep(2)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                pritisnuto = event.key
                if event.key == pygame.K_ESCAPE:
                    pygame.mouse.set_visible(True)
                    if escape_screen():
                        igranje = False
                        return True
                    
                provjeraSkokaISkakanje(BORCI["igrac1"], pritisnuto, BORCI["igrac1"].dictionary["up"])
                provjeraUdarcaIUdaranje(BORCI["igrac1"], pritisnuto, BORCI["igrac1"].dictionary["punch"])
                provjeraNogeINogatanje(BORCI["igrac1"], pritisnuto, BORCI["igrac1"].dictionary["kick"])

                provjeraSkokaISkakanje(BORCI["igrac2"], pritisnuto, BORCI["igrac2"].dictionary["up"])
                provjeraUdarcaIUdaranje(BORCI["igrac2"], pritisnuto, BORCI["igrac2"].dictionary["punch"])
                provjeraNogeINogatanje(BORCI["igrac2"], pritisnuto, BORCI["igrac2"].dictionary["kick"])


        pygame.display.update()
        clock.tick(FPS)

def winscreen():
    global pobjednik, shef, luzer, pob_score, luz_score
    pygame.mouse.set_visible(True)
    naslov_font = pygame.font.Font(None, 110)
    naslov_surface = naslov_font.render(f"{pobjednik} je ultimativni pobjednik/ca!!!", False, "Black")
    naslov_rectangle = naslov_surface.get_rect(center = (WIDTH/2, 50))
    stats_font = pygame.font.Font(None, 70)
    wrunde = stats_font.render(f"{shef.score}", False, "Black")
    wrunde_rect = wrunde.get_rect(center = (830, 330))
    wudarci = stats_font.render(f"{shef.udarci}", False, "Black")
    wudarci_rect = wudarci.get_rect(center = (815, 410))
    wpostotak = stats_font.render(f"{int(shef.hit / shef.udarci * 100)}%", False, "Black")
    wpostotak_rect = wpostotak.get_rect(center = (830, 497))
    wblokirano = stats_font.render(f"{shef.blokirano}", False, "Black")
    wblokirano_rect = wblokirano.get_rect(center = (830, 582))
    wvinluz = stats_font.render(f"{pob_score.Ws}W - {pob_score.Ls}L", "False", "Black")
    wvinluz_rect = wvinluz.get_rect(center = (797, 670))
    lrunde = stats_font.render(f"{luzer.score}", False, "Black")
    lrunde_rect = lrunde.get_rect(center = (1330, 325))
    ludarci = stats_font.render(f"{luzer.udarci}", False, "Black")
    ludarci_rect = ludarci.get_rect(center = (1345, 402))
    try:
        postotak_value = int(luzer.hit / luzer.udarci * 100)
    except ZeroDivisionError:
        postotak_value = 0 
    lpostotak = stats_font.render(f"{postotak_value}%", False, "Black")
    lpostotak_rect = lpostotak.get_rect(center = (1353, 485))
    lblokirano = stats_font.render(f"{luzer.blokirano}", False, "Black")
    lblokirano_rect = lblokirano.get_rect(center = (1335, 582))
    lvinluz = stats_font.render(f"{luz_score.Ws}W - {luz_score.Ls}L", False, "Black")
    lvinluz_rect = lvinluz.get_rect(center = (1390, 657))
    dalje_botun = SlikeGumbi(dalje, dalje_hover, 1420, 750)
    run = True
    while run == True:
        mouse_position = pygame.mouse.get_pos()
        SCREEN.blit(bekigrunt, (0, 0))
        if isinstance(shef, Broz):
            SCREEN.blit(bruce, (0, 0))
        else:
            SCREEN.blit(andrew, (0, 0))
        SCREEN.blit(naslov_surface, naslov_rectangle)
        SCREEN.blit(wrunde, wrunde_rect)
        SCREEN.blit(wudarci, wudarci_rect)
        SCREEN.blit(wpostotak, wpostotak_rect)
        SCREEN.blit(wblokirano, wblokirano_rect)
        SCREEN.blit(wvinluz, wvinluz_rect)
        SCREEN.blit(lrunde, lrunde_rect)
        SCREEN.blit(ludarci, ludarci_rect)
        SCREEN.blit(lpostotak, lpostotak_rect)
        SCREEN.blit(lblokirano, lblokirano_rect)
        SCREEN.blit(lvinluz, lvinluz_rect)
        dalje_botun.crtanjeGumba(mouse_position)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.Sound.play(EXIT_GUMB_ZVUK)
                time.sleep(2)
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if escape_screen():
                        return
            if event.type == pygame.MOUSEBUTTONDOWN:
                if dalje_botun.provjeraSudara(mouse_position):
                    pygame.mixer.Sound.play(KLIK_GUMB_ZVUK)
                    return

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()