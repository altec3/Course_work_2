from players import Player
from utils import load_random_word, get_ending

DATA_SOURCE = "https://jsonkeeper.com/b/R9TU"
ENDS = {1: ["", "о", "а"]} # dictionary with sets of endings


if __name__ == "__main__":
    word = load_random_word(DATA_SOURCE)
    if word is None:
        raise ValueError("Data received error")
    player = Player(input('Введите имя игрока: '))

    print(f"Привет, {player.name}!")
    print(f"Составьте {word.counts_subwords()} слов из слова \"{word.root_word.upper()}\"")
    print(f"\nСлова должны быть не короче {len(min(word.subwords))} букв")
    print("Чтобы закончить игру, угадайте все слова или напишите \"stop\"\nПоехали, ваше первое слово?")

    for try_ in range(word.counts_subwords()):
        user_input = input(": ").lower()

        if user_input == "stop" or user_input == "стоп":
            break

        while player.is_used_word(user_input):
            print("Не жульничай) Это слово уже было!")
            user_input = input(": ").lower()

        if word.is_correct(user_input):
            print("Верно")
            player.set_used_word(user_input)
        else:
            print("Неверно")

    print("\nСлова закончились, игра завершена!")
    print(f"Вы угадали {player.get_words_count()} слов{get_ending(player.get_words_count(), ENDS[1])}!")
