from abc import ABC, abstractmethod

class Employee(ABC):
  
  def __init__(self,employee_name,category):
    self.__employee_name = employee_name
    self.__category = category
  
  @abstractmethod
  def calculate_pay(self):
    pass

  def get_name(self):
    return self.__employee_name

  def get_category(self):
    return self.__category
   

class FulltimeEmployee(Employee):
  def __init__(self,employee_name,category,fixed_monthly_salary):
    super(). __init__(employee_name,category)
    if fixed_monthly_salary <= 0:
      raise ValueError("Salary must be greater than zero")
    self.__monthly_salary = fixed_monthly_salary
    
  def calculate_pay(self):
    print(f'Employee: {self.get_name()}')
    print(f'Category: {self.get_category()}')
    print(f'Monthly Payment: {self.__monthly_salary}')
    return self.__monthly_salary
    
    
class ContractEmployee(Employee):
  def __init__(self,employee_name,category,daily_rate,working_days):
    super(). __init__(employee_name,category)
    if daily_rate <= 0:
      raise ValueError("Daily rate must be greater than zero")
    self.__daily_rate = daily_rate
    
    if working_days <= 0:
      raise ValueError("Working days must be greater than zero")
    self.__working_days = working_days
    
  def calculate_pay(self):
    print(f'Employee: {self.get_name()}')
    print(f'Category: {self.get_category()}')
    print(f'Monthly Payment: {self.__daily_rate * self.__working_days}')
    return self.__daily_rate * self.__working_days

print("==== EMPLOYMENT PAYROLL ====")
print("")

profile1 = FulltimeEmployee("David","Fulltime",150000)
profile2 = ContractEmployee("John","Contract",5000,20)
profile3 = FulltimeEmployee("Grace","Fulltime",200000)
profile4 = ContractEmployee("Esther","Contract",8000,15)

profiles = [profile1,profile2,profile3,profile4]

total = 0
  

for profile in profiles:
  total += profile.calculate_pay()

print("")

print(f'Total Payroll: {total}')


