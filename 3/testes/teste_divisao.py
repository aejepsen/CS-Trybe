import pytest

from divisao import divide

def test_divisao():
    with pytest.raises(ZeroDivisionError, match='division by zero'):
      divide(10, 0)
