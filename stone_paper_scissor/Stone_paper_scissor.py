import pygame
import random
import time


#Loop ------------ ---------------------------------------------Starts
def loop():
  pygame.init()
  #Computer Choise
  rand = random.randint(0, 2500)
  if rand <= 128:
    compchoise = "stone"
  elif rand <= 255:
    compchoise = "paper"
  else:
    compchoise = "scissors"

  #Display
  display = pygame.display.set_mode((800, 590))
  pygame.display.set_caption("Stone Paper Scissors By Sameer")
  #Variables
  exit = False
  User_choice = ""
  key1 = False
  key2 = False
  key3 = False
  Image = True
  Comp = False
  confirm = False
  Comp_win = False
  User_win = False
  choice = False
  Tie = False
  Display = True
  #Images
  stone = pygame.image.load('stone.jpg')
  stone2 = pygame.image.load('stone2.jpg')
  paper = pygame.image.load('paper.jpg')
  paper2 = pygame.image.load('paper2.jpg')
  sccissor = pygame.image.load('sccissor.jpg')
  sccissor2 = pygame.image.load('sccissor2.jpg')
  # FPS
  clock = pygame.time.Clock()
  #Colour
  grey = (90, 90, 90)
  black = (0, 0, 0)
  red = (255, 0, 0)
  white = (255, 255, 255)
  button1 = (334, 553)
  #Text
  font = pygame.font.Font('font.ttf', 18)
  font2 = pygame.font.Font('font.ttf', 50)
  font3 = pygame.font.Font('font.ttf', 30)
  text = font.render('Stone', True, black)
  text2 = font.render('Paper', True, black)
  text3 = font.render('Scissor', True, black)
  text4 = font.render('Chose your choice', True, red)
  text5 = font.render('Are you confirm?', True, red)
  text6 = font.render('Yes', True, black)
  text7 = font.render('No', True, black)
  text8 = font2.render('You won!!', True, white)
  text9 = font2.render('You lose!!', True, white)
  text10 = font2.render('Tie!!', True, white)
  text11 = font3.render('Press space to continue', True, white)
  while not exit:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        exit = True
    display.fill((255, 255, 255))
    pygame.draw.rect(display, grey, (300, 520, 55, 20))
    pygame.draw.rect(display, black, (300, 520, 55, 20), 2)
    pygame.draw.rect(display, grey, (400, 520, 60, 20))
    pygame.draw.rect(display, black, (400, 520, 60, 20), 2)
    pygame.draw.rect(display, grey, (500, 520, 70, 20))
    pygame.draw.rect(display, black, (500, 520, 70, 20), 2)
    display.blit(text, (300, 520))
    display.blit(text2, (400, 518))
    display.blit(text3, (500, 518))
    display.blit(text4, (350, 550))
    #Choices
    if pygame.mouse.get_pos()[0] >= 300 and pygame.mouse.get_pos(
    )[0] <= 355 and pygame.mouse.get_pos()[1] >= 520 and pygame.mouse.get_pos(
    )[1] <= 540 and pygame.mouse.get_pressed()[0] == True and Display == True:
      key1 = True
      key2 = False
      key3 = False
      confirm = True
      Image = True
      User_choice = "stone"
    elif pygame.mouse.get_pos()[0] >= 400 and pygame.mouse.get_pos(
    )[0] <= 460 and pygame.mouse.get_pos()[1] >= 520 and pygame.mouse.get_pos(
    )[1] <= 540 and pygame.mouse.get_pressed()[0] == True and Display == True:
      key1 = False
      key2 = True
      key3 = False
      Image = True
      confirm = True
      User_choice = "paper"
    elif pygame.mouse.get_pos()[0] >= 500 and pygame.mouse.get_pos(
    )[0] <= 570 and pygame.mouse.get_pos()[1] >= 520 and pygame.mouse.get_pos(
    )[1] <= 540 and pygame.mouse.get_pressed()[0] == True and Display == True:
      key1 = False
      key2 = False
      key3 = True
      Image = True
      confirm = True
      User_choice = "scissors"
      #Image Formation
    if key1 == True and Image == True and Display == True:
      display.blit(stone2, (500, 150))
      choice = True
    elif key2 == True and Image == True and Display == True:
      display.blit(paper2, (500, 150))
      choice = True
    elif key3 == True and Image == True and Display == True:
      display.blit(sccissor2, (500, 150))
      choice = True
      #Confirmation
    if confirm == True and Display == True:
      pygame.draw.rect(display, grey, (300, 200, 200, 120))
      pygame.draw.rect(display, black, (300, 200, 200, 120), 2)
      display.blit(text5, (330, 210))
      pygame.draw.rect(display, white, (330, 270, 50, 20))
      pygame.draw.rect(display, black, (330, 270, 50, 20), 2)
      pygame.draw.rect(display, white, (420, 270, 50, 20))
      pygame.draw.rect(display, black, (420, 270, 50, 20), 2)
      display.blit(text6, (340, 270))
      display.blit(text7, (430, 270))
      #Yes
    if pygame.mouse.get_pos()[0] >= 330 and pygame.mouse.get_pos(
    )[0] <= 380 and pygame.mouse.get_pos()[1] >= 270 and pygame.mouse.get_pos(
    )[1] <= 290 and pygame.mouse.get_pressed()[0] == True and Display == True:
      Comp = True
      #No
    elif pygame.mouse.get_pos()[0] >= 420 and pygame.mouse.get_pos(
    )[0] <= 470 and pygame.mouse.get_pos()[1] >= 270 and pygame.mouse.get_pos(
    )[1] <= 290 and pygame.mouse.get_pressed()[0] == True and Display == True:
      confirm = False
      Image = False
      loop()
    #Computer Image
    if compchoise == "stone" and choice == True and Comp == True and Display == True:
      display.blit(stone, (20, 150))
      confirm = False
      pygame.display.flip()
      Image = False
    elif compchoise == "paper" and choice == True and Comp == True and Display == True:
      display.blit(paper, (20, 150))
      confirm = False
      pygame.display.flip()
      Image = False
    elif compchoise == "scissors" and choice == True and Comp == True and Display == True:
      display.blit(sccissor, (20, 150))
      confirm = False
      pygame.display.flip()
      Image = False
  # Winner
    if User_choice == "stone" and compchoise == "paper":
      Comp_win = True
    elif User_choice == "stone" and compchoise == "scissors":
      User_win = True
    elif User_choice == "stone" and compchoise == "stone":
      Tie = True
    elif User_choice == "paper" and compchoise == "paper":
      Tie = True
    elif User_choice == "paper" and compchoise == "scissors":
      Comp_win = True
    elif User_choice == "paper" and compchoise == "stone":
      User_win = True
    elif User_choice == "scissors" and compchoise == "paper":
      User_win = True
    elif User_choice == "scissors" and compchoise == "scissors":
      Tie = True
    elif User_choice == "scissors" and compchoise == "stone":
      Comp_win = True
    #Win
    if User_win == True and Image == False:
      confirm = False
      time.sleep(1)
      display.fill(black)
      display.blit(text8, (300, 100))
      display.blit(text11, (280, 250))
      pygame.display.flip()
      Display = False
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            loop()
            break
        if event.type == pygame.QUIT:
          exit = True
          break
    elif Comp_win == True and Image == False:
      confirm = False
      time.sleep(1)
      display.fill(black)
      display.blit(text9, (300, 100))
      display.blit(text11, (280, 250))
      pygame.display.flip()
      Display = False
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            loop()
            break
        if event.type == pygame.QUIT:
          exit = True
          break
    elif Tie == True and Image == False:
      confirm = False
      time.sleep(1)
      display.fill(black)
      display.blit(text10, (300, 100))
      display.blit(text11, (280, 250))
      pygame.display.flip()
      Display = False
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            loop()
            break
        if event.type == pygame.QUIT:
          exit = True
          break
    pygame.display.flip()
    clock.tick(60)
    #Confirm condition


loop()
pygame.quit()