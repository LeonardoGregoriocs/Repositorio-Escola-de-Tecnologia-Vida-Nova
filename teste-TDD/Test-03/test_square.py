"""
source: https://www.tutorialspoint.com/pytest/pytest_quick_guide.htm
"""

import pytest
import math

@pytest.mark.square
def test_sqrt() -> None:
   num: int = 25
   assert math.sqrt(num) == 5

@pytest.mark.square
def test_square() -> None:
   num: int = 7
   assert 7*7 == 49

@pytest.mark.others
def test_equality() -> None:
   assert 10 != 11
