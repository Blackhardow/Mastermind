#Please check out README.md for the rules of Mastermind game
import random, pygame, sys

SQUARE_SIZE = 50

abs_white = (194, 188, 187)

attempts = 10
num_pieces = 4
 
#Creating a window
width = SQUARE_SIZE * num_pieces * 2 + SQUARE_SIZE
hight = SQUARE_SIZE * attempts + SQUARE_SIZE
screen = pygame.display.set_mode((width, hight))
background = pygame.image.load('assets/bg_game.png')


piece_im = {
  "r": 'assets/red_button_46x46.png',
  "o": 'assets/orange_button_46x46.png',
  "y": 'assets/yellow_button_46x46.png',
  "g": 'assets/green_button_46x46.png',
  "b": 'assets/blue_button_46x46.png',
  "p": 'assets/purple_button_46x46.png'
}


def Img(Img, x, y):
  #drawing pegs or images on the specific coordinates
  screen.blit(Img, (x, y))

def game_setup():
  #Initiailize the pygame
  pygame.init() 

  #Title and Icon
  pygame.display.set_caption("MasterMind")

  #Screen background
  screen.blit(background, (0, 0))

  def grid1():
    #draw grid for the codebreacker input and codemaker output 
    #c - column, r - row
    for c in range(num_pieces):
      for r in range(attempts):
        rect = pygame.Rect(c * SQUARE_SIZE + 5, (r+1) * SQUARE_SIZE, SQUARE_SIZE - 5, SQUARE_SIZE - 5)
        pygame.draw.rect(screen, abs_white,rect,1)
        pygame.draw.circle(screen, abs_white,((c + num_pieces +1/2) * SQUARE_SIZE, (r+1.5) * SQUARE_SIZE), (SQUARE_SIZE - 20)/2,2)
  grid1()

  def grid2():
    #draw grid for the hidden row
    for c in range(num_pieces):
      rect = pygame.Rect(c * SQUARE_SIZE + 5, 0, SQUARE_SIZE - 5, SQUARE_SIZE - 5)
      pygame.draw.rect(screen, abs_white,rect,3)
  grid2()

  # Draw the side bar
  red_im = pygame.image.load(piece_im["r"])
  red_choice_x = (width - SQUARE_SIZE)
  red_choice_y = (hight - SQUARE_SIZE)

  oran_im = pygame.image.load(piece_im["o"])
  oran_choice_x = (width - SQUARE_SIZE)
  oran_choice_y= (hight - SQUARE_SIZE * 2)

  yel_im = pygame.image.load(piece_im["y"])
  yel_choice_x = (width - SQUARE_SIZE)
  yel_choice_y = (hight - SQUARE_SIZE * 3)

  gre_im = pygame.image.load(piece_im["g"])
  gre_choice_x = (width - SQUARE_SIZE)
  gre_choice_y = (hight - SQUARE_SIZE * 4)

  ble_im = pygame.image.load(piece_im["b"])
  ble_choice_x = (width - SQUARE_SIZE)
  ble_choice_y = (hight - SQUARE_SIZE * 5)

  pple_im = pygame.image.load(piece_im["p"])
  pple_choice_x= (width - SQUARE_SIZE)
  pple_choice_y= (hight - SQUARE_SIZE * 6)

  rel = pygame.image.load('assets/reload.png')
  rel_x = (8 * SQUARE_SIZE)
  rel_y = 0

  Img(red_im, red_choice_x, red_choice_y)
  Img(oran_im, oran_choice_x, oran_choice_y)
  Img(yel_im, yel_choice_x, yel_choice_y)
  Img(gre_im, gre_choice_x, gre_choice_y)
  Img(ble_im, ble_choice_x, ble_choice_y)
  Img(pple_im, pple_choice_x,  pple_choice_y)
  Img(rel, rel_x, rel_y)
  pygame.display.update()


def color_pieces(im_piece, i, row):
  choiceX = (i*SQUARE_SIZE+5)
  choiceY = (hight - (11-row)*SQUARE_SIZE)
  Img(im_piece, choiceX, choiceY)
  pygame.display.update()

def conf_pieces(im_piece, i, row):
  respond_x = ((4+i)*SQUARE_SIZE)
  respond_y = (hight - (11-row)*SQUARE_SIZE)
  Img(im_piece, respond_x, respond_y)
  pygame.display.update()


game_setup()

piece_conf = {
  "black": 'assets/black_button_46x46.png',
  "abs_white": 'assets/abs_white_button_46x46.png'
}

def select_random_piece():
  selected_one = []
  for i in range(4):
    list_of_colors = list(piece_im.keys())
    selected_one.append(random.choice(list_of_colors))
  print(f"La piece cachee est : {selected_one}")
  return selected_one

def reload(a, b, c, d, event):
  if a < event.pos[0] < b and c < event.pos[1]< d:
    attempts = 10
    game_setup()
    game(attempts)

def show_hidden_row(selected_one):
  for index, val in enumerate(selected_one):
    im_piece = pygame.image.load(piece_im[val])
    color_pieces(im_piece, index, 0)

def game_over_screen(selected_one):
    show_hidden_row(selected_one)
    EndImg = pygame.image.load('assets/game_over.png')
    Img(EndImg, 0, 0)
    pygame.display.update()

def game(attempts):
  
  #Creating codemaker row
  selected_one = select_random_piece()
  game_is_on = True
  #Game Loop
  while True:
    #Sidebar panel
    while game_is_on == True: 
      codebreaker_row = [] 
      i = 0
      while i < num_pieces and attempts > 0:
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
            #Quiting the game
            pygame.quit()
            sys.exit()
          elif event.type == pygame.MOUSEBUTTONDOWN:
            #Color pegs
            if 400 < event.pos[0] < 450 and event.pos[1]>250:
              if 500 < event.pos[1] < 550:
                selected_color = "r"
              elif 450 < event.pos[1] < 500:
                selected_color = "o"
              elif 400 < event.pos[1] < 450:
                selected_color = "y"
              elif 350 < event.pos[1] < 400:
                selected_color = "g"
              elif 300 < event.pos[1] < 350:
                selected_color = "b"
              elif 250 < event.pos[1] < 300:
                selected_color = "p"
              codebreaker_row.append(selected_color)
              im_piece = pygame.image.load(piece_im[selected_color])
              color_pieces(im_piece, i, attempts)
              i +=1
            # Reload button
            reload(400, 450, 0, 50, event)
         

      selected_one_copy = selected_one[:]
      codebreaker_row_copy = codebreaker_row[:]
      codemaker_response = []

      #Computer response
      for index1, val1 in enumerate(codebreaker_row_copy):
        for index2, val2 in enumerate(selected_one_copy):
          if index1 == index2 and val1 == val2:
            codemaker_response.append("black")
            selected_one_copy[index2] = None
            codebreaker_row_copy[index1] = None
      for index1, val1 in enumerate(codebreaker_row_copy):
        for index2, val2 in enumerate(selected_one_copy):
          if val2 == val1 and index1 != index2 and val1 != None:
            codemaker_response.append("abs_white")
            selected_one_copy[index2] = None 
            codebreaker_row_copy[index1] = None
            break

      #Computer response - visual part
      for index, val in enumerate(codemaker_response):
        im_piece = pygame.image.load(piece_conf[val])
        conf_pieces(im_piece, index, attempts)


      print(f"Les resultats sont :\n{codemaker_response}")
      
      attempts = attempts - 1

      # Win/lose check
      if attempts >= 0 and codemaker_response == ["black", "black", "black", "black"]:
        WinImg = pygame.image.load('assets/you_win.png')
        Img(WinImg, 200, 0)
        print ("VOUS AVEZ GAGNEZ HOURRAAA HOURRAAA!")
        game_over_screen(selected_one) 
        game_is_on = True 
        break
      elif attempts < 0 and codemaker_response != ["black", "black", "black", "black"]:
        LoseImg = pygame.image.load('assets/you_lose.png')
        Img(LoseImg, 200, 0)
        print ("DESOLE TU PERDUS")
        game_over_screen(selected_one)
        game_is_on = True
        break

      print (f"Il te reste {attempts} tentative")
    
    #Reload the game
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        reload(100, 350, 250, 300, event)
  
game(attempts)
