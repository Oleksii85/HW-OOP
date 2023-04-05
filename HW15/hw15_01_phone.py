class Phone:
    number = 123
    _counter = 0

    def new_number(self):
        self.number = str(input('Please enter number: '))
        return self.number

    def _call_accept(self):
        self._counter += 1
        return self._counter

    def call(self, inp):
        if inp == 'y':
            self._call_accept()

    def get_counter(self):
        return self._counter


def tot_call(telnum):
    return sum(tel.get_counter() for tel in telnum)


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
print('Numbers: ', p1.number, p2.number, p3.number, 'calls accepted: ', p1._counter + p2._counter + p3._counter)
print('Total calls: ', tot_call(l))
