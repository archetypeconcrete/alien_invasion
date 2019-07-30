import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from alien import Alien
from pygame.sprite import Group
from button import Button
import game_functions as gf
from scoreboard import Scoreboard


def run_game():
    # Инициализирует игру и создает область экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Создание корабля, группы пуль и группы пришельцев
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Создание пришельца
    alien = Alien(ai_settings, screen)

    # Создание флота пришельцев
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Создание экземпляров GameStats и Scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Создание кнопки Play.
    play_button = Button(ai_settings, screen, "Play")

    # Запуск основного цикла игры
    while True:
        # Отслеживание событий клавиатуры и мыши
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                             bullets)
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button)


run_game()
