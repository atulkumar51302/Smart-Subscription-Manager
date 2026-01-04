#Dictionary comprehension
labour_with_cost = {"Mahesh:":500,"Ramesh:":400,"Om:":200,"Jagmohan":1000,"Rampyare":800}
labour_with_cost = {key:labour_with_cost.get(key)+100 for key in labour_with_cost}
print(labour_with_cost)
