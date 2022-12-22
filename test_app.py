import pytest
from app import square

@pytest.fixture
def input_value():
	return 2

def test_square_gives_correct_value(input_value):
    subject = square(input_value)
    assert subject == 4
