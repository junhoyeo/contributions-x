from get_contributions import get_contributions
from datetime import datetime

def get_average_of_contributions(contributions):
  total = 0
  for contribution in contributions:
    total += contribution['count']
  return total / len(contributions)

def get_contributions_until_today(contributions):
  today = datetime.today().strftime('%Y-%m-%d')
  contributions_until_today = []
  for contribution in contributions:
    if contribution['date'] <= today:
      contributions_until_today.append(contribution)
  return contributions_until_today

def get_total_contributions(contributions):
  total = 0
  for contribution in contributions:
    total += contribution['count']
  return total

def get_accumulated_total_contributions_for_this_year(contributions_until_today):
  number_of_days_passed = len(contributions_until_today)
  number_of_contributions_until_today = get_total_contributions(contributions_until_today)
  return 365 * number_of_contributions_until_today / number_of_days_passed

this_year = datetime.today().year

years = [2017, 2018, 2019, 2020, 2021, 2022]
average_of_years = []
total_of_years = []

for year in years:
  contributions = get_contributions('junhoyeo', year)
  if year == this_year:
    contributions_until_today = get_contributions_until_today(contributions)
    average = get_average_of_contributions(contributions_until_today)
    average_of_years.append(average)

    accumulated_contributions_for_this_year = get_accumulated_total_contributions_for_this_year(contributions_until_today)
    total_of_years.append(accumulated_contributions_for_this_year)
  else:
    average = get_average_of_contributions(contributions)
    average_of_years.append(average)

    total_contributions = get_total_contributions(contributions)
    total_of_years.append(total_contributions)

print(average_of_years)
print(total_of_years)

def format(value):
  return '{:2f}'.format(value).rstrip('0').rstrip('.')

prev_count = 1
prev_average = 1
for index, count in enumerate(total_of_years):
  average = average_of_years[index]

  print(
    count,
    f'x{format(count / prev_count)}',
    '/',
    format(average),
    f'x{format(average / prev_average)}',
  )

  prev_count = count
  prev_average = average
