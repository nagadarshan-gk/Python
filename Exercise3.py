number_of_km = 10_000
number_of_days = input("Enter the kilomenters per day:")

perdaykm = (int)(number_of_km)/(int)(number_of_days)

years = (int)(perdaykm / 365)
months = (int)((perdaykm - years * 365) / 30)
days = (int)(perdaykm - years * 365 - months * 30)

# Output
print(years, " Year, ", months, " Months, and ", days, " Days")
