student_name = input("Enter Your name: ")
student_id = int(input("Enter Your id: "))
student_class = int(input("Enter your class(1-12): "))
current_fee = int(input("Enter Your current_fee: "))
Grade = input("Enter Your Grade (A/a): ")
if student_class in range(9,13) and Grade == "A" or "a":
    Discount = current_fee * 0.20
    Final_fee = current_fee - Discount
    print(f"Your elgible For 20% Discount:{Final_fee}")
    print(f"Your Savings:{Discount}")
    
else:
    print("Not Eligible For Discount")    

if student_class in range(10,13):
    extra_Discount = Final_fee * 0.05
    final_fee = Final_fee - extra_Discount
    print(f"Your eligible for extra 5% Discount:{final_fee}")
    print(f"Your Savings after 5% discount:{extra_Discount}")
else:
    print("Not eligible for 5%")    