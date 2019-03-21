class Employee:

    number_of_employees = 0
    raise_amount = .04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # Using Employee. instead of self. to overwrite for all instances
        Employee.number_of_employees += 1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self._get_raise_amount())

    def _get_raise_amount(self):
        return self.raise_amount + 1

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


class Developer(Employee):
    raise_amount = .10

    def __init__(self, first, last, pay, programming_language):
        super().__init__(first, last, pay)
        self.programming_language = programming_language

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def remove_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def print_employees(self):
        for employee in self.employees:
                print('-->', employee.full_name())


# CREATE INSTANCES
dev_1 = Developer('Taylor', 'Buckner', 69000, 'Python')
dev_2 = Developer('Anna', 'Buckner', 69000, 'Javascript')
man_1 = Manager('Joe', 'Schmo', 100000, [dev_1, dev_2])

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print(dev_2.__dict__)
man_1.print_employees()

print(isinstance(man_1, Developer)) # False
print(isinstance(man_1, Employee)) # True
print(isinstance(man_1, Manager)) # True
print(issubclass(Manager, Developer)) # False
print(issubclass(Manager, Employee)) # True

