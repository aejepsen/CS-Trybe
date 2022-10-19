from codigo import is_odd, is_even

def test_is_odd():
    'Para um número ímpar a função deve retornar o valor True'
    assert is_odd(3) == True
    'Para um número par a função deve retornar o valor False'
    assert is_odd(4) == False

def test_is_even():
    'Para um número ímpar a função deve retornar o valor False'
    assert is_even(3) == False
    'Para um número par a função deve retornar o valor True'
    assert is_even(4) == True