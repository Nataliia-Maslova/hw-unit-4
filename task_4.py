from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.04.26"},
    {"name": "Jane Smith", "birthday": "1990.05.01"},
    {"name": "Jay Smith", "birthday": "1990.03.02"}
]
birthday_list = []

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    this_year = datetime.today().year
    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday_date.replace(year=this_year) 
        if birthday_this_year < today:
            birthday_this_year = birthday_date.replace(year=this_year+1)
        difference = birthday_this_year - today
        if difference <= timedelta(days=7):
            birthday_day_of_week = birthday_date.isoweekday()
            if birthday_day_of_week == 6:
                congratulation_day = birthday_this_year.replace(day=+2) 
            elif birthday_day_of_week == 7:
                congratulation_day = birthday_this_year.replace(day=+1)
            else:
                congratulation_day = birthday_this_year
        formatted_congratulation_day = congratulation_day.strftime("%A, %d %B %Y")
        name = user["name"]
        new_data = {name: formatted_congratulation_day}
        birthday_list.append(new_data)
        return birthday_list
    
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
