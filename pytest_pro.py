from light import F
import pytest

def test_F1():
    assert len(F(['a','b','c','d'],10)) == 10

def test_F2():
    assert 'a' in F(['a','b','c','d'],10)
