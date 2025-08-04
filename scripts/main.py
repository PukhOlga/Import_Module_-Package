from dirty_main import *

if __name__ == '__main__':
    get_employees()
    calculate_salary()
    print(datetime.date.today())
    pprint(search_in_json('lastName', 'sample4.json'))
