""" Tests for 'hammerai' package """
import pytest
from hammerai import hammerai

def test_hammer(capsys):
    """ Correct object argument prints """
    hammerai.hammer("nail")
    captured = capsys.readouterr()
    assert "nail" in captured.out
def test_hammer_exception():
    with pytest.raises(TypeError):
        hammerai.hammer(1)
        