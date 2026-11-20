salary=int(input("enter yout salary: "))
if(salary<20000):
    bonus=salary * 5/100
elif(salary<40000 && salary>20000):
    bonus=salary * 10/100
else:
     bonus=salary * 15/100
    annual_salary=salary+bonus
print("your salary is= ",annual_salary)
