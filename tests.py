#DO NOT TAMPER WITH THIS FILE
#ANY EDITS YOU MAKE TO THIS FILE WILL BE SAVED TO YOUR PUBLIC GITHUB HISTORY
#TAMPERING WITH THIS FILE WILL BE OBVIOUS AND WILL RESULT IN A ZERO

import main;


def test_code1():
    assert main.times10(4) == 40, "error"
    assert main.times10(67) == 670, "error"

def test_code2():
    assert main.firstA("ant") == True, "error"
    assert main.firstA("salsa") == False, "error"

def test_code3():
    assert main.sizer(4) == "small", "error"
    assert main.sizer(67) == "medium", "error"
    assert main.sizer(999) == "large", "error"

def test_code4():
    assert main.doubleWord("brake") == "brakebrake", "error"
    assert main.doubleWord("hot") == "hothot", "error"

def test_code5():
    assert main.penguin("king") == "increasing", "error"
    assert main.penguin("macaroni") == "vulnerable", "error"
    assert main.penguin("royal") == "near threatened", "error"
    assert main.penguin("african") == "endangered", "error"





