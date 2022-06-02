import random
import requests

from basic_word import BasicWord


def load_random_word(url: str):
    """
    Returns an object of the BasicWord class based on a random word from the list loaded from the URL

    :param url: source URL
    :return: object of the BasicWord class
    """
    request = requests.get(url)
    if request.status_code == 200:
        try:
            words_list = request.json()
        except ValueError:
            return None
        else:
            rand_word = random.choice(words_list)
            return BasicWord(rand_word["word"], rand_word["subwords"])
    else:
        raise ConnectionError


def get_ending(number: int, kit: list) -> str:
    """Returns a correct ending for word

    :param number: number to match the word with
    :param kit: set of endings
    :return: correct ending from the set
    """
    if (not isinstance(number, int) or
            not isinstance(kit, list) or
            len(kit) != 3):
        return ""
    if 10 < number % 100 < 15:
        return kit[0]
    temp = number % 10
    if temp == 1:
        return kit[1]
    elif 1 < temp < 5:
        return kit[2]
    else:
        return kit[0]
