"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте класс-структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
class QueueClass:
    def __init__(self):
        self.base = []
        self.not_done = []
        self.done = []

    def base_is_empty(self):
        return self.elems == []

    def to_base_queue(self, item):
        self.base.insert(0, item)

    # перемещаем из базовой очереди в очередь на доработку
    def from_base_queue_to_not_done(self):
        el = self.base.pop()
        self.to_not_done_queue(el)

    # перемещаем из базовой очереди в очередь решенных
    def from_base_queue_to_done(self):
        el = self.base.pop()
        self.to_done_queue(el)

    def size_base(self):
        return len(self.base)

    def show_base(self):
        print(self.base)

    def not_done_is_empty(self):
        return self.not_done == []

    def to_not_done_queue(self, item):
        self.not_done.insert(0, item)

    # перемещаем из базовой очереди в очередь решенных
    def from_not_done_queue_to_done(self):
        el = self.not_done.pop()
        self.to_done_queue(el)

    def size_not_done(self):
        return len(self.not_done)

    def show_not_done(self):
        print(self.not_done)

    def done_is_empty(self):
        return self.not_done == []

    def to_done_queue(self, item):
        self.done.insert(0, item)

    def from_done_queue(self):
        return self.not_done.pop()

    def size_done(self):
        return len(self.not_done)

    def show_done(self):
        print(self.done)

if __name__ == '__main__':
    qc_obj = QueueClass()

    # помещаем объекты в очереди
    qc_obj.to_base_queue('First task')
    qc_obj.to_base_queue('Second task')
    qc_obj.to_base_queue('Third task')
    qc_obj.to_base_queue('Fourth task')

    qc_obj.show_base()

    # перемещаем объект из первой очереди в нерешенные
    qc_obj.from_base_queue_to_not_done()
    qc_obj.show_base()
    qc_obj.show_not_done()

    # перемещаем объект из первой очереди в решенные
    qc_obj.from_base_queue_to_done()
    qc_obj.show_base()
    qc_obj.show_done()

    # перемещаем объект из очереди нерешенных в очередь решенных
    qc_obj.from_not_done_queue_to_done()
    qc_obj.show_not_done()
    qc_obj.show_done()