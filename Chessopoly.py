# Importing built-in modules
from tkinter import *
from PIL import ImageTk
import pygame as p
import sys

# Importing self-defined module
import Engine
import Modules


def main():
      '''Starts the game. Does not take any argument. Returns None'''

      p.init()

      # Stops all current sound channels
      p.mixer.quit()

      # Eliminates the menu from the screen
      menu.destroy()

      Modules.loop_music()
      mute = False

      # Dimensions of the game window.
      width = 880
      height = 612

      # Rows & Columns on the board
      rows = 6
      columns = 10

      # Dimensions of each rectangle
      rec_height = int(height/rows)
      rec_width = int(width/columns)

      # Initializing variables
      screen = p.display.set_mode((width, height+60))
      screen.fill(p.Color('White'))
      
      turn_black = True
      the_end = False
      rec_click = ()
      one_turn = []
      total_time = 0
      turn_done = False
      animate = False

      # True when human plays the color but when AI does, its false
      player_black  = False
      player_cyan = False
      
      gp = Engine.GamePos()

      # Icon & caption on the window
      p.display.set_icon(p.image.load('images\\icon.png'))
      p.display.set_caption('CHESSOPOLY')

      # Object to track time
      clock = p.time.Clock()

      # Object storing all possible turns
      allowed_turns = gp.allowed_turns()

      Modules.load_images(rec_width, rec_height)

      # To enter while loop
      ev = p.event.get()[0]

      
      # Exit only when X is pressed
      while ev.type != p.QUIT:

            # by default, black is for human, cyan is for AI
            human_turn = (gp.black_turn and player_black) or (not gp.black_turn and player_cyan)
            
            for ev in p.event.get():

                  if ev.type == p.QUIT:

                        p.quit()

                        # Back to Main Menu
                        menu_func()

                  elif ev.type == p.MOUSEBUTTONDOWN:

                        if human_turn:

                              # Position of the cursor
                              coord = p.mouse.get_pos()

                              # clicking on white sectioning
                              if coord[1] > 612:
                                    continue

                              # Column & Row number
                              col = coord[0]//rec_width
                              row = coord[1]//rec_height
      
                              # Empties the variables if clicked on same rectangle twice
                              if rec_click == (row, col):
                                    rec_click = ()
                                    one_turn = []
      
                              else:
                                    # Storing the cursor positions
                                    rec_click = (row, col)
                                    one_turn.append(rec_click)
      
                              if len(one_turn) == 2:
      
                                    # Object of the class 'Turn'
                                    turn = Engine.Turn(one_turn[0], one_turn[1], gp.board)
      
                                    # iterating through the valid moves
                                    for i in range(len(allowed_turns)):
      
                                          # If it's a possible turn
                                          if turn == allowed_turns[i]:
            
                                                # Making the turn
                                                gp.your_turn(allowed_turns[i], 'decide', 'decide')
      
                                                turn_done = True
                                                animate = True
      
                                                # Boolean Var. to see if second click was on Rector
                                                the_end = gp.if_end()
      
                                                # For alternate turns
                                                turn_black = not turn_black
                                          
                                    if not turn_done:
                                          # Stores the invalid click
                                          one_turn = [rec_click]

                  elif ev.type == p.KEYDOWN:

                        # Undo button
                        if ev.key == p.K_z:

                              # Undo move when one is A.I.
                              if not player_black or not player_cyan:

                                    gp.undo_turn()
                                    gp.undo_turn()

                              # Undo move when both players are humans
                              else:
                                    gp.undo_turn()

                              turn_done = True

                              # not animating turn
                              animate = False

                        # Mute Button
                        if ev.key == p.K_m:

                              # Turning music on
                              if mute:
                                    Modules.loop_music()

                              # Turning music off
                              else:
                                    p.mixer.quit()

                              # Alternating status
                              mute = not mute

            # if its AI's turn
            if not human_turn:

                  # choosing the best move
                  AI_move, attack_choice, shop_choice = gp.best_move(allowed_turns)

                  if AI_move is None:

                        AI_move = gp.random_move(allowed_turns, attack_choice, shop_choice)

                  # making that move
                  gp.your_turn(AI_move, attack_choice, shop_choice)

                  turn_done = True
                  animate = True

                  # Boolean Var. to see if second click was on Rector
                  the_end = gp.if_end()
      
                  # For alternate turns
                  turn_black = not turn_black

                  
            # when move is made
            if turn_done:

                  # animating the turn
                  if animate:
                        Modules.animate_turns(gp.turns_record[-1], screen, gp.board, clock, rec_width, rec_height, rows, columns)

                  # when Rector's captured
                  if the_end:
      
                        # Points of the teams
                        team_black, team_cyan = gp.the_end()
      
                        # Result of game
                        Modules.result(team_black, team_cyan)

                  # animating take_switch turn
                  if gp.switch:

                        gp.board[gp.turn.first_col][gp.turn.first_row] = gp.turn.turn_to
                        gp.switch = False

                  # Empties the variables for next click
                  rec_click = ()
                  one_turn = []

                  # Updating list of possible moves
                  allowed_turns = gp.allowed_turns()

                  turn_done = False


            # Turn message in the bottom
            Modules.turn_of(screen, turn_black)

            # Updating characters position
            Modules.draw_board_characs(screen, gp, rec_width, rec_height, rows, columns, rec_click, allowed_turns)

            # Seconds per frame (spf)
            spf = clock.tick()
            
            total_time += spf

            # Loop on music file
            if total_time >= 58000:

                  total_time = 0
                  Modules.loop_music()
                  
            # Updating display
            p.display.flip()



def menu_func():
      '''Displays Main Menu of the Game'''
      global menu

      # Creating the main menu window
      menu = Tk()
      menu.title('CHESSOPOLY')
      menu.geometry('880x614')
      menu.resizable(False,False)
      menu.iconbitmap('images\\icon.ico')

      # Loading the background
      bg = ImageTk.PhotoImage(file = 'images\\background.png')

      # Displaying image
      bg_img = Label(menu, image = bg).place(x = 0, y = 0, relwidth = 1, relheight = 1)

      # Displaying buttons
      playbtn = Button(menu, text = 'PLAY GAME', command = main, bg = '#7e6b26', fg = 'black', font = ('Brush Script MT', 20))
      playbtn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

      rulesbtn = Button(menu, text = 'RULES', command = to_rules, bg = '#7e6b26', fg = 'black', font = ('Brush Script MT', 20))
      rulesbtn.place(relx = 0.5, rely = 0.64, anchor = CENTER)

      exitbtn = Button(menu, text = 'EXIT', command = exit_menu, bg = '#7e6b26', fg = 'black', font = ('Brush Script MT', 20))
      exitbtn.place(relx = 0.5, rely = 0.78, anchor = CENTER)

      menu.mainloop()
      

      
def to_rules():
      '''Closes the menu window & opens the Rules window'''
      menu.destroy()
      Modules.rules1()



def exit_menu():
      '''Closes the program'''
      menu.destroy()
      sys.exit()



# To avoid execution of the function when called in Modules.py
if __name__ == '__main__':
      menu_func()



