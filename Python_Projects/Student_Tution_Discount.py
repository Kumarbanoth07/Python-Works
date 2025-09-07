Name = input("Enter your name: ")
id = int(input("Enter your id: "))
S_fee = int(input("Enter your current fee: "))
Grade = int(input("Enter your Grade (6-12): "))
is_Topper = input("Enter your A Topper (yes/no) ")
if Grade in range(9,13) and is_Topper == "yes":

    saving = S_fee * 0.20

    
    final_fee = S_fee - saving
    
    print(f"Eligible for 20% discount. Final fee:{final_fee}")
    print(f"your savings after 20% Discount:{saving}")
elif Grade in range(9,13) and is_Topper == "no":
    saving = S_fee * 0.10 
    final_fee = S_fee - saving
    print(f"Your eligible for 10% discount:{final_fee}")
    print(f"your savings after 10% Discount:{saving}")

elif Grade in range(6,9) and is_Topper == "yes" or "no":
    saving = S_fee * 0.05
    final_fee = S_fee - saving
    print(f"Your eligible for 5% discount:{final_fee}")  
    print(f"your savings after 5% Discount:{saving}")  
else:
    print("your not eligible")    

