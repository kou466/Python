import time

birth = str(input("주민등록번호 년월일: "))
year = birth[0:2]
now = time.localtime()
year = int(year)
age = (now.tm_year - (year + 1900) + 1)
print("나이:", age)
