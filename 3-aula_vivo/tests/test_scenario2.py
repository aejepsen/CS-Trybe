import pytest
import json
from src.scenario2 import retrieve_stock_from_json
from unittest.mock import mock_open, patch
from tests.test_scenario1 import stock


def test_when_extension_was_incorrect_raises_an_exception():
    with pytest.raises(ValueError, match="Formato inválido!"):
        retrieve_stock_from_json("qlqcoisa.eli")


def test_when_successful_it_must_return_stock_of_products(stock):
    with patch("builtins.open", mock_open(read_data=json.dumps(stock))):
        given = retrieve_stock_from_json("qlqrcoisa.json")
        assert given == stock