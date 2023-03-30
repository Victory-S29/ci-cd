import pytest
from main import word_counter, find_top_words


@pytest.fixture
def words():
    return ['milk', 'banana', 'milk', 'fish', 'milk', 'banana', 'bread', 'milk', 'milk', 'bread']


def test_word_counter_fixture(words):
    expected_output = {'milk': 5, 'banana': 2, 'bread': 2, 'fish': 1}
    assert word_counter(words) == expected_output


@pytest.mark.parametrize("input_data, expected_output", [
    (["cat", "dog", "fish", "fish", "cat", "cat", "dog", "bird", "dog", "bird"],
     {"cat": 3, "dog": 3, "bird": 2, "fish": 2}),

    (["hello", "universe", "hello", "universe", "world",
      "world", "world", "hello", "hello", "moon"],
     {"world": 3, "hello": 4, "universe": 2, "moon": 1}),

    (["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"],
     {"one": 1, "two": 1, "three": 1, "four": 1, "five": 1, "six": 1, "seven": 1,
      "eight": 1, "nine": 1, "ten": 1})
])

def test_word_counter_parametrize(input_data, expected_output):
    assert word_counter(input_data) == expected_output


@pytest.fixture
def word_counts():
    return {"apple": 10, "banana": 5, "orange": 3, "pear": 2, "grape": 1}


def test_find_top_words(word_counts):
    expected_result = {"apple": 10, "banana": 5, "orange": 3, "pear": 2, "grape": 1}
    assert find_top_words(word_counts) == expected_result
