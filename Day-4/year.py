def days_to_years_months_days(number_of_days):
  years = number_of_days // 365
  remaining_days = number_of_days % 365
  months = remaining_days // 30
  days = remaining_days % 30
  print("Years: ", years)
  print("Months: ", months)
  print("Days: ", days)


days_to_years_months_days(100)
