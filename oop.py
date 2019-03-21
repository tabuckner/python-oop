class Employee:

  number_of_employees = 0
  raise_amount = .04

  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'

    Employee.number_of_employees += 1 # Using Employee. instead of self. to overwrite for all instances

  def full_name(self):
    return '{} {}'.format(self.first, self.last)

  def apply_raise(self):
    self.pay = int(self.pay * self._get_raise_amount())

  def _get_raise_amount(self):
    return self.raise_amount + 1

  @classmethod
  def set_raise_amount(cls, amount):
    cls.raise_amount = amount

# CREATE INSTANCES
emp_1 = Employee('Taylor', 'Buckner', 69000)
emp_2 = Employee('Anna', 'Buckner', 69000)


print(emp_1.full_name())
print(Employee.full_name(emp_1)) # Can pass instance to Class method.
print(emp_2.full_name())

Employee.set_raise_amount(.05)

print(emp_1.raise_amount)
print(emp_2.raise_amount)
