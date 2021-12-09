import pygame


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
