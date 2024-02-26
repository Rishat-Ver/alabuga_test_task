"""
Межпланетная организация имеет иерархическую древовидную структуру:
•	Корнем иерархии является генеральный директор;
•	У каждого сотрудника 0 или более непосредственных подчиненных;
•	Каждый сотрудник, кроме генерального директора, является непосредственным подчиненным ровно одному сотруднику.
Каждый сотрудник, кроме генерального директора, говорит либо на языке A, либо на языке B.
Директор говорит на двух языках для управления всей организацией.
Структура всей организации хранится в текстовом документе.
Каждый сотрудник представлен уникальным идентификатором - целым числом от 0 до N включительно,
где 0 - идентификатор генерального директора.
Каждый сотрудник представлен в документе ровно два раза.
Между первым и вторым вхождением идентификатора сотрудника в аналогичном формате представлены все его подчиненные.
Если у сотрудника нет подчиненных, то два его идентификатора расположены один за другим.

Например, если
•	генеральный директор имеет в прямом подчинении сотрудника 1;
•	сотрудник 1 имеет в прямом подчинении сотрудника 2;
•	сотрудник 2 имеет в прямом подчинении сотрудников 3 и 4;
то документ будет представлен в виде строки:
0123344210
Если при этом сотрудники 1, 3, 4 говорят на языке A, а сотрудник 2 говорит на языке B, то вся организация выглядит так:
"""

class Employee:
    def __init__(self, id: int, lang: str) -> None:
        self.id = id
        self.lang = lang
        self.subordinate = []
        self.employee = []


def subordinates(hierarchy: list[int], lst_employee: list[Employee]) -> None:
    stack = []
    for i in range(len(hierarchy)):
        sub_employee = [employee for employee in lst_employee if employee.id == hierarchy[i]][0]
        if not stack:
            stack.append(sub_employee)
        else:
            if stack[-1].id != hierarchy[i]:
                stack[-1].subordinate.append(sub_employee)
                stack.append(sub_employee)
            else:
                stack.pop()

def employees(lst_employee: list[Employee]) -> None:
    for employee in lst_employee:
        current = employee
        while True:
            flag = False
            for x in lst_employee:
                if current in [sub_emp for sub_emp in x.subordinate]:
                    employee.employee.append(x)
                    current = x
                    flag = True
                    break
            if not flag or current == 0:
                break

def func(n: int, lst_employee: list[Employee]) -> list:
    result = []
    for i in range(1, n+1):
        emp = [e for e in lst_employee if e.id == i][0]
        barrier = 0
        flag = False
        for i in emp.employee:
            manager = [e for e in lst_employee if e.id == i.id][0]
            if emp.lang == manager.lang or 'AB' in manager.lang:
                flag = True
                break
            else:
                barrier += 1
        result.append(barrier if flag else 0)
    return result


if __name__ == '__main__':

    # n = int(input())
    # language = list(map(str, input().split()))
    # hierarchy = list(map(int, input().split()))
    # lst_employee = [Employee(0, 'AB')]
    # lst_employee.extend([Employee(i, language[i-1]) for i in range(1, n+1)])
    # subordinates(hierarchy, lst_employee)
    # employees(lst_employee)
    # print(*func(n, lst_employee))


    n = 4
    language = ['A', 'B', 'A', 'A']
    hierarchy = [0, 1, 2, 3, 3, 4, 4, 2, 1, 0]
    lst_employee = [Employee(0, 'AB')]
    lst_employee.extend([Employee(i, language[i-1]) for i in range(1, n+1)])
    subordinates(hierarchy, lst_employee)
    employees(lst_employee)
    assert func(n, lst_employee) == [0, 1, 1, 1]

    n = 5
    language = ['A', 'B', 'B', 'A', 'B']
    hierarchy = [0, 1, 1, 2, 3, 4, 4, 5, 5, 3, 2, 0]
    lst_employee = [Employee(0, 'AB')]
    lst_employee.extend([Employee(i, language[i-1]) for i in range(1, n+1)])
    subordinates(hierarchy, lst_employee)
    employees(lst_employee)
    assert func(n, lst_employee) == [0, 0, 0, 2, 0]

    print('Test OK')
