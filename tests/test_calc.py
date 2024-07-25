import hypot.source as source
import pytest

def test_even():
    input1, input2 = 3,4
    expected_output = 5.0
    output = source.hypot(input1, input2)
    assert output == expected_output
    
def test_2():
    input1, input2 = 5,12
    expected_output = 13.0
    output = source.hypot(input1, input2)
    assert output == expected_output
    