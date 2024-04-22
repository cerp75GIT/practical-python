# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
total_paid = 0.0
nMonth = 1
payment=0

while principal > 0 :
    if nMonth <=12 :
        payment = 2684.11 + 1000 
    else:
        payment = 2684.11

    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    nMonth+=1

print('Total paid', total_paid)
print('Months ', nMonth-1)
