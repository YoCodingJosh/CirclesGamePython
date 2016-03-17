# HighScore.py - New high score. Woo hoo!! :D
# Created by Josh Kennedy on 30 June 2014
#
# Pop a Dots
# Copyright 2014 Chad Jensen and Josh Kennedy
# Copyright 2015-2016 Sirkles LLC

import os

# Algorithm:
# output = ((userScore * 6 / 2) + 100) * 7
#
# userScore is the score that the user got. (0, Infinity]
# 6 is the non-prime multiplier constant, preferably even.
# 2 is the LCM of the non-prime multiplier constant.
# 100 is a constant, can be any value.
# 7 is the prime multiplier constant, must not be 2 (especially if the non-prime multiplier constant is even).

# It would be fun to implement a simple RSA public key encrypter.

class HighScore():
    def setScore(self, gameplay, score):
        gameplayMode = gameplay
        directory = os.path.dirname(os.path.realpath(__file__)) + "/Scores/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = directory + gameplay + ".shsf" # Sirkles High Score File = SHSF
        file = open(filename, "w")
        newScore = hex(int(((score * 6 / 2) + 100) * 7))
        file.write(str(newScore))
        file.write('\n')
        file.close()

    def getScore(self, gameplay):
        gameplayMode = gameplay
        directory = os.path.dirname(os.path.realpath(__file__)) + "/Scores/"
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = directory + gameplay + ".shsf"

        try:
            file = open(filename, "r")
            scoreString = file.readline()
            file.close()
        except FileNotFoundError:
            # If there isn't a score file, then there isn't a score.
            return 0
        except io.UnsupportedOperation:
            # The file is empty or something else... :\
            file.close()
            return 0

        if (scoreString is None or scoreString is ''):
            return 0
        else:
            try:
                return int(((int(scoreString, 0) / 7) - 100) * 2 / 6)
            except ValueError:
                # The contents of the file can not be parsed to an integral value.
                return 0
