import pygame
import random

pygame.init()

ladder = {
    1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 51: 67, 72: 91, 80: 99
}
snake = {
    17: 7, 54: 34, 62: 19, 64: 60, 87: 36, 93: 73, 95: 75, 98: 79
}


next_player = {
    1: 2, 2: 1
}


mute = {
    0: 1, 1: 0
}


# Shows winner and individual points
def winner_msg(id):
    window.blit(bgimg, (0, 0))
    pygame.draw.rect(window, (250, 0, 0), [300, 500, 200, 50])
    print_text("Playfair", 30, "Play Again", (350, 512), (250, 250, 250))
    print_text("Playfair", 35, "Player " + str(id) + " won this game !!!", (250, 250), (250, 0, 0))
    print_text("Playfair", 25, "Player 1 - " + str(player1.points), (250, 300), (250, 0, 0))
    print_text("Playfair", 25, "Player 2 - " + str(player2.points), (250, 320), (250, 0, 0))
    win_sound()


def snake_sound():
    snake_hiss = pygame.mixer.Sound('snake.wav')
    snake_hiss.play()


def ladder_sound():
    ladder_climb = pygame.mixer.Sound('ladder.wav')
    ladder_climb.play()


def win_sound():
    winning = pygame.mixer.Sound('Win.wav')
    winning.play()


# green flag
def gf_sound():
    green_flag_sound = pygame.mixer.Sound('chime.wav')
    green_flag_sound.play()


# red flag
def rf_sound():
    red_flag_sound = pygame.mixer.Sound('lose.wav')
    red_flag_sound.play()


# returns True if play again button is clicked
def play_again_clicked():
    mouse = pygame.mouse.get_pos()
    if 300 < mouse[0] < 500 and 500 < mouse[1] < 550:
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True
        else:
            return False


def mute_clicked():
    mouse = pygame.mouse.get_pos()
    if 50 < mouse[0] < 150 and 500 < mouse[1] < 550:
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True
        else:
            return False


def unmute_clicked():
    mouse = pygame.mouse.get_pos()
    if 650 < mouse[0] < 750 and 500 < mouse[1] < 550:
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True
        else:
            return False


# returns True if play button is clicked
def play_clicked():
    mouse = pygame.mouse.get_pos()
    if 350 < mouse[0] < 450 and 200 < mouse[1] < 250:
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True
        else:
            return False


# returns True if quit button is clicked
def quit_clicked():
    mouse = pygame.mouse.get_pos()
    if 350 < mouse[0] < 450 and 450 < mouse[1] < 500:
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True
        else:
            return False


# returns True if how to play button is clicked
def tut_clicked():
    mouse = pygame.mouse.get_pos()
    if 325 < mouse[0] < 495 and 320 < mouse[1] < 370:
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True
        else:
            return False


# returns True if Back is clicked inside how to play guide
def tut_back_clicked():
    mouse = pygame.mouse.get_pos()
    if 300 < mouse[0] < 400 and 555 < mouse[1] < 595:
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True
        else:
            return False


# returns True if Roll Dice button is clicked
def rd_clicked():
    mouse = pygame.mouse.get_pos()
    if 645 < mouse[0] < 765 and 150 < mouse[1] < 190:
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True
        else:
            return False


# Rolls a dice and displays appropriate dice image
def roll_dice():
    d = random.randint(1, 6)
    dice = "dice" + str(d) + ".png"
    dice_img = pygame.image.load(dice)
    time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - time < 1000:
        window.blit(dice_img, (645, 15))
        pygame.display.update()
    return d


def dice_border():
    pygame.draw.rect(window, (153, 204, 255), (635, 15, 140, 125))
    pygame.draw.rect(window, (133, 173, 173), (635, 0, 140, 15))


def textbox_border():
    pygame.draw.rect(window, (0, 0, 255), (610, 200, 185, 100))
    print_text("Playfair", 20, " "*14 + "UPDATES", (610, 200), (0, 0, 0))
    pygame.draw.rect(window, (255, 255, 0), (610, 220, 185, 280))


# Shows the text updates about what is happening in the game
def implement_stack(stack):
    textbox_border()
    for i in range(0, 14):
        print_text("Playfair", 20, stack[i], (610, 220 + 20*i), (51, 202, 51))


def add_stack(string, stack):
    stack = [string] + stack
    stack.pop()
    return stack


def player_display(id):

    if id == 1:
        pygame.draw.rect(window, (0, 0, 204), (240, 510, 120, 30))
    else:
        pygame.draw.rect(window, (255, 0, 0), (240, 510, 120, 30))
    if id == 2:
        pygame.draw.rect(window, (0, 0, 204), (440, 510, 120, 30))
    else:
        pygame.draw.rect(window, (255, 0, 0), (440, 510, 120, 30))

    print_text("Playfair", 30, "Player 1", [260, 515, 120, 30])
    print_text("Playfair", 30, "Player 2", [460, 515, 120, 30])


# Displays the current position of both players
def display_check(p):
    pygame.draw.rect(window, (255, 255, 204), (240, 540, 120, 30))
    pygame.draw.rect(window, (255, 255, 204), (440, 540, 120, 30))

    print_text("Playfair", 30, "Check :" + str(p[0]), [260, 545, 120, 30])
    print_text("Playfair", 30, "Check :" + str(p[1]), [460, 545, 120, 30])


# Shows the nearest ladders, snakes, red flags, and green flags
def show_stats(p):
    pygame.draw.rect(window, (102, 102, 153), [34, 70, 120, 30])
    print_text("Playfair", 30, "Player Stats", [34, 75, 120, 30])
    window.blit(blue_pin, (120, 120))
    window.blit(yellow_pin, (170, 120))

    lst = ["Ladder", "Snake", "G_flag", "R_flag"]
    for i in range(0, len(lst)):
        pygame.draw.rect(window, (102, 255, 102), (0, 190 + 80*i, 110, 21))
        print_text("Playfair", 21, "Nearest "+lst[i], (0, 190 + 80*i), (0, 0, 0))

    pygame.draw.rect(window, (255, 255, 255), (120, 190, 80, 300))
    for i in range(0,2):
        print_text("Playfair", 21, nearest(ladder.keys(), p[i]), (120+50*i, 195), (0, 0, 0))
        print_text("Playfair", 21, nearest(snake.keys(), p[i]), (120+50*i, 275), (0, 0, 0))
        print_text("Playfair", 21, nearest(green_flags, p[i]), (120+50*i, 345), (0, 0, 0))
        print_text("Playfair", 21, nearest(red_flags, p[i]), (120+50*i, 425), (0, 0, 0))


def nearest(lst, a):
    x = [(y - a) for y in lst if y > a]
    if len(x):
        return str(min(x) + a)
    else:
        return '-'


def scoreboard(points1, points2):
    pygame.draw.rect(window, (250, 0, 0), [24, 520, 160, 90])
    print_text("Playfair", 30, "Scoreboard", (50, 525))
    print_text("Playfair", 20, "Player 1: " + str(points1), (70, 555))
    print_text("Playfair", 20, "Player 2: " + str(points2), (70, 575))


# general function to display texts on screen
#font style, font size,text to be printed, position
def print_text(f, fs, text, pos, clr=(0, 0, 0)):
    fnt = pygame.font.SysFont(f, fs)
    txtsurf = fnt.render(text, True, clr)
    window.blit(txtsurf, pos)
    pygame.display.update()


# The starting screen
def start():
    pygame.display.set_caption("Snake N Ladders: But Different")
    window.blit(bgimg, (0, 0))
    pygame.draw.rect(window, (250, 0, 0), [350, 200, 100, 50])
    pygame.draw.rect(window, (250, 0, 0), [325, 320, 170, 50])
    pygame.draw.rect(window, (250, 0, 0), [350, 450, 100, 50])
    pygame.draw.rect(window, (250, 0, 0), [50, 500, 100, 50])
    pygame.draw.rect(window, (250, 0, 0), [650, 500, 100, 50])
    print_text("Playfair", 30, "PLAY", (372, 215), (250, 250, 250))
    print_text("Playfair", 30, "HOW TO PLAY", (340, 335), (250, 250, 250))
    print_text("Playfair", 30, "QUIT", (372, 465), (250, 250, 250))
    print_text("Playfair", 30, "Mute", (65, 515), (250, 250, 250))
    print_text("Playfair", 30, "Unmute", (665, 515), (250, 250, 250))


# The screen when the game starts
def play():
    window.blit(bg, (0, 0))
    textbox_border()
    display_check([0, 0])
    player_display(1)
    scoreboard(player1.points, player2.points)
    show_stats([0, 0])
    window.blit(brd, (brd_x, brd_y))
    dice_border()
    pygame.draw.rect(window, (255, 0, 0), [645, 150, 120, 40])
    print_text("Playfair", 30, "Roll Dice", (665, 160), (255, 255, 0))
    show_flags(green_flags, red_flags)


# Displays how to play
def tut():
    window.blit(tut_ins, (180, 0))
    pygame.draw.rect(window, (255, 0, 0), [300, 545, 100, 50])
    print_text("Playfair", 30, "BACK", (317, 555), (250, 250, 250))


def tut_playing():
    tut()

    tut_viewing = True

    while tut_viewing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        if tut_back_clicked():
            tut_viewing = False

    pygame.display.update()


# Displays which piece represents which player
def player_clr(text):
    if text == "Player 1":
        pygame.draw.rect(window, (250, 0, 0), [640, 510, 96, 20])
        print_text("Playfair", 30, text, [645, 510, 60, 20])
    else:
        pygame.draw.rect(window, (250, 0, 0), [640, 560, 96, 20])
        print_text("Playfair", 30, text, [645, 560, 60, 20])


def get_row(ps):
    if ps <= 10:
        return 1
    elif ps <= 20:
        return 2
    elif ps <= 30:
        return 3
    elif ps <= 40:
        return 4
    elif ps <= 50:
        return 5
    elif ps <= 60:
        return 6
    elif ps <= 70:
        return 7
    elif ps <= 80:
        return 8
    elif ps <= 90:
        return 9
    elif ps <= 100:
        return 10


# Calculates the pixel position where the piece will now move
def next_pixel_pos(row, ps, id):
    if row % 2:
        if id == 1:
            add = 15
        else:
            add = 5
        return brd_x + (ps - 1 - (row - 1) * 10) * 40 + add
    else:
        if id == 1:
            add = 25
        else:
            add = 35
        return brd_x + 400 - (ps - 1 - (row - 1) * 10) * 40 - add


# Function to move the pieces around the board
def move(p):
    row1 = get_row(p[0])
    row2 = get_row(p[1])
    next_x_pos1 = next_pixel_pos(row1, p[0], 1)
    next_x_pos2 = next_pixel_pos(row2, p[1], 2)
    window.blit(brd, (brd_x, brd_y))
    show_flags(green_flags, red_flags)
    window.blit(blue_pin, (next_x_pos1, brd_y + (10 - row1) * 40 + 10))
    if p[1] != 0:
        window.blit(yellow_pin, (next_x_pos2, brd_y + (10 - row2) * 40 + 10))
    pygame.display.update()


# Generates flags at random positions
def generate_flags():
    lst_flags = []
    while len(lst_flags) != 10:
        # Choosing which tile the flag appears
        x = random.randint(1, 100)
        lst_flags.append(x)
        # Checking whether the element is repeated
        for i in range(0, len(lst_flags) - 1):
            if lst_flags[len(lst_flags) - 1] == lst_flags[i]:
                lst_flags.pop()
                break
    # first five will be green flags and next red
    return lst_flags[:5], lst_flags[5:]


def show_flags(green, red):
    for p in green:
        window.blit(gflag, generate_coords(p))
    for p in red:
        window.blit(rflag, generate_coords(p))
    pygame.display.update()


# Pixel coordinates of flags
# Coordinates of check p is coordinates[100-p]
def generate_coords(s):
    coords = []
    for y in range(100, 500, 40):
        row = []
        for x in range(200, 600, 40):
            row.append((x, y))
        if ((y - 100) / 40) % 2 != 0:
            row.sort(reverse=True)
        coords.extend(row)
    return coords[100 - s]


brd_x = 200
brd_y = 100
brd_width = brd_height = 400
stack = [' ']*20
#all images
bgimg = pygame.image.load("menu1.jpg")
bg = pygame.image.load("background.jpg")
brd = pygame.image.load("board1.jpg")
tut_ins = pygame.image.load("instruc.png")
window = pygame.display.set_mode((800, 600))
blue_pin = pygame.image.load("blue.png")
yellow_pin = pygame.image.load("yellow.png")
green_flags, red_flags = generate_flags()
gflag = pygame.image.load("greenflag.png")
rflag = pygame.image.load("redflag.png")


class player:
    def __init__(self, points):
        self.points = points


player1 = player(0)
player2 = player(0)


def main():
    m = 1
    play_again = 0
    # Start screen
    start()
    pygame.mixer.music.load('sample2.wav')
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play(-1)
    menu = True
    tut_viewing = False
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        if play_clicked():
            # Starts the game
            play()
            break
        if tut_clicked():
            tut_viewing = True
            break
        if mute_clicked():
            pygame.mixer.music.pause()
        if unmute_clicked():
            pygame.mixer.music.unpause()
        if quit_clicked():
            exit()
    while tut_viewing:
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        # See the guide (how to play)
        tut()
        if tut_back_clicked():
            return 1

        pygame.display.update()
    window.blit(blue_pin, (760, 510))
    window.blit(yellow_pin, (760, 560))
    player_clr("Player 1")
    player_clr("Player 2")
    i = 1   # Whose chance to play
    p = [0, 0]     # Starting positions
    playing = True
    while playing:
        pygame.display.update()
        if rd_clicked():
            player_display(i)
            d = roll_dice()
            global stack
            stack = add_stack("Player " + str(i) + " has rolled a " + str(d), stack)
            implement_stack(stack)
            p[i - 1] += d   # Change the position
            if p[i - 1] < 100:
                move(p)

            delay = 0
            # if the player lands on ladder's base or snake's mouth
            if p[i - 1] in ladder.keys():
                p[i - 1] = ladder[p[i - 1]]
                ladder_sound()
                stack = add_stack("Player " + str(i) + " climbed up a ladder", stack)
                implement_stack(stack)
                delay = 1

            elif p[i - 1] in snake.keys():
                p[i - 1] = snake[p[i - 1]]
                snake_sound()
                stack = add_stack("Player " + str(i) + " slid down a snake", stack)
                implement_stack(stack)

                delay = 1
            if delay:
                pygame.time.delay(500)
                # To show the intermediate position during climbing ladder or sliding down a snake
            if p[i - 1] < 100:
                move(p)
            # Counting points
            if p[i - 1] in red_flags:
                rf_sound()
                if i == 1:
                    player1.points -= 3
                else:
                    player2.points -= 3
            elif p[i - 1] in green_flags:
                gf_sound()
                if i == 1:
                    player1.points += 5
                else:
                    player2.points += 5
            if p[i - 1] >= 100:
                if i == 1:
                    player1.points += 10    # Finished the game
                else:
                    player2.points += 10
                if player1.points > player2.points:
                    winner_msg(1)
                elif player2.points > player1.points:
                    winner_msg(2)
                else:   # If scores are tied then the one who reached the end of the board wins
                    winner_msg(i)
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()
                    if play_again_clicked():
                        play_again = 1
                        break

            if play_again == 1:
                break
            display_check(p)
            show_stats(p)
            scoreboard(player1.points, player2.points)
            if d != 6:  # If d == 6 then the player gets another chance
                i = next_player[i]

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
    return play_again


pa = main()
while pa:
    stack = [' '] * 20
    pa = main()

