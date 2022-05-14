from collections import namedtuple
import time
import pygame, sys
from score_file import *
from constants import *
from random import randint
from floor import Floor
from score import Score
from clouds import Clouds
from player import Player
from skull import Skulls
from decoration import Decorator

# Config
""" pygame.mixer.pre_init(44100, -16, 2, 512) """
pygame.init()
pygame.display.set_caption("GOSH, Cari!")

# Display screen
screen = pygame.display.set_mode((SIZE, SIZE))

# Font
game_font = pygame.font.Font('Fonts/Super-Mario2.ttf', 20)
game_font2 = pygame.font.Font('Fonts/Super-Mario2.ttf', 16)

# Clock object
clock = pygame.time.Clock()

# Clouds image
clouds_img_original = pygame.image.load('Images/clouds.png').convert_alpha()
clouds_img = pygame.transform.scale(clouds_img_original, (700, 500))

# Skull decoration
decorator_img_original = pygame.image.load('Images/skull-decoration.png').convert_alpha()
decorator_img_original2 = pygame.transform.scale(decorator_img_original, DECORATION_SIZE)
decorator_img = pygame.transform.flip(decorator_img_original2, True, False)

# Player image
ghost_img_original = pygame.image.load('Images/ghost_player.png').convert_alpha()
ghost_img_left = pygame.transform.scale(ghost_img_original, PLAYER_SIZE)
ghost_img_right = pygame.transform.flip(ghost_img_left, True, False)

# Skull image
skull_img_original = pygame.image.load('Images/skull_color.png').convert_alpha()
skull_img = pygame.transform.scale(skull_img_original, ENEMY_SIZE)

# Enemy image
enemy_img_original = pygame.image.load('Images/heart.png').convert_alpha()
enemy_img = pygame.transform.scale(enemy_img_original, ENEMY_SIZE)

# Groups
skull_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

# Flag for change the heading direction of the player
is_left = False

# Flag for pause the game until the player press any key
is_on = False

# Game over
game_over = False

def message_game_over(msg, game_font, color, go_y):
    text = game_font.render(msg, False, color)
    go_x = int(SIZE / 2)
    go_rect = text.get_rect(center = (go_x, go_y))
    screen.blit(text, go_rect)
    
game_over_time = 0
       
# Handling scores
current_dir = Path.cwd()
path = Path(current_dir)
best_score_file = path / 'best_score.txt'
       
new_best_score = 0
new_best_score_time = 0


def is_new_score():
        return message_game_over('New highest score!', game_font2, (25, 50, 10), int(SIZE / 4))
    

# Main
class Main():
    def __init__(self):
        self.floor = Floor(0, (SIZE - (CELL_SIZE * 2)))
        self.score = Score()
        self.cloud = Clouds()
        self.decorator = Decorator(decorator_img)
        self.player = Player(CELL_SIZE, PLAYER_FLOOR)
        # Sounds and music
        self.music = pygame.mixer.Sound('Sounds/ghost-sounds-theremin.wav')
        self.bonus_music = pygame.mixer.Sound('Sounds/arcade-retro-run.wav')
        self.reload_sound = pygame.mixer.Sound('Sounds/recharging.wav')
        self.game_over_sound = pygame.mixer.Sound('Sounds/loosing.wav')
        
    def draw_objects(self):
        self.cloud.draw_clouds(screen, clouds_img)
        self.score.draw_score(game_font, screen)
        self.floor.draw_floor(screen)
        
    def play_music(self, sound, repeat):
        sound.play(repeat) # -1 repeat indefinitelly
        
    def reload(self, sound):
        enemy_group.empty()
        skull_group.empty()
        self.player.rect.x = (SIZE / 2)
        self.player.rect.y = PLAYER_FLOOR
        self.play_music(sound, 0)
        
# Creating an instance of the class Main.
main = Main()

# current_score = main.score.score_text NOT WORKING

# Musical theme
main.play_music(main.music, -1)



# Main Loop
while True:
    score_file_content = read_best_score(best_score_file)
   
    """ if main.score.score_text > mejor_puntaje:
        new_best_score_time = seconds
        mejor_puntaje = main.score.score_text """
        
    # Bg color of the screen    
    if main.score.score_text < 200:    
        screen.fill(SKY_COLOR)
    elif main.score.score_text > 200:
        screen.fill(SKY_DARK)
              
    # Adding some skulls to skull_group and defining some progressive levels   
    if is_on:      
        if len(skull_group) == 0:
            if main.score.score_text < 200:
                for number in range(0, 15):           
                    skull = Skulls(skull_img, skull_group, randint(2, 3))
                    skull_group.add(skull)
            elif main.score.score_text >= 200 and main.score.score_text < 400:
                main.player.speed += 3
                main.music.set_volume(0.3) # !!
                main.bonus_music.play(1) # !!
                for number in range(0, 50):
                    skull = Skulls(skull_img, skull_group, randint(4, 5))
                    skull_group.add(skull)
            elif main.score.score_text >= 400 and main.score.score_text < 600:
                main.player.speed = 4
                main.bonus_music.stop()
                main.music.set_volume(1) # !!
                for number in range(0, 10):
                    skull = Skulls(skull_img, skull_group, randint(2, 3))
                    skull_group.add(skull)
            elif main.score.score_text >= 600 and main.score.score_text < 800:
                for number in range(0, 25):
                    skull = Skulls(skull_img, skull_group, randint(2, 3))
                    skull_group.add(skull)
            elif main.score.score_text >= 800 and main.score.score_text < 1200:
                main.player.speed += 4
                main.music.set_volume(0.3) # !!
                main.bonus_music.play(2) # !!
                for number in range(0, 60):
                    skull = Skulls(skull_img, skull_group, randint(5, 6))
                    skull_group.add(skull)
            else:
                main.player.speed = 5
                main.bonus_music.stop() # !!
                main.music.set_volume(1) # !!
                for number in range(0, 30):
                    skull = Skulls(skull_img, skull_group, randint(2, 3))
                    skull_group.add(skull)

        # Drawing skulls
        for skull in skull_group:
            skull.draw_skulls(screen)
            skull.dropping()
            # When they hit the floor
            if skull.rect.y > (main.floor.floor_rect.top - CELL_SIZE):
                skull_group.remove(skull)
                main.score.score_text -= 1
            # When they collied
            elif pygame.sprite.spritecollide(main.player, skull_group, True):
                skull_group.remove(skull)
                main.play_music(main.player.eat_sound, 0)
                main.score.score_text += 2
           
            
        # Adding some enemies
        if len(enemy_group) == 0:
                if main.score.score_text > 200 and main.score.score_text < 400:
                    for number in range(0, 1):           
                        enemy = Skulls(enemy_img, enemy_group, randint(3, 8))
                        enemy_group.add(enemy)
                else: 
                    for number in range(0, 3):           
                        enemy = Skulls(enemy_img, enemy_group, randint(3, 8))
                        enemy_group.add(enemy)
                # if the player fly to the top, more enemies drops
                if main.player.rect.y < (SIZE / 3):
                    for number in range(2, 10):
                        enemy = Skulls(enemy_img, enemy_group, randint(2, 6))
                        enemy_group.add(enemy)
                
        # Drawing enemies creating an instance of class Skulls
        for enemy in enemy_group:
            enemy.draw_skulls(screen)
            enemy.dropping()
            # When they hit the floor
            if enemy.rect.y > (main.floor.floor_rect.top - CELL_SIZE):
                enemy_group.remove(enemy)
                main.score.score_text += 6
            # When they collied
            elif pygame.sprite.spritecollide(main.player, enemy_group, True) or main.score.score_text < 0:
                enemy_group.remove(enemy)
                main.reload(main.game_over_sound)
                game_over = True
                game_over_time = seconds
                print(game_over_time)
                last_score = main.score.score_text
                main.score.score_text = 0
                time.sleep(1.1)
    
    # Draw elements
    main.draw_objects()
    main.cloud.move_clouds()
    
    # Time flag
    seconds = pygame.time.get_ticks() / 1000
    # print(seconds)    
    if seconds < 3:
        message_game_over('BEST SCORE: ' + str(score_file_content), game_font, (0, 0, 50), int(SIZE / 2))
     
    
    # Game over text
    if seconds < game_over_time + 4:
        if game_over == True:
            message_game_over('GAME OVER', game_font, (0, 0, 50), int(SIZE / 2 - CELL_SIZE))
            message_game_over('Your score: ' + str(last_score), game_font2, (0, 0, 50), int(SIZE / 2 + CELL_SIZE))
            if main.score.score_text > int(score_file_content):
                change_best_score_file(score_file_content, best_score_file, new_best_score)


    
    before_new_score = 0

    # New best score  
    if main.score.score_text < int(score_file_content):
        main.score.draw_best_score(game_font2, screen, ('BEST: ' + str(score_file_content)))  
    elif main.score.score_text >= int(score_file_content):
        new_best_score = main.score.score_text
        new_best_score_time = seconds
        change_best_score_file(score_file_content, best_score_file, new_best_score)   
        # is_new_score()
        main.score.draw_best_score(game_font2, screen, ('NEW HIGH SCORE!')) 
    elif main.score.score_text == new_best_score:
        main.score.draw_best_score(game_font2, screen, ('NEW HIGH SCORE!')) 

    
    # Changing the flag
    if is_left:
        main.player.draw_player(screen, ghost_img_left)
    else:
        main.player.draw_player(screen, ghost_img_right)
        
    # Decorator drawed after all other elements
    main.decorator.draw_decorator(screen)
    
    
    # EVENTS
        
    # Quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    key_pressed = pygame.key.get_pressed()
    
    # Reload position
    if key_pressed[pygame.K_SPACE]:
        main.reload(main.reload_sound)
        main.score.score_text = 0
    
    # Assign keys for move the player
    if key_pressed[pygame.K_LEFT]:
        main.player.left()
        is_left = True
        is_on = True
        
    elif key_pressed[pygame.K_RIGHT]:
        main.player.right()
        is_left = False
        is_on = True
        
    elif key_pressed[pygame.K_UP]:
        main.player.up()
        is_on = True
        
    elif key_pressed[pygame.K_DOWN]:
        main.player.down()
        is_on = True
    
    if event.type == pygame.KEYUP:
        main.player.down()
        # is_on = True
    
    
    """ FOR A SECOND PLAYER
    if key_pressed[pygame.K_a]:
        main.player2.left()
    elif key_pressed[pygame.K_d]:
        main.player2.right()
    elif key_pressed[pygame.K_w]:
        main.player2.up()
    elif key_pressed[pygame.K_s]:
        main.player2.down() """
        
    # Updating the display surface with all the elements that were drawn in the screen.
    pygame.display.update()
    
    # Using Clock passing framerates (how many times the loop can runs per second)
    clock.tick(60)
