import numpy as np


def median(min_value, max_value):
    return (max_value + min_value) // 2


def game(number):
    min_value = 1
    max_value = 100
    predict = median(min_value, max_value)
    count = 1

    while number != predict:
        count += 1

        if number > predict:
            min_value = predict
        elif number < predict:
            max_value = predict

        predict = median(min_value, max_value)
    return count


def get_score():
    count_list = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=100)

    for number in random_array:
        count_list.append(game(number))

    score = int(np.mean(count_list))

    return score


print(f"Ваш алгоритм угадывает число в среднем за {get_score()} попыток")
