#inputs from the user
student_name= input("Enter student's name: ")
discount_percentage= 0
is_topper = str(input("Is the student an Academic topper(yes/no):"))
grade_level = int(input("Enter stduent's Grade level(1-12):"))
base_tuition_fee = float(input(" Enter Base Tuition Fee: "))
student_gpa = float(input("Enter student GPA:"))

if 55000<= base_tuition_fee <=65000:
    print("High grade level(9-12)")
    if 9<= grade_level <=12:
      if is_topper == 'yes':
       discount_percentage = 20
       print(f" Total discount Percentage:{discount_percentage:.2f}%")
      else: 
       discount_percentage = 10
       print(f" Total discount Percentage:{discount_percentage:.2f}%")
if  45000<= base_tuition_fee <55000:
  print("Intermediate Grade level(6-8)") 
if 6<= grade_level <=8:
     discount_percentage =5 
     print(f" Total discount Percentage:{discount_percentage:.2f}%")
if base_tuition_fee <45000:
   print("Low Grade level(1-5)")
   if 1<= grade_level <6:
    discount_percentage = 0
    print("sorry You got no discount")
elif student_gpa<4:
  print("The Student is not the topper")

discount_amount_saved = base_tuition_fee * (discount_percentage/100)
final_fee = base_tuition_fee - discount_amount_saved

#output results
print(f" Student's Name:{student_name:}")
print(f" Grade Level:{grade_level}")
print(f"Academic Topper: {is_topper}")
print(f" Base Tuition Fee: ${base_tuition_fee}")

print(f"Discount Amount saved: ${discount_amount_saved}")
print(f"Final Tuition Fee after Discount: ${final_fee} ")





   


