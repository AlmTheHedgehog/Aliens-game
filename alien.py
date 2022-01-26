'''Pygame Goats and Wolves

by AlmTheHedgehog - Tymofii Bereznytskyi
'''
import pygame
import sys
from pygame.display import set_mode
from random import randint

#palette
BLACK = (0, 0, 0)
WHITE = (137, 186, 242)
GREEN = (14, 142, 44)
BLUE = (0, 0, 205)
RED = (220, 20, 60)
YELLOW = (255, 133, 40)
#Constances
SCR_WIDTH = 1280
SCR_HEIGHT = 720
GAME_SPEED = 10   #seconds between diff changes 30-standart                !!CHANGE!!

#Var
cur_scr = 0  #current screen
player_win = False  #True when player win
actors_list = []  #list of actors
timer = 0  #timer for speed control
creating_timer_zero = 0  #timer for enemies creating
start_timer_zero = 0  #time of game start, add boss killing time
supply_timer_zero = 0  #timer for sullpy
boss_on_field = False  #True if boss on field
supply_on_field = False  #True if supply on field
boss_killing_time = 0 #time which was spent on killing
killed_en = 0  #number of killed enemies
killed_bosses = 0  #number of killed bosses


#functions
def game_start(skin):
    """Variables refresh
    Param: skin for main actor
    """
    global player_win, main_actor, actors_list, killed_bosses,\
        killed_en, creating_timer_zero, start_timer_zero,\
        boss_on_field, boss_killing_time, supply_on_field
    for act in actors_list:
        del act
    player_win = False
    killed_en = 0 
    killed_bosses = 0
    boss_killing_time = 0
    boss_on_field = False
    supply_on_field = False
    creating_timer_zero = pygame.time.get_ticks()//1000
    start_timer_zero = pygame.time.get_ticks()//1000
    main_actor = m_actor([(SCR_WIDTH/2)-40, SCR_HEIGHT-10], skin)
    actors_list = [main_actor]

def info_scr_event_processing():
    """information screen event processing"""
    global cur_scr
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if (back_butt.top <= pos[1]) and (back_butt.bottom\
                    >= pos[1]) and (back_butt.left <= pos[0]) and\
                    (back_butt.right >= pos[0]):
                cur_scr = 0
        

def menu_event_processing():
    """event processing for menu """
    global cur_scr
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if (play_butt_1.top <= pos[1]) and (play_butt_1.bottom\
                    >= pos[1]) and (play_butt_1.left <= pos[0]) and\
                    (play_butt_1.right >= pos[0]):
                cur_scr = 1
                game_start(0)
            if (play_butt_2.top <= pos[1]) and (play_butt_2.bottom\
                    >= pos[1]) and (play_butt_2.left <= pos[0]) and\
                    (play_butt_2.right >= pos[0]):
                cur_scr = 1
                game_start(1)
            if (info_butt.top <= pos[1]) and (info_butt.bottom\
                    >= pos[1]) and (info_butt.left <= pos[0]) and\
                    (info_butt.right >= pos[0]):
                cur_scr = 3
                

def game_event_processing():
    """event processing for game"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                main_actor.vel_vector = [-1, 0]
            if event.key == pygame.K_RIGHT:
                main_actor.vel_vector = [1, 0]
            if event.key == pygame.K_SPACE:
                main_actor.shoot(0)
        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT) or (event.key == pygame.K_RIGHT):
                main_actor.vel_vector = [0, 0]
                main_actor.move(0)
            if event.key == pygame.K_SPACE:
                main_actor.shoot(1)
            
def final_scr_event_processing():
    """event processing for final screen"""
    global cur_scr
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if (play_more_butt.top <= pos[1]) and (play_more_butt.bottom\
                    >= pos[1]) and (play_more_butt.left <= pos[0]) and\
                    (play_more_butt.right >= pos[0]):
                cur_scr = 0
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_KP_ENTER:
                cur_scr = 0


def game_render():
    """game screen rendering"""
    global timer
    scr.blit(screen_img, win)
    for act in actors_list:
        act.move()
        scr.blit(act.img, act.rect)
    pygame.display.flip()
    if timer == 300:
        timer = 0
    else:
        timer += 1 
    fps.tick(300)

def menu_render():
    """menu screen rendering"""
    scr.fill(WHITE)
    pygame.draw.rect(scr, YELLOW, play_butt_1, 0, 50)
    pygame.draw.rect(scr, YELLOW, play_butt_2, 0, 50)
    pygame.draw.rect(scr, RED, info_butt, 0, 10)
    img_m1 = pygame.image.load("Python labs/final/pictures/main_actor/0_m_prev.png")
    img_m2 = pygame.image.load("Python labs/final/pictures/main_actor/1_m_prev.png")
    t_game_name = font_name.render("Aliens", True, BLUE)
    t_q = font_name.render("?", True, BLACK)
    scr.blit(t_game_name, (480, 50))
    scr.blit(t_q, (SCR_WIDTH-88, 20))
    scr.blit(img_m1, [play_butt_1.left + 20, play_butt_1.top + 20])
    scr.blit(img_m2, [play_butt_2.left + 20, play_butt_2.top + 20])
    pygame.display.flip()

def final_scr_render():
    """final screen rendering"""
    scr.fill(WHITE)
    if player_win:
        t_winner = font_name.render("You win!!", True, GREEN)
    else:
        t_winner = font_name.render("You lose :(", True, RED)
    pygame.draw.rect(scr, YELLOW, play_more_butt, 0, 50)
    t_play = font.render("Play more", True, GREEN)
    t_bosses = font_info.render("Killed bosses: " + str(killed_bosses), True, BLUE)
    t_enemies = font_info.render("Killed enemies: " + str(killed_en), True, BLUE)
    scr.blit(t_bosses, (435, 200))
    scr.blit(t_enemies, (435, 270))
    scr.blit(t_play, ((SCR_WIDTH/2) - 160, (SCR_HEIGHT*2/3) + 55))
    scr.blit(t_winner, ((SCR_WIDTH/2) - 225, 50))
    pygame.display.flip()

def info_scr_render():
    """information screen rendering"""
    info_img = pygame.image.load("Python labs/final/pictures/info.png").convert()
    t_play = font.render("Back to the menu", True, GREEN)
    scr.blit(info_img, win)
    pygame.draw.rect(scr, BLACK, back_butt, 0, 40)
    scr.blit(t_play, ((SCR_WIDTH/2) - 285, (SCR_HEIGHT*3/4) + 65))
    pygame.display.flip()

def boss_enemies_creating(enemy_t_1, enemy_t_2, enemy_1_fast, enemy_2_fast, max_en, deley):
    """Create enemies near the boss
    
    takes two types of enemies and fast/slow they are, max enemies on field, time between creatings
    """
    global creating_timer_zero
    enemies_n = 0
    for act in actors_list:
        if act.type in ["le", "me", "he"]:
            enemies_n+=1
    if (enemies_n < max_en) and ((pygame.time.get_ticks() / 1000) - creating_timer_zero >= deley):
        for act in actors_list:
            if act.type == "he":
                if (act.rect.left > 80) and ((act.rect.right + 80) < SCR_WIDTH):
                    enem1 = enemy(enemy_t_1, act.rect.left - 81, act.rect.top)
                    enem2 = enemy(enemy_t_2, act.rect.right + 1, act.rect.top)
                    enem1.fast_enemy = enemy_1_fast
                    enem2.fast_enemy = enemy_2_fast
                    coll = False
                    for act_2 in actors_list:
                        if enem1.rect.colliderect(act_2) or enem2.rect.colliderect(act_2):
                            coll = True
                    if coll:
                        del enem1
                        del enem2
                    else:
                        actors_list.append(enem1) 
                        actors_list.append(enem2)
                        creating_timer_zero = pygame.time.get_ticks() / 1000

def enemy_create(type, fast_speed, deley, max_en):
    """Create 1 enemy

        Param:enemy type, will it be fast/slow(fast - True), 
        time between two creatings, max enemies on field
    """
    global creating_timer_zero
    enemies_n = 0
    for act in actors_list:
        if act.type in ["le", "me", "he"]:
            enemies_n+=1
    if (enemies_n < max_en) and (((pygame.time.get_ticks() / 1000) - creating_timer_zero) >= deley):
        x_coord = randint(15, SCR_WIDTH-95)
        enem = enemy(type, x_coord)
        enem.fast_enemy = fast_speed
        coll = False
        for act in actors_list:
            if enem.rect.colliderect(act):
                coll = True
        if coll:
            del enem
        else:
            actors_list.append(enem)
            creating_timer_zero = pygame.time.get_ticks() / 1000

def boss_create(health, fast_speed):
    """Create boss

    Param:health, fast/slow(True if fast)
    """
    global boss_killing_time, creating_timer_zero, boss_on_field
    boss_killing_time = pygame.time.get_ticks() / 1000
    while not boss_on_field:
        x_coord = randint(15, SCR_WIDTH-95)
        y_coord = randint(80 ,330)
        check_rect = pygame.Rect(x_coord, y_coord-80, 80, 80)
        coll = False
        for act in actors_list:
            if check_rect.colliderect(act):
                coll = True
        if coll:
            del check_rect
        else:
            enem = enemy("he", x_coord, y_coord, health)
            enem.fast_enemy = fast_speed
            boss_on_field = True
            actors_list.append(enem)
            creating_timer_zero = pygame.time.get_ticks() / 1000

def enemies_creating():
    """Algorithm of creating enemies and difficulty control"""
    global creating_timer_zero, boss_on_field, boss_killing_time,\
         player_win, cur_scr, supply_on_field
    if not boss_on_field:
        #creating enemies depens on time in game
        if ((pygame.time.get_ticks() / 1000) - start_timer_zero) < GAME_SPEED:
            enemy_create("le", False, 2, 10)
        elif ((pygame.time.get_ticks() / 1000) - start_timer_zero) < (GAME_SPEED*2):
            if randint(0, 1) == 0: 
                enemy_create("le", False, 2, 10)
            else:
                enemy_create("me", False, 2, 10)
        elif ((pygame.time.get_ticks() / 1000) - start_timer_zero) < ((GAME_SPEED*2)+1):
            boss_create(10, False)  #1st boss
        elif ((pygame.time.get_ticks() / 1000) - start_timer_zero) < ((GAME_SPEED*3)+1):
            if randint(0, 1) == 0: 
                enemy_create("le", False, 1.5, 11)
            else:
                enemy_create("me", False, 1.5, 11)
        elif ((pygame.time.get_ticks() / 1000) - start_timer_zero) < ((GAME_SPEED*3)+2):
            boss_create(14, False)  #2nd boss
        elif ((pygame.time.get_ticks() / 1000) - start_timer_zero) < ((GAME_SPEED*4)+2):
            if randint(0, 3) > 0: 
                enemy_create("me", False, 1.4, 13)
            else:
                enemy_create("le", False, 1.4, 13)
        elif ((pygame.time.get_ticks() / 1000) - start_timer_zero) < ((GAME_SPEED*4)+3):
            boss_create(11, True)  #3rd boss
        elif ((pygame.time.get_ticks() / 1000) - start_timer_zero) < ((GAME_SPEED*5)+3):
            if randint(0, 3) > 0: 
                enemy_create("me", False, 1.4, 13)
            else:
                enemy_create("le", True, 1.4, 13)
        elif ((pygame.time.get_ticks() / 1000) - start_timer_zero) < ((GAME_SPEED*5)+4):
            boss_create(20, False)  #4th boss
        elif ((pygame.time.get_ticks() / 1000) - start_timer_zero) < ((GAME_SPEED*6)+4):
            if randint(0, 3) > 0: 
                if randint(0, 2) > 0:
                    enemy_create("me", False, 1.4, 15)
                else:
                    enemy_create("me", True, 1.4, 15)
            else:
                enemy_create("le", True, 1.4, 15)
        elif ((pygame.time.get_ticks() / 1000) - start_timer_zero) < ((GAME_SPEED*6)+5):
            boss_create(15, True)  #5th boss
        elif ((pygame.time.get_ticks() / 1000) - start_timer_zero) < ((GAME_SPEED*7)+5):
            if randint(0, 5) > 0: 
                if randint(0, 2) > 0:
                    enemy_create("me", True, 1.3, 15)
                else:
                    enemy_create("me", False, 1.3, 15)
            else:
                enemy_create("le", True, 1.3, 15)
        elif ((pygame.time.get_ticks() / 1000) - start_timer_zero) < ((GAME_SPEED*8)+5):
            if randint(0, 5) > 0: 
                enemy_create("me", True, 1.1, 17)
            else:
                enemy_create("le", True, 1.1, 17)
        elif ((pygame.time.get_ticks() / 1000) - start_timer_zero) < ((GAME_SPEED*8)+6):
            boss_create(35, True)  #6th boss
        elif ((pygame.time.get_ticks() / 1000) - start_timer_zero) < ((GAME_SPEED*8)+7):
            player_win = True
            cur_scr = 2
    else:
        #Creating enemies near the boss
        if killed_bosses == 0:
            boss_enemies_creating("le", "le", True, True, 13, 4)  #slow boss
        elif killed_bosses == 1:
            boss_enemies_creating("le", "me", True, False, 13, 3.5)  #slow boss
        elif killed_bosses == 2:
            boss_enemies_creating("me", "me", False, True, 13, 3.2)  #fast boss - less hp
        elif killed_bosses == 3:
            boss_enemies_creating("me", "me", True, True, 15, 2.5)  #slow boss - more hp
        elif killed_bosses == 4:
            boss_enemies_creating("me", "me", True, True, 15, 2)  #fast boss - mid hp
        elif killed_bosses == 5:
            boss_enemies_creating("me", "me", True, True, 20, 1.5)  #fast boss - more hp
    if (not supply_on_field) and ((pygame.time.get_ticks() // 1000) % (GAME_SPEED * 3)\
         == 0) and ((pygame.time.get_ticks() // 1000) != 0):
        if randint(0, 2) == 0:
            supply_on_field = True
            if randint(0, 2) == 0:
                sup = supply("sm")
            else:
                sup = supply("sl")
            actors_list.append(sup)



#classes
class actor():
    """actor class 
        "m" - main actor
        "le" - light enemy
        "me" - mid enemy
        "he" - hard enemy
        "ab" - ammo bullet
        "sm" - supply multi shot
        "sl" - supply laser
        coords for left bottom corner
    """
    def __init__(self, act, coords):
        if act == "m":
            self.img = pygame.image.load("Python labs/final/pictures/main_actor/0_m_wait_for_s.png")
        elif act == "le":
            self.img = pygame.image.load("Python labs/final/pictures/enemies/light.png")
        elif act == "me":
            self.img = pygame.image.load("Python labs/final/pictures/enemies/mide.png")
        elif act == "he":
            self.img = pygame.image.load("Python labs/final/pictures/enemies/hard.png")
        elif act == "ab":
            self.img = pygame.image.load("Python labs/final/pictures/ammo/bullet.png")
        elif act == "al":
            self.img = pygame.image.load("Python labs/final/pictures/ammo/laser.png")
        elif act == "sm":
            self.img = pygame.image.load("Python labs/final/pictures/supply/multishot.png")
        elif act == "sl":
            self.img = pygame.image.load("Python labs/final/pictures/supply/laser.png")
        self.type = act
        self.rect = self.img.get_rect()
        self.rect.bottomleft = coords
        self.vel_vector = [0, 0]

class m_actor(actor):
    """main actor class"""
    def __init__(self, coords, skin):
        super().__init__("m", coords)
        self.move_phase = 0
        self.skin = skin
        self.supply = 0  #0-no, 1-multishot
        self.img = pygame.image.load("Python labs/final/pictures/main_actor/" + str(self.skin) + "_m_wait_for_s.png")
    def shoot(self, stade):  #stade 0 - prepearing, 1 -shooting
        if self.supply != 0:
            if (pygame.time.get_ticks() / 1000) - supply_timer_zero > (GAME_SPEED/2):
                self.supply = 0
        if stade == 0:
            self.img = pygame.image.load("Python labs/final/pictures/main_actor/" + str(self.skin) + "_m_s.png")
        if stade == 1:
            self.img = pygame.image.load("Python labs/final/pictures/main_actor/" + str(self.skin) + "_m_wait_for_s.png")
            if self.supply == 2:
                laser = bullet([self.rect.left+35, 635], "al")
                actors_list.append(laser)
            else:
                bul = bullet([self.rect.left+35, self.rect.top+13], "ab")
                actors_list.append(bul)
            if self.supply == 1:
                bul0 = bullet([self.rect.left+35, self.rect.top+13], "ab")
                bul0.vel_vector[0] = -1
                actors_list.append(bul0)
                bul1 = bullet([self.rect.left+35, self.rect.top+13], "ab")
                bul1.vel_vector[0] = 1
                actors_list.append(bul1)
    def move(self, in_move=1):
        if (self.vel_vector[0] < 0) and (self.rect.left >= win.left):
            self.rect = self.rect.move(self.vel_vector)
            self.move_img_ch(0)
        elif (self.vel_vector[0] > 0) and (self.rect.right <= win.right):
            self.rect = self.rect.move(self.vel_vector)
            self.move_img_ch(1)
        if in_move == 0:
            self.img = pygame.image.load("Python labs/final/pictures/main_actor/" + str(self.skin) + "_m_wait_for_s.png")
    def move_img_ch(self, side):  #side 0 - left, 1 - right
        if 0 <= self.move_phase < 15:
            self.img = pygame.image.load("Python labs/final/pictures/main_actor/" + str(self.skin) + "_m_move_1.png")
            self.move_phase += 1
        elif 15 <= self.move_phase < 30:
            self.img = pygame.image.load("Python labs/final/pictures/main_actor/" + str(self.skin) + "_m_move_2.png")
            self.move_phase += 1
        elif 30 <= self.move_phase < 45:
            self.img = pygame.image.load("Python labs/final/pictures/main_actor/" + str(self.skin) + "_m_move_3.png")
            self.move_phase += 1
            if self.move_phase == 45:
                self.move_phase = 0
        if side == 0:
            self.img = pygame.transform.flip(self.img, True, False)

class bullet(actor):
    """bullets class type ab - bullet, al - laser"""
    def __init__(self, coords, type):
        super().__init__(type, coords)
        self.vel_vector = [0, -1]
        if type == "al":
            self.life_time = pygame.time.get_ticks() / 100
    def move(self):
        if self.type == "ab":
            self.rect = self.rect.move(self.vel_vector)
            if not self.rect.colliderect(win):
                del actors_list[actors_list.index(self)]
        elif self.type == "al":
            self.del_laser()
    def del_laser(self):
        if ((pygame.time.get_ticks() / 100) - self.life_time) > 2:
                for act in actors_list:
                    if self.rect.colliderect(act.rect) and (act.type in ["le", "me", "he"]):
                        act.lassered = False
                del actors_list[actors_list.index(self)]

class supply(actor):
    """class for supplying boxes "sl"-laser, "sm"-multishot"""
    def __init__(self, act):
        super().__init__(act, [randint(20, SCR_WIDTH - 79), 59])
        self.vel_vector = [0, 1]
    def move(self):
        if (timer % 4) == 0:
            self.rect = self.rect.move(self.vel_vector)
        self.col_chk()
    def col_chk(self):
        global supply_timer_zero, supply_on_field
        if self.rect.bottom > SCR_HEIGHT-100:
            supply_on_field = False
            del actors_list[actors_list.index(self)]
        for act in actors_list:
            if (act.type == "ab") or (act.type == "al"):
                if self.rect.colliderect(act.rect):
                    del actors_list[actors_list.index(self)]
                    if act.type == "ab":
                        del actors_list[actors_list.index(act)] 
                    supply_on_field = False
                    if self.type == "sm":
                        main_actor.supply = 1
                    elif self.type == "sl":
                        main_actor.supply = 2
                    supply_timer_zero = (pygame.time.get_ticks() / 1000)


class enemy(actor):
    def __init__(self, act, coordx, coordy=100, health = 0):  #health only for boss
        super().__init__(act, [coordx, coordy])
        self.fast_enemy = False
        self.lassered = False
        if act == "he":
            v = randint(-1, 1)
            while v == 0:
                v = randint(-1, 1)
            self.vel_vector = [v, 1]
            self.health = health
        else:
            self.vel_vector = [0, 1]
            if act == "me":
                self.health = 2
            else:
                self.health = 1
    def move(self):
        global cur_scr
        if self.type == "he":
            if (self.rect.right + 15) > win.right:
                self.rect.right = win.right - 15
                self.vel_vector[0] = -self.vel_vector[0]
            elif (self.rect.left - 15) < win.left:
                self.rect.left = win.left + 15
                self.vel_vector[0] = -self.vel_vector[0]
            if self.rect.top < (win.top + 30):
                self.rect.top = win.top + 30
                self.vel_vector[1] = -self.vel_vector[1]
            elif self.rect.bottom > (win.top + 330):
                self.rect.bottom = win.top + 330
                self.vel_vector[1] = -self.vel_vector[1]
            if self.fast_enemy:
                self.rect = self.rect.move(self.vel_vector)
            elif (timer % 2) == 0:
                self.rect = self.rect.move(self.vel_vector)
        else:
            if not self.fast_enemy:
                if ((self.type == "le") and ((timer % 5) == 0)) or\
                    ((self.type == "me") and ((timer % 8) == 0)):
                    self.rect = self.rect.move(self.vel_vector)
            else:
                if ((self.type == "le") and ((timer % 2) == 0)) or\
                    ((self.type == "me") and ((timer % 4) == 0)):
                    self.rect = self.rect.move(self.vel_vector)
        if (self.rect.bottom >= SCR_HEIGHT-100):
                cur_scr = 2           
        self.check_col()
    def check_col(self):
        global start_timer_zero, boss_on_field, killed_bosses,  killed_en, creating_timer_zero
        #add colisions with another aliens
        for act in actors_list:
            if (act.type == "ab") or (act.type == "al"):
                if self.rect.colliderect(act.rect):
                    if ((act.type == "al") and (self.lassered == False)) or (act.type == "ab"):
                        self.health -= 1
                        if act.type == "ab":
                            del actors_list[actors_list.index(act)]
                        else:
                            self.lassered = True
                        if self.health == 0:
                            if self.type == "he":
                                start_timer_zero += ((pygame.time.get_ticks() / 1000) - boss_killing_time)
                                start_timer_zero -= 1
                                boss_on_field = False
                                killed_bosses += 1
                                creating_timer_zero = pygame.time.get_ticks() / 1000
                            else:
                                killed_en += 1
                            del actors_list[actors_list.index(self)]


if __name__ == "__main__":
    pygame.init()
    
    #game objects creating
    fps = pygame.time.Clock()
    font_info = pygame.font.SysFont('Arial.TTF', 70)
    font = pygame.font.SysFont('Arial.TTF', 100)
    font_name = pygame.font.SysFont('Arial.TTF', 135)
    scr = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
    win = pygame.Rect(0, 0, SCR_WIDTH, SCR_HEIGHT)
    screen_img = pygame.image.load("Python labs/final/pictures/game_field.png").convert()
    

    #menu objects creating
    play_butt_1 = pygame.Rect(SCR_WIDTH/5, SCR_HEIGHT/3,\
                            SCR_WIDTH/5, SCR_WIDTH/5)
    play_butt_2 = pygame.Rect(SCR_WIDTH*3/5, SCR_HEIGHT/3,\
                            SCR_WIDTH/5, SCR_WIDTH/5)
    play_more_butt = pygame.Rect(SCR_WIDTH/4, SCR_HEIGHT*2/3,\
                            SCR_WIDTH/2, SCR_HEIGHT/4)
    back_butt = pygame.Rect(SCR_WIDTH/4, SCR_HEIGHT*4/5,\
                            SCR_WIDTH/2, SCR_HEIGHT/6)
    info_butt = pygame.Rect(SCR_WIDTH-100, 20, 80, 80)

    #main loop
    while True:
        if cur_scr == 0:  #menu
            #events processing
            menu_event_processing()

            #rendering
            menu_render()

        elif cur_scr == 1:  #screen of game
            #events processing 
            game_event_processing()

            #creating new enemies
            enemies_creating()
            
            #rendering
            game_render()
        
        elif cur_scr == 2:  #final screen
            #events processing 
            final_scr_event_processing()
            
            #rendering
            final_scr_render()
        
        elif cur_scr == 3:  #info screen
            #events processing 
            info_scr_event_processing()
            
            #rendering
            info_scr_render()
        