#----------------------------VERSION 10------AUG 15 2026

#WARRIORS VERSION --------- KEEP IN CUSS WORDS....ALL OTHERS REMOVE line around 2500

#Ehancements


# KEY IN "SCORES" AND SEE SCOREBOARD




# SOUNDS FOR DIFFERENT ACTIONS........'JUICE'
# have python voice say SUGGESTED WORDS  with a few smirky remarks
#1st time reaching game board..enter key after a guess..different
#sounds for keyed input HELP..TIMEOUT..RESET..+ - !...changing colors
#on workheet with mouse, deduction in points at severity levels, getting hints,
#different sounds keying vs using icons, dragging letters to scratchpad, invalid
#input.winning, RESET "Giving up.stupid...rotate 5 sounds', theme sound with a
#switch to turn it off......heart beat as time # of guesses and point reduction levels
# harsh warnings when getting close to zero points........a loser scpreboard for
# quitting, points less 10,000?..




# Different difficulty levels.......three different scoreboards
# Put difficulty level on splash screen..replace scoreboard...lev 1..500,000 points
#(default)...lev 2 200,000 points......lev 3 100,000 points..increase point reductions
# based on difficulty....lev 1 3rd grader words ....level 2 high school...level 3
# college.....lev 1 and lev 2 use WORDS for secret word...level 3 usE DICTIONARY.TXT 

#Reward bonus points for hints not used
                                  
#BUGS..............-abc-def-ghi....will turn all 10 letters grey same for + and ! 


# Do not change any of my variable names!!!!

# I use the Thonny IDE, so If possible reference sequence line numbers
# and not 'page numbers'

#TO STOP FUZZY LETTERS PUT CANVAS.FILL IN ALL FUNTIONS.........GO INTO ALL PRINT AREAS
# AND THE WORD BLACK
#                       
#                       

# NEXT STEPS            
#  				        
#                       3. Fix wording/format on HELP..SPLASH..ORGIN screens
#                       
#                       5. Verify points are deducted correctly
#                       6. Backup python/Wonder Word files to H:drive plus

# Initialize the real monitor window to be RESIZABLE
#HOLLY SAID HER SPLASH SCREEN WAS CUT OFF AT THE BOTTOM "SO I ADDED SCALED"
#SCREEN = pygame.display.set_mode((current_width, current_height), pygame.RESIZABLE)
#SCREEN = pygame.display.set_mode((current_width, current_height), pygame.RESIZABLE | pygame.SCALED)
#                     
#
#BUGS
# WOOSH SOUND WHEN TYPING HELP FOR HELP SCREEN 8-10-26





#                       1. When branching to ORGIN story gets this error
#                          "CRITICAL ERROR: Logic overload detected." but hitting
#                          takes you back to the game correctly. A version of
#                          around June 6 works correctly because "If" statement
#                          is placed in a different spot in the code
#                       1A Sometimes the two Suggested Words are the same
#                       
#R
#
#VERSION 10- Use python voice....piece together viet nam audio.....more sounds for
#special action.......look at place holders
#
#version 11....THERE IS AN EASY WAT TO cONVERT MY GAME TO A BROWZER.......USE ITCH
# AND OR GIT-HUB SO PLAYERS CAN SHARE THE SAME SCOREBOARD TO COMPETE




#================================IMPORT FUNTIONS====================================
import datetime
import math  
import random
import sys
import platform
import shutil
from pathlib import Path


# --- SETUP PYGAME INITIALIZATION ---
import pygame
pygame.init()
pygame.mixer.init()


# ==============================================================================
# 1. SETUP BASE DIRECTORIES & FILE PATHS (Unified Sections 1, 3, & 5)
# ==============================================================================

if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    bundle_dir = Path(sys._MEIPASS)
else:
    bundle_dir = Path(__file__).parent

# exe_dir handles files we want to edit/save right next to where the user plays
if getattr(sys, 'frozen', False):
    exe_dir = Path(sys.executable).parent
else:
    exe_dir = Path(__file__).parent

# Assign all absolute paths using our base engines
words_file_path = bundle_dir / "WORDS.txt"
dict_file_path = bundle_dir / "DICTIONARY.txt"
sound_dir_path  = bundle_dir / "SOUNDS"
master_score_path = bundle_dir / "HIGHSCORES.txt"
game_board_path = bundle_dir / "GAME_BOARD.png"




#insert new code begin
# Route the scoreboard dynamically based on the Operating System
if platform.system() == "Darwin":
    # On macOS: Redirect writing to the Application Support folder to guarantee permissions
    mac_save_dir = Path.home() / "Library" / "Application Support" / "WonderWord"
    try:
        mac_save_dir.mkdir(parents=True, exist_ok=True)
        score_file_path = mac_save_dir / "HIGHSCORES.txt"
    except Exception:
        # If macOS blocks the folder, fallback safely to bundle/exe dir
        score_file_path = exe_dir / "HIGHSCORES.txt"
else:
    # On Windows/Linux: Retain your original executable directory logic
    score_file_path = exe_dir / "HIGHSCORES.txt"
#Insert new code end














# UNIFIED DEPLOYMENT: Clone master or create defaults regardless of OS
if not score_file_path.exists():
    # Strategy A: Try to copy the HIGHSCORES.txt built into your PyInstaller bundle
    if master_score_path.exists():
        try:
            shutil.copy(master_score_path, score_file_path)
        except Exception:
            pass
            
    # Strategy B: Hardcoded fallback if the bundle file copy fails or is missing
    if not score_file_path.exists():
        try:
            with open(score_file_path, "w") as f:
                f.write("499788,HITLER,1,0.1,07/28/26  06:23PM\n")
                f.write("383156,TRACI,7,1.9,07/04/26  01:27PM\n")
                f.write("499788,HUTCH,1,0.1,07/28/26  06:23PM\n")
                f.write("287632,HOLLY,3,0.8,07/16/26  09:17AM\n")	
                f.write("281778,JAN,5,1.8,07/21/26  11:19AM\n")
                f.write("250288,ELAINE,8,4.7,07/31/26  05:33PM\n")
                f.write("199784,D TRUMP,3,0.1,07/19/26  04:07PM\n")
        except Exception:
            pass

#stopped//////////////////////////////////////////1








# ===============================Initialize variables===============================
timeout_break = 2
points_allowed = 500000
#points_allowed = 500000
#points_allowed = 100000 
points = points_allowed 
MAX_HINTS_ALLOWED = 4    
HINT_COST_1 = 1000
HINT_COST_2 = 3000
HINT_COST_3 = 5000
HINT_COST_4 = 10000

allow_hints_now = False
hint_status_msg = ""
max_hints_allowed = 0
start_time = datetime.datetime.now()
elapsed_seconds = 0           
elapsed_time = 0
total_break_seconds = 0
turn_start_time = datetime.datetime.now()

username = ""
hold_secret_word = ""
hold_user_input = ""
try_again = ""
num_matches = 0
num_sequence = 0
penalty_alert = ""
number_of_guesses = 0

origin_music_playing = False

play_again = 'N'
revealed_indices = []
letters_not_in_word = set()
letters_might_be_in_word = set()
letters_in_word = set()
suggested_hints = []
dig_scratch_pad_slots = [" ", " ", " ", " ", " "]
scroll_index = 0   
show_help_overlay = 0
show_help_index = False

break_start = None
words_entered = []
paused = False
pause_start = None
game_over = False


# ====================================================================
# DRAG AND DROP CONFIGURATION PROPERTIES (ADD TO INITIALIZATION AREA)
# ====================================================================
dragging_letter = None  # Stores the string character being dragged (e.g., 'A'). None means empty.
drag_source = None      # Stores where the letter came from: "WORKSHEET" or an integer index (0-4)
drag_pos = [0, 0]       # Keeps track of the live X and Y pixel positions under the mouse cursor


# --- STATE MANAGEMENT VARIABLES
# State flags: NAME_INPUT, PLAYING, TIMEOUT, GAME_OVER, CLEAR_LEADERBOARD
game_state = "NAME_INPUT"  

# MESSAGES
feedback_message = "Welcome to 'Wonder Word'.............. Type your name and press Enter."
game_status_message = "Type a 5 letter word"
hold_user_input_msg = "Welcome to 'Wonder Word'"
#///////////////////////////////end of chunk 2




#START CUNK 3



# DEFINE SCREEN SIZE
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

# We set up tracking for the active window layout sizes
current_width = SCREEN_WIDTH
current_height = SCREEN_HEIGHT

# --- MAC SAFETY CHECK ---
# Checks the tester's screen size so the game never bleeds off the edge at launch
desktop_sizes = pygame.display.get_desktop_sizes()
if desktop_sizes:
    desktop_width, desktop_height = desktop_sizes[0]
 
    # CHANGED: Only shrink if the desktop height is strictly less than 700 pixels.
    # This prevents it from shrinking on your standard or high-res monitor!
    if desktop_height < 700 and current_height > (desktop_height - 50):
        ratio = (desktop_height - 50) / SCREEN_HEIGHT
        current_height = int(desktop_height - 50)
        current_width = int(SCREEN_WIDTH * ratio)

# Initialize the real monitor window using ONLY RESIZABLE 
SCREEN = pygame.display.set_mode((current_width, current_height), pygame.RESIZABLE)

# === THE FIX: Force variables to match what macOS actually gave you ===
current_width, current_height = SCREEN.get_size()

# Create the virtual surface canvas at your exact designed aspect ratio
canvas = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))



# ==============================================================================
# 1. SETUP BASE DIRECTORIES & FILE PATHS (Unified Sections 1, 3, & 5)
# ==============================================================================
# bundle_dir handles read-only game assets stored inside the app package
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    bundle_dir = Path(sys._MEIPASS)
else:
    bundle_dir = Path(__file__).parent

# exe_dir handles files we want to edit/save right next to where the user plays
if getattr(sys, 'frozen', False):
    exe_dir = Path(sys.executable).parent
else:
    exe_dir = Path(__file__).parent

# Assign all absolute paths using our base engines
words_file_path = bundle_dir / "WORDS.txt"
dict_file_path = bundle_dir / "DICTIONARY.txt"
sound_dir_path  = bundle_dir / "SOUNDS"
score_file_path = exe_dir / "HIGHSCORES.txt"
game_board_path = bundle_dir / "GAME_BOARD.png"



#CHUNK 3 END


#START CHUNK 4

# ==============================================================================
# 2. LOAD VISUAL & AUDIO ASSETS 
# ==============================================================================
# CRITICAL COMPATIBILITY FIX: Added bundle_dir to locate the PNG asset inside the app package

try:
    # FIX: Use the smart path variable you defined in your setup section
    base_snapshot = pygame.image.load(str(game_board_path)).convert()
    
    # Keep your size check and auto-scale feature safely intact
    if base_snapshot.get_width() != 1000 or base_snapshot.get_height() != 600:
        base_snapshot = pygame.transform.scale(base_snapshot, (1000, 600))
except Exception as e:
    print(f"Critical Error: Could not load GAME_BOARD.png asset. Error: {e}")
    import sys
    sys.exit() # Stops the program here so it doesn't crash with "not defined" later




try:
    Roy_Rogers_path = bundle_dir / "ROY_ROGERS.png"
    Roy_Rogers_snapshot = pygame.image.load(Roy_Rogers_path).convert()
    
    # SMOOTHSCALE forces the pixels to stretch completely to the 1000x600 canvas borders
    Roy_Rogers_snapshot = pygame.transform.smoothscale(Roy_Rogers_snapshot, (1000, 600))
    
except Exception as e:
    print(f"Critical Error: Could not load ROY_ROGERS.png asset. Error: {e}")




# Load Audio Sounds
try:
    sound_error = pygame.mixer.Sound(sound_dir_path / "error.wav")
    sound_error.set_volume(0.5)
    
    # 1. KEYBOARD CLICK (Letters/Commands Typing)
    # TRIGGER LOCATION: Inside the KEYDOWN 'else' block where event.unicode is checked.
    sound_click = pygame.mixer.Sound(sound_dir_path / "keyboard_click.wav")
    sound_click.set_volume(0.2) # Set to 0.0 to keep silent during your testing phase.
    
    # 2. EXIT MELODY (Happy Trails Song)
    # TRIGGER LOCATION: Right at the very first line of the "def quit_game():" function.
    sound_happy_trails = pygame.mixer.Sound(sound_dir_path / "happy_trails.wav")
    sound_happy_trails.set_volume(0.4)
    
    sound_VietNam = pygame.mixer.Sound(sound_dir_path / "VietNam.wav")  
    sound_VietNam.set_volume(0.07)
    
    tile_click = pygame.mixer.Sound(sound_dir_path / "tile_click.wav")  
    tile_click.set_volume(0.3)
    
    woosh = pygame.mixer.Sound(sound_dir_path / "woosh.wav")
    woosh.set_volume(0.05)
    
    # 3. INSTANT VICTORY FANFARE (Rocky Theme Opening)
    # TRIGGER LOCATION: Inside the KEYDOWN block under "elif num_sequence == 5:".
    #sound_victory = pygame.mixer.Sound(sound_dir_path / "victory.wav")
    #sound_victory.set_volume(1.0)
    
    # --- CROWD SOUNDS ---
    sound_vic_crowd1 = pygame.mixer.Sound(sound_dir_path / "vic_crowd1.wav")
    sound_vic_crowd1.set_volume(0.4)
    sound_vic_crowd2 = pygame.mixer.Sound(sound_dir_path / "vic_crowd2.wav")
    sound_vic_crowd2.set_volume(0.4)
    sound_vic_crowd3 = pygame.mixer.Sound(sound_dir_path / "vic_crowd3.wav")
    sound_vic_crowd3.set_volume(0.4)
    sound_vic_crowd4 = pygame.mixer.Sound(sound_dir_path / "vic_crowd4.wav")
    sound_vic_crowd4.set_volume(0.4)



#END OF CHUNK 4

#start chunk#5

    # --- FIREWORKS SOUNDS ---
    sound_vic_fireworks1 = pygame.mixer.Sound(sound_dir_path / "vic_fireworks1.wav")
    sound_vic_fireworks1.set_volume(1.0)
    sound_vic_fireworks2 = pygame.mixer.Sound(sound_dir_path / "vic_fireworks2.wav")
    sound_vic_fireworks2.set_volume(1.0)
    sound_vic_fireworks3 = pygame.mixer.Sound(sound_dir_path / "vic_fireworks3.wav")
    sound_vic_fireworks3.set_volume(1.0)
    sound_vic_fireworks4 = pygame.mixer.Sound(sound_dir_path / "vic_fireworks4.wav")
    sound_vic_fireworks4.set_volume(1.0)
    
    # --- MUSIC SOUNDS ---
    sound_vic_music1 = pygame.mixer.Sound(sound_dir_path / "vic_music1.wav")
    sound_vic_music1.set_volume(0.20)
    sound_vic_music2 = pygame.mixer.Sound(sound_dir_path / "vic_music2.wav")
    sound_vic_music2.set_volume(0.60)
    sound_vic_music3 = pygame.mixer.Sound(sound_dir_path / "vic_music3.wav")
    sound_vic_music3.set_volume(0.60)
    sound_vic_music4 = pygame.mixer.Sound(sound_dir_path / "vic_music4.wav")
    sound_vic_music4.set_volume(0.60)
    
    # 3. LEADERBOARD DATA WIPE RESET (System Zap/Whoosh)
    # TRIGGER LOCATION: Inside the CLEAR_LEADERBOARD state block when input == "Y".
    ##sound_clear = pygame.mixer.Sound(sound_dir_path / "clear_reset.wav")
    #sound_clear.set_volume(1.0)
    
    # 4. FORFEIT / RESET VALUE (Wistful Descending Chime)
    # TRIGGER LOCATION: Under input == "RESET" and the Reset Circle Button collision check.
    #sound_reset = pygame.mixer.Sound(sound_dir_path / "forfeit_reset.wav")
    #sound_reset.set_volume(1.0)
    
    # 5. ENCOURAGING RESTART CHIRP (Upward Scale/Power-up)
    # TRIGGER LOCATION: Inside the GAME_OVER loop right after arrays are cleared for a new game.
    #sound_restart = pygame.mixer.Sound(sound_dir_path / "new_game.wav")
    #sound_restart.set_volume(1.0)
    
    # 6. EXIT MELODY (Happy Trails Song)
    # TRIGGER LOCATION: Right at the very first line of the "def quit_game():" function.
    #sound_happy_trails = pygame.mixer.Sound(sound_dir_path / "Happy_Trails.wav")
    #sound_happy_trails.set_volume(1.0)
    
    #theme_music_path = str(sound_dir_path / "TheEnd.wav")
    #pygame.mixer.music.load(theme_music_path)
    #pygame.mixer.music.set_volume(0.4)                  
except Exception as e:
    sound_error = None
    sound_click = None
    sound_happy_trails = None
    sound_VietNam = None
    
    tile_click = None
    
    woosh - None
    
    sound_vic_crowd1 = None
    sound_vic_crowd2 = None
    sound_vic_crowd3 = None
    sound_vic_crowd4 = None
   
    sound_vic_fireworks1 = None
    sound_vic_fireworks2 = None
    sound_vic_fireworks3 = None
    sound_vic_fireworks4 = None
   
    sound_vic_music1 = None
    sound_vic_music2 = None
    sound_vic_music3 = None
    sound_vic_music4 = None
  
    #sound_victory = None
    #sound_clear = None
    #sound_reset = None
    #sound_restart = None
    #sound_happy_trails = None

    print(f"Warning: AI - One or more audio files not found. Audio disabled. Error: {e}")




#end of chunk 5


#begin chunk 6
# ====================================================================
# FIREWORKS ENGINE BLUEPRINT
# ====================================================================
class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        angle = random.uniform(0, 2 * math.pi)
        # Adjusted speed magnitudes for a punchy burst at 30 FPS
        speed = random.uniform(3, 9)
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.alpha = 255  
        # Controlled fade speed so they linger nicely
        self.fade_speed = random.uniform(4, 8)

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.15  # Gravity drifting downward
        self.alpha -= self.fade_speed

    def draw(self, surface):
        if self.alpha > 0:
            # Create a small surface to handle transparency fading
            p_surface = pygame.Surface((4, 4), pygame.SRCALPHA)
            # Cleanly unpack the RGB components from the tuple and add alpha
            color_with_alpha = (self.color[0], self.color[1], self.color[2], int(self.alpha))
            pygame.draw.circle(p_surface, color_with_alpha, (2, 2), 2)
            surface.blit(p_surface, (int(self.x), int(self.y)))        


class FireworkSystem:
    def __init__(self):
        self.particles = []

    def launch(self, x, y):
        color = random.choice([
            (255, 50, 50),   # Vibrant Red
            (50, 255, 50),   # Electric Green
            (50, 100, 255),  # Cyan Blue
            (255, 215, 0),   # Gold
            (255, 50, 255)   # Hot Pink
        ])
        for _ in range(50):  # 50 particles per burst is perfect for performance
            self.particles.append(Particle(x, y, color))

    def update_and_draw(self, surface):
        for p in self.particles[:]:
            p.update()
            if p.alpha <= 0:
                self.particles.remove(p)
            else:
                p.draw(surface)

    def clear_all(self):
        # Clears all elements instantly when leaving the screen
        self.particles.clear()



        
        
# ====================================================================
# INITIALIZE GLOBAL FIREWORKS ENGINE AND TIMERS
# ====================================================================
# Create the persistent manager object
celebration_fireworks = FireworkSystem()

# This tracks frames to stagger background bursts at 30 FPS
firework_timer = 0



# Keep your base SCALE_FACTOR fallback intact for existing font engines
desktop_w = pygame.display.get_desktop_sizes()[0][0]
SCALE_FACTOR = 1.0 if desktop_w <= SCREEN_WIDTH else (SCREEN_WIDTH / desktop_w)

#END OF CHUNK 6





#START CHUNK 7



# ==================================================================================
# NEW FONT INITIALIZATION AUGUST 01, 2026
# ==================================================================================
font_sz_72 = 72  
font_sz_64 = 64          
font_sz_48 = 48       
font_sz_32 = 32          
font_sz_24 = 24         
font_sz_20 = 20
font_sz_18 = 18
font_sz_16 = 16       
font_sz_14 = 14     

#  JULY 17  CHANGES (2ND SET) FOR HANDLING ASSET FOLDER ACCESS FOR FONTS START
assets_dir_path = bundle_dir / "assets"
sans_font_file  = assets_dir_path / "GameFont-Sans.ttf"
mono_font_file  = assets_dir_path / "GameFont-Mono.ttf"

try:
    # Attempt to load custom bundled fonts if they exist in the /assets folder
    # Wrapped paths in str() for older Pygame compatibility
    font_sz_72x = pygame.font.Font(str(sans_font_file), font_sz_72)
    font_sz_64x = pygame.font.Font(str(sans_font_file), font_sz_64)
    font_sz_48x = pygame.font.Font(str(sans_font_file), font_sz_48)
    font_sz_32x = pygame.font.Font(str(sans_font_file), font_sz_32)
    font_sz_24x = pygame.font.Font(str(sans_font_file), font_sz_24)
    font_sz_20x = pygame.font.Font(str(sans_font_file), font_sz_20)
    font_sz_18x = pygame.font.Font(str(sans_font_file), font_sz_18)
    font_sz_16x = pygame.font.Font(str(sans_font_file), font_sz_16)    
    font_sz_14x = pygame.font.Font(str(mono_font_file), font_sz_14)    
except Exception:
    # FIX: Converted raw strings into Python lists so Windows and Mac can resolve them natively
    sans_fallbacks = ["arial", "helvetica", "sans-serif"]
    mono_fallbacks = ["couriernew", "courier", "monospace"]

    # Safe system fallback structure if asset files are completely absent
    font_sz_72x = pygame.font.SysFont(sans_fallbacks, font_sz_72, bold=True)
    font_sz_64x = pygame.font.SysFont(sans_fallbacks, font_sz_64, bold=True) 
    font_sz_48x = pygame.font.SysFont(sans_fallbacks, font_sz_48, bold=True)
    font_sz_32x = pygame.font.SysFont(sans_fallbacks, font_sz_32, bold=True)  
    font_sz_24x = pygame.font.SysFont(sans_fallbacks, font_sz_24, bold=True)
    font_sz_20x = pygame.font.SysFont(sans_fallbacks, font_sz_20, bold=True)
    font_sz_18x = pygame.font.SysFont(sans_fallbacks, font_sz_18, bold=False)
    font_sz_16x = pygame.font.SysFont(sans_fallbacks, font_sz_16, bold=False)  
    font_sz_14x = pygame.font.SysFont(sans_fallbacks, font_sz_14, bold=True)
    font_sz_leaderboard = pygame.font.SysFont(mono_fallbacks, font_sz_20, bold=True)


pygame.display.set_caption("WONDER WORD Version 10")
CLOCK = pygame.time.Clock() 
#=============================DEFINE COLORS AND FONTS===============================

# --- COLORS (OPTIMIZED FOR HIGH CONTRAST DARK MODE) ---
BLACK = (24, 26, 27)         # Slate charcoal background (Easier to layer colors over)
BLACKLESS = (30, 30, 32) 	#BEST USED FOR GAME BOARDS INSTEAD OF SOLID BLACK	

WHITE = (255, 255, 255)
LIGHT_GRAY = (175, 180, 182) # Brightened up for column text and table borders

# ---Worksheet status grid colors
BG_GREEN = (46, 139, 87)     # Sea green for confirmed letters (!GHI)
BG_YELLOW = (212, 163, 89)   # Bright goldenrod for possible letters (+DEF)
BG_GRAY = (70, 75, 79)       # Medium charcoal gray for omitted letters (-ABC)

# ---High-contrast text updates
BOX_BORDER = (100, 105, 110)  # Distinct box frames

                            #OFF WHITE CHOICES
#TEXT_MAIN = (245, 245, 220) Cream: Soft, traditional, and easy on the eyes   
#TEXT_MAIN = (255, 255, 240) Ivory: Rich, classic white with a very subtle yellow undertone.   
#TEXT_MAIN = (242, 240, 235) Alabaster:  A popular, balanced architectural white. 
#TEXT_MAIN = (248, 248, 255) Ghost White: A very cool, crisp white with a tiny hint of blue.  
#TEXT_MAIN = (250, 250, 250) Snow White: Just a touch softer than pure white to cut the glare.
#TEXT_MAIN = (244, 244, 244) Isabelline: A popular, ultra-light grey-white used in modern user
#TEXT_MAIN = (245, 245, 220) Warm cream  

TEXT_MAIN = (248, 248, 255)   #Ghost White: A very cool, crisp white with a tiny hint of blue.
RED = (239, 83, 80)           # Vivid warning red

# Initialize the font module explicitly just in case it hasn't been called yet
pygame.font.init()

# Fake placeholder variables needed by display_score()
large_hint_bank = []
user_input = ""

#END OF CHUNK 7



#BEGIN CHUNK 8



 
# ==============================================================================
# MAIN GAME SPLASH SCREEN RENDERING ENGINE 
# ==============================================================================


def draw_main_splash_screen(player_name_input=""):
    """
    Renders the Wonder Word title screen, dynamic center-aligned elements, 
    developer warning narrative, high scores placeholder, and reactive input line.
    Uses pre-scaled global font variables to guarantee cross-platform accuracy.
    MODIFICATION: Draws directly onto the virtual canvas surface instead of SCREEN.
    """
    screen_center_x = SCREEN_WIDTH // 2
    
    # 1. Fill base canvas with your custom slate charcoal background (BLACK)
    canvas.fill(BLACKLESS)
    
    # 2. Draw Game Header Banner using your pre-scaled global font_title
    title_surf = font_sz_48x .render("W O N D E R   W O R D", True, BG_YELLOW, BLACKLESS)
    canvas.blit(title_surf, (screen_center_x - (title_surf.get_width() // 2), 20))
    
    tagline_surf = font_sz_20x.render('"A game of logic disguised as a word game"', True, BG_YELLOW, BLACKLESS)
    canvas.blit(tagline_surf, (screen_center_x - (tagline_surf.get_width() // 2), 90))
    
    # 3. Render Core Gameplay Concept Bullets using your pre-scaled  font_sz_16x
    bullets = [
        "• Discover the five letter 'secret word' using logical deduction.",
        "• Track matching letters and exact sequence positions.",
        "• A 'MASTERMIND' like board game — rebuilt with words instead",
        "  of colored pegs."
    ]
    curr_y = 120
    line_h = font_sz_20x.get_linesize() + 4
    for b_line in bullets:
        b_surf = font_sz_20x.render(b_line, True, TEXT_MAIN, BLACKLESS)
        canvas.blit(b_surf, (screen_center_x - 260, curr_y))
        curr_y += line_h
        
    # 4. Render Developer Warning Story Box (Uses font_sz_14x for clean structure)
    warning_box_y = curr_y + 30
    pygame.draw.rect(canvas, (40, 26, 27), (screen_center_x - 300, warning_box_y, 600, 110), border_radius=4)
    pygame.draw.rect(canvas, BG_YELLOW, (screen_center_x - 300, warning_box_y, 600, 110), width=1, border_radius=4)
    
    warn_lines = [
        "*** WARNING: Think twice before guessing 'ERROR' ***",
        "This brutal triple-letter trap broke a brilliant mathematician's ",
        "spirit, forcing them to quit a wartime postal word game match",
        "in absolute frustration!"
    ] 
    warn_y = warning_box_y + 8
    for w_line in warn_lines:
        cleaned_line = w_line.strip()
        color = BG_YELLOW if "WARNING" in cleaned_line else TEXT_MAIN
        w_surf = font_sz_20x.render(cleaned_line, True, color, (40, 26, 27))
        canvas.blit(w_surf, (screen_center_x - (w_surf.get_width() // 2), warn_y))
        warn_y += font_sz_20x.get_linesize() + 2


      # 5. Render Leaderboard Block
    leaderboard_y = warning_box_y + 130
    lead_title = font_sz_20x .render("--- ALL TIME TOP SCORES ---", True, TEXT_MAIN, BLACKLESS)
    canvas.blit(lead_title, (screen_center_x - (lead_title.get_width() // 2), leaderboard_y))
    
    scores_data = [
        ("1.", "HITLER", "298,420"),
        ("2.", "OTTO SWARTZ", "295,100"),
        ("3.", "D TRUMP", "111,250")
    ]
    score_y = leaderboard_y + 30
    
    # Tightened width slightly to match the smaller text size beautifully
    total_leaderboard_width = 280 
    left_margin_x = screen_center_x - (total_leaderboard_width // 2)
    right_margin_x = screen_center_x + (total_leaderboard_width // 2)
    
    for rank, name, score in scores_data:
        # SWITCHED: Now using font_sz_16x for a smaller, crisp layout
        name_surf = font_sz_16x.render(f"{rank}  {name}", True, LIGHT_GRAY, BLACKLESS)
        score_surf = font_sz_16x.render(score, True, LIGHT_GRAY, BLACKLESS)
        
        # Blit columns using our locked margins
        canvas.blit(name_surf, (left_margin_x, score_y))
        
        final_score_x = right_margin_x - score_surf.get_width()
        canvas.blit(score_surf, (final_score_x, score_y))
        
        # Step down using the normal body text line size
        score_y += font_sz_16x.get_linesize() + 4    
        
  
    # 6. Render Footer Prompt Action Line
    footer_y = SCREEN_HEIGHT - 100
    help_prompt = font_sz_18x.render("[ Type 'HELP' during play for game instructions ]", True, BG_YELLOW, BLACKLESS)
    canvas.blit(help_prompt, (screen_center_x - (help_prompt.get_width() // 2), footer_y))
    
    # 7. Interactive Name Entry Line
    input_prompt = f">>> ENTER YOUR NAME TO BEGIN PLAYING: {player_name_input}_"
    input_surf = font_sz_18x.render(input_prompt, True, BG_YELLOW, BLACKLESS)
    canvas.blit(input_surf, (screen_center_x - (input_surf.get_width() // 2), footer_y + 55)) 
 
#END OF CHUNK 8
    
    
    
    
    
#BEGIN CHUNK 9    
    
# ==============================================================================
# SECRET ORIGIN STORY SCREEN RENDERING ENGINE  
# ==============================================================================
def draw_origin_story_screen():
    """
    Renders the safe wartime backstory when the user inputs the word 'ERROR'.
    Uses pre-scaled global variables to handle cross-platform screen layouts.
    MODIFICATION: Draws directly onto the virtual canvas surface instead of SCREEN.
    """
     
    
    screen_center_x = SCREEN_WIDTH // 2
    
    # 1. Fill base canvas with your custom slate charcoal background (BLACKLESS)
    canvas.fill(BLACKLESS)
    

    # 2. Render Header Banner using your pre-scaled global font
    # FIXED: Added BLACKLESS to fix ghost pixels on title
    title_surf = font_sz_32x.render("THE ORIGIN OF WONDER WORD", True, BG_YELLOW, BLACKLESS)
    canvas.blit(title_surf, (screen_center_x - (title_surf.get_width() // 2), 10))
    
    # 3. Setup Layout Alignment and Line Spacing
    story_left_x = 60  
    
    # FIXED: Reverted vertical spacing math to original size while retaining a clean look
    text_h = font_sz_20x.get_linesize() + 2
    curr_y = 45
    
    # RESTORED: Kept your exact divider line string length
    divider_line = "------------------------------------------------------------------------------------------"
    
    # Streamlined list matching your exact history, capped to safe character widths
    story_paragraphs = [
        "This game was born long before digital apps or modern board games.",
        "While serving in Vietnam, a U.S. Serviceman received a church care package",
        "containing a letter from a stranger—a brilliant Mathematics student. They",
        "began a battle of minds through the mail, playing a custom game of logic.",
        "Letters took weeks to travel the Pacific, making every single guess critical.",        
        divider_line,
        "THE 'ERROR' INCIDENT:",
        "You just guessed the word 'ERROR'. This triple-R repetition string was",
        "deployed as a logical weapon during that wartime mail exchange. The math ",
        "required to decipher it was so brutally complex and frustrating that the ",
        "Mathematician promptly quit the match in protest!",
        divider_line,
        "THE MAINFRAME EVOLUTION:",
        "In the late 1970s, this same Serviceman brought the game to life on an IBM",
        "mainframe—compiling it in COBOL with a custom CICS interactive interface.",
        "",
        "Now, this same 78-year-old developer is bringing this piece of history",
        "back to life using a more modern programming language...... Python.",
        "",
        "Pure deduction, a bit of psychological warfare, and a true story."
    ]
    
    # Loop over and render lines using font_sz_20x to keep it uniform
    for line in story_paragraphs:
        # Highlight important headings in gold
        if "INCIDENT:" in line or "EVOLUTION:" in line:
            # FIXED: Added BLACKLESS to heading render
            line_surf = font_sz_18x.render(line, True, BG_YELLOW, BLACKLESS)
        else:
            # FIXED: Added BLACKLESS to body text render
            line_surf = font_sz_18x.render(line, True, WHITE, BLACKLESS)
            
        # RESTORED: All text, including the divider line, aligns left to story_left_x
      
        canvas.blit(line_surf, (story_left_x, curr_y))
        curr_y += text_h
        
    # 4. Prompt footer to return to the active puzzle match
    footer_y = SCREEN_HEIGHT - 50
    # FIXED: Added BLACKLESS to footer prompt render
    prompt_surf =  font_sz_16x.render("[ PRESS ENTER TO RESUME THE GAME ]", True, BG_YELLOW, BLACKLESS)
    canvas.blit(prompt_surf, (screen_center_x - (prompt_surf.get_width() // 2), footer_y))
    

#END OF CHUNK 9


#BEGIN CHUNK 10

HELP_DATA = {
    1: {
        "title": "BASIC GAMEPLAY",
        "page_num": "Page 1 of 5",
        "rect": (35, 35, 330, 550),
        "text_x": 390,
        "text_y": 10,
        "lines": [
            "Your objective is to guess a five-letter secret word known as the",
            "'Wonder Word'. Type your name to begin, then enter any valid",
            "five-letter word as your first guess. The 'WORDS GUESSED' column",
            "can be scrolled.",
            "",
            "The game compares your guess to the 'Wonder Word' and returns:",
            "  • MATCHES: Total letters shared between your guess and the secret word.",
            "  • SEQ    : How many of those matching letters are in their correct position. ", 
            "",            
            "Example: If the 'Wonder Word' is 'APPLE' and you enter 'STORE',",
            "the game returns the following information:",
            "",          
            "                WORD          MATCHES         SEQ",
            "                ----------------------------------------------",
            "                STORE               1                    1",           
            "",
            "Input Entry_ ",
            "Use this line to type your name, game commands, or worksheet updates.",                                   
            "",
            "                       PRESS ENTER TO RETURN TO INDEX"
        ]
    },

    2: {
        "title": "SCORING",
        "page_num": "Page 2 of 5",        
        "rect": (35, 440, 310, 135),
        "text_x": 380,
        "text_y":  50,
        "lines": [
            "You start each game with a bank of 500,000 points.",
            "      • Point deductions increase progressively per guess:",
            "          Guesses 01 - 05:  -200 points",
            "          Guesses 06 - 10:  -1,000 points",
            "          Guesses 11 - 14:  -2,000 points",
            "          Guesses >= 15:    -5,000 points",
            "",
            "      • Timer Penalty: -2 points for every elapsed second.",
            "",
            "If your score drops to zero, the game instantly ENDS.",
            "",
            "Score enough poinsts and secure a spot on the 'ALL TIME",
            "TOP SCORES' leaderboard!",
            "",
            "Input Entry_",
            "Use this line to type your name, game commands, or worksheet updates.",
            "",
            "",
            "                  PRESS ENTER TO RETURN TO INDEX"
        ]
    },

    3: {
        "title": "               KEYBOARD COMMANDS & ICONS",
        "page_num": "Page 3 of 5",
        "rect": (840, 1, 150, 45),
        "text_x": 280,
        "text_y": 100,
        "lines": [
            "",
            "Type these specific commands directly into 'Input Entry_'",
            "",
            "  • 'RESET'   - End the active session (or click the 'R' icon circle)",
            "",
            "  • 'HINT'    - Reveal an unknown letter (or click the 'H' icon circle)",
            "",
            "  • 'HELP'    - Open the help screen (or click the '?' incon circle)",
            "",
            "  • 'TIMEOUT' - Pause the game timer (Limit: 2 breaks per match).",
            "",
            "",
            "",
            "                       PRESS ENTER TO RETURN TO INDEX"           
        ]
    },

    4: {
        "title": "",
        "page_num": "Page 4 of 5",
        "rect": (390, 40, 480, 350),
        "text_x": 10,
        "text_y": 10,
        "lines": [
           "Use the WORKSHEET matrix to visually track",  
           "your letter theories with your mouse or",
           "keyboard:",
           "",
           "Each 'RIGHT' button mouse click on a letter",
           "in the WORKSHEET will rotate the letter ",
           "through 4 colors",
           "",
           "            •  Mouse click 1 = GREEN",
           "            •  Mouse click 2 = YELLOW", 
           "            •  Mouse click 3 = GRAY", 
           "            •  Mouse click 4 = BLACK", 
           "",                   
           "                     KEYBOARD COMMANDS",
           "  • GRAY   (-ABC) = Letters NOT in the word. (Precede with '-')",
           "  • YELLOW (+DEF) = Letters that MIGHT be in the word. (Precede with '+')", 
           "  • GREEN  (!GHI) = Letters definitely IN the word. (Precede with '!')",
           "",
           "After 20 guesses, the game will begin to make 'SUGGESTED GUESSES' to assit you.",
           "",
           "                       PRESS ENTER TO RETURN TO INDEX"
        ]
    },


#END OF CHUNK 10


#begin chunk 11

    5: {
        "title": "               HINTS & DIGITAL SCRATCHPAD",
        "page_num": "Page 5 of 5",
        "rect": (470, 375, 340, 200),
        "text_x": 20,
        "text_y": 20,
        "lines": [ 
            "You can request hints, but they progressively cost more points:",
            "  • 1st Hint:   -1,000 points (Available after 4 guesses)", 
            "  • 2nd Hint:  -3,000 points (Available after 14 guesses)",
            "  • 3rd Hint:  -5,000 points (Available after 19 guesses)",
            "  • 4th Hint: -10,000 points (Available after 29 guesses)", 
            "Revealed hints automatically lock letters into the HINTS and the",
            "'DIGITAL SCRATCHPAD' slots.",
            "",
            "The DIGITAL SCRATCHPAD is your virtual pen and paper. Use it",
            "freely to test letter arrangements before making a guess.",
            "To organize letters, use the pound sign (#) followed by the letter",
            "and the slot number (1 through 5):", 
            "  • Example: #L4 places the letter L into Slot 4 (_ _ _ L _).",
            "  • Erase a letter: Type # + SPACE + SLOT NUMBER.",
            "  • Example: # 4 clears Slot 4, making it blank again.", 
            "",
            "In addition, a mouse can be used to drag/drop letters", 
            "from the WORKSHEET to the DIGITAL SCRATCHPAD.",
            "Also, drag/drop can be used within the scratchpad.",
            "",
            "                       PRESS ENTER TO RETURN TO INDEX"
        ]
    },

    6: {
        "title": "HELP INDEX",
        "page_num": "",
        "rect": (0, 0, 0, 0),
        "text_x": 300,
        "text_y": 50,
        "lines": [
            "Select a topic by pressing the corresponding number key:",
            "",
            "  1. BASIC GAMEPLAY",
            "  2. SCORING",
            "  3. KEYBOARD COMMANDS & ICONS",
            "  4. WORKSHEET",
            "  5. HINTS & DIGITAL SCRATCHPAD",
            "",
            "",
            "            PRESS ENTER TO RETURN TO GAME"
        ]
    }
}    



#end chunk 11



#BEGIN CHUNK 12


# ==============================================================================
# MODERN SPOTLIGHT OVERLAY RENDERING ENGINE (DYNAMIC CROSS-PLATFORM CENTERING)
# ==============================================================================


def draw_help_overlay():
    # ------------------------------------------------------------------
    # NEW VARIABLE CHECK: Override layout if the help index is active
    # ------------------------------------------------------------------
    if 'show_help_index' in globals() and show_help_index:
        page_info = HELP_DATA[6]  # Force-route to the Index page layout
    else:
        # Fallback validation check for your standard pages 1-5
        if show_help_overlay not in HELP_DATA:
            return
        page_info = HELP_DATA[show_help_overlay]
    
    # 1. Capture a clean snapshot copy of the existing board graphics onto the canvas
    canvas.blit(base_snapshot, (0, 0))
    
    # 2. Instantiate our alpha canvas sheet across the native 1000x600 size
    mask = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    mask.fill((12, 14, 15, 225)) # Smooth matte dark shading
    
    # 3. Punch a clear window hole ONLY if a valid highlight box is specified
    if page_info["rect"] and page_info["rect"] != (0, 0, 0, 0):
        pygame.draw.rect(mask, (0, 0, 0, 0), page_info["rect"])
    
    # Commit mask onto canvas viewport display
    canvas.blit(mask, (0, 0))
    
    # 4. Draw bright Cyan border outline ONLY if a valid spotlight zone exists
    if page_info["rect"] and page_info["rect"] != (0, 0, 0, 0):
        pygame.draw.rect(canvas, (0, 255, 255), page_info["rect"], width=3)
    
    # 5. Use pre-scaled global font mappings to ensure unified appearance
    font_title_smooth = font_sz_24x
    font_body_smooth = font_sz_18x
    
    start_x = page_info["text_x"]
    start_y = page_info["text_y"]
    
    # --- MAC COMPATIBILITY FIX: Calculate Dynamic Text Center Line ---
    max_body_width = 0
    for line in page_info["lines"]:
        if "PRESS ENTER" not in line and line.strip() != "":
            line_w = font_body_smooth.size(line)[0]
            if line_w > max_body_width:
                max_body_width = line_w
                
    if max_body_width == 0:
        max_body_width = 400
    
    # Establish the absolute mathematical center point for titles/prompts
    text_center_x = start_x + (max_body_width // 2)
    
    # Clean the title string of hardcoded spaces and center it perfectly
    clean_title = page_info["title"].strip()
    
    # FIXED: Added (12, 14, 15) to title text rendering
    title_surf = font_title_smooth.render(clean_title, True, BG_YELLOW, (12, 14, 15))
    title_x = text_center_x - (title_surf.get_width() // 2)
    canvas.blit(title_surf, (title_x, start_y))
    
    # Dynamic Font Line Spacing
    line_height = font_body_smooth.get_linesize() + 4 
    
    # Loop over text rows line-by-line using custom screen offset trackers
    curr_y = start_y + 35
    for line in page_info["lines"]:
        if "PRESS ENTER" in line or "RETURN TO GAME" in line:
            # Anchor prompt markers cleanly highlighted at the bottom center
            # FIXED: Added (12, 14, 15) to prompt text rendering
            line_surf = font_body_smooth.render(line.strip(), True, BG_YELLOW, (12, 14, 15))
            line_x = text_center_x - (line_surf.get_width() // 2)
            canvas.blit(line_surf, (line_x, curr_y + 10))
        else:
            # Draw primary informational body lines left-aligned to column boundaries
            # FIXED: Added (12, 14, 15) to body text rendering
            line_surf = font_body_smooth.render(line, True, TEXT_MAIN, (12, 14, 15))
            canvas.blit(line_surf, (start_x, curr_y))
        curr_y += line_height
        
    # Draw page numbers cleanly positioned in the upper right quadrant
    if "page_num" in page_info and page_info["page_num"] != "":
        # FIXED: Added (12, 14, 15) to page number rendering
        page_surf = font_body_smooth.render(page_info["page_num"], True, LIGHT_GRAY, (12, 14, 15))
        canvas.blit(page_surf, (SCREEN_WIDTH - page_surf.get_width() - 35, 535))

#END CHUNK 12
        
        
#BEGIN CHUNK 15        


# ---  RESET ICON BUTTON CONFIGURATION ---
reset_btn_x = SCREEN_WIDTH - 140
reset_btn_y = 30
reset_btn_radius = 15

# --- HINT ICON BUTTON CONFIGURATION ---
hint_btn_x = SCREEN_WIDTH - 90  
hint_btn_y = 30                 
hint_btn_radius = 15    

# --- HELP ICON BUTTON CONFIGURATION ---
help_btn_center = (SCREEN_WIDTH - 40, 30) 
help_btn_radius = 15

# Graphical toggle for HELP screen  
show_help_overlay = False


def draw_worksheet(words_entered, letters_not_in_word, letters_might_be_in_word, letters_in_word, scroll_index):
    canvas.fill(BLACKLESS)
    
    # ------------------------------------------------------------
    # 1. DRAW GUESS HISTORY (LEFT SIDE - FIXED COLUMN COLUMNS)
    # ------------------------------------------------------------
    start_x = 45
    start_y = 50
    
    col1_x = 65       
    col2_x = start_x + 115 
    col3_x = start_x + 240 
    
    # Header Title
    title_surface = font_sz_32x.render("-WORDS GUESSED-", True, TEXT_MAIN, BLACKLESS)
    canvas.blit(title_surface, (start_x, start_y))

    # Draw Headers Individually at Fixed Anchors
    canvas.blit(font_sz_20x.render("WORD", True, LIGHT_GRAY, BLACKLESS), (col1_x, start_y + 40))
    canvas.blit(font_sz_20x.render("MATCHES", True, LIGHT_GRAY, BLACKLESS), (col2_x, start_y + 40))
    canvas.blit(font_sz_20x.render("SEQ", True, LIGHT_GRAY, BLACKLESS), (col3_x, start_y + 40))
    
    # Divider line beneath headers
    pygame.draw.line(canvas, BG_GRAY, (start_x - 3, start_y + 65), (start_x + 310, start_y + 65), 2)
    
    # History Entries Loop - SLICED TO A MAXIMUM OF 10 ITEMS
    current_y = start_y + 80
    for entry in words_entered[scroll_index : scroll_index + 10]:
        word_str = str(entry[0])
        matches_str = str(entry[1])
        seq_str = str(entry[2])
        
        canvas.blit(font_sz_20x.render(word_str, True, TEXT_MAIN, BLACKLESS), (col1_x, current_y))
        canvas.blit(font_sz_20x.render(matches_str, True, TEXT_MAIN, BLACKLESS), (col2_x + 40, current_y)) 
        canvas.blit(font_sz_20x.render(seq_str, True, TEXT_MAIN, BLACKLESS), (col3_x + 15, current_y))
        
        canvas.blit(font_sz_16x.render("|", True, BG_GRAY, BLACKLESS), (col1_x - 20, current_y))
        canvas.blit(font_sz_16x.render("|", True, BG_GRAY, BLACKLESS), (col1_x + 85, current_y))
        canvas.blit(font_sz_16x.render("|", True, BG_GRAY, BLACKLESS), (col1_x + 190, current_y))
        canvas.blit(font_sz_16x.render("|", True, BG_GRAY, BLACKLESS), (col2_x + 190, current_y))
        
        current_y += 30

    # ----------------------------------------------------
    # 2. DRAW WORKSHEET KEYBOARD (RIGHT SIDE)
    # ----------------------------------------------------
    layout = ["ABCDEFG", "HIJKLMN", "OPQRSTU", "VWXYZ"]
    keyboard_start_x = 450
    keyboard_start_y = 50
    
    box_size = 45
    spacing = 10
   
    ws_title_surface = font_sz_32x.render("--- WORKSHEET ---", True, TEXT_MAIN, BLACKLESS)
    grid_width = (7 * box_size) + (6 * spacing)
    grid_center_x = keyboard_start_x + (grid_width // 2)
    ws_title_rect = ws_title_surface.get_rect(center=(grid_center_x, keyboard_start_y + 15))
    canvas.blit(ws_title_surface, ws_title_rect)
   
    # Loop through grid rows
    for row_idx, row in enumerate(layout):
        for col_idx, char in enumerate(row):
            box_x = keyboard_start_x + (col_idx * (box_size + spacing))
            box_y = keyboard_start_y + 80 + (row_idx * (box_size + spacing))
            
            if char in letters_in_word:
                box_color = BG_GREEN
                text_color = WHITE
            elif char in letters_might_be_in_word:
                box_color = BG_YELLOW
                text_color = WHITE
            elif char in letters_not_in_word:
                box_color = BG_GRAY
                text_color = WHITE   
            else:
                box_color = BLACK
                text_color = TEXT_MAIN
                
            pygame.draw.rect(canvas, box_color, (box_x, box_y, box_size, box_size))
            pygame.draw.rect(canvas, BOX_BORDER, (box_x, box_y, box_size, box_size), 2)

            char_surface = font_sz_20x.render(char, True, text_color, box_color)
            char_rect = char_surface.get_rect(center=(box_x + box_size // 2, box_y + box_size // 2))
            
            char_rect.x = int(char_rect.x)
            char_rect.y = int(char_rect.y)
            canvas.blit(char_surface, char_rect)

#END CHUNK 15


#BEGIN CHUNK 16


    # ==================== HINT BOXES =================================
    hint_row_idx = 4  
    extra_y_offset = 60  
    section_base_y = keyboard_start_y + 80 + (hint_row_idx * (box_size + spacing)) + extra_y_offset

    shift_right = 1 * (box_size + spacing)
    hints_title_surface = font_sz_20x.render("HINTS", True, LIGHT_GRAY, BLACKLESS)
    hints_title_center_x = keyboard_start_x + shift_right + ((box_size * 5 + spacing * 4) // 2)
    hints_title_rect = hints_title_surface.get_rect(center=(hints_title_center_x, section_base_y - 20))
    canvas.blit(hints_title_surface, hints_title_rect)

    for box_idx in range(5):
        hint_box_x = keyboard_start_x + shift_right + (box_idx * (box_size + spacing))
        hint_box_y = section_base_y
     
        hint_rect = pygame.Rect(hint_box_x, hint_box_y, box_size, box_size)
        pygame.draw.rect(canvas, BLACK, hint_rect)
        pygame.draw.rect(canvas, BOX_BORDER, hint_rect, 2)
    
        if box_idx in revealed_indices and box_idx < len(hold_secret_word):
            secret_letter = hold_secret_word[box_idx].upper()
            secret_surface = font_sz_20x.render(secret_letter, True, BG_GREEN, BLACK)
            secret_rect = secret_surface.get_rect(center=hint_rect.center)
            canvas.blit(secret_surface, secret_rect) 

    # ==================== DIGITAL SCRATCHPAD BOXES =================================
    seq_row_idx = 4
    seq_y_offset = 140 
    seq_base_y = keyboard_start_y + 80 + (seq_row_idx * (box_size + spacing)) + seq_y_offset
 
    seq_center_x = keyboard_start_x + shift_right + ((box_size * 5 + spacing * 4) // 2)
    seq_title_surface = font_sz_20x.render("DIGITAL SCRATCHPAD", True, LIGHT_GRAY, BLACKLESS)
    seq_title_rect = seq_title_surface.get_rect(center=(seq_center_x, seq_base_y - 20))
    canvas.blit(seq_title_surface, seq_title_rect)
 
    for seq_idx in range(5):
        seq_box_x = keyboard_start_x + shift_right + (seq_idx * (box_size + spacing))
        seq_box_y = seq_base_y
     
        seq_rect = pygame.Rect(seq_box_x, seq_box_y, box_size, box_size)
        pygame.draw.rect(canvas, BLACK, seq_rect)
        pygame.draw.rect(canvas, BOX_BORDER, seq_rect, 2)
     
        tracked_letter = dig_scratch_pad_slots[seq_idx]
        if tracked_letter != " ":
            seq_char_surface = font_sz_20x.render(tracked_letter, True, TEXT_MAIN, BLACK)
            seq_char_rect = seq_char_surface.get_rect(center=seq_rect.center)
            canvas.blit(seq_char_surface, seq_char_rect)
                     
    # ====================================================================
    # HOVER HIGHLIGHTING SYSTEM (ADD BEFORE THE TILE IS DRAWN)
    # ====================================================================
    if dragging_letter is not None:
        for seq_idx in range(5):
            seq_box_x = keyboard_start_x + shift_right + (seq_idx * (box_size + spacing))
            slot_rect = pygame.Rect(seq_box_x, seq_base_y, box_size, box_size)
            
            if slot_rect.collidepoint(drag_pos):
                pygame.draw.rect(canvas, BG_YELLOW, slot_rect, 3)        

    # ====================================================================
    # DRAGGING FLOATING TILE RENDERING
    # ====================================================================
    if dragging_letter is not None:
        drag_rect = pygame.Rect(drag_pos[0] - 22, drag_pos[1] - 22, 45, 45)
        
        pygame.draw.rect(canvas, BLACK, drag_rect)
        pygame.draw.rect(canvas, BOX_BORDER, drag_rect, 2)
        
        drag_surface = font_sz_20x.render(dragging_letter, True, TEXT_MAIN, BLACK)
        drag_char_rect = drag_surface.get_rect(center=drag_rect.center)
        canvas.blit(drag_surface, drag_char_rect)

#END CHUNK 16
        
        
        
#BEGIN CHUNK 17        
        
# ==============================================================================
# UPDATED RENDERING ENGINE FUNCTION
# ==============================================================================
def display_score(): 
    # FIXED: Added BLACKLESS to score and guess text meters
    points_surface = font_sz_18x.render(f"Score: {max(0, points)}", True, BG_YELLOW, BLACKLESS)
    canvas.blit(points_surface, (50, 450)) 

    number_guesses_surface = font_sz_18x.render(f"Guess #: {max(0, number_of_guesses)}", True, BG_YELLOW, BLACKLESS)
    canvas.blit(number_guesses_surface, (190, 450))

    max_chars_per_line = 42 # Safely breaks text before hitting right-side boxes
    if len(feedback_message) > max_chars_per_line:
        # Find the last space within the limit to avoid breaking words
        split_idx = feedback_message.rfind(' ', 0, max_chars_per_line)
        if split_idx == -1: 
            split_idx = max_chars_per_line 
        line1 = feedback_message[:split_idx]
        line2 = feedback_message[split_idx:].strip() 
        
        # FIXED: Added BLACKLESS to wrapped text surfaces
        status_surface_1 = font_sz_18x.render(line1, True, WHITE, BLACKLESS)
        status_surface_2 = font_sz_18x.render(line2, True, WHITE, BLACKLESS)
        canvas.blit(status_surface_1, (50, 480))
        canvas.blit(status_surface_2, (50, 505)) 
    else:
        # FIXED: Added BLACKLESS to single line text surfaces
        status_surface = font_sz_18x.render(feedback_message, True, WHITE, BLACKLESS) 
        canvas.blit(status_surface, (50, 480)) 
        
    # --- CROSS-PLATFORM INPUT SAFETY CHECK ---
    try:
        active_input = user_input
    except NameError:
        active_input = hold_user_input

    # FIXED: Added BLACKLESS to your interactive text input line
    input_surface = font_sz_18x.render(f"Input Entry: {active_input}_", True, WHITE, BLACKLESS)
    canvas.blit(input_surface, (50, 540)) 

    # --- STRATEGIC TIPS (ACTIVATES ONLY ON GUESS 11 OR LATER) ---
    if number_of_guesses > 10:
        # FIXED: Added BLACKLESS to the suggested guesses header line
        tips_header = font_sz_18x.render("SUGGESTED GUESSES: ", True, BG_YELLOW, BLACKLESS)
        canvas.blit(tips_header, (445, 355))
                
        # Calculate the words using the pre-loaded large dictionary list
        strategic_tips = get_strategic_hints(large_hint_bank, letters_not_in_word, 
        letters_in_word, letters_might_be_in_word, hold_secret_word, top_n=2)
        
        # 3. RESTORED: Returned tips_str back to your original suggested_hints mapping
        if strategic_tips:
            tips_str = ", ".join(suggested_hints)
            header_width = tips_header.get_width()        
            
            # FIXED: Added BLACKLESS to hint choices text string content
            tips_content = font_sz_18x.render(tips_str, True, BG_YELLOW, BLACKLESS)
            canvas.blit(tips_content, (445 + header_width + 10, 355))

#END CHUNK 17
            
            
#START CHUNK 18            

# ==============================================================================
# CROSS-PLATFORM LEADERBOARD MAINTENANCE ENGINE
# ==============================================================================                 
def clear_high_scores():
    
    global score_file_path
    
    try:
        with open(score_file_path, 'w', encoding="utf-8") as f:
            pass           
    except Exception as e:
        pass


# ==============================================================================
# 4. LEADERBOARD RENDERING & RETRIEVAL ENGINE  
# ==============================================================================

def draw_high_scores():
    
    
    global score_file_path
     
     
    # Clear with Slate Charcoal background
    canvas.fill(BLACKLESS) 

    # RENDER VISUAL FIREWORKS LAYER HERE
    # NOTE: By placing the fireworks update call right here, after the background is cleared 
    # but BEFORE the text fields are blitted, your particles will realistically burst and drift 
    # behind your score rankings and text windows without washing out the text readability!
    # update_and_draw_fireworks(active_fireworks, canvas)
   
    #if sound_vic_crowd2: sound_vic_crowd2.play()
      
    #if sound_vic_fireworks4: sound_vic_fireworks4.play()
    
    #if sound_vic_music4: sound_vic_music4.play()


    # Render the title surface
    title_surface = font_sz_48x.render("----- ALL TIME TOP SCORES -----", True, BG_YELLOW, BLACKLESS)

    # Dynamically calculate the centered X position
    canvas_width = canvas.get_width()
    center_x = (canvas_width - title_surface.get_width()) // 2

    # Blit using the calculated center_x
    canvas.blit(title_surface, (center_x, 50))
                         
    # --- 2. THE SHARED COORDINATE DICTIONARY ---
    COL_X = {
        'rank': 160,
        'name': 237,  
        'score': 368,  
        'guesses': 460,  
        'time': 610, 
        'date': 730
    }
    
    # --- 3. PRINT HEADERS ---
    header_y = 125
    canvas.blit(font_sz_24x.render("RANK", True, LIGHT_GRAY, BLACKLESS), (COL_X['rank'], header_y))
    canvas.blit(font_sz_24x.render("NAME", True, LIGHT_GRAY, BLACKLESS), (COL_X['name'], header_y))
    canvas.blit(font_sz_24x.render("SCORE", True, LIGHT_GRAY, BLACKLESS), (COL_X['score'], header_y))
    canvas.blit(font_sz_24x.render("# GUESSES", True, LIGHT_GRAY, BLACKLESS), (COL_X['guesses'], header_y)) 
    canvas.blit(font_sz_24x.render("MINUTES", True, LIGHT_GRAY, BLACKLESS), (COL_X['time'], header_y))
    canvas.blit(font_sz_24x.render("DATE / TIME", True, LIGHT_GRAY, BLACKLESS), (COL_X['date'], header_y))
    
    pygame.draw.line(canvas, BG_GRAY, (140, 155), (845, 155), 2)
    
    scores = []
    try:
        with open(score_file_path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    scores.append((int(parts[0]), parts[1], parts[2], parts[3], parts[4]))
        
        scores.sort(key=lambda x: x[0], reverse=True)               
       
        # --- 4. PRINT ROW DATA USING THE EXACT SAME DICTIONARY KEYS ---
        COL_Xx = {
            'rank': 172,
            'name': 242,  
            'score': 374,  
            'guesses': 530,  
            'time': 650, 
            'date': 720
        }
                               
        current_y = 185
        for i, (s, n, g, t, dt) in enumerate(scores[:10], 1):                                    
            canvas.blit(font_sz_20x.render(str(i), True, TEXT_MAIN, BLACKLESS), (COL_Xx['rank'], current_y))
            canvas.blit(font_sz_20x.render(str(n), True, TEXT_MAIN, BLACKLESS), (COL_Xx['name'], current_y))
            canvas.blit(font_sz_20x.render(str(s), True, TEXT_MAIN, BLACKLESS), (COL_Xx['score'], current_y))
            canvas.blit(font_sz_20x.render(str(g), True, TEXT_MAIN, BLACKLESS), (COL_Xx['guesses'], current_y)) 
            canvas.blit(font_sz_20x.render(str(t), True, TEXT_MAIN, BLACKLESS), (COL_Xx['time'], current_y))                  
            canvas.blit(font_sz_20x.render(str(dt), True, TEXT_MAIN, BLACKLESS), (COL_Xx['date'], current_y))                 
            current_y += 25 
 
 
 
 
 #END CHUNK 18
 
 
#START 19 
    except Exception as e:
        error_surface = font_sz_16x.render(f"Could not load leaderboard: {e}", True, RED, BLACKLESS)
        canvas.blit(error_surface, (220, 180))
        
    # --- 5. FOOTER TEXT ---
    # FIXED BUG: Removed the hardcoded local overwrite so your global "CONGRATULATIONS!" message 
    # can actually display cleanly when called from the main game loop sequence triggers.
    
    points_surface = font_sz_18x.render(f"Score: {max(0, points)}", True, BG_YELLOW, BLACKLESS)
    canvas.blit(points_surface, (50, 465)) 
    
    number_guesses_surface = font_sz_18x.render(f"Guess #: {max(0, number_of_guesses)}", True, BG_YELLOW, BLACKLESS)
    canvas.blit(number_guesses_surface, (190, 465)) 

    # Blits your global variable text instead of the old hardcoded duplicate string
    status_surface = font_sz_18x.render(feedback_message, True, WHITE, BLACKLESS) 
    canvas.blit(status_surface, (50, 495)) 
    
    try:
        active_input = user_input
    except NameError:
        active_input = hold_user_input

    input_surface = font_sz_18x.render(f"Input Entry: {active_input}_", True, WHITE, BLACKLESS)
    canvas.blit(input_surface, (50, 545)) 


#INSERT NEW CODE START
def save_high_score(name, final_score, total_guesses, seconds):
    global score_file_path
    safe_name = str(name).replace(",", "")
    timestamp = datetime.datetime.now().strftime("%m/%d/%y  %I:%M%p ")
        
    # --- SAFETY WRAPPER: Prevents crashes on protected operating systems ---
    try:
        with open(score_file_path, "a", encoding="utf-8") as f:
            f.write(f"{final_score},{safe_name},{total_guesses},{seconds},{timestamp}\n")    
    except Exception as e:
        print(f"[PERMISSION ALERT] File write blocked by OS: {e}")
        print("[DEBUG] Bypassing file update to keep the game loop running.")
    
    # --- LEADERBOARD SORTING AND TRUNCATION ENGINE ---
    scores = []
    try:
        with open(score_file_path, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 5:
                    # FIXED: Added the correct index numbers [0] through [4] so it reads data perfectly
                    scores.append((int(parts[0]), parts[1], parts[2], parts[3], parts[4]))
        
        scores.sort(key=lambda x: x[0], reverse=True)
       
        # FIXED: Changed back to your original format to keep all your leaderboard entries safe
        with open(score_file_path, "w", encoding="utf-8") as f:
            for s, n, g, t, dt in scores[:9]:
                f.write(f"{s},{n},{g},{t},{dt}\n")
    except Exception as e:
        print(f"[DEBUG] Leaderboard memory array parse warning: {e}") 






#INSERT NEW CODE STOP








        
        
        
        
        


#START CHUNK 20

# --- DRAW THE RESET ICON BUTTON ---
def draw_reset_icon():
    # 1. Draw the clean outer structural circle background frame
    pygame.draw.circle(canvas, (50, 150, 200), (reset_btn_x, reset_btn_y), reset_btn_radius)
    
    # --- MAC COMPATIBILITY FIX: Reusing your main game's pre-scaled structural font block ---
    # Centered flawlessly inside the geometric circle via an explicit Rect object
    reset_text =  font_sz_16x.render("R", True, WHITE)
    reset_rect = reset_text.get_rect(center=(reset_btn_x, reset_btn_y))  
    canvas.blit(reset_text, reset_rect)  
    
# --- DRAW THE HINT ICON BUTTON ---
def draw_hint_icon(): 
    pygame.draw.circle(canvas, (200, 150, 50), (hint_btn_x, hint_btn_y), hint_btn_radius)           
    
    # --- MAC COMPATIBILITY FIX: Avoid SysFont(None, bold=True) height shifting ---
    hint_text =  font_sz_16x.render("H", True, WHITE)
    hint_rect = hint_text.get_rect(center=(hint_btn_x, hint_btn_y))  
    canvas.blit(hint_text, hint_rect)     


# --- DRAW THE HELP ICON BUTTON --- 
def draw_help_icon():           
    pygame.draw.circle(canvas, WHITE, help_btn_center, help_btn_radius, 2)
    
    # --- MAC COMPATIBILITY FIX: Bypassing generic engine fallbacks ---
    btn_text =  font_sz_16x.render("?", True, WHITE)
    btn_rect = btn_text.get_rect(center=help_btn_center)
    canvas.blit(btn_text, btn_rect)



# ==============================================================================
# 3. WORD RETRIEVAL & DICTIONARY ENGINE  
# ==============================================================================
def load_words_from_file():
    try:
        with open(words_file_path, "r", encoding="utf-8") as file:
            words = [line.strip().upper() for line in file if len(line.strip()) == 5]
            return words
    except FileNotFoundError:    
        return ["APPLE", "BEACH", "CLIMB", "ZEBRA", "YOUTH"]

# Choose the WONDER WORD
word_list = load_words_from_file()
hold_secret_word = random.choice(word_list).upper()

# Load the comprehensive dictionary fallback system
try:
    with open(dict_file_path, 'r', encoding="utf-8") as file: 
        large_hint_bank = [line.strip().upper() for line in file if len(line.strip()) == 5]
except FileNotFoundError:
    large_hint_bank = word_list

def find_word_in_dictionary(target_word, file_path):
    """ Validates that user input is in the dictionary of allowable words """
    target_word = target_word.upper().strip()    
    try:
        with open(file_path, 'r', encoding="utf-8") as file:            
            dictionary_set = {line.strip().upper() for line in file if len(line.strip()) == 5}           
    except FileNotFoundError:
        # SAFE FALLBACK: Small emergency list to prevent loops from locking up
        dictionary_set = {"CARRY", "FIFTH", "SIXTH", "ERROR", "STORK", "CRIME", "FLANK", "CLIMB"}     

    return target_word in dictionary_set

#CHUNK 20 END

#NEED TO READ THE DICTIONARY ONLY ONCE



#CHUNK 21 START

def get_strategic_hints(word_bank, letters_not_in_word, letters_in_word, letters_might_be_in_word, hold_secret_word, top_n=2):
    """
    Analyzes the game word list against the player's scratchpad/worksheet sets.
    Finds words that maximize letter elimination without using known wrong letters.
    CRITICAL: Explicitly skips the secret word so the computer never spoils the solution!
    """
    scored_words = []
    possible_solutions = []
    
    for word in word_bank:
        word_upper = word.upper()
        word_set = set(word_upper)
        
        # EXCLUDE SECRET WORD: If this word is the actual answer, skip it entirely!
        if word_upper == hold_secret_word.upper():
            continue
        
        # 1. Skip words that contain letters the player explicitly marked as NOT in the word (-)
        if not word_set.isdisjoint(letters_not_in_word):
            continue
            
        # Keep track of words that are still legally possible solutions based on grey letters
        possible_solutions.append(word_upper)
            
        # 2. Score based on testing NEW letters (untested variables)
        known_letters = letters_in_word.union(letters_might_be_in_word)
        untested_letters = word_set.difference(known_letters)
        score = len(untested_letters)
        
        # 3. Penalize duplicate letters inside the word itself
        if len(word_set) < len(word_upper):
            score -= 0.5
            
        scored_words.append((word_upper, score))
        
    # Sort by elimination score descending
    scored_words.sort(key=lambda x: x[1], reverse=True)    
    # Filter out words that give 0 new elimination value
    best_fillers = [word for word, score in scored_words if score > 0]

     
    # If we found good filler words to eliminate letters, grab a random pair from the top tier
    if best_fillers:
        # Look at the top 10 choices (or fewer if 10 don't exist)
        pool_size = min(10, len(best_fillers))
        top_tier_pool = best_fillers[:pool_size]
        
        # Randomly select top_n words from that pool
        return random.sample(top_tier_pool, min(top_n, len(top_tier_pool)))
        
    # FALLBACK: If no fillers remain, pull randomly from the top 10 possible solutions
    if possible_solutions:
        pool_size = min(10, len(possible_solutions))
        top_tier_solutions = possible_solutions[:pool_size]
        return random.sample(top_tier_solutions, min(top_n, len(top_tier_solutions)))

    return []
       

#END CHUNK 21

#START 22

def digital_scratchpad(processed_input, revealed_indices):  
    global feedback_message  # Add this right here!
               
    if len(processed_input) == 3:
        target_char = processed_input[1]
        pos_char = processed_input[2]
         
        if pos_char.isdigit() and 1 <= int(pos_char) <= 5:
            target_idx = int(pos_char) - 1
            
            if target_idx in revealed_indices:
                feedback_message = f"Slot {pos_char} is locked by an official hint letter!"
                return
                
            if target_char == " ":
                dig_scratch_pad_slots[target_idx] = " "
                feedback_message = f"Cleared Digital Scratchpad slot {pos_char}."
            else:
                dig_scratch_pad_slots[target_idx] = target_char            
                feedback_message = f"Placed '{target_char}' into Digital Scratchpad slot {pos_char}."
        else:
            feedback_message = "Invalid slot! Use positions 1 through 5."
    else:
        feedback_message = "Invalid scratchpad command format! Use layout like #F3."
    return  
  

def hint_command():
    global points 
    global revealed_indices  # 🌟 Access your tracking list from the top of the script
    global hint_status_msg
    if len(revealed_indices) >= MAX_HINTS_ALLOWED:
        hint_status_msg = "MAX HINTS REACHED!"
        return hint_status_msg
    current_hint_number = len(revealed_indices) + 1    
    if current_hint_number == 1:
        cost = HINT_COST_1
    elif current_hint_number == 2:
        cost = HINT_COST_2
    elif current_hint_number == 3:
        cost = HINT_COST_3
    elif current_hint_number == 4:
        cost = HINT_COST_4
    else:
        cost = 0
    points -= cost
    hint_status_msg = f"{cost} points."   
    unrevealed_indices = [i for i in range(len(hold_secret_word)) if i not in revealed_indices]

    # 5. Pick one random index from the unrevealed options
    if unrevealed_indices:
        hint_idx = random.choice(unrevealed_indices)
        
        # 6. Update tracking lists and game state
        revealed_indices.append(hint_idx)
        hint_char = hold_secret_word[hint_idx].upper()
        dig_scratch_pad_slots[hint_idx] = hint_char

        if hint_char not in letters_in_word:
            letters_in_word.add(hint_char)
            
        # Exit immediately and display the random position
        return f"Position {hint_idx + 1} in the Wonder Word is '{hint_char}'.... Score reduced by {hint_status_msg}"
  
#END CHUNK 22
    
    
#START CHUNK 23    
    
    
#==============Quit Game===========
    
def quit_game():
    # 1. Start the sound on a channel right away (instead of just .play())
    #channel = None
    if sound_happy_trails: 
        channel = sound_happy_trails.play()
        
    
   
    canvas.blit(Roy_Rogers_snapshot, (0, 0))

    try:
        active_name = player_name_input
    except NameError:
        try:
            active_name = username
        except NameError:
            active_name = "PLAYER"

    text_alpha = 255 # Make text fully solid white so it is highly readable

    # 1. Render base text lines
    raw_word = font_sz_20x.render(f"The Wonder Word was: {hold_secret_word}", True, (BLACK))
    raw_score = font_sz_20x.render(f"Your Final Score Was: {points}", True, (BLACK))
    raw_thanks = font_sz_20x.render(f"THANKS FOR PLAYING ...{active_name}", True, (BLACK))

    # 2. Setup text layers
    text_word = pygame.Surface(raw_word.get_size(), pygame.SRCALPHA)
    text_word.set_alpha(text_alpha)
    text_word.blit(raw_word, (0, 0))

    text_score = pygame.Surface(raw_score.get_size(), pygame.SRCALPHA)
    text_score.set_alpha(text_alpha)
    text_score.blit(raw_score, (0, 0))

    text_thanks = pygame.Surface(raw_thanks.get_size(), pygame.SRCALPHA)
    text_thanks.set_alpha(text_alpha)
    text_thanks.blit(raw_thanks, (0, 0))
    
    rect_word = text_word.get_rect(center=(170, 480))
    rect_score = text_score.get_rect(center=(170, 520))
    rect_thanks = text_thanks.get_rect(center=(170, 560))
    
    # 3. CREATE A SEMI-TRANSPARENT BACKGROUND BOX FOR THE TEXT
    bg_box = pygame.Surface((300, 100), pygame.SRCALPHA) 
    bg_box.fill((0, 0, 0, 35)) # Black color with 130/255 transparency 
    bg_rect = bg_box.get_rect(center=(1000 // 2, 500))
    
    # 4. Blit everything to canvas (Box first, then text layers)
    canvas.blit(text_word, rect_word) 
    canvas.blit(text_score, rect_score)
    canvas.blit(text_thanks, rect_thanks)
    
    scaled_canvas = pygame.transform.scale(canvas, (current_width, current_height))
    SCREEN.blit(scaled_canvas, (0, 0))
    pygame.display.flip() 
    
    # ========================================================
    # TIMING AND FADE CONTROLS (ADJUST THESE NUMBERS)
    # ========================================================

    play_time_ms = 9999  
    
    # How long the new fade-out lasts (in milliseconds)
    fade_time_ms = 1500   


    # 1. Wait out the initial full-volume playback time
    pygame.time.wait(play_time_ms) 
    
    # 2. Trigger the smooth fade-out on the channel
    if channel:
        channel.fadeout(fade_time_ms)
        
    # 3. Wait for the fade-out to finish completely before quitting
    pygame.time.wait(fade_time_ms) 
    
    # ========================================================
     
    pygame.quit()
    import sys
    sys.exit()


#END CHUNK 23


# ================================================================================
#                     GAME ENGINE LOOP (COMPLETE PROCEDURE DIVISION)
# ================================================================================

user_input = "" 
feedback_message = "Welcome to 'Wonder Word'                Type your name and press enter."
running = True

while running:
 
    # 1. REAL-TIME SCORING CONTROLLER
    if game_state == "PLAYING" and not show_help_overlay:
        current_time = datetime.datetime.now()
        elapsed_seconds = int((current_time - start_time).total_seconds() - total_break_seconds)
 
        if points <= 0:
            points = 0
            game_state = "GAME_OVER"
            feedback_message = f"GAME OVER! Your points are zero. The Wonder Word was: {hold_secret_word}. Play again? (Y/N)"

    # >>> INSERT THIS SAFE GUARD GATE HERE <<<
    elif game_state == "ORIGIN_STORY":
        # Freeze all calculations, background penalties, and inputs until dismissed
        pass

    # 2. KEYBOARD AND SYSTEM EVENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            import sys
            sys.exit()

         # Track when the player stretches, minimizes, or maximizes the window
        elif event.type == pygame.VIDEORESIZE:
            # Update variables directly from the event size
            current_width, current_height = event.size
            
            # REMOVED: pygame.display.set_mode() from here.
            # This stops the infinite warning/resize loop on macOS.

        # ----------------------------------------------------------------------
        # NEW MAC COMPATIBLE TRACKPAD & MOUSE WHEEL LOGIC  
        # ----------------------------------------------------------------------
        elif event.type == pygame.MOUSEWHEEL:
            actual_mx, actual_my = pygame.mouse.get_pos()
            
            # Guard against division by zero if window is minimized
            safe_width = max(1, current_width)
            safe_height = max(1, current_height)
            
            # Apply your proportional scaling math back to 1000x600 coordinates
            mx = int(actual_mx * (1000 / safe_width))
            my = int(actual_my * (600 / safe_height))
            
            # Match the left column boundaries from your drawing script (WORDS GUESSED zone)
            if 40 <= mx <= 390 and 40 <= my <= 440:
                
                # Math constraint: Maximum index we can jump to without trailing blank lines
                max_scroll = max(0, len(words_entered) - 10)
                
                # event.y is positive when scrolling up, negative when scrolling down
                if event.y > 0:
                    scroll_index = max(0, scroll_index - 1)
                elif event.y < 0:
                    scroll_index = min(max_scroll, scroll_index + 1)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            actual_mx, actual_my = event.pos                
            
            # Guard against division by zero if window is minimized
            safe_width = max(1, current_width)
            safe_height = max(1, current_height)
            
            # Proportional math to translate scaled mouse positions back to 1000x600 coordinates
            mx = int(actual_mx * (1000 / safe_width))
            my = int(actual_my * (600 / safe_height))

    
            # ====================================================================
            # LEFT CLICK ACTION CONTROLLER (BUTTON 1)
            # ====================================================================
            if event.button == 1: # Left click
                
                # A. Check Help/help Circle Button
                help_dist = ((mx - help_btn_center[0])**2 + (my - help_btn_center[1])**2)**0.5

                if help_dist <= help_btn_radius:
                    # MODIFICATION: Toggle help on/off using the Index page (0)
                    #if show_help_overlay is False:   
                                           
                    if not show_help_overlay:   
                        show_help_index = True
                        show_help_overlay = 1
                        help_opened_at = pygame.time.get_ticks()
                        feedback_message = "Help Index opened."   
                        

                    else:                       
                        show_help_overlay = False
                        help_duration = pygame.time.get_ticks() - help_opened_at
                        start_time += datetime.timedelta(milliseconds=help_duration)
                        feedback_message = "Returned to game !"


                # C. Check Reset Circle Button
                reset_dist = math.hypot(mx - reset_btn_x, my - reset_btn_y)
                if reset_dist <= reset_btn_radius:
                    if game_state == "PLAYING":
                        feedback_message = f"RESET.....The Wonder Word was '{hold_secret_word}'. Play again? (Y/N)"

                        # PLACEHOLDER SOUND FOR MANUALLY RESETTING / GIVING UP
                        # NOTE: This triggers the same wistful, descending chime or gentle sequence 
                        # as typing the text command. It provides a sympathetic "curtain drop" 
                        # atmosphere when revealing the secret word.
                        if sound_click:
                            sound_click.play()

                        game_state = "GAME_OVER"


                # B. Check Hint Circle Button
                hint_dist = math.hypot(mx - hint_btn_x, my - hint_btn_y)
                if hint_dist <= hint_btn_radius: 
                    if game_state == "PLAYING":
                        if number_of_guesses < 5:
                             max_hints_allowed = 0
                        elif 5 <= number_of_guesses < 15:
                             max_hints_allowed = 1
                        elif 15 <= number_of_guesses < 20:
                             max_hints_allowed = 2
                        elif 20 <= number_of_guesses < 30:
                             max_hints_allowed = 3
                        else:
                             max_hints_allowed = 4

                        if len(revealed_indices) >= max_hints_allowed:
                            if max_hints_allowed == 0:
                                feedback_message = f"No hints allowed until after 4 guesses!"
                            elif max_hints_allowed == 1:
                                feedback_message = f"2nd hint not allowed until after 14 guesses!"
                            elif max_hints_allowed == 2:
                                feedback_message = f"3rd hint not allowed until after 19 guesses!"
                            elif max_hints_allowed == 3:
                                feedback_message = f"4th hint not allowed until after 29 guesses! "
                            else:
                                feedback_message = "All 4 hints have already been used!"
                        else:
                            feedback_message = hint_command()                        

#start copy

# ============================
# GRABBING A LETTER TO DRAG 
# ============================
             
                if game_state == "PLAYING":
                # --- A. CHECK IF CLICKING A LETTER ON THE WORKSHEET ---
                    keyboard_layout = ["ABCDEFG", "HIJKLMN", "OPQRSTU", "VWXYZ"]
                    kb_start_x = 450
                    kb_start_y = 50
                    kb_box_size = 45
                    kb_spacing = 10
                    
                    for row_idx, letter_row in enumerate(keyboard_layout):
                        for col_idx, clicked_char in enumerate(letter_row):
                            box_left = kb_start_x + (col_idx * (kb_box_size + kb_spacing))
                            box_top = kb_start_y + 80 + (row_idx * (kb_box_size + kb_spacing))
                            
                        # If cursor falls inside an alphabet square, grab a copy
                            if box_left <= mx <= (box_left + kb_box_size) and box_top <= my <= (box_top + kb_box_size):
                                dragging_letter = clicked_char
                                drag_source = "WORKSHEET"
                                drag_pos = [mx, my]
                    
                    # --- B. CHECK IF CLICKING A LETTER ALREADY IN THE SCRATCHPAD ---
                    #        use the exact positioning math from your drawing logic
                    seq_base_y = kb_start_y + 80 + (4 * (kb_box_size + kb_spacing)) + 140
                    shift_right = 1 * (kb_box_size + kb_spacing)
                    
                    for seq_idx in range(5):
                        seq_box_x = kb_start_x + shift_right + (seq_idx * (kb_box_size + kb_spacing))
                        
                        # Test if cursor falls inside this specific scratchpad box boundaries
                        if seq_box_x <= mx <= (seq_box_x + kb_box_size) and seq_base_y <= my <= (seq_base_y + kb_box_size):
                            # HINT LOCK CONSTRAINT: Cannot pick up or clear a slot locked by a hint!
                            if seq_idx not in revealed_indices:
                                current_occupant = dig_scratch_pad_slots[seq_idx]
                                if current_occupant != " " and current_occupant != "":
                                    dragging_letter = current_occupant
                                    drag_source = seq_idx  # Keep track of which slot it came from (0-4)
                                    drag_pos = [mx, my]
                                    # Lift the letter out immediately so the box visually clears during dragging
                                    dig_scratch_pad_slots[seq_idx] = " "
                            

            # ====================================================================
            # RIGHT CLICK ACTION CONTROLLER (BUTTON 3)
            # ====================================================================
            elif event.button == 3: # Right click
                if game_state == "PLAYING":
                    
                    # D. WORKSHEET KEYBOARD LETTER CLICK CONTROLLER
                    keyboard_layout = ["ABCDEFG", "HIJKLMN", "OPQRSTU", "VWXYZ"]
                    kb_start_x = 450
                    kb_start_y = 50
                    kb_box_size = 45
                    kb_spacing = 10

                    for row_idx, letter_row in enumerate(keyboard_layout):
                        for col_idx, clicked_char in enumerate(letter_row):
                            
                            box_left = kb_start_x + (col_idx * (kb_box_size + kb_spacing))
                            box_top = kb_start_y + 80 + (row_idx * (kb_box_size + kb_spacing))
                            
                            if box_left <= mx <= (box_left + kb_box_size) and box_top <= my <= (box_top + kb_box_size):
                                
                                if clicked_char in letters_in_word:
                                    letters_in_word.discard(clicked_char)
                                    letters_might_be_in_word.add(clicked_char)
                                    feedback_message = f"Letter '{clicked_char}' toggled to MIGHT BE IN WORD (Yellow)."
                                    
                                elif clicked_char in letters_might_be_in_word:
                                    letters_might_be_in_word.discard(clicked_char)
                                    letters_not_in_word.add(clicked_char)
                                    feedback_message = f"Letter '{clicked_char}' toggled to NOT IN WORD (Gray)."
                                    
                                elif clicked_char in letters_not_in_word:
                                    letters_not_in_word.discard(clicked_char)
                                    feedback_message = f"Letter '{clicked_char}' cleared back to Neutral (Black)."
                                    
                                else:
                                    letters_in_word.add(clicked_char)
                                    feedback_message = f"Letter '{clicked_char}' toggled to IN WORD (Green)."                            
 
 
 
                                  # PLACEHOLDER SOUND FOR RIGHT-CLICK TOGGLING
                                # NOTE: When replacing this sound file down the road, look for a very short,
                                # snappy, muted sound like an "interface tick", "plastic mouse click", or a 
                                # dry "wood tap". Avoid heavy echoy sounds because players will likely spam 
                                # right-clicks quickly to cycle through colors, and overlapping long sounds 
                                # will become noisy and annoying. Keep duration under 0.2 seconds.
                                if sound_click:
                                    sound_click.play()
 

        # ====================================================================
        # NEW EVENT: LIVE DRAG TRACKING (INSERT BETWEEN MOUSE CLICKS AND KEYDOWN)
        # ====================================================================
        elif event.type == pygame.MOUSEMOTION:
            # Only track movement if the player is actively holding a letter!
            if dragging_letter is not None:
                actual_mx, actual_my = event.pos
                
                # Apply your excellent scaling math so coordinates stay perfectly calibrated
                drag_pos[0] = int(actual_mx * (1000 / current_width))
                drag_pos[1] = int(actual_my * (600 / current_height))                            
                                    


        # ========================================== 
        # NEW EVENT: DROPPING THE DRAGGED LETTER  
        # ========================================== 
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and dragging_letter is not None:
                actual_mx, actual_my = event.pos
                mx = int(actual_mx * (1000 / current_width))
                my = int(actual_my * (600 / current_height))
                
                # Re-calculate scratchpad boundary math to verify landing zone
                kb_start_x = 450
                kb_start_y = 50
                kb_box_size = 45
                kb_spacing = 10
                seq_base_y = kb_start_y + 80 + (4 * (kb_box_size + kb_spacing)) + 140
                shift_right = 1 * (kb_box_size + kb_spacing)
                
                dropped_successfully = False
                
                # Loop through the 5 scratchpad boxes to check for a drop hit
                for seq_idx in range(5):
                    seq_box_x = kb_start_x + shift_right + (seq_idx * (kb_box_size + kb_spacing))
                    
                    if seq_box_x <= mx <= (seq_box_x + kb_box_size) and seq_base_y <= my <= (seq_base_y + kb_box_size):
                        # RULE CONSTRAINT: Protect locked hint slots!
                        if seq_idx not in revealed_indices:
                            old_letter = dig_scratch_pad_slots[seq_idx]
                            
                            # Place our moving tile cleanly into the array
                            dig_scratch_pad_slots[seq_idx] = dragging_letter
                            dropped_successfully = True
                            
                            # SWAP FEATURE: If we dragged this letter from another scratchpad slot,
                            # and the destination box wasn't empty, move the bumped letter to the old slot!
                            if isinstance(drag_source, int) and old_letter != " " and old_letter != "":
                                dig_scratch_pad_slots[drag_source] = old_letter
                        break
                
                # IF RELEASED IN NO MAN'S LAND (Acts like your old "# 4" text command)
                if not dropped_successfully:
                    # If it came from a scratchpad slot, dropping it in empty space erases it
                    if isinstance(drag_source, int):
                        dig_scratch_pad_slots[drag_source] = " "
                    # (If it was a clone from the top grid, it simply vanishes from the air)

                    # PLACEHOLDER SOUND FOR MISSED DROP / ERASE
                    # NOTE: For the miss or "vanish" action, look for a soft, hollow 
                    # "slide," a subtle "whoosh," or a damp miniature rustle sound. 
                    # It should feel clean and indicate that the letter safely 
                    # slid back home or melted away, rather than sounding like a harsh error.
                      
                    if woosh: woosh.play()
                    
                else:
                    # PLACEHOLDER SOUND FOR SUCCESSFUL DROP / ARRANGEMENT
                    # NOTE: For a successful slot placement, look for a solid, rewarding 
                    # "tack," a dull "wood block drop," or a plastic tile placement sound 
                    # (think of a Scrabble or Rummikub piece snapping firmly into a slot). 
                    # It needs to sound physical, satisfying, and grounding.
                  
                    if tile_click: tile_click.play()

                # RESET TRACKING STATE FLAGS TO END DRAG MODE
                dragging_letter = None
                drag_source = None



#end copy



        # ====================================================================
        # KEYBOARD INPUT HANDLER (BACK OUTSIDE THE MOUSE LOOP)
        # ====================================================================
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RETURN and game_state == "ORIGIN_STORY":
                sound_VietNam.stop()         # Shut off the music!
                origin_music_playing = False  # Reset the switch for next time
         
                game_state = "PLAYING"      # (Or whatever your normal state is called)
                continue


#THIS MAY ALL BE DEAD CODE FOR TRYING TO USE NUMBERS TO SKIP TO HELP SCREENS
#HOWEVER DELETING THIS CODE STOPS THE HELP SCREENS FROM WORKING AUG 10 2026
            
                       
            
            # ----------------------------------------------------------------
            # INSTANT NUMBER HOTKEYS: Intercepts keys, wipes buffer, draws screen
            # ----------------------------------------------------------------
            if 'show_help_index' in globals() and show_help_index:
                hotkey_pressed = False
                
                if event.key in [pygame.K_1, pygame.K_KP1]:
                    show_help_overlay = 1
                    show_help_index = False
                    user_input = ""  # WIPES OUT THE NUMBER CHARACTER INSTANTLY
                    hotkey_pressed = True
                elif event.key in [pygame.K_2, pygame.K_KP2]:
                    show_help_overlay = 2
                    show_help_index = False
                    user_input = ""  # WIPES OUT THE NUMBER CHARACTER INSTANTLY
                    hotkey_pressed = True
                elif event.key in [pygame.K_3, pygame.K_KP3]:
                    show_help_overlay = 3
                    show_help_index = False
                    user_input = ""  # WIPES OUT THE NUMBER CHARACTER INSTANTLY
                    hotkey_pressed = True
                elif event.key in [pygame.K_4, pygame.K_KP4]:
                    show_help_overlay = 4
                    show_help_index = False
                    user_input = ""  # WIPES OUT THE NUMBER CHARACTER INSTANTLY
                    hotkey_pressed = True
                elif event.key in [pygame.K_5, pygame.K_KP5]:
                    show_help_overlay = 5
                    show_help_index = False
                    user_input = ""  # WIPES OUT THE NUMBER CHARACTER INSTANTLY
                    hotkey_pressed = True

                # If a valid number was pressed, repaint the screen instantly
                if hotkey_pressed:
                    canvas.fill(BLACKLESS) 
                    draw_worksheet(words_entered, letters_not_in_word, letters_might_be_in_word, letters_in_word, scroll_index)
                    if game_state == "PLAYING":
                        display_score()
                    draw_help_overlay() 
                    
                    scaled_canvas = pygame.transform.scale(canvas, (current_width, current_height))
                    SCREEN.blit(scaled_canvas, (0, 0))
                    pygame.display.flip()
                    continue  # Safely consumes the key event and returns to top of loop


#////////////////DEAD CODE END






            if event.key == pygame.K_RETURN:
                processed_input = user_input.strip().upper()
                user_input = ""
                

                # STATE 1: SPLASH SCREEN & NAME PROCESSING
                if game_state == "SPLASH" or game_state == "NAME_INPUT":
                    if not processed_input:
                        continue
                    username = processed_input
                    feedback_message = f"Hello, {username}.                          Input a five letter word to start!"
                    start_time = datetime.datetime.now()
                    game_state = "PLAYING"
                    # TURN ON THE BACKGROUND MUSIC HERE
                    #if sound_theme_music: sound_theme_music.play(-1)  # <--- Fired for fake words!
                    #print("--- right before TRY that plays theme sound ---")
                    
                    #try:
                        # Only try to play if pygame initialized successfully earlier
                        #pygame.mixer.music.play(-1)
                    #except Exception:
                        #pass # Safely bypasses if audio was disabled in the try block above
                    continue                

                # STATE 2: SECRET ORIGIN STORY DISMISSAL
                if game_state == "ORIGIN_STORY":
                    game_state = "PLAYING"
                    continue    

     
                if game_state == "TIMEOUT":
                # Check if the player pressed ENTER to resume
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        break_end = datetime.datetime.now()
        
                        # Calculate how long they paused and add it to your game timer offset
                        paused_time = (break_end - break_start).total_seconds()
                        # total_game_time += paused_time (or however you track total time)
        
                        feedback_message = "Welcome back!" 
                        game_state = "PLAYING"  # Change this to whatever your normal game state variable is
                        continue  # Skip the rest of the loop so it doesn't validate an empty input


                    
                # ==================================================================
                # UNIFIED HELP SYSTEM MASTER CONTROLLER (Handles Enter Key Content)
                # ==================================================================
                
                # CATCH A: The player types 'HELP' 
                if processed_input == "HELP":
                    if show_help_overlay == 0 and show_help_index is False:
                        show_help_index = True
                        show_help_overlay = 1  
                        help_opened_at = pygame.time.get_ticks()
                        feedback_message = "Help Index opened."
                    else:
                        show_help_index = False
                        show_help_overlay = 0
                        help_duration = pygame.time.get_ticks() - help_opened_at
                        start_time += datetime.timedelta(milliseconds=help_duration)
                        feedback_message = "Returned to game - TYPED HELP!"
                    
                    user_input = ""
                    canvas.fill(BLACKLESS)
                    #if woosh: woosh.play()
                    draw_worksheet(words_entered, letters_not_in_word, letters_might_be_in_word, letters_in_word, scroll_index)
                    if game_state == "PLAYING":
                        display_score()
                    draw_help_overlay()
                    scaled_canvas = pygame.transform.scale(canvas, (current_width, current_height))
                    SCREEN.blit(scaled_canvas, (0, 0))
                    pygame.display.flip()
                    continue  

                # CATCH B: The player presses a blank ENTER key while help is active
                elif show_help_overlay > 0 and not processed_input:
                    if show_help_index:
                        # Pressing ENTER on the Index page closes the manual entirely
                        show_help_index = False
                        show_help_overlay = False  # Reset completely back to a boolean
                        help_duration = pygame.time.get_ticks() - help_opened_at
                        start_time += datetime.timedelta(milliseconds=help_duration)                    
                        feedback_message = "Returned to game!"
                        
                        # FORCE IMMEDIATE GRAPHICS REDRAW TO ELIMINATE THE DOUBLE-ENTER STATE
                        canvas.fill(BLACKLESS) 
                        draw_worksheet(words_entered, letters_not_in_word, letters_might_be_in_word, letters_in_word, scroll_index)
                        if game_state == "PLAYING":
                            display_score()
                    else:
                        # Pressing ENTER on pages 1-5 bounces them right back to the Index
                        show_help_index = True
                        canvas.fill(BLACKLESS) 
                        draw_worksheet(words_entered, letters_not_in_word, letters_might_be_in_word, letters_in_word, scroll_index)
                        if game_state == "PLAYING":
                            display_score()
                        draw_help_overlay()
                        
                    user_input = ""
                    processed_input = ""
                    scaled_canvas = pygame.transform.scale(canvas, (current_width, current_height))
                    SCREEN.blit(scaled_canvas, (0, 0))
                    pygame.display.flip()
                    continue  


                # CATCH C: Safeguard against ANY other text typed while help is open
                elif show_help_overlay > 0 and processed_input:
                    user_input = ""
                    processed_input = ""
                    continue      

                # STATE: RESET PROCESSING
                if processed_input == "RESET":
                    feedback_message = f"RESET........The Wonder Word was '{hold_secret_word}'. Play again? (Y/N)"
                    # PLACEHOLDER SOUND FOR MANUALLY RESETTING / GIVING UP
                    # NOTE: Since the player is choosing to forfeit or reset, look for a soft, 
                    # gentle, descending chime scale or a minor-key musical sequence. Avoid 
                    # harsh buzzers; it should feel like a sympathetic "Aww, so close!" curtain drop.
                    if sound_click:
                        sound_click.play()
    

                    game_state = "GAME_OVER"
                    continue


                # STATE 3: PLAY AGAIN SELECTION
                if game_state == "GAME_OVER":
                    if not processed_input:
                        continue
                    if processed_input == "Y":
                        points = points_allowed
                        start_time = datetime.datetime.now()
                        turn_start_time = datetime.datetime.now()
                        total_break_seconds = 0
                        number_of_guesses = 0 
                        #allow_hints_now = False
                        penalty_alert = ""
                        hold_secret_word = random.choice(word_list).upper()
                        words_entered.clear()
                        scroll_index = 0  # Reset scroll position for new games
                        letters_not_in_word.clear()
                        letters_might_be_in_word.clear()
                        letters_in_word.clear()
                        revealed_indices.clear()
                        dig_scratch_pad_slots = [" ", " ", " ", " ", " "]
                        game_state = "PLAYING"
                        feedback_message = "New game started ...Good luck!"
                        # PLACEHOLDER SOUND FOR ENCOURAGEMENT / RESTART
                        # NOTE: When replacing this file, choose a bright, short, and ascending 
                        # chime or an electronic "power-up" chirp. It needs to sound optimistic and 
                        # fresh, providing a clean acoustic restart that wipes away any frustration 
                        # from the previous game. Keep duration short, around 0.3 seconds.
                        if sound_click:
                            sound_click.play()

                    else:
                        quit_game()
                    continue
                
                # STATE 4: CLEAR HIGHSCORES CONFIRMATION
                if game_state == "CLEAR_LEADERBOARD":
                    if not processed_input:
                        continue
                    
                    # <<< INSERT THIS STOP ENGINE HERE >>>
                    # The player has submitted their choice, silence the 3-layer victory tracks instantly!
                    pygame.mixer.Channel(1).stop()
                    pygame.mixer.Channel(2).stop()
                    pygame.mixer.Channel(3).stop()

                       # Clear all remaining spark records from memory instantly
                    celebration_fireworks.clear_all()
               
                    if processed_input == "Y":
                        clear_high_scores()
                        feedback_message = "Leaderboard cleared. Do you want to play again? (Y/N)"

                        # PLACEHOLDER SOUND FOR CLEARING LEADERBOARD
                        # NOTE: Look for a destructive but intentional sound like a digital "System Zap," 
                        # a sweeping "Whoosh," or a physical sound like a sheet of paper being crumpled. 
                        # This confirms to the player that the data has been wiped clean.
                        if sound_click:
                            sound_click.play()

                    else:
                        feedback_message = "Leaderboard saved. Do you want to play again? (Y/N)"                                        
                        # PLACEHOLDER SOUND FOR SAVING/SKIPPING LEADERBOARD CLEAR
                        # NOTE: A standard, clean UI click or page-flip texture. It tells the 
                        # player their choice was logged and the leaderboard is secure.
                        if sound_click:
                            sound_click.play()

                    game_state = "GAME_OVER"
                    continue

                
# STATE 5: ACTIVE GAME PLAY ENGINE (Standard Commands & Guesses) 
                if processed_input == "RESET":
                    feedback_message = f"RESET: The Wonder Word was '{hold_secret_word}'. Play again? (Y/N)"
                    game_state = "RESET_PROMPT"
                    continue
                elif processed_input == "HINT":
                    if number_of_guesses < 5:
                        max_hints_allowed = 0
                    elif 5 <= number_of_guesses < 15:
                        max_hints_allowed = 1
                    elif 15 <= number_of_guesses < 20:
                        max_hints_allowed = 2
                    elif 20 <= number_of_guesses < 30:
                        max_hints_allowed = 3
                    else:
                        max_hints_allowed = 4

                    if len(revealed_indices) >= max_hints_allowed:
                        if max_hints_allowed == 0:
                            feedback_message = f"No hints allowed until after 4 guesses!"
                        elif max_hints_allowed == 1:
                            feedback_message = f"2nd hint not allowed until after 14 guesses!"
                        elif max_hints_allowed == 2:
                            feedback_message = f"3rd hint not allowed until after 19 guesses!"
                        elif max_hints_allowed == 3:
                            feedback_message = f"4th hint not allowed until after 29 guesses!"
                        else:
                            feedback_message = f"All 4 hints have already been used!"
                    else:
                        feedback_message = hint_command()
                    continue 

                elif processed_input == "TIMEOUT":
                    if timeout_break > 0:
                        timeout_break -= 1  # FIX 2: Deduct a timeout break so they only get 2!
                        break_start = datetime.datetime.now()
                        feedback_message = "------------ TIMER PAUSED ------------ Press Enter to resume."
                        game_state = "TIMEOUT"
                    else:
                        feedback_message = "SORRY! No breaks remaining."
                    continue


                # --- FIXED: CHANGED == TO .startswith() TO TRAP CODES LIKE #F4 ---
                elif len(processed_input) > 0 and processed_input.startswith('#'):
                    digital_scratchpad(processed_input, revealed_indices)                    
                    continue

                # Prefix Matrix Evaluations (-, +, !)
                elif processed_input.startswith(('-', '+', '!')):
                     # --- FIXED: EXTRACT THE EXACT FIRST CHARACTER AS THE PREFIX ---
                     prefix = processed_input[0] 
                     chars = processed_input[1:]
     
                     for c in chars:
                         if c.isalpha(): 
                             letters_not_in_word.discard(c)
                             letters_might_be_in_word.discard(c)
                             letters_in_word.discard(c)
             
                             if prefix == '-':
                                 letters_not_in_word.add(c)
                             elif prefix == '+':
                                 letters_might_be_in_word.add(c)
                             elif prefix == '!':
                                 letters_in_word.add(c)
              
                     feedback_message = "WORKSHEET updated successfully."
                     continue                    


                # 5-Letter Word Entry Evaluations
                elif len(processed_input) == 5 and processed_input.isalpha():
                    validation_result = find_word_in_dictionary(processed_input, dict_file_path) 
                    if not validation_result:
                        feedback_message = f"SORRY! {processed_input} not found in dictionary. Try again."
                        penalty_alert = ""
                        continue
                                       
                    if number_of_guesses >= 10:
                        suggested_hints = get_strategic_hints(large_hint_bank, letters_not_in_word, 
                                                              letters_in_word, letters_might_be_in_word, hold_secret_word, top_n=2)
                    
                    secret_word_list = list(hold_secret_word.upper())
                    user_input_list = list(processed_input) 
                    num_matches = 0 
                    num_sequence = 0 

                    for i in range(5):
                        if user_input_list[i] == secret_word_list[i]:
                            num_sequence += 1
                            num_matches += 1
                            secret_word_list[i] = None
                            user_input_list[i] = "used"

                    for i in range(5):
                        if user_input_list[i] != "used" and user_input_list[i] in secret_word_list:
                            num_matches += 1
                            match_idx = secret_word_list.index(user_input_list[i])
                            secret_word_list[match_idx] = None

                    points -= 10
                    points -= (elapsed_seconds * 2)
                    turn_elapsed = (datetime.datetime.now() - turn_start_time).total_seconds()
                    turn_start_time = datetime.datetime.now()                                 
                    number_of_guesses += 1
                    if number_of_guesses >= 15:
                        points -= 5000
                        if number_of_guesses == 15:
                            penalty_alert = f"(Each guess will now cost 5,000 points.)"
                    elif number_of_guesses >= 10:
                        points -= 2000
                        if number_of_guesses == 10:
                            penalty_alert = f"(Each guess will now cost 2,000 points.)"
                    elif number_of_guesses >= 5:
                        points -= 1000
                        if number_of_guesses == 5:
                            penalty_alert = f"(Each guess will now cost 1,000 points.)"
                    else:
                        points -= 200
                        penalty_alert = "" # Blank for normal guesses        
                  
                    
                    # --- NATIVE LIST EXPANSION MECHANISM (REMOVED POP CONTROLS) ---
                    words_entered.append([processed_input, num_matches, num_sequence])
                    
                    # --- ADVANCE SELECTION POINTER AUTOMATICALLY DOWNWARD ON RECORD 11 ---
                    scroll_index = max(0, len(words_entered) - 10)

                    # --- TRIPWIRE TRAP FOR THE WARTIME EXCHANGE ORIGIN STORY ---
                    if processed_input == "ERROR":
                
                        game_state = "ORIGIN_STORY"
                      
                        feedback_message = "Logical exclusion resolved...continue game."
                        #feedback_message = "LOGICAL EXCLUSION RESOLVED... PRESS ENTER TO CONTINUE GAME"
                        
                        
                    elif num_sequence == 5:
                        final_calculated_score = max(0, points)
                        game_seconds = round(elapsed_seconds / 60, 1)
                        save_high_score(username, final_calculated_score, number_of_guesses, game_seconds)
                        feedback_message = "CONGRATULATIONS! Clear Leaderboard? (Y/N)"
                        # PLACEHOLDER SOUND FOR INSTANT VICTORY
                        # NOTE: This is the big moment! Look for a prominent, high-energy "Level Clear" 
                        # chime or a triumphant brass fanfare blast (like the opening chords of Rocky). 
                        # It should hit hard and instantly celebrate the completion of the 5th sequence.
                        # --- COBOL TO PYTHON ROTATION ENGINE ---
                        #import random
                        crowds = (sound_vic_crowd1, sound_vic_crowd2, sound_vic_crowd3, sound_vic_crowd4)
                        fireworks = (sound_vic_fireworks1, sound_vic_fireworks2, sound_vic_fireworks3, sound_vic_fireworks4)
                        music = (sound_vic_music1, sound_vic_music2, sound_vic_music3, sound_vic_music4)
                        
                        # Pick one random track from each category
                        chosen_crowd = random.choice(crowds)
                        chosen_fireworks = random.choice(fireworks)
                        chosen_music = random.choice(music)
                        
                        # Fire all three channels simultaneously in an infinite loop (-1)
                        if chosen_crowd: pygame.mixer.Channel(1).play(chosen_crowd, loops=-1)
                        if chosen_fireworks: pygame.mixer.Channel(2).play(chosen_fireworks, loops=-1)
                        if chosen_music: pygame.mixer.Channel(3).play(chosen_music, loops=-1)

                        
                         # >>> TRIGGER INITIAL VISUAL BLASTS HERE <<<
                        # Launch 3 distinct fireworks at random spots across your 1000x600 grid
                        celebration_fireworks.launch(random.randint(200, 600), random.randint(100, 200))
                        celebration_fireworks.launch(random.randint(450, 650), random.randint(80, 200))
                        celebration_fireworks.launch(random.randint(700, 950), random.randint(120, 200))
                        
                        #celebration_fireworks.launch(random.randint(200, 400), random.randint(100, 250))
                        #celebration_fireworks.launch(random.randint(450, 650), random.randint(80, 200))
                        #celebration_fireworks.launch(random.randint(700, 850), random.randint(120, 260))    
 
                        game_state = "CLEAR_LEADERBOARD"
                    else:
                        feedback_message = f"WORD GUESSED - - Matches: {num_matches}   Sequence: {num_sequence} {penalty_alert}"                    
                else:
                    feedback_message = "Invalid input! Use 5 letters or standard command layouts."
                    if sound_error: sound_error.play()  # <--- Fired for fake words!



            elif event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
 
            else:
                if len(user_input) < 15 and event.unicode and event.unicode.isprintable():
                    user_input += event.unicode
                    # Play the crisp mechanical sound on every letter typed
                    #if sound_click:
                        #sound_click.play()


 # 3. DRAW GRAPHICS ON CANVAS (Redirected entirely from SCREEN to canvas)
    canvas.fill(BLACKLESS)    
    if game_state == "CLEAR_LEADERBOARD":
        draw_high_scores()          
    else:       
        draw_worksheet(words_entered, letters_not_in_word, letters_might_be_in_word, letters_in_word, scroll_index)


    if game_state != "CLEAR_LEADERBOARD":
        display_score()
        penalty_alert = "" 
              
# --- DRAW THE HELP ICON BUTTON ---   
    draw_help_icon()

# --- DRAW THE HINT ICON BUTTON ---
    draw_hint_icon()

# --- DRAW THE RESET ICON BUTTON ---
    draw_reset_icon()
    

# ====================================================================
# RENDER SECTION BRANCH
# ====================================================================



    if game_state == "SPLASH" or game_state == "NAME_INPUT":
    # Call our dynamic title routine and pass the active typing buffer
        #print(game_state, "Bypassing file update to keep the game loop running.")
        draw_main_splash_screen(user_input)

# >>> INSERT THIS BRAND NEW BRANCH HERE <<<
    elif game_state == "ORIGIN_STORY":
    # Paint the safe, refactored wartime narrative window
        # 1. Start the music ONLY if it isn't already playing
        if not origin_music_playing:
            sound_VietNam.play(-1)
            origin_music_playing = True  # Locks this so it won't trigger again next frame
                             
        draw_origin_story_screen()

    
    elif game_state == "CLEAR_LEADERBOARD":
        # >>> ADDED BRANCH: Explicitly forces the engine to draw the high scores list <<<
        canvas.fill(BLACKLESS)
        draw_high_scores()
          # Increment the frame counter (runs 30 times a second)
        firework_timer += 1
        if firework_timer >= 45:  # Every 1.5 seconds...
            firework_timer = 0    # Reset the frame counter
            # Launch a single new firework at a random width/height position
            celebration_fireworks.launch(random.randint(100, 850), random.randint(100, 300))
            #celebration_fireworks.launch(random.randint(150, 850), random.randint(100, 300))
            
        # Update math positions and paint the flying particles onto the canvas
        celebration_fireworks.update_and_draw(canvas)        


    else:
    # ----------------------------------------------------------------
    # LEAVE ALL OF YOUR EXISTING DRAWING CODE EXACTLY AS IT IS HERE:
    # ----------------------------------------------------------------
        canvas.fill(BLACKLESS) 
        draw_worksheet(words_entered, letters_not_in_word, letters_might_be_in_word, letters_in_word, scroll_index)
        display_score()
    
    # --- DRAW THE HELP ICON BUTTON ---   
        draw_help_icon()

    # --- DRAW THE HINT ICON BUTTON ---
        draw_hint_icon()

    # --- DRAW THE RESET ICON BUTTON ---
        draw_reset_icon()
 

    if game_state == "PLAYING" or game_state == "ORIGIN_STORY":
        debug_surface = font_sz_20x.render(f"DEBUG MODE - SECRET WORD...... " + hold_secret_word, True, RED)
        canvas.blit(debug_surface, (330, 15)) 

    if show_help_overlay > 0:
        draw_help_overlay()     

    # ================================================================
    # FINAL DISPLAY SCALE FLIP ENGINE (AUTOMATIC MONITOR FIT)
    # ================================================================
    # Blow up our virtual 1000x600 canvas layout grid to fit the user's monitor surface size cleanly
    scaled_canvas = pygame.transform.smoothscale(canvas, (current_width, current_height))
    SCREEN.blit(scaled_canvas, (0, 0))

    pygame.display.flip()
    CLOCK.tick(30)                    
                    
                    
                        
                        
                        