""" Определим близость двух целочисленных массивов как длину их наибольшего совпадающего префикса (см. примечание).

Примеры:
•	Близость [1, 2, 1, 3] и [1, 2, 3, 2] равна 2 — префикс [1, 2] совпадает;
•	Близость [1, 2, 3] и [3, 2, 1] равна 0.

Дано n целочисленных массивов a1,a2,…,an.
Необходимо вычислить сумму близостей массивов ai и aj для каждой пары 1≤i<j≤n.

ФОРМАТ ВВОДА:
Первая строка содержит одно целое число n(1≤n≤3⋅105)  — количество массивов.
Каждый массив задаётся двумя строками.
Первая строка описания массива содержит единственное целое число ki (1≤k≤3⋅105)  — размер i-го массива.
Вторая строка описания содержит ki целых чисел aij (1≤aij≤109) — элементы i-го массива.
Гарантируется, что ∑ni=1ki≤3⋅105.

ФОРМАТ ВЫВОДА:
Выведите единственное целое число  — суммарную попарную близость массивов.
 """

def calculate(lst: list[list]) -> int:
    def prefix(a, b):
        min_length = min(len(a), len(b))
        len_prefix = 0
        for i in range(min_length):
            if a[i] != b[i]:
                break
            len_prefix += 1
        return len_prefix
    total = 0
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n):
            total += prefix(lst[i], lst[j])
    return total


if __name__ == '__main__':
    # lst = []
    # len_lst = []
    # for i in range(int(input())):
    #     len_lst.append(int(input()))
    #     lst.append(list(map(int, input().split())))
    # print(calculate(lst))

    lst = [[5],[1, 2],[5, 1, 2]]
    assert calculate(lst) == 1

    lst = [[1, 2],[1, 3],[1, 2, 3]]
    assert calculate(lst) == 4


    print('Test OK')
