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

    #Test Muting TV when it's on, after increasing volume
    TV.power() #turn TV ON
    TV.volume_up()  #increases Volume by 1
    TV.mute()  #Mutes the TV
    assert str(TV) == "Power = True, Channel = 0, Volume = 0"  # Volume should be 0 when muted

    #test unmuting the TV
    TV.mute()  #Unmutes
    assert str(TV) == "Power = True, Channel = 0, Volume = 1"

    #test muting when TV's OFF
    TV.mute()
    assert str(TV) == "Power = False, Channel = 0, Volume = 0"  #WHen TV's off, VOlume = 0



