# Impprts
import sys
import pygame
from pygame.locals import QUIT
# Start-------------------------------------------------------------------------------
pygame.init()
# Display
display = pygame.display.set_mode((700, 500))
# Title5
pygame.display.set_caption('Calculator made by Sameer')
# Variable
clock = pygame.time.Clock()
white = (255, 255, 255)
cyan = (0, 255, 255)
grey = (90, 90, 90)
black = (0, 0, 0)
answer_area_color = (220, 246, 247)
answer = ''
font_answer = pygame.font.Font('calculator_text.ttf', 60)
font_button = pygame.font.Font('calculator_text.ttf', 50)
font_operator = pygame.font.Font(None, 50)
text_answer = font_answer.render(answer, True, black)
text_dict = {
    '1': font_button.render('1', True, black),
    '2': font_button.render('2', True, black),
    '3': font_button.render('3', True, black),
    '4': font_button.render('4', True, black),
    '5': font_button.render('5', True, black),
    '6': font_button.render('6', True, black),
    '7': font_button.render('7', True, black),
    '8': font_button.render('8', True, black),
    '9': font_button.render('9', True, black),
    '0': font_button.render('0', True, black),
    '=': font_operator.render("=", True, black),
    '+': font_operator.render("+", True, black),
    '-': font_operator.render("-", True, black),
    '×': font_button.render('×', True, black),
    '÷': font_button.render('÷', True, black),
    'C': font_button.render('C', True, black),
    '←': font_button.render('←', True, black),
}
rect_dimensions_dict = {
    'rect1': (5, 100, 145, 100),
    'rect2': (153, 100, 152, 100),
    'rect3': (310, 100, 140, 100),
    'rect4': (5, 205, 145, 100),
    'rect5': (153, 205, 152, 100),
    'rect6': (310, 205, 140, 100),
    'rect7': (5, 310, 145, 100),
    'rect8': (153, 310, 152, 100),
    'rect9': (310, 310, 140, 100),
    'rect10': (5, 415, 145, 80),
    'rect11': (153, 415, 297, 80),
    'rect12': (455, 100, 130, 100),
    'rect13': (455, 205, 130, 100),
    'rect14': (455, 310, 130, 100),
    'rect15': (455, 415, 130, 80),
    'rect16': (590, 100, 105, 190),
    'rect17': (590, 300, 105, 195),
}
blit_dimensions_dict = {
    'rect1': (158/2, 122.5),
    'rect2': (220, 122.5),
    'rect3': (365, 122.5),
    'rect4': (65, 235),
    'rect5': (220, 235),
    'rect6': (365, 235),
    'rect7': (65, 330),
    'rect8': (220, 330),
    'rect9': (365, 330),
    'rect10': (65, 430),
    'rect11': (300, 440),
    'rect12': (510, 130),
    'rect13': (510, 235),
    'rect14': (510, 340),
    'rect15': (510, 440),
    'rect16': (630, 160),
    'rect17': (630, 350),
}
button_logic_dict = {
    '1': (5, 100, 145, 100),
    '2': (153, 100, 152, 100),
    '3': (310, 100, 140, 100),
    '4': (5, 205, 145, 100),
    '5': (153, 205, 152, 100),
    '6': (310, 205, 140, 100),
    '7': (5, 310, 145, 100),
    '8': (153, 310, 152, 100),
    '9': (310, 310, 140, 100),
    '0': (5, 415, 145, 80),
    '=': (153, 415, 297, 80),
    '+': (455, 100, 130, 100),
    '-': (455, 205, 130, 100),
    '×': (455, 310, 130, 100),
    '÷': (455, 415, 130, 80),
    'C': (590, 100, 105, 190),
    '←': (590, 300, 105, 195),
}
# Loop-----------------------------------------------------------------------------------
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for key, rect in button_logic_dict.items():
                if pygame.Rect(rect).collidepoint(mouse_x, mouse_y):
                    pygame.draw.rect(display, (200, 200, 200), rect, border_radius=20)
                    pygame.display.flip()
                    pygame.time.delay(100)
                    if key.isdigit() or key in ['+', '-', '×', '÷']:
                        answer += key
                        text_answer = font_answer.render(answer, True, black)
                        display.blit(text_answer, (50, 30))
                    elif key=='C':
                        answer=''
                        text_answer = font_answer.render(answer, True, black)
                        display.blit(text_answer, (50, 30))
                    elif key=='←':
                        answer=answer[:-1]
                        text_answer = font_answer.render(answer, True, black)
                        display.blit(text_answer, (50, 30))
                    elif key=="=":
                        try:
                            if '÷' in answer:
                                answer=answer.replace('÷', '/')
                                answer=eval(answer)
                            elif '×' in answer:
                                answer=answer.replace('×', '*')
                                answer=eval(answer)
                            else:
                                answer=eval(answer)
                            text_answer = font_answer.render(str(answer), True, black)
                            display.blit(text_answer, (50, 30))
                            answer=str(answer)
                        except Exception as e:
                            answer = 'Error'
                            text_answer = font_answer.render(answer, True, black)
                            display.blit(text_answer, (50, 30))
                            pygame.display.flip()
                            pygame.time.delay(2000)
                            answer=''
                            text_answer = font_answer.render(answer, True, black)
                            display.blit(text_answer, (50, 30))
                            pygame.display.flip()
    # Display color
    display.fill((40, 40, 40))
    # Main border
    pygame.draw.rect(display, cyan, pygame.Rect(
        0, 0, 700, 500), 5, border_radius=20)
    # Answer area
    pygame.draw.rect(display, answer_area_color, pygame.Rect(
        0, 0, 700, 100), border_radius=20)
    # Answer Text
    display.blit(text_answer, (50, 30))
    # Drawing of rectangles for buttons
    for key, value in rect_dimensions_dict.items():
        pygame.draw.rect(display, grey, pygame.Rect(value), border_radius=20)
    # Drawing of Buttons
    for (key1, value1), (key2, value2) in zip(blit_dimensions_dict.items(), text_dict.items()):
        display.blit(value2, value1)
#     # Display update
    pygame.display.flip()
    clock.tick(60)
# End-------------------------------------------------------------------------------