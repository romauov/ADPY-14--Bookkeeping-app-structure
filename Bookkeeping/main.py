from Bookkeeping.application.salary import calculate_salary
from Bookkeeping.application.db.people import get_employees
from datetime import datetime

current_date = datetime.date(datetime.today())

def its_some_oclock():
    print(f'it\'s {current_date} already')

if __name__ == '__main__':
    its_some_oclock()
    get_employees()
    calculate_salary()




