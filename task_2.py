""" Два друга A и B постоянно играют в коллекционную карточную игру (ККИ),
поэтому у каждого игрока скопилась довольно большая коллекция карт.

Каждая карта в данной игре задаётся целым числом (одинаковые карты — одинаковыми числами, разные карты — разными).

Таким образом коллекцию можно представить как неупорядоченный набор целых чисел (с возможными повторениями).

После каждого изменения коллекций друзья вычисляют показатель разнообразия следующим образом:
• A и B выкладывают на стол все карты из своей коллекции в два раздельных ряда;
• Далее друзья итеративно делают следующее:
    1.	Если среди лежащих на столе карт игрока A есть такая же карта, как и среди лежащих карт игрока
        B — каждый игрок убирает данную карту со стола;
    2.	Если таковых совпадений нет — процесс заканчивается.
• Разнообразием коллекций друзья называют суммарное количество оставшихся карт на столе.

Обратите внимание:
друзья убирают карты только со стола, карты не удаляются из коллекций при вычислении разнообразия.
Даны начальные состояния коллекций игроков, а также Q изменений их коллекций.
После каждого изменения необходимо вычислить разнообразие коллекций друзей.

ФОРМАТ ВВОДА:
В первой строке через пробел заданы числа N, M, Q (1≤N, M, Q≤105) —
    количество карт в коллекциях игрока A и B и количество изменений соответственно.

Вторая строка содержит через пробел N целых чисел ai (1≤ai≤109) —
    карты в коллекции игрока A.

Третья строка содержит через пробел M целых чисел bj (1≤bj≤109) —
    карты в коллекции игрока B.

Далее на каждой из следующих Q строк описано изменение коллекции:
через пробел заданы typek playerk cardk (typek=±1; playerk∈(A,B); 1≤cardk≤109) —
    тип k-го изменения, имя игрока и значение карты:
• Если type=1, то в коллекцию игрока player добавился экземпляр карты card;
• Если type=−1, то из коллекции игрока player удалился один экземпляр карты card.
• Гарантируется, что при запросе type=−1 хотя бы один экземпляр карты card присутствует в коллекции игрока player.

ФОРМАТ ВЫВОДА:
Необходимо вывести через пробел Q целых чисел — разнообразие коллекций игроков A и B после k-го изменения.
"""

from collections import defaultdict


def player_cards(iterable: map) -> defaultdict:
    cards = defaultdict(int)
    for card in iterable:
        cards[card] += 1
    return cards

def indicator_diversity(player1: defaultdict, player2: defaultdict) -> int:
    uniq_cards = set(player1)
    uniq_cards.update(set(player2))
    cards = []
    for card in uniq_cards:
        count = abs(player1.get(card, 0) - player2.get(card, 0))
        if count > 0:
            cards.append(count)
    return len(cards)

def play_kki(player1: defaultdict, player2: defaultdict, changes: tuple) -> list:
    result = []
    for i in changes:
        chang, igrok, card = int(i[0]), i[1], int(i[2])
        if igrok == "A":
            if chang == 1:
                player1[card] += 1
            else:
                player1[card] -= 1
        else:
            if chang == 1:
                player2[card] += 1
            else:
                player2[card] -= 1
        result.append(indicator_diversity(player1, player2))
    return result


if __name__ == '__main__':
    
    # lst = tuple(map(int, input().split()))
    # player1 = player_cards(map(int, input().split()))
    # player2 = player_cards(map(int, input().split()))
    # changes = tuple(input().split() for _ in range(lst[2]))
    # print(*play_kki(player1, player2, changes))

    lst = 2, 5, 10
    player1 = player_cards(map(int, '1 2'.split()))
    player2 = player_cards(map(int, '1 2 3 4 5'.split()))
    changes = tuple(i.split() for i in ('1 A 3', '1 A 4', '1 A 5', '1 A 6', '1 A 7', '-1 A 1', '1 B 7', '-1 A 6', '-1 B 1', '1 A 7'))
    assert play_kki(player1, player2, changes) == [2, 1, 0, 1, 2, 3, 2, 1, 0, 1]

    lst = 3, 3, 5
    player1 = player_cards(map(int, '1000 2000 1001'.split()))
    player2 = player_cards(map(int, '1001 2001 1000'.split()))
    changes = tuple(i.split() for i in ('1 A 100000', '-1 B 2001', '1 B 2000', '1 B 100001', '1 A 1'))
    assert play_kki(player1, player2, changes) == [3, 2, 1, 2, 3]
    lst = 2, 5, 10
    player1 = player_cards(map(int, '1 2'.split()))
    player2 = player_cards(map(int, '1 2 3 4 5'.split()))
    changes = tuple(i.split() for i in ('1 A 3', '1 A 4', '1 A 5', '1 A 6', '1 A 7', '-1 A 1', '1 B 7', '-1 A 6', '-1 B 1', '1 A 7'))
    assert play_kki(player1, player2, changes) == [2, 1, 0, 1, 2, 3, 2, 1, 0, 1]

    lst = 3, 3, 20
    player1 = player_cards(map(int, '1 6 7'.split()))
    player2 = player_cards(map(int, '2 4 5'.split()))
    changes = tuple(i.split() for i in ('1 A 2', '1 B 1', '1 B 8', '1 B 5', '1 A 3',
                                        '1 A 2', '1 B 10', '1 A 9', '1 A 8', '1 B 7',
                                        '-1 A 1', '-1 B 5', '-1 B 5', '-1 B 4', '-1 A 6',
                                        '-1 A 8', '-1 A 2', '-1 B 8', '-1 B 10', '-1 A 2'))
    assert play_kki(player1, player2, changes) == [5, 4, 5, 5, 6, 7, 8, 9, 8, 7, 8, 8, 7, 6, 5, 6, 5, 4, 3, 4]

    print("Test OK")
