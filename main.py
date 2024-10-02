import pygame
import sys
from button import button_class
from functions import count_eng
from functions import count_ru

#инициализация
pygame.init()

#размер экрана
width, height = 800, 800

#фоны
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("nedoscrabble")
background_main_eng = pygame.image.load("backgrounds/back_main_eng.png")
background_main_ru = pygame.image.load("backgrounds/back_main_ru.png")
background_rules_eng = pygame.image.load("backgrounds/back_rules_eng.png")
background_rules_ru = pygame.image.load("backgrounds/back_rules_ru.png")
background_game_eng = pygame.image.load("backgrounds/back_game_eng.png")
background_game_ru = pygame.image.load("backgrounds/back_game_ru.png")

#функция окна главного меню (англ)
def main_menu_eng():
    #создание кнопок
    start_height = 350
    start_button = button_class(70, start_height, 374.5, 90, "", "buttons/start_button_eng.png", "buttons/start_button_hover_eng.png")
    rules_button = button_class(70, start_height + 120, 464.5, 90, "", "buttons/rules_button_eng.png", "buttons/rules_button_hover_eng.png")
    exit_button = button_class(70, start_height + 240, 374.5, 90, "", "buttons/exit_button_eng.png", "buttons/exit_button_hover_eng.png")
    language_button = button_class(620, 660, 123.2, 60, "", "buttons/language_button_eng.png", "buttons/language_button_hover_eng.png")
    running = True
    while running:
        #вывод фон
        screen.fill((0, 0, 0))
        screen.blit(background_main_eng, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == start_button:
                game_eng()
            if event.type == pygame.USEREVENT and event.button == rules_button:
                rules_eng()
            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT and event.button == language_button:
                main_menu_ru()

            for buttons in [start_button, rules_button, exit_button, language_button]:
                buttons.handle_event(event)

        for buttons in [start_button, rules_button, exit_button, language_button]:
            buttons.draw(screen)
            buttons.check_hover(pygame.mouse.get_pos())

        pygame.display.flip()

#функция окна главного меню (рус)
def main_menu_ru():
    #создание кнопок
    start_height = 350
    start_button = button_class(70, start_height, 374.5, 90, "", "buttons/start_button_ru.png", "buttons/start_button_hover_ru.png")
    rules_button = button_class(70, start_height + 120, 647.4, 90, "", "buttons/rules_button_ru.png", "buttons/rules_button_hover_ru.png")
    exit_button = button_class(70, start_height + 240, 464.5, 90, "", "buttons/exit_button_ru.png", "buttons/exit_button_hover_ru.png")
    language_button = button_class(620, 660, 123.2, 60, "", "buttons/language_button_ru.png", "buttons/language_button_hover_ru.png")
    running = True
    while running:
        #вывод экрана
        screen.fill((0, 0, 0))
        screen.blit(background_main_ru, (0, 0))

        #события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT and event.button == start_button:
                game_ru()
            if event.type == pygame.USEREVENT and event.button == rules_button:
                rules_ru()
            if event.type == pygame.USEREVENT and event.button == exit_button:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT and event.button == language_button:
                main_menu_eng()

            for buttons in [start_button, rules_button, exit_button, language_button]:
                buttons.handle_event(event)

        #вывод кнопок
        for buttons in [start_button, rules_button, exit_button, language_button]:
            buttons.draw(screen)
            buttons.check_hover(pygame.mouse.get_pos())

        pygame.display.flip()

#функция окна игры (англ)
def game_eng():
    #создание кнопок
    back_button = button_class(70, 590, 374.5, 90, "", "buttons/back_button_eng.png",
                               "buttons/back_button_hover_eng.png")
    count_button = button_class(70, 470, 464.5, 90, "", "buttons/count_button_eng.png",
                               "buttons/count_button_hover_eng.png")
    again_button = button_class(70, 470, 464.5, 90, "", "buttons/again_button_eng.png",
                               "buttons/again_button_hover_eng.png")
    language_button = button_class(620, 660, 123.2, 60, "", "buttons/language_button_eng.png",
                                   "buttons/language_button_hover_eng.png")
    #введенный текст
    input_text = ''
    #возможность ввода
    need_input = True

    running = True
    while running:
        #вывод экрана
        screen.fill((0, 0, 0))
        screen.blit(background_game_eng, (0, 0))

        #события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT and event.button == count_button:
                input_text = count_eng(input_text)
                need_input = False
            if event.type == pygame.USEREVENT and event.button == again_button:
                input_text = ''
                need_input = True
            if event.type == pygame.KEYDOWN and need_input:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
            if event.type == pygame.USEREVENT and event.button == back_button:
                main_menu_eng()
            if event.type == pygame.USEREVENT and event.button == language_button:
                game_ru()

            if need_input:
                for buttons in [back_button, language_button, count_button]:
                    buttons.handle_event(event)
            if not need_input:
                for buttons in [back_button, language_button, again_button]:
                    buttons.handle_event(event)

        #вывод кнопок
        if need_input:
            for buttons in [back_button, language_button, count_button]:
                buttons.draw(screen)
                buttons.check_hover(pygame.mouse.get_pos())
        if not need_input:
            for buttons in [back_button, language_button, again_button]:
                buttons.draw(screen)
                buttons.check_hover(pygame.mouse.get_pos())

        #вывод текста
        font = pygame.font.Font('fonts/Uncage.ttf', 30)
        text_surface = font.render(input_text, True, (230,230,230))
        text_rect = text_surface.get_rect(center=(width/2, 200))
        screen.blit(text_surface, text_rect)

        pygame.display.flip()

#функция окна игры (рус)
def game_ru():
    #создание кнопок
    back_button = button_class(70, 590, 464.5, 90, "", "buttons/back_button_ru.png",
                               "buttons/back_button_hover_ru.png")
    count_button = button_class(70, 470,374.5 , 90, "", "buttons/count_button_ru.png",
                               "buttons/count_button_hover_ru.png")
    again_button = button_class(70, 470, 557.4, 90, "", "buttons/again_button_ru.png",
                               "buttons/again_button_hover_ru.png")
    language_button = button_class(620, 660, 123.2, 60, "", "buttons/language_button_ru.png",
                                   "buttons/language_button_hover_ru.png")
    #введенный текст
    input_text = ''
    #возможность ввода
    need_input = True

    running = True
    while running:
        #вывод экрана
        screen.fill((0, 0, 0))
        screen.blit(background_game_ru, (0, 0))

        #события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT and event.button == count_button:
                input_text = count_ru(input_text)
                need_input = False
            if event.type == pygame.USEREVENT and event.button == again_button:
                input_text = ''
                need_input = True
            if event.type == pygame.KEYDOWN and need_input:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
            if event.type == pygame.USEREVENT and event.button == language_button:
                game_eng()
            if event.type == pygame.USEREVENT and event.button == back_button:
                main_menu_ru()

            if need_input:
                for buttons in [back_button, language_button, count_button]:
                    buttons.handle_event(event)
            if not need_input:
                for buttons in [back_button, language_button, again_button]:
                    buttons.handle_event(event)

        #вывод кнопок
        if need_input:
            for buttons in [back_button, language_button, count_button]:
                buttons.draw(screen)
                buttons.check_hover(pygame.mouse.get_pos())
        if not need_input:
            for buttons in [back_button, language_button, again_button]:
                buttons.draw(screen)
                buttons.check_hover(pygame.mouse.get_pos())

        #вывод текста
        font = pygame.font.Font('fonts/Uncage.ttf', 30)
        text_surface = font.render(input_text, True, (230,230,230))
        text_rect = text_surface.get_rect(center=(width/2, 200))
        screen.blit(text_surface, text_rect)

        pygame.display.flip()

#функция окна правил (англ)
def rules_eng():
    #создание кнопок
    back_button = button_class(70, 590, 374.5, 90, "", "buttons/back_button_eng.png", "buttons/back_button_hover_eng.png")
    language_button = button_class(620, 660, 123.2, 60, "", "buttons/language_button_eng.png",
                                   "buttons/language_button_hover_eng.png")

    running = True
    while running:
        #вывод экрана
        screen.fill((0, 0, 0))
        screen.blit(background_rules_eng, (0, 0))

        #события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT and event.button == back_button:
                main_menu_eng()
            if event.type == pygame.USEREVENT and event.button == language_button:
                rules_ru()

            for buttons in [back_button, language_button]:
                buttons.handle_event(event)

        #вывод кнопок
        for buttons in [back_button, language_button]:
            buttons.draw(screen)
            buttons.check_hover(pygame.mouse.get_pos())

        pygame.display.flip()

#функция окна правил (рус)
def rules_ru():
    # создание кнопок
    back_button = button_class(70, 590, 464.5, 90, "", "buttons/back_button_ru.png",
                               "buttons/back_button_hover_ru.png")
    language_button = button_class(620, 660, 123.2, 60, "", "buttons/language_button_ru.png",
                                   "buttons/language_button_hover_ru.png")
    running = True
    while running:
        #вывод экрана
        screen.fill((0, 0, 0))
        screen.blit(background_rules_ru, (0, 0))

        #события
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT and event.button == back_button:
                main_menu_ru()
            if event.type == pygame.USEREVENT and event.button == language_button:
                rules_eng()

            for buttons in [back_button, language_button]:
                buttons.handle_event(event)

        #вывод кнопок
        for buttons in [back_button, language_button]:
            buttons.draw(screen)
            buttons.check_hover(pygame.mouse.get_pos())

        pygame.display.flip()


#вызов функции главного меню, включение игры
main_menu_eng()