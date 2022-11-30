import pygame
import math
import time


class SuperTicTacToe:
    def __init__(self):
        self.available_positions = {
            0: [(0, 0), (50, 0), (100, 0), (0, 50), (50, 50), (100, 50), (0, 100), (50, 100), (100, 100)
                ],
            1: [(200, 0), (250, 0), (300, 0), (200, 50), (250, 50), (300, 50), (200, 100), (250, 100),
                (300, 100)],
            2: [(400, 0), (450, 0), (500, 0), (400, 50), (450, 50), (500, 50), (400, 100), (450, 100),
                (500, 100)],
            3: [(0, 200), (50, 200), (100, 200), (0, 250), (50, 250), (100, 250), (0, 300), (50, 300),
                (100, 300)],
            4: [(200, 200), (250, 200), (300, 200), (200, 250), (250, 250), (300, 250), (200, 300),
                (250, 300), (300, 300)],
            5: [(400, 200), (450, 200), (500, 200), (400, 250), (450, 250), (500, 250), (400, 300),
                (450, 300), (500, 300)],
            6: [(0, 400), (50, 400), (100, 400), (0, 450), (50, 450), (100, 450), (0, 500), (50, 500),
                (100, 500)],
            7: [(200, 400), (250, 400), (300, 400), (200, 450), (250, 450), (300, 450), (200, 500),
                (250, 500), (300, 500)],
            8: [(400, 400), (450, 400), (500, 400), (400, 450), (450, 450), (500, 450), (400, 500),
                (450, 500), (500, 500)]
        }
        self.cross_positions = {0: [None, None, None, None, None, None, None, None, None],
                                1: [None, None, None, None, None, None, None, None, None],
                                2: [None, None, None, None, None, None, None, None, None],
                                3: [None, None, None, None, None, None, None, None, None],
                                4: [None, None, None, None, None, None, None, None, None],
                                5: [None, None, None, None, None, None, None, None, None],
                                6: [None, None, None, None, None, None, None, None, None],
                                7: [None, None, None, None, None, None, None, None, None],
                                8: [None, None, None, None, None, None, None, None, None]}
        self.naught_positions = {0: [None, None, None, None, None, None, None, None, None],
                                 1: [None, None, None, None, None, None, None, None, None],
                                 2: [None, None, None, None, None, None, None, None, None],
                                 3: [None, None, None, None, None, None, None, None, None],
                                 4: [None, None, None, None, None, None, None, None, None],
                                 5: [None, None, None, None, None, None, None, None, None],
                                 6: [None, None, None, None, None, None, None, None, None],
                                 7: [None, None, None, None, None, None, None, None, None],
                                 8: [None, None, None, None, None, None, None, None, None]}

        self.cross_sqrs_won = [False, False, False, False, False, False, False, False, False]
        self.naught_sqrs_won = [False, False, False, False, False, False, False, False, False]

        self.big_sqr_corner_coords = [(0, 0), (200, 0), (400, 0), (0, 200), (200, 200),
                                      # coordinates of the big square corners
                                      (400, 200), (0, 400), (200, 400), (400, 400)]
        self.green_bar_pos_coords = [(0, 150), (200, 150), (400, 150), (0, 185), (200, 185),
                                     # the coords where the green bar will
                                     (400, 185), (0, 385), (200, 385), (400, 385)]  # go
        self.big_sqrs_not_won = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        self.available_big_squares = [0, 1, 2, 3, 4, 5, 6, 7, 8]

        # load all the images that we will need, and assign them to variables
        self.icon = pygame.image.load(r"Assets\tic-tac-toe.png")
        self.cross = pygame.image.load(r"Assets\x.png")
        self.big_cross = pygame.image.load(r"Assets\big_x.png")
        self.nought = pygame.image.load(r"Assets\o.png")
        self.big_nought = pygame.image.load(r"Assets\big_o.png")
        self.grey_sqr = pygame.image.load(r"Assets\grey_45x45_sqr.png")
        self.sqr_in_play_bar = pygame.image.load(r"Assets\green_bar.png")   # green bar that shows what squares in play
        self.remove_sqr_in_play_bar = pygame.image.load(r"Assets\white_bar.png")  # white bar
        self.game_over_screen = pygame.image.load(r"Assets\gameover.png")

        pygame.init()
        self.screen = pygame.display.set_mode((550, 550))
        pygame.display.set_icon(self.icon)  # make the window look nice
        pygame.display.set_caption("Super Tic-Tac-Toe")

    @staticmethod
    def round_down_coords(mouse_position, number_to_round_to):  # rounds the coordinates of the click down to the nearest x.
        x = (math.floor(mouse_position[0] / number_to_round_to)) * number_to_round_to
        y = (math.floor(mouse_position[1] / number_to_round_to)) * number_to_round_to

        return x, y

    @staticmethod
    def current_big_square_calc(mouse_positions):  # returns which square the user clicked in
        x = (math.floor(mouse_positions[0] / 200)) * 200
        y = (math.floor(mouse_positions[1] / 200)) * 200
        big_square_coords_pos = {(0, 0): 0,
                                 (200, 0): 1,
                                 (400, 0): 2,
                                 (0, 200): 3,
                                 (200, 200): 4,
                                 (400, 200): 5,
                                 (0, 400): 6,
                                 (200, 400): 7,
                                 (400, 400): 8
                                 }
        return big_square_coords_pos[(x, y)]

    def place_move(self, team, coords, current_big_sqr):  # this function does the stuff required for a move
        if team == "Cross":
            self.screen.blit(self.cross, coords)  # place a cross on the screen

            coord_list_pos = self.available_positions[current_big_sqr].index(coords)
            self.cross_positions[current_big_sqr][coord_list_pos] = coords  # add in where the cross went
            # replace the available coord with None so that the player can't just go there again
            self.available_positions[current_big_sqr][coord_list_pos] = None

            return "Naught"  # switch the team over

        elif team == "Naught":  # same as for cross, but with the naught's variables
            self.screen.blit(self.nought, coords)
            coord_list_pos = self.available_positions[current_big_sqr].index(coords)
            self.naught_positions[current_big_sqr][coord_list_pos] = coords

            self.available_positions[current_big_sqr][coord_list_pos] = None
            return "Cross"

    def place_sqr_in_play_bar(self, bar, sqrs_in_play):
        for element in sqrs_in_play:
            if element is not None:
                self.screen.blit(bar, self.green_bar_pos_coords[element])  # place in the green bar

    def small_sqr_win_recognition(self, big_sqr, team_dictionary, team_name, team_image, team_list):
        square_won = False
        # for the big square we just played in, check if the coords line up
        for i in range(3):  # for each row and column
            num = 3 * i
            # check if one of the rows or columns won
            if "None" not in f"{team_dictionary[big_sqr][0 + num]}{team_dictionary[big_sqr][1 + num]}" \
                             f"{team_dictionary[big_sqr][2 + num]}" or "None" not in f"{team_dictionary[big_sqr][0 + i]}" \
                                                                                     f"{team_dictionary[big_sqr][3 + i]}" \
                                                                                     f"{team_dictionary[big_sqr][6 + i]}":
                square_won = True
        # check if the team won on the diagonal
        if None not in (team_dictionary[big_sqr][0], team_dictionary[big_sqr][4], team_dictionary[big_sqr][8]) or \
                None not in (team_dictionary[big_sqr][2], team_dictionary[big_sqr][4], team_dictionary[big_sqr][6]):
            square_won = True

        if square_won:
            # print(f"{team_name} won square {big_sqr + 1}!")
            self.available_positions[big_sqr] = [None]
            self.big_sqrs_not_won[self.big_sqrs_not_won.index(big_sqr)] = None
            self.screen.blit(team_image, self.big_sqr_corner_coords[big_sqr])

            team_list[big_sqr] = True

            return self.big_sqr_win_recognition(team_list)

        # check if the square is filled. the len is to ensure that the square we are checking is not already won
        # the team_name == Cross is because the win rec is run multiple times.
        elif team_name == "Cross" and len(self.available_positions[big_sqr]) > 1 and all(i is None for i in self.available_positions[big_sqr]):
            self.available_positions[big_sqr] = [None]
            self.big_sqrs_not_won[self.big_sqrs_not_won.index(big_sqr)] = None

    def big_sqr_win_recognition(self, list_of_sqrs):
        victory = False
        for i in range(3):  # check if any rows or columns won
            num = 3 * i
            if False not in (list_of_sqrs[0 + i], list_of_sqrs[3 + i], list_of_sqrs[6 + i]):  # check if column won
                line_start_stop_positions = {0: [(75, 75), (75, 475)],  # where to draw the connecting line
                                             1: [(275, 75), (275, 475)],
                                             2: [(475, 75), (475, 475)]}
                line_start_stop = [line_start_stop_positions[i][0], line_start_stop_positions[i][1]]
                victory = True

            if False not in (list_of_sqrs[0 + num], list_of_sqrs[1 + num], list_of_sqrs[2 + num]):  # check if row won
                line_start_stop_positions = {0: [(75, 75), (475, 75)],
                                             1: [(75, 275), (475, 275)],
                                             2: [(75, 475), (475, 475)]}
                line_start_stop = [line_start_stop_positions[i][0], line_start_stop_positions[i][1]]
                victory = True

        if False not in (list_of_sqrs[0], list_of_sqrs[4], list_of_sqrs[8]):  # check diagonal top left to bottom right
            line_start_stop = [(75, 75), (475, 475)]
            victory = True

        if False not in (list_of_sqrs[2], list_of_sqrs[4], list_of_sqrs[6]):  # check diagonal bottom left to top right
            line_start_stop = [(475, 75), (75, 475)]
            victory = True

        if all(i is None for i in self.big_sqrs_not_won):
            line_start_stop = [(0, 0), (0, 0)]
            victory = True

        if victory:  # draw on the line if someone has won
            pygame.draw.line(surface=self.screen, color=(236, 28, 36), start_pos=line_start_stop[0],
                             end_pos=line_start_stop[1],
                             width=30)
        return victory

    def setup(self):
        self.screen.fill((255, 255, 255,))  # set a white background

        for key in self.available_positions.keys():  # draw in all the grey squares
            for coord in self.available_positions[key]:
                self.screen.blit(self.grey_sqr, coord)

        self.place_sqr_in_play_bar(self.sqr_in_play_bar, self.available_big_squares)  # place in the green bars

    def game_run(self, team_turn):
        self.setup()
        game_over = False
        while not game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            mouse_click_detect = pygame.mouse.get_pressed(num_buttons=3)

            if mouse_click_detect[0]:  # when someone right clicks
                mouse_pos = pygame.mouse.get_pos()  # get the position of the mouse
                rounded_coords = self.round_down_coords(mouse_pos, 50)  # round it down to lowest 50, so that x/o lines up nicely
                time.sleep(0.2)  # insert small break to stop it registering the same click multiple times
                clicked_big_square = self.current_big_square_calc(mouse_pos)

                if clicked_big_square in self.available_big_squares:
                    small_available_positions = self.available_positions[clicked_big_square]

                    if str(rounded_coords) in str(small_available_positions):

                        coord_position = small_available_positions.index(
                            rounded_coords)  # where in the big square is it (0-8)

                        self.place_sqr_in_play_bar(self.remove_sqr_in_play_bar,
                                                   self.available_big_squares)  # remove all the green bars
                        team_turn = self.place_move(team_turn, rounded_coords,
                                                    clicked_big_square)  # place the x or o, and switch over the team
                        # set the caption so players know who's turn it is.
                        pygame.display.set_caption(f"{team_turn}'s turn")

                        # check if a win has happened

                        if self.small_sqr_win_recognition(clicked_big_square,
                                                                                     self.naught_positions, "Naughts",
                                                                                     self.big_nought,
                                                                                     self.naught_sqrs_won):
                            game_over = True
                        if self.small_sqr_win_recognition(clicked_big_square,
                                                                                       self.cross_positions, "Cross",
                                                                                       self.big_cross,
                                                                                       self.cross_sqrs_won):
                            game_over = True

                        big_sqr_in_play = int(coord_position)  # find out in which position the square we just played was, and

                        if big_sqr_in_play not in self.big_sqrs_not_won:
                            self.available_big_squares = self.big_sqrs_not_won
                        else:
                            self.available_big_squares = [big_sqr_in_play]

                        self.place_sqr_in_play_bar(self.sqr_in_play_bar,
                                                   self.available_big_squares)  # show user where they can go
                    else:
                        continue
                else:
                    continue

            pygame.display.flip()
            pygame.display.update()

    def play_again_loop(self):
        self.screen.blit(self.game_over_screen, (0, 0))
        pygame.display.flip()
        pygame.display.update()

        # place rectangles in the same positions as the buttons in the image, without drawing them.
        play_again_rect = pygame.Rect(0, 230, 230, 110)
        exit_game_rect = pygame.Rect(315, 230, 235, 110)

        while True:
            # event check
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            mouse_click_detect = pygame.mouse.get_pressed(num_buttons=3)

            if mouse_click_detect[0]:
                mouse_pos = pygame.mouse.get_pos()  # get the position of the mouse

                if play_again_rect.collidepoint(mouse_pos) == 1:
                    return

                elif exit_game_rect.collidepoint(mouse_pos) == 1:
                    quit()
                time.sleep(0.1)  # prevent double-clicking


while True:
    game = SuperTicTacToe()
    game.game_run("Cross")
    game.play_again_loop()
