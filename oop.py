class Employee:

  raise_amount = 1.04
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'

  def full_name(self):
    return '{} {}'.format(self.first, self.last)

  def apply_raise(self):
    self.pay = int(self.pay * self.raise_amount)

emp_1 = Employee('Taylor', 'Buckner', 69000)
emp_2 = Employee('Anna', 'Buckner', 69000)


print(emp_1.full_name())
print(Employee.full_name(emp_1))
print(emp_2.full_name())

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print(emp_1.__dict__)
