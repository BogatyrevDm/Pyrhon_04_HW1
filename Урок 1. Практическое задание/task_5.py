"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте собственный класс-структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""
class StackClass:
    def __init__(self, max_count):
        self.elems = []
        self.max_count = max_count

    def is_empty(self):
        return self.elems == []

    def push_in(self, el):
        """Предполагаем, что верхний элемент стека находится в конце списка"""
        if self.is_empty():
            self.elems.append([])
        last_pack = self.elems[len(self.elems)-1]

        elements_count = len(last_pack)
        for i in range(el):
            if elements_count == self.max_count:
                self.elems[len(self.elems) - 1] = last_pack
                self.elems.append([])
                last_pack = self.elems[len(self.elems) - 1]
                elements_count = 0
            last_pack.append(1)
            elements_count += 1

    def pop_out(self):
        last_pack = self.elems[len(self.elems) - 1]
        return last_pack.pop()

    def get_val(self):
        last_pack = self.elems[len(self.elems) - 1]
        return last_pack[len(last_pack) - 1]

    def print_stack(self):
        for i in self.elems:
            print(i)



if __name__ == '__main__':

    SC_OBJ = StackClass(10)

    print(SC_OBJ.is_empty())  # -> стек пустой

    # наполняем стек
    SC_OBJ.push_in(25)

    SC_OBJ.print_stack()
    # получаем значение первого элемента с вершины стека,
    # но не удаляем сам элемент из стека
    print(SC_OBJ.get_val())

    # выводим стек на экран
    SC_OBJ.print_stack()

    print(SC_OBJ.is_empty())  # -> стек уже непустой

    # убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())
    SC_OBJ.print_stack()

    # снова убираем элемент с вершины стека и возвращаем его значение
    print(SC_OBJ.pop_out())
    SC_OBJ.print_stack()

