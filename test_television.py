import pytest
from television import *

def test_innit():
    TV = Television()
    #test if TV initializes w/ correctly (TV off, channel 0, volume 0)
    assert str(TV) == "Power = False, Channel = 0, Volume = 0"

def test_power_ON():
    TV = Television()

    TV.power() #test turning it on
    assert str(TV) == "Power = True, Channel = 0, Volume = 0"

    TV.power() #test turning it OFF
    assert str(TV) == "Power = False, Channel = 0, Volume = 0"

def test_mute():
    TV = Television()

    

