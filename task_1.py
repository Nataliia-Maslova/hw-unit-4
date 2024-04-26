from datetime import datetime


date = input("Write the date in the format: YYYY-MM-DD >>> ")

def get_days_from_today(date):
    date_object = datetime.strptime(date, "%Y-%m-%d")
    
    current_date = datetime.now()
    
    days_since = current_date.toordinal() - date_object.toordinal()

    return days_since
try:
    res = get_days_from_today(date)
    print(f"Кількість днів від заданої дати до поточно = {res}.")
except ValueError:
    print("Wrong format of the date. Print YYYY-MM-DD (for example: 2020-12-14)")
 