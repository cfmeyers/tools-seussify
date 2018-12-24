import re
from random import seed, choice
from sys import stdin, stdout

from silly_words_collected import silly_words
from sql_reserved_words_collected import reserved_words


def get_all_words(text):
    return [w.lower() for w in re.findall(r'\w+', text, flags=re.M)]


def exclude_numbers(words):
    return [w for w in words if not re.findall(r'^\d+$', w)]


def get_words_to_replace(text):
    all_words = exclude_numbers(get_all_words(text))
    excluded_words = set([w.lower() for w in reserved_words])
    words_to_replace = []
    for word in all_words:
        if word.lower() not in excluded_words:
            words_to_replace.append(word)

    return words_to_replace


def seussify(text: str, random_seed: int = None) -> str:
    if random_seed is not None:
        seed(random_seed)
    words_to_replace = get_words_to_replace(text)
    seussified_text = text
    for word_to_replace in words_to_replace:
        replacement = choice(silly_words)
        case_insensitive_replacer = re.compile(word_to_replace, re.IGNORECASE)
        seussified_text = case_insensitive_replacer.sub(replacement, seussified_text)
    return seussified_text


if __name__ == '__main__':
    text = stdin.read()
    seussified_text = seussify(text)
    stdout.write(seussified_text)
