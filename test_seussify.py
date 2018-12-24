from seussify import seussify, get_words_to_replace, get_all_words


def test_seussify():
    text = """\
SELECT
hello
, world
FROM greetings
"""
    expected_text = """\
SELECT
beezlenut
, jibboo
FROM klunk
"""
    assert expected_text == seussify(text=text, random_seed=1)


def test_seussify_excludes_numbers():
    text = """\
SELECT
hello
, world1
FROM greetings
GROUP BY 1,2, 3
"""
    expected_text = """\
SELECT
beezlenut
, jibboo
FROM klunk
GROUP BY 1,2, 3
"""
    assert expected_text == seussify(text=text, random_seed=1)


def test_get_words_to_replace():
    text = """\
SELECT
hello AS hello
, world
FROM my.greetings
"""
    expected = ['hello', 'hello', 'world', 'my', 'greetings']
    assert expected == get_words_to_replace(text=text)


def test_get_all_words():
    text = """\
SELECT
hello AS hello
, world
FROM my.greetings
"""
    expected = ['select', 'hello', 'as', 'hello', 'world', 'from', 'my', 'greetings']
    assert expected == get_all_words(text=text)
    assert [] == get_all_words(text='')
