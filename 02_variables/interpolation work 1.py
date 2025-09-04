# --car specifications 

engine_type ="mHawk (CRDi)"
displacement = "2198 cc"
max_power = "172.45bhp@3500 rpm"
max_torque = "400 Nm @ 1750-2750 rpm"
cylinders = 4
valves_per_cylinder = 4
turbo_charger = True
transmission = "Automatic"
gearbox = "6-Speed"
driver_type = "4WD"

# car specifications using f-strings

print(f" ---- Car  Specifications -----")
print(f"Engine Type         :   {engine_type} ")
print(f"Displacement        :   {displacement}   ")
print(f"Max Power           :   {max_power}") 
print(f"Max Torque          :   {max_torque}")
print(f"No. of Cylinders    :   {cylinders}")
print(f"Valves per Cylinder :  {valves_per_cylinder}")
print(f"Turbo Charger       :   {'Yes' if turbo_charger else 'No'}")
print(f"Transmission Type   :   {transmission}")
print(f"Gearbox             :   {gearbox}")
print(f"Drive Type          :   {driver_type}")


#Product Info
brand = "HIGHLANDER"
product_name ="Men white Slim Fit Printed Casual Shirt"
rating = 4.2
ratings_count ="8.5k Ratings"
mrp = "Rs.1399"
discount_percent = "67% OFF"
selling_price = "Rs. 461"

# Displaying product details using f-string

print(f"----Product Details----")


print(f"Brand        :{brand}")
print(f"Product Name :{product_name}")
print(f"Rating       :{rating}")
print(f"Rating Count :{ratings_count}")
print(f"MRP          :{mrp}")
print(f"Discount     :{discount_percent} ")
print(f"Selling Price:{selling_price}")


#EMI Calculator


car_name = "Mahindra Scorpio S"
car_price =  1723757
annual_interest = 8.50
monthly_interest = annual_interest /12 /100 #percentage 
down_payment = 200000
loan_amount = car_price - down_payment
loan_period = 36.0 #months
emi_monthly = (loan_amount * monthly_interest*(1+ monthly_interest)**loan_period) / ((1+ monthly_interest)**loan_period -1)
payable_amount = emi_monthly * loan_period

# calculating EMI

print(f"------CAR EMI------")
print(f"Car Name  : {car_name}")
print(f"Car price  : Rs.{car_price}")
print(f"Loan Amount : Rs.{loan_amount}")
print(f"EMI per Month : Rs.{emi_monthly}")
print(f"Payable Amount  : Rs.{payable_amount}")
      



