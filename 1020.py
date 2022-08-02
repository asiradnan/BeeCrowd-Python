days=int(input())
years=days//365
remain=days%365
months=remain//30
print(years,'ano(s)')
print(months,'mes(es)')
print(remain%30,'dia(s)')
