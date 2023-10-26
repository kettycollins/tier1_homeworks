from collections import defaultdict
from datetime import datetime, timedelta


def get_birthdays_per_week(users):
    # словник для збереження імен користувачів
    birthday_week = defaultdict(list)

    # поточна дата
    today = datetime.today().date()

    # поточний рік
    current_year = today.year

    # перевірка дня народження
    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()

        # цей рік
        birthday_this_year = birthday.replace(year=current_year)

        # різниця
        delta_days = (birthday_this_year - today).days

        # коли дн
        if delta_days >= 0:
            # якщо субота або неділя --> переніс на понеділок
            birthday_date = today + timedelta(days=delta_days)
            if birthday_date.weekday() in [5, 6]:
                birthday_date = today + timedelta(days=delta_days + 2)
            birthday_week[birthday_date.strftime("%A")].append(name)
        else:
            # дн минув --> перенос на наступний рік
            delta_days = (
                birthday_this_year.replace(year=current_year + 1) - today
            ).days
            # якщо субота або неділя --> переніс на понеділок
            birthday_date = today + timedelta(days=delta_days)
            if birthday_date.weekday() in [5, 6]:
                birthday_date = today + timedelta(days=delta_days + 2)
            birthday_week[birthday_date.strftime("%A")].append(name)
    # результат
    for day, names in birthday_week.items():
        print(f"{day}: {', '.join(names)}")


# тестування
users = [
    {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Kim Kardashian", "birthday": datetime(1980, 10, 21)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 11, 30)},
]
get_birthdays_per_week(users)
