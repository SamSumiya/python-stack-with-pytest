import pytest
from typing import List
from stack import Stack, match_symbols


@pytest.fixture(scope='session')
def items_list():
    return Stack()


def test_push(items_list: List[str]):
    items_list.my_push('Apple')
    items_list.my_push('bananas')
    items_list.my_push('Pineapple')
    assert items_list.length() > 0


def test_length(items_list):
    leng = items_list.length()
    length = len(items_list.show())
    assert leng == length


def test_pop(items_list):
    items_list.my_push('apple')
    items_list.my_pop()
    assert items_list.length() == 3


def test_shift(items_list):
    first_item = [items_list.show()[0]]
    shifted_item = items_list.my_shift()
    assert first_item == shifted_item
    assert items_list.length() == 2


def test_unshift(items_list):
    items_list.my_unshift('Mango')
    first_item = items_list.show()[0]
    assert first_item == 'Mango'


def test_peek(items_list):
    first_item = items_list.show()[-1]
    assert first_item == 'Pineapple'


def test_is_not_emptyor_not(items_list):
    items_list.my_pop()
    items_list.my_pop()
    items_list.my_pop()
    result = items_list.is_empty()
    assert result == True


def test_are_symbols_balanced_pass(items_list):
    for item in list('([{}])'):
        items_list.my_push(item)
    assert items_list.are_symbols_balanced() == True


def test_are_symbols_balanced_fail_not_even(items_list):
    for item in list('([{(}])'):
        items_list.my_push(item)
    assert items_list.are_symbols_balanced() == False


def test_are_symbols_balanced_fail(items_list):
    for item in list('([{(}}])'):
        items_list.my_push(item)
    assert items_list.are_symbols_balanced() == False


def test_match_symbols():
    result = match_symbols("[{()}]")
    assert result == True


def test_match_symbols():
    result = match_symbols("[{(}]")
    assert result == False


def test_match_symbols():
    result = match_symbols("[{(]}]")
    assert result == False