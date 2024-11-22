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

#test Channel_up method
def test_channel_up():
    TV = Television()

    #test increasing channel when TV's OFF
    TV. channel_up()
    assert str(TV) == "Power = False, Channel = 0, Volume = 0"

    #test increasing channel when TV's ON
    TV.power()  #to turn ON
    TV.channel_up()  #i ^ channel
    assert str(TV) == "Power = True, Channel = 1, Volume = 0"

    #test increasing channel past Max Value
    for _ in range (4):
        TV.channel_up()
    assert str(TV) == "Power = True, Channel = 0, Volume = 0"

#test channel_down method
def test_channel_down():
    TV = Television()

    #Test decreasing channel when TV's OFF
    TV. channel_down()
    assert str(TV) == "Power = False, Channel = 0, Volume = 0"

    #test decreasing channel when TV's off
    TV.power() 
    TV.channel_down() 
    assert str(TV) == "Power = True, Channel = 3, Volume = 0"  # Wraps around to MAX_CHANNEL (3)

    #test decreasing channel past the Minimum value (wraps around)
    TV.channel_down()
    assert str(TV) == "Power = True, Channel = 3, Volume = 0"
   







