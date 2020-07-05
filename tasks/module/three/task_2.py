import re
import pytest

NO_SPLITTER_ERROR_MESSAGE = "Splitter is not provided"


def my_split(string_to_split, splitter=None, max_split=-1):
    if splitter == "":
        raise ValueError(NO_SPLITTER_ERROR_MESSAGE)

    split_result = []

    if splitter is None:
        splitter = ' '
        string_to_split = re.sub('[ \t\n]+', ' ', string_to_split)

    while len(string_to_split) >= len(splitter) and max_split != 0:
        splitter_position = string_to_split.find(splitter)
        if splitter_position == -1:
            split_result.append(string_to_split)
            string_to_split = ''
        else:
            split_result.append(string_to_split[0:splitter_position])
            string_to_split = string_to_split[splitter_position + len(splitter):]
            max_split -= 1
    if len(string_to_split) > 0:
        split_result.append(string_to_split)
    return split_result


@pytest.mark.parametrize("text_to_split,splitter",
                         [('abd acd', ' ')])
def test_my_split(text_to_split, splitter):
    assert my_split(text_to_split, splitter) == text_to_split.split(splitter)


@pytest.mark.parametrize("text_to_split,splitter,expected_result",
                         [('a,b', ',', ['a', 'b']),
                          ('a1b', '1', ['a', 'b']),
                          (',a', ',', ['', 'a']),
                          ('AaAaAaA', 'a', ['A', 'A', 'A', 'A']),
                          ('abcd', 'e', ['abcd']),
                          ('aaaa', 'a', ['', '', '', '']),
                          ('a b c d', ' ', ['a', 'b', 'c', 'd']),
                          ('%*^*&', '*', ['%', '^', '&']),
                          ('ab ba', ' ', ['ab', 'ba'])])
def test_my_split_with_defined_splitter(text_to_split, splitter, expected_result):
    assert my_split(text_to_split, splitter) == expected_result


@pytest.mark.parametrize("text_to_split,max_split,expected_result",
                         [('a b c', 2, ['a', 'b', 'c']),
                          ('a b c', 1, ['a', 'b c']),
                          ('a b c', 0, ['a b c']),
                          ('a b c', 4, ['a', 'b', 'c'])])
def test_my_split_with_defined_count(text_to_split, max_split, expected_result):
    assert my_split(text_to_split, max_split=max_split) == expected_result


@pytest.mark.parametrize("text_to_split,expected_result",
                         [("a b c", ['a', 'b', 'c'])])
def test_my_split_not_provided_splitter(text_to_split, expected_result):
    assert my_split(text_to_split) == expected_result


@pytest.mark.parametrize("text_to_split,splitter",
                         [('abcd', '')])
def test_my_split_empty_splitter(text_to_split, splitter):
    with pytest.raises(ValueError, match=NO_SPLITTER_ERROR_MESSAGE):
        my_split(text_to_split, splitter)
