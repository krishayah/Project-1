import pytest
from television import *

def test_innit():
    TV = Television()
    #test if TV initializes w/ correct default values
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"