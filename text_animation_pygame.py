import sys
import time
import pygame
# Display------------------------------------------------------------------------
display = pygame.display.set_mode((300, 50))
pygame.display.set_caption("By Sameer")
# Variables---------------------------------------------------------------------
alphabets =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",' ']
exit=False
white = (255, 255, 255)
black = (0, 0, 0)
clock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.Font(None, 40)
to_print=''
txt="HP"
pygame.init()
#Main Loop ----------------------------------------------------------------------
while not exit:
  display.fill(white)
  pygame.display.flip()
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      exit = True
  if exit:
    pygame.quit()
    sys.exit()
  for a in txt:
    for i in alphabets:
      time.sleep(0.02)
      if to_print==txt:
        time.sleep(0.5)
        exit=True
        pygame.quit()
        sys.exit()
      display.fill(white)
      pygame.display.flip()
      text = font.render(to_print+i, True, black)
      display.blit(text, (0, 0))
      pygame.display.flip()
      time.sleep(0.05)
      if i ==a:
        to_print=to_print+i
        break
  clock.tick(59)
#Ending----------------------------------------------------------------------
pygame.quit()