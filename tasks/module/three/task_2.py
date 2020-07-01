import pytest

NO_SPLITTER_ERROR_MESSAGE = "Splitter is not provided"


def my_split(string_to_split, splitter=' '):
    if splitter == "":
        raise ValueError(NO_SPLITTER_ERROR_MESSAGE)

    split_result = []
    text = ''
    for character in string_to_split:
        if character == splitter:
            split_result.append(text)
            text = ''
        else:
            text = text + character
    if not text == '':
        split_result.append(text)
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
def test_my_split_basic_split(text_to_split, splitter, expected_result):
    assert my_split(text_to_split, splitter) == expected_result


@pytest.mark.parametrize("text_to_split,expected_result",
                         [("a b c", ['a', 'b', 'c'])])
def test_my_split_not_provided_splitter(text_to_split, expected_result):
    assert my_split(text_to_split) == expected_result


@pytest.mark.parametrize("text_to_split,splitter",
                         [('abcd', '')])
def test_my_split_empty_splitter(text_to_split, splitter):
    with pytest.raises(ValueError, match=NO_SPLITTER_ERROR_MESSAGE):
        my_split(text_to_split, splitter)
