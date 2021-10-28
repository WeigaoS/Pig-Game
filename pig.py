#!/usr/bin/env python3
'''module for Pig game'''

__author__ = 'Weigao Sun'
__email__ = 'swg9527666@csu.fullerton.edu'
__maintainer__ = 'WeigaoSun'



import random
import time


class Player:
    '''class for player including computer player'''

    def __init__(self, name='Computer', iscomputer=True):
        self.pname = name
        self.iscomputer = iscomputer  # am i a computer player
        self.totalscore = 0  # total score
        self.turnscore = 0  # current turn score
        self.rolltime = 0  # how many times the player has rolled
        self.order = -1    # the order of playing
        self.dieval = -1  # the value of latest die roll

    # do one roll
    def roll(self):
        ''' simulate player roll the die'''
        print(self.pname+', roll the die....')

        self.dieval = random.randint(1, 6)
        time.sleep(1)
        print('%s rolled %d' % (self.pname, self.dieval))

    # print some info
    def info(self):
        ''' print player info before each rolling '''
        print('%s, total score: %d, current turn score: %d, rolled times: %d'
              % (self.pname, self.totalscore, self.turnscore, self.rolltime))

    # ask the user if he wants to hold
    def hold(self):
        ''' check if the user want to hold '''
        # computer will choose to hold randomly
        if self.iscomputer:
            choice = random.randint(0, 1)
            if choice == 1:   # computer choose to hold in 1/2
                print('computer choose to hold')
                return True

            return False

        # for human user
        while True:
            choice = input('do you want to hold ?(Y,N): ').strip()
            if choice in ('Y', 'N'):
                return choice == 'Y'

            print('invalid input, try again...')

    # do the play, return True if win
    def play(self):
        ''' simulate a turn of a user play '''
        while True:
            self.info()
            self.roll()
            self.rolltime += 1
            if self.dieval == 1:  # roll get 1, turn score cleared
                self.turnscore = 0
                print('%s total score by now: %d\n' %
                      (self.pname, self.totalscore))
                return False

            self.turnscore += self.dieval

            if self.hold():
                self.totalscore += self.turnscore
                print('%s total score by now: %d\n' %
                      (self.pname, self.totalscore))
                self.turnscore = 0
                return self.totalscore > 99

# check if want to play with comptuer


def play_with_compter():
    ''' check if the user want to play with computer '''
    while True:
        choice = input('do you want to play with computer ?(Y,N): ').strip()
        if choice in ('Y', 'N'):
            return choice == 'Y'

        print('invalid input, try again...')


def get_player_number():
    ''' get number of human players in the game '''
    ret = -1
    while ret == -1:
        choice = input('how many human players ?(2,3,4): ').strip()
        if choice == '2':
            ret = 2
        elif choice == '3':
            ret = 3
        elif choice == '4':
            ret = 4
        else:
            print('invalid input, try again...')

    return ret


def main():
    ''' the main function of the program '''
    random.seed()
    print('Hello - welcome to my dice game!')
    players = []  # save player in a list
    if play_with_compter():
        players.append(Player("Player1", False))
        players.append(Player())
    else:
        num = get_player_number()
        for i in range(num):
            players.append(Player("Player"+str(i+1), False))

    num = len(players)
    print('Let us decide the order first: ')
    for player in players:
        player.roll()

    # sort player by roll number
    players = sorted(players, key=lambda x: x.dieval)

    print("\n!!Game Start!!\n")
    finish = False
    while not finish:
        for player in players:
            if player.play():
                finish = True
                print('%s win!!' % player.pname)
                break


if __name__ == '__main__':
    main()
