from typing import List


class Phone:
    number: str = '123'
    _counter: int = 0

    def new_number(self) -> None:
        self.number = str(input('Please enter number: '))

    def _call_accept(self) -> None:
        self._counter += 1

    def call(self, inp) -> None:
        if inp == 'y':
            self._call_accept()

    def get_counter(self) -> int:
        return self._counter


def tot_call(phones: List[Phone]) -> int:
    return sum(phone.get_counter() for phone in phones)


p1 = Phone()
p2 = Phone()
p3 = Phone()
p1.new_number()
p2.new_number()
p3.new_number()
p1.call('n')
p1.call('y')
p2.call('y')
p2.call('n')
p2.call('y')
p3.call('n')
p3.call('y')
l = [p1, p2, p3]
print('Total calls: ', tot_call(l))
