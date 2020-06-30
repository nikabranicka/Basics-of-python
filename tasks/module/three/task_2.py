import pytest

NO_SPLITTER_ERROR_MESSAGE = "Splitter is not provided"


def my_split(string_to_split, splitter):
    return string_to_split.split(splitter)


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


@pytest.mark.parametrize("text_to_split,splitter",
                         [('abcd', '')])
def test_my_split_empty_splitter(text_to_split, splitter, ):
    with pytest.raises(ValueError) as actual_error_message:
        assert my_split(text_to_split, splitter)
    assert str(actual_error_message.value) == NO_SPLITTER_ERROR_MESSAGE
