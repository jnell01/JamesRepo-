import twohundred
import random

def test_roll_():
    result = twohundred.roll_()
    assert result >= 1 and result <=6 

"""def test_show_results():
    assert computer_score == 120
    assert human_score == 80
    result = twohundred.show_results(computer_score, human_score)
    assert result == "Your score is",human_score,"and the computer's score is",computer_score,". \nYou have lost the Game")"""

"""def test_show_results2():
    assert computer_score == 80
    assert human_score == 100
    result = twohundred.show_results(computer_score, human_score)
    assert result == "Your score is",human_score,"and the computer's score is",computer_score,". \nYou have lost the Game")"""

def test_is_game_over():
    result = twohundred.is_game_over(100, 30)
    assert result == True         

def test_is_game_over():
    result = twohundred.is_game_over(50, 30)
    assert result == False  


