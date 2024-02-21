from datetime import datetime, timedelta


def get_birthdays_per_week(users):

# Визначаємо поточну дату
  today = datetime.now().date()
# Визначаємо дату понеділка на поточному тижні
  monday = (today - timedelta(days=today.weekday()))

# Визначаємо дату понеділка на наступному тижні
  next_monday = monday + timedelta(weeks=1)

# Визначаємо дату останнього дня на наступному тижні
  end_of_next_week = next_monday + timedelta(days=7)

  #Аналіз дати народження
  birthday_dict = {}
  for user in users:  
        #Отримуємо дату народження
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
  # Перевіряємо, чи вже минув день народження цього року
        if birthday_this_year < today:
  # Якщо так, то розглядаємо дату на наступний рік
            birthday_this_year = birthday.replace(year=today.year+1)

    # Перевіряємо чи ця дата наступного тижня
        if next_monday <= birthday_this_year < end_of_next_week:
            weekday = birthday_this_year.strftime('%A')
            if weekday == "Saturday" or weekday == "Sunday":
                weekday = 'Monday'

            if weekday not in birthday_dict:
                birthday_dict[weekday] = []
            
            birthday_dict[weekday].append(user['name'])

  print(birthday_dict)


# Тестуємо
users = [
  {"name": "Bill Gates", "birthday": datetime(1955, 10, 28)},
  {"name": "Jill Valentine", "birthday": datetime(1979, 3, 2)},
  {"name": "Kim Kardashian", "birthday": datetime(1980, 2, 28)},
  {"name": "Jan Koum", "birthday": datetime(1976, 2, 27)},
]

get_birthdays_per_week(users)