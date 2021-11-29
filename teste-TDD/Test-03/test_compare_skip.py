"""
source: https://www.tutorialspoint.com/pytest/pytest_quick_guide.htm
"""

import pytest

@pytest.mark.xfail
@pytest.mark.great
def test_greater() -> None:
   num: int = 100
   assert num >= 100

@pytest.mark.xfail
@pytest.mark.great
def test_greater_equal() -> None:
   num: int = 100
   assert num >= 100

@pytest.mark.skip
@pytest.mark.others
def test_less() -> None:
   num: int = 100
   assert num < 200
