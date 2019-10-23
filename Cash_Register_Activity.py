#Austin Salvesen
#9/19
#Cash register activity
#Declare and intialize variables
num_items= 100
cost_per_item= 3.99
tax_rate= 0.09

#Calculate and store the sub-total
sub_total= num_items *cost_per_item


#Calculate the amount of tax and store as a result
tax_amount = sub_total * tax_rate

#Calculate the total price and store the amount
total_price= sub_total + tax_amount

#show the full receipt to the screen
sep1 =  ": "
sep2 = ": $"

print("------Reciept------")
print("Number of items                          : "+str(num_items))
print("Cost  per item                             : $"+str(cost_per_item))
print("Tsx rate                                        : "+str(tax_rate))
print("Tax amount                                 : $"+str(tax_amount))
print("TOTAL SALE PRICE : $"+str(total_price))
