# Importing modules

import pygame as p
from tkinter import *
from PIL import ImageTk
import random

# Class to manage the movements and points of the teams
class GamePos():
    def __init__(self):
        '''Initializes necessary variables'''

        # Board of CHESSOPOLY
        self.board = [
            ['BL1', 'BP1', 'BR', 'BH', 'BP2', 'BL2'],
            ['BS1', 'BS2', 'BS3', 'BS4', 'BS5', 'BS6'],
            ['__', '__', '__', '__', '__', '__'],
            ['Sp', '__', 'Sp', '__', 'Sp', '__'],
            ['__', 'Sp', '__', 'Sp', '__', 'Sp'],
            ['__', 'Sp', '__', 'Sp', '__', 'Sp'],
            ['Sp', '__', 'Sp', '__', 'Sp', '__'],
            ['__', '__', '__', '__', '__', '__'],
            ['CS1', 'CS2', 'CS3', 'CS4', 'CS5', 'CS6'],
            ['CL1', 'CP1', 'CR', 'CH', 'CP2', 'CL2']
            ]

        # Assets of every character
        self.prop = {
            'BL1':[200, 100, 'Lab 1'],
            'BL2':[200, 100, 'Lab 2'],
            'CL1':[200, 100, 'Lab 3'],
            'CL2':[200, 100, 'Lab 4'],
            'BP1':[400, 200, 'Office 412'],
            'BP2':[400, 200, 'Office 420'],
            'CP1':[400, 200, 'Office 408'],
            'CP2':[400, 200, 'Office 405'],
            'BR':[800, 1000, 'NUST'],
            'CR':[800, 1000, 'NUST'],
            'BH':[600, 400, 'SEECS'],
            'CH':[600, 400, 'NBS'],
            'BS1':[80],
            'BS2':[80],
            'BS3':[80],
            'BS4':[80],
            'BS5':[80],
            'BS6':[80],
            'CS1':[80],
            'CS2':[80],
            'CS3':[80],
            'CS4':[80],
            'CS5':[80],
            'CS6':[80]}

        # Character names
        self.char_name = {
            'L':'Lab Engineer',
            'P':'Professor',
            'R':'Rector',
            'H':'HOD',
            'S':'Student'}

        # Lab Engineer's scores for positional intelligence
        self.lab_eng_score = [
            [5, 5, 5, 5, 5, 5],
            [5, 10, 10, 10, 10, 5],
            [5, 10, 10, 10, 10, 5],
            [5, 10, 10, 10, 10, 5],
            [5, 10, 20, 20, 10, 5],
            [5, 10, 20, 20, 10, 5],
            [5, 10, 10, 10, 10, 5],
            [5, 10, 10, 10, 10, 5],
            [5, 10, 10, 10, 10, 5],
            [5, 5, 5, 5, 5, 5]]

        # Professor's scores for positional intelligence
        self.prof_score = [
            [40, 25, 10, 10, 25, 40],
            [32, 35, 16, 16, 35, 32],
            [24, 40, 24, 24, 40, 24],
            [16, 30, 32, 32, 30, 16],
            [10, 25, 40, 40, 25, 10],
            [10, 25, 40, 40, 25, 10],
            [16, 30, 32, 32, 30, 16],
            [24, 40, 24, 24, 40, 24],
            [32, 35, 16, 16, 35, 32],
            [40, 25, 10, 10, 25, 40]]

        # HOD's scores for positional intelligence
        self.hod_score = [
            [40, 25, 35, 35, 25, 40],
            [32, 35, 16, 16, 35, 32],
            [24, 40, 24, 24, 40, 24],
            [32, 30, 32, 32, 30, 32],
            [40, 25, 40, 40, 25, 40],
            [40, 25, 40, 40, 25, 40],
            [32, 30, 32, 32, 30, 32],
            [24, 40, 24, 24, 40, 24],
            [32, 35, 16, 16, 35, 32],
            [40, 25, 35, 35, 25, 40]]

        # Black Student's scores for positional intelligence
        self.bl_std_score = [
            [0, 0, 0, 0, 0, 0],
            [5, 5, 5, 5, 5, 5],
            [10, 10, 10, 10, 10, 10],
            [15, 15, 15, 15, 15, 15],
            [20, 20, 20, 20, 20, 20],
            [25, 25, 25, 25, 25, 25],
            [30, 30, 30, 30, 30, 30],
            [35, 35, 35, 35, 35, 35],
            [40, 40, 40, 40, 40, 40],
            [40, 40, 40, 40, 40, 40]]

        # Cyan Student's scores for positional intelligence
        self.cy_std_score = [
            [40, 40, 40, 40, 40, 40],
            [40, 40, 40, 40, 40, 40],
            [35, 35, 35, 35, 35, 35],
            [30, 30, 30, 30, 30, 30],
            [25, 25, 25, 25, 25, 25],
            [20, 20, 20, 20, 20, 20],
            [15, 15, 15, 15, 15, 15],
            [10, 10, 10, 10, 10, 10],
            [5, 5, 5, 5, 5, 5],
            [0, 0, 0, 0, 0, 0]]

        # To check the character's positional score
        self.char_scores = {'L':self.lab_eng_score,
                            'P':self.prof_score,
                            'H':self.hod_score,
                            'BS':self.bl_std_score,
                            'CS':self.cy_std_score}

        # For alternate turns
        self.black_turn = True

        # For the end
        self.result = False

        # for take_switch animation
        self.switch = False

        # For undo move
        self.turns_record = []
        self.props_to_rec = []
        self.props_fr_rec = []



    def your_turn(self, turn, attack_choice, shop_choice):
        '''Moves the characters to the possible places.
            Takes the object of 'Turn' Class as an argument'''

        self.attack_choice = attack_choice
        self.shop_choice = shop_choice

        # Assigning the object to a variable
        self.turn = turn

        # Rectangles where shops exist
        shop_spots = [(0, 3), (2, 3), (4, 3), (1, 4), (3, 4), (5, 4), (1, 5), (3, 5), (5, 5), (0, 6), (2, 6), (4, 6)]

        for spot in shop_spots:

            # If character stands on a shop
            if (turn.first_row, turn.first_col) == spot:
                self.board[turn.first_col][turn.first_row] = 'Sp'
                break

        else:
            self.board[turn.first_col][turn.first_row] = '__'

        # to undo props later
        self.props_fr_rec.append(self.prop[turn.turn_from])

        try:
            self.props_to_rec.append(self.prop[turn.turn_to])
            
        except:
            self.props_to_rec.append([0])

        # Opposite team's variable
        if self.black_turn:
            oppo_team = 'C'
        else:
            oppo_team = 'B'

        # If second click's on a shop & it's first time of this character on a shop
        if self.board[turn.sec_col][turn.sec_row] == 'Sp' and len(self.prop[turn.turn_from]) == 3:

            if self.shop_choice == 'accept':

                self.agree()

            elif self.shop_choice == 'ignore':

                self.destroyed()

            else:

                # Used in decide_menu()
                self.shop = True

                self.decide_menu()

        # If second click's on opposite team character
        elif self.board[turn.sec_col][turn.sec_row][0] == oppo_team:

            # depends on the attack_choice string
            if self.attack_choice == 'capture':

                self.capture_take()

            elif self.attack_choice == 'take_switch':

                self.take_switch()

            else:
                
                # Used in decide_menu()
                self.shop = False

                self.decide_menu()

        # Replacing second click with first to move characters
        self.board[turn.sec_col][turn.sec_row] = turn.turn_from
        
        # To undo moves later
        self.turns_record.append(turn)

        # Alternate turns
        self.black_turn = not self.black_turn



    def undo_turn(self):
        '''To undo turns. Also used to toggle between the teams at the start of the game.
            Note: It does not undo the properties & assets traded between the characters or with the shops.'''

        if len(self.turns_record) != 0:

            # Pop out the last move
            turn = self.turns_record.pop()

            # Switch places according to last move
            self.board[turn.first_col][turn.first_row] = turn.turn_from
            self.board[turn.sec_col][turn.sec_row] = turn.turn_to

            # Switch props on undo
            self.prop[turn.turn_from] = self.props_fr_rec.pop()

            if turn.turn_to[0] == 'B' or turn.turn_to[0] == 'C':
                self.prop[turn.turn_to] = self.props_to_rec.pop()

            else:
                self.props_to_rec.pop()

        # Alternate Turns
        self.black_turn = not self.black_turn



    def the_end(self):
        '''Adds the points of all characters of a team in one variable.
            Returns 2 variables each with a team's total points.'''
        
        black_team = 0
        cyan_team = 0

        # To visit every single rectangle on board
        for col in range(len(self.board)):

            for row in range(len(self.board[col])):

                char = self.board[col][row]

                # If team black's character
                if char[0] == 'B':

                    # if still holding a property
                    if len(self.prop[char]) == 3:
                        char_points = self.prop[char][0] + self.prop[char][1]

                    else:
                        char_points = self.prop[char][0]
                    
                    black_team += char_points

                # If team cyan's character
                elif char[0] == 'C':
                
                    # if still holding a property
                    if len(self.prop[char]) == 3:
                        char_points = self.prop[char][0] + self.prop[char][1]

                    else:
                        char_points = self.prop[char][0]

                    cyan_team += char_points

        return black_team, cyan_team



    def if_end(self):
        '''Returns True if the Rector was captured in the last move.'''
        
        # If Rector is captured
        return self.turn.turn_to[1] == 'R' and self.attack_choice == 'capture'



    def random_move(self, allowed_turns):
        '''Finds a random move for A.I.'''
      
        return allowed_turns[random.randint(0, len(allowed_turns)-1)]



    def best_move(self, allowed_turns):
        '''calls the best move finder & starts its recursion'''

        # declarnig global variables to be used in alpha beta pruning function
        global next_move, shop_choices_list, attack_choices_list, final, final_choices

        # initializing the variables
        next_move = None
        final = False
        final_choices = [0, 0]
        dep = 1
        final_moves = []
        attack_choices_list = ['capture',
                               'take_switch',
                               'capture if depth == 2 else take_switch',
                               'take_switch if depth == 2 else capture']
        
        shop_choices_list = ['accept',
                             'ignore',
                             'accept if depth == 2 else ignore',
                             'ignore if depth == 2 else accept']
        
        # starting the recurssion for move_alpha_beta_pruning()
        for i in range(4):
            for j in range(4):
                self.move_alpha_beta_pruning(allowed_turns, dep, -50000, 50000, 1 if not self.black_turn else -1, i, j)

                final_moves.append(next_move)

        final = True

        # starting the recurssion for move_alpha_beta_pruning()
        self.move_alpha_beta_pruning(final_moves, dep, -50000, 50000, 1 if not self.black_turn else -1, 0, 0)

        final = False

        return next_move, final_choices[0], final_choices[1]
    


    def move_alpha_beta_pruning(self, allowed_turns, depth, alpha, beta, turn_multiplier, counter1, counter2):
        '''best move finder using alpha beta pruning algorithm
                sets the best move equal to the global variable next_move'''

        global next_move, shop_choices_list, attack_choices_list, final, final_choices
        capture, take_switch, accept, ignore = 'capture', 'take_switch', 'accept', 'ignore'

        # when the finder is deepest in the tree
        if depth == 0:

            # returns score of the board based on material
            return turn_multiplier * self.score_board(self.board)

        # a small value to initialize the variable
        max_score = -50000

        # shuffling for next iteration
        random.shuffle(allowed_turns)

        # for every possible turn
        for turn in allowed_turns:

            self.your_turn(turn, eval(attack_choices_list[counter1]), eval(shop_choices_list[counter2]))

            # if final execution of the function
            if final:

                # to set the values of the counters for next iteration
                if counter2 == 3:

                    counter1 += 1

                    counter2 = 0

                # for next pair of choices
                else:

                    counter2 += 1

            # finding opponent's all possible turns
            next_moves = self.allowed_turns()

            # getting board's score if its deepest
            score = -self.move_alpha_beta_pruning(next_moves, depth - 1, -beta, -alpha, -turn_multiplier, counter1, counter2)

            # setting max_score for next iteration
            if score > max_score:

                max_score = score

                # if the finder is on top in the tree
                next_move = turn

                # the choices for the selected move
                final_choices[0], final_choices[1] = eval(attack_choices_list[counter1]), eval(shop_choices_list[counter2])

            # undoing the turns made
            self.undo_turn()

            # setting the new highest limit to search in
            if max_score > alpha:

                alpha = max_score

            # alpha must be smaller than beta for next iteration
            if alpha >= beta:

                break

        return max_score



    def score_board(self, board):
        '''scores the board to find best move'''
      
        # initial score
        score = 0

        # going thru the board
        for row in range(len(board)):

            for col in range(len(board[row])):

                sqr = board[row][col]

                if sqr != '__' and sqr != 'Sp':

                    # looking for positionally intelligent move

                    char_score = 0

                    # Shouldn't be Rector
                    if sqr[1] != 'R':

                        # Lab Engineer's Score
                        char_score = self.char_scores[sqr[:2]][row][col]*0.5 if sqr[1] == 'S' else self.char_scores[sqr[1]][row][col]

                    # for cyan pieces
                    if sqr[0] == 'C':

                        # maximizing the score for Cyan
                        if len(self.prop[sqr]) == 3:

                            score += (self.prop[sqr][0] + self.prop[sqr][1] + char_score)

                        else:

                            score += (self.prop[sqr][0] + char_score)

                    # for black pieces
                    elif sqr[0] == 'B':

                        # minimizing the score for Black
                        if len(self.prop[sqr]) == 3:

                            score -= (self.prop[sqr][0] + self.prop[sqr][1] + char_score)

                        else:

                            score -= (self.prop[sqr][0] + char_score)

        # score of the board state
        return score



    def decide_menu(self):
        '''Displays a window to select options either when clicked on shop or when capturing a character.
            Depends on self.shop'''

        # Specifying window's details
        self.decide = Tk()
        self.decide.title('Decide - CHESSOPOLY')
        self.decide.geometry('404x254')
        self.decide.resizable(False, False)
        self.decide.iconbitmap('images\\icon.ico')

        # Background image
        self.bg = ImageTk.PhotoImage(file='images\\decide.png')
        self.bg_img = Label(self.decide, image = self.bg)
        self.bg_img.place(x = 0, y = 0, relwidth = 1, relheight = 1)

        # True means a shop was clicked
        if self.shop:

            # Question
            self.question = f'''Welcome to the Shop, {self.char_name[self.turn.turn_from[1]]}!
You own "{self.prop[self.turn.turn_from][2]}".
Will you accept {self.prop[self.turn.turn_from][1]} points for this property?'''

            # Coordinates for question in decide window
            x_pos = 35
            y_pos = 45

            # Buttons to Accept OR Ignore
            self.agree_btn = Button(self.decide, text = 'Accept', command = self.agree, bg = '#7e6b26', fg = '#e7d789', font = ('Brush Script MT', 17))
            self.agree_btn.place(x = 227, y = 180)
        
            self.ignore_btn = Button(self.decide, text = 'Ignore', command = self.destroyed, bg = '#7e6b26', fg = '#e7d789', font = ('Brush Script MT', 17))
            self.ignore_btn.place(x = 87, y = 180)

        # False means opponent team member was clicked
        else:

            # If holding a property while being captured
            if len(self.prop[self.turn.turn_to]) == 3:

                self.worth = self.prop[self.turn.turn_to][0] + self.prop[self.turn.turn_to][1]


            # If not holding any property
            else:

                self.worth = self.prop[self.turn.turn_to][0]

            # Question
            self.question = f'''Hey {self.char_name[self.turn.turn_from[1]]}!
{self.char_name[self.turn.turn_to[1]]}'s Worth: {self.worth} Points.
Do you want to capture it?
OR
Will you take {self.prop[self.turn.turn_to][0]} Points and switch places with it?
What do you say?'''

            # Coordinates for question in decide window
            x_pos = 20
            y_pos = 12

            # Buttons to either take assets or capture
            self.agree_btn = Button(self.decide, text = 'Take & Switch', command = self.take_switch, bg = '#7e6b26', fg = '#e7d789', font = ('Brush Script MT', 14))
            self.agree_btn.place(x = 59, y = 190)
        
            self.capture_btn = Button(self.decide, text = 'Capture', command = self.capture_take, bg = '#7e6b26', fg = '#e7d789', font = ('Brush Script MT', 14))
            self.capture_btn.place(x = 259, y = 190)
            
        # Text Box to show the question
        self.txt_box = Label(self.decide, text = self.question, bg = '#e7d789', fg = '#7e6b26', font = ('Brush Script MT', 16))
        self.txt_box.place(x = x_pos, y = y_pos)

        self.decide.mainloop()



    def take_switch(self):
        '''Command to be executed when button 'Take & Switch' is chosen.'''

        # If first piece holding a property
        if len(self.prop[self.turn.turn_from]) == 3:

            # Adding the points of second character to first
            self.prop[self.turn.turn_from] = [self.prop[self.turn.turn_from][0] + self.prop[self.turn.turn_to][0], self.prop[self.turn.turn_from][1], self.prop[self.turn.turn_from][2]]

        # If not holding a prop
        else:

            self.prop[self.turn.turn_from] = [self.prop[self.turn.turn_from][0] + self.prop[self.turn.turn_to][0]]


        # Updating second piece's points
        if len(self.prop[self.turn.turn_to]) == 3:

            # points set to zero
            self.prop[self.turn.turn_to] = [0, self.prop[self.turn.turn_to][1], self.prop[self.turn.turn_to][2]]

        # if no property held
        else:

            self.prop[self.turn.turn_to] = [0]

        # Switching places
        self.switch = True

        # Closing decide window if opened
        if self.attack_choice == 'decide':
            self.decide.destroy()



    def capture_take(self):
        '''Command to be executed when button 'Capture' is chosen.'''

        # Properties of captured one
        self.prop[self.turn.turn_to] = [0]

        # Closing decide window if opened
        if self.attack_choice == 'decide':
            self.decide.destroy()



    def destroyed(self):
        '''Closes the shops message window'''

        if self.shop_choice == 'decide':
            self.decide.destroy()



    def agree(self):
        '''Updates the property details of the character'''

        # Updating property list of certain character
        self.prop[self.turn.turn_from] = [self.prop[self.turn.turn_from][0] + self.prop[self.turn.turn_from][1]]

        # Closing decide window when opened
        if self.shop_choice == 'decide':
            self.decide.destroy()



    def allowed_turns(self):
        '''Creates a list of possible turns.'''
        
        turns = []
        
        for col in range(len(self.board)):
            for row in range(len(self.board[col])):

                # First letter of character's name
                team = self.board[col][row][0]
                
                if (team == 'C' and (not self.black_turn)) or (team == 'B' and self.black_turn):

                    # Second letter of character's name
                    char = self.board[col][row][1]
                    
                    if char == 'S':
                        self.students_turns(col, row, turns)

                    elif char == 'L':
                        self.lab_eng_turns(col, row, turns)

                    elif char == 'P':
                        self.prof_turns(col, row, turns)

                    elif char == 'R':
                        self.rector_turns(col, row, turns)

                    elif char == 'H':
                        self.hod_turns(col, row, turns)

        # removing moves with same board state for the last 3 moves
        if len(self.turns_record) >= 6:
                        
            if self.turns_record[-1] == self.turns_record[-3] and self.turns_record[-1] in turns:

                turns.remove(self.turns_record[-1])

        return turns



    def students_turns(self, col, row, turns):
        '''Creates a list of possible turns of Students'''

        if self.black_turn:
            # Checking if the move's on board
            if col+1 < 10:

                # Checking if second click's a shop or empty space
                if self.board[col+1][row] == '__' or self.board[col+1][row] == 'Sp':
                    
                    turns.append(Turn((row, col), (row, col+1), self.board))

                    # Move 2 columns if on starting position
                    if col == 1 and (self.board[col+2][row] == '__' or self.board[col+2][row] == 'Sp'):
                        turns.append(Turn((row, col), (row, col+2), self.board))

                # Generating turns to capture diagonally
                
                if row-1 >= 0:
                    if self.board[col+1][row-1][0] == 'C':
                        turns.append(Turn((row, col), (row-1, col+1), self.board))

                if row+1 < 6:
                    if self.board[col+1][row+1][0] == 'C':
                        turns.append(Turn((row, col), (row+1, col+1), self.board))
                        
        else:
            # Again Checking same things for Cyan Team
            if col-1 >= 0:
                
                if self.board[col-1][row] == '__' or self.board[col-1][row] == 'Sp':
                    turns.append(Turn((row, col), (row, col-1), self.board))
                    
                    if col == 8 and (self.board[col-2][row] == '__' or self.board[col-2][row] == 'Sp'):
                        turns.append(Turn((row, col), (row, col-2), self.board))

                # Generating moves to kill diagonally
                if row-1 >= 0:
                    if self.board[col-1][row-1][0] == 'B':
                        turns.append(Turn((row, col), (row-1, col-1), self.board))

                if row+1 < 6:
                    if self.board[col-1][row+1][0] == 'B':
                        turns.append(Turn((row, col), (row+1, col-1), self.board))



    def lab_eng_turns(self, col, row, turns):
        '''Creates a list of possible turns of Lab Engineers'''

        # Possible spots for Lab Engineer
        lab_eng_spots = [(row-2, col+1), (row-1, col+2), (row+1, col+2), (row+2, col+1),
                         (row+2, col-1), (row+1, col-2), (row-1, col-2), (row-2, col-1)]
        
        if self.black_turn:
            same_team = 'B'
        else:
            same_team = 'C'

        
        for spot in lab_eng_spots:
            
            # Dividing spot into row & column
            sec_row = spot[0]
            sec_col = spot[1]
            
            if 0 <= sec_row < 6 and 0 <= sec_col < 10:
                # Character on that position
                sec_char = self.board[sec_col][sec_row]

                # If opposite team's character
                if sec_char[0] != same_team:
                    turns.append(Turn((row, col), (sec_row, sec_col), self.board))



    def prof_turns(self, col, row, turns):
        '''Creates a list of possible turns of Professors'''

        # Possible directions for Professor
        prof_spots = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
        
        if self.black_turn:
            oppo_team = 'C'
        else:
            oppo_team = 'B'

        for spot in prof_spots:

            # Validating moves in a direction
            for i in range(1, 6):
                sec_row = (spot[0] * i) + row
                sec_col = (spot[1] * i) + col

                # Does not move out of board
                if 0 <= sec_row < 6 and 0 <= sec_col < 10:
                    
                    sec_char = self.board[sec_col][sec_row]

                    # If empty or shops, keep going in this direction
                    if sec_char == '__' or sec_char == 'Sp':
                        turns.append(Turn((row, col), (sec_row, sec_col), self.board))

                    elif sec_char[0] == oppo_team:
                        turns.append(Turn((row, col), (sec_row, sec_col), self.board))
                        # If opposite team character, stop at that point
                        break

                    # Same team character
                    else:
                        break

                else:
                    break


        
    def hod_turns(self, col, row, turns):
        '''Creates a list of possible turns of HOD'''

        # Combination of Professor's move & some other moves
        self.prof_turns(col, row, turns)

        # Possible Directions for HOD
        hod_spots = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        if self.black_turn:
            oppo_team = 'C'
        else:
            oppo_team = 'B'

        for spot in hod_spots:

            # Generating moves for 5 steps in a direction
            for i in range(1, 6):
                
                sec_row = (spot[0] * i) + row
                sec_col = (spot[1] * i) + col

                # Checking if not out of board
                if 0 <= sec_row < 6 and 0 <= sec_col < 10:
                    
                    sec_char = self.board[sec_col][sec_row]
                    
                    if sec_char == '__' or sec_char == 'Sp':
                        turns.append(Turn((row, col), (sec_row, sec_col), self.board))
                        
                    # If opponent encountered, stop checking in this direction
                    elif sec_char[0] == oppo_team:
                        turns.append(Turn((row, col), (sec_row, sec_col), self.board))
                        break

                    # Same team member
                    else:
                        break

                else:
                    break



    def rector_turns(self, col, row, turns):
        '''Creates a list of possible turns of Rector'''

        # Possible spots for Rector
        rector_spots = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)]
        
        if self.black_turn:
            same_team = 'B'
        else:
            same_team = 'C'
            
        for spot in rector_spots:
            
            sec_row = spot[0] + row
            sec_col = spot[1] + col

            # Checking to see if move is out of board
            if 0 <= sec_row < 6 and 0 <= sec_col < 10:
                sec_char = self.board[sec_col][sec_row]

                # Dont move if same team member standing
                if sec_char[0] != same_team:
                    turns.append(Turn((row, col), (sec_row, sec_col), self.board))



# Class to generate the possible turns & turn IDs.
class Turn():
    def __init__(self, first_rec, sec_rec, board):
        '''Initializes variables & defines places on board for characters'''

        # First Click's coordinates
        self.first_row = first_rec[0]
        self.first_col = first_rec[1]

        # Second Click's coordinates
        self.sec_row = sec_rec[0]
        self.sec_col = sec_rec[1]

        # Spot from where character moves
        self.turn_from = board[self.first_col][self.first_row]

        # Spot where character lands after turn
        self.turn_to = board[self.sec_col][self.sec_row]

        # Unique turn ID of every move
        self.turn_ID = str(self.first_row) + str(self.first_col) + str(self.sec_row) + str(self.sec_col)
        
    def __eq__(self, other):
        '''Returns True if the turn ID is an instance of this class.
            Returns False otherwise.'''
        
        if isinstance(other, Turn):
            return self.turn_ID == other.turn_ID
        return False


        
