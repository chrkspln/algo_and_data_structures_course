#   Рівень 3
#   Варіант 1
#   Зоомагазин займається продажем хом’ячкiв. Це мирнi домашнi iстоти, проте,
#   як виявилося, вони мають цiкаву харчову поведiнку. Для того,
#   щоб прогодувати хом’ячка, який живе наодинцi, потрiбно H пакетiв корму на день.
#   Однак, якщо кiлька хом’ячкiв живуть разом, у них прокидається жадiбнiсть.
#   У такому випадку кожен хом’ячок з’їдає додатково G пакетiв корму в день
#   за кожного сусiда. Денна норма H та жадiбнiсть G є iндивiдуальними
#   для кожного хом’ячка. Всього в магазинi є C хом’ячкiв. Ви бажаєте придбати
#   якомога бiльше, проте у вас є всього S пакетiв їжi на день.
#   Визначте максимальну кiлькiсть хом’ячкiв, яку ви можете прогодувати.
#
#   Реалізуйте функцію, яка поверне число - максимальне число хом'ячків.
#   Вхідні параметри функції: S — ваш денний запас їжi. 0 ≤ S ≤ 109
#   C — загальна кiлькiсть хом’ячкiв, яка є в продажу, 1 ≤ C ≤ 105
#   Матриця hamsters, яка містить С рядків, перший стовчик якої містить
#   денну норму корму, другий - рiвень жадiбностi кожного хом’ячка.
#   Денні норми є цілими додатніми числами і гарантовано меншими за 109.
#   Іноді у вас можуть бути не жадібні хом’ячки, але також можуть
#   траплятись і надзвичайно жадібні, рівень жадібності може бути 
#   як нульовим, так і великим цілим числом.
#
#   Приклад 1
#   S = 7 C = 3 hamsters = `[ [1 2], [2 2], [3 1]]``
#   Результат: 2
#   Пояснення: Можна взяти першого хом’ячка та будь-якого з iнших двох.
#
#   Приклад 2
#   S = 19 C = 4 hamsters = `[ [5 0], [2 2], [1 4], [5 1]]
#   Результат: 3
#   Пояснення: Третiй хом’ячок надто жадiбний. Можна взяти всiх iнших трьох,
#   тодi за день вони з’їдять (5 + 0 · 2) + (2 + 2 · 2) + (5 + 1 · 2) = 18 пакетiв
#
#   Приклад 3
#   S = 2 C = 2 hamsters = `[[1 50000], [1 60000]]
#   Результат: 1 Пояснення: Обидва хом’ячки надто жадiбнi, щоб їсти разом.
#
#   Для перевірки виконання роботи реалізованого алгоритму
#   слід використати бібліотеку unittest та перевірити роботу вашої функції на прикладах, наведених вище

import unittest


def how_many_hamsters(hamsters_list, hamsters_quantity, daily_food):
    if not hamsters_list:
        return 0

    result = hamsters_search(hamsters_list, 0, hamsters_quantity - 1, daily_food, 0)
    return result


def hamsters_search(list, end, food_av, count, prev_count):
    start = 0
    mid = (start + end) // 2
    mid = count
    food_needed_list = []

    for for_one, greedy in list:
        food_needed_list.append(for_one + greedy * mid)
        
    food_needed_list = sorted(food_needed_list)
    required_food = sum(food_needed_list[:mid])

    if required_food > food_av:
        if prev_count == count:
            return count
        elif prev_count < count:
            hamsters_search(list[:mid], mid - 1, food_av, 0, prev_count)
            return count
    elif required_food < food_av and len(list) != 1:
        if prev_count > count:
            return count
        elif prev_count == count:
            count += 1
            hamsters_search(list[mid:], len(list) - 1, food_av, count, prev_count)
            return count
    else:
        return len(food_needed_list)


class Lab2Test(unittest.TestCase):
    # task tests
    def test_example1(self):
        S = 7
        C = 3
        hamsters = [
            [1, 2],
            [2, 2],
            [3, 1]
        ]
        self.assertEqual(how_many_hamsters(hamsters, C, S), 2, "error!")

    def test_example2(self):
        S = 19
        C = 4
        hamsters = [
            [5, 0],
            [2, 2],
            [1, 4],
            [5, 1]
        ]
        self.assertEqual(how_many_hamsters(hamsters, C, S), 3, "error!")

    def test_example3(self):
        S = 2
        C = 2
        hamsters = [
            [1, 50000],
            [1, 60000]
        ]
        expected_result = 1
        self.assertEqual(how_many_hamsters(hamsters, C, S), expected_result, "error!")

    # gpt tests
    def test_basic_case(self):
        hamsters_list = [(10, 5), (8, 4), (7, 3)]
        hamsters_quantity = 3
        daily_food = 30
        expected_result = 2
        self.assertEqual(how_many_hamsters(hamsters_list, hamsters_quantity, daily_food), expected_result)

    def test_no_hamsters_needed(self):
        hamsters_list = [(10, 5), (8, 4), (7, 3)]
        hamsters_quantity = 3
        daily_food = 5
        expected_result = 1
        self.assertEqual(how_many_hamsters(hamsters_list, hamsters_quantity, daily_food), expected_result)

    def test_empty_hamsters_list(self):
        hamsters_list = []
        hamsters_quantity = 5
        daily_food = 30
        expected_result = 0
        self.assertEqual(how_many_hamsters(hamsters_list, hamsters_quantity, daily_food), expected_result)

    def test_zero_daily_food(self):
        hamsters_list = [(10, 5), (8, 4), (7, 3)]
        hamsters_quantity = 3
        daily_food = 0
        expected_result = 0
        self.assertEqual(how_many_hamsters(hamsters_list, hamsters_quantity, daily_food), expected_result)

    # student tests
    def v_test(self):
        hamsters_list = [(17, 3), (8, 4), (7, 3)]
        hamsters_quantity = 3
        daily_food = 30
        expected_result = 2
        self.assertEqual(how_many_hamsters(hamsters_list, hamsters_quantity, daily_food), expected_result)

    def my_test(self):
        hamsters_list = [[4, 2], [2, 3], [1, 4], [6, 2], [1, 5]]
        hamsters_quantity = 5
        daily_food = 29
        expected_result = 2
        self.assertEqual(how_many_hamsters(hamsters_list, hamsters_quantity, daily_food), expected_result)

    def test_all_greedy_hamsters(self):
        S = 24
        C = 4
        hamsters = [[5, 2], [5, 3], [2, 1], [5, 5]]
        self.assertEqual(how_many_hamsters(hamsters, C, S), 3)

if __name__ == '__main__':
    unittest.main()
