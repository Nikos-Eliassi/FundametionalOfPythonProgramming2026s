calendar = [[0 for hour in range(24)] for day in range(7)]

print(calendar)
# Mark Monday at 10:00 as booked
calendar[0][10] = 1

print(calendar[0][10]) # 1 (booked)
   
