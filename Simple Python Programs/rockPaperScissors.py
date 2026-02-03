# Learn how to build rock paper scissor game with control flow

import random
import sys

while True: # main game looping
    print('ROCK, PAPER, SCISSOR GAME!!!')
    wins = 0
    losses = 0
    ties = 0

    while True: # player input looping
        print('%s Wins %s Losses %s Ties' % (wins, losses, ties))
        print('Enter your move : (r)ock, (p)aper, (s)cissor, or type (q) for Quit Game')
        player_input = input('> ')

        if player_input == 'q' :
            print('Thank you for playing, see you next time 👋')
            sys.exit()
        if player_input == 'r':
            print('ROCK! versus ...')
        elif player_input == 'p':
            print('PAPER! versus ...')
        elif player_input == 's':
            print('SCISSOR! versus ...')
        else :
            print('Please try again')
            break
        
            
        # computer randomly pick a number
        computer_input = int(random.randint(1, 3))
        if computer_input == 1:
            print('ROCK!')
        elif computer_input == 2:
            print('PAPER!')
        elif computer_input == 3:
            print('SCISSOR!')

        # give the result of the game
        # add score to the screboard
        game_result = player_input + str(computer_input)
        if game_result == 'r3' :
            print('YOU WON! 🎉 congratulations!')
            wins = wins + 1
        elif game_result == 'p1':
            print('YOU WON! 🎉 congratulations!')
            wins = wins + 1
        elif game_result == 's2':
            print('YOU WON! 🎉 congratulations!')
            wins = wins + 1
        elif game_result == 'r2':
            print('YOU LOSE HAHAHA! better luck next time 😬')
            losses = losses + 1
        elif game_result == 'p3':
            print('YOU LOSE HAHAHA! better luck next time 😬')
            losses = losses + 1
        elif game_result == 's1':
            print('YOU LOSE HAHAHA! better luck next time 😬')
            losses = losses + 1
        else:
            print('TIES!😌😌')
            ties = ties + 1

       


        
