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
    def __init__(self, id, lang):
        self.id = id
        self.lang = lang
        self.subordinate = []


def subordinate(hierarchy, lst_employee):
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



if __name__ == '__main__':
    n = int(input())                                 # 4
    language = list(map(str, input().split()))       # A B A A
    hierarchy = list(map(int, input().split()))      # 0 1 2 3 3 4 4 2 1 0
    lst_employee = [Employee(0, 'AB')]
    lst_employee.extend([Employee(i, language[i-1]) for i in range(1, n+1)])
    subordinate(hierarchy, lst_employee)
    for i in lst_employee:
        print(i.id, i.subordinate)
        # 0 [<__main__.Employee object at 0x0000021DF73DF450>]
        # 1 [<__main__.Employee object at 0x0000021DF73DF490>]
        # 2 [<__main__.Employee object at 0x0000021DF73DF4D0>, <__main__.Employee object at 0x0000021DF73DF510>]
        # 3 []
        # 4 []



"""
4
A B A A
0 1 2 3 3 4 4 2 1 0


0 1 1 1
"""
