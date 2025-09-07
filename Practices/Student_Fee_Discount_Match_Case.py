s_name = input("Enter Your Name: ")
s_id = int(input("Enter Your ID: "))
s_Class = int(input("Enter Your Class: "))
s_current_fee = int(input("Enter Your Fee: "))
s_Grade = input("Enter Your Grade(A/B/C): ")

match s_Grade:
    case "a" | "A" | "b" | "B" if s_Class in range(5,10):
        Discount = s_current_fee * 0.10
        final_Fee = s_current_fee - Discount
        print(f"Your Eligible for 10% Discount:{final_Fee}")
        print(f"Your Saving :{Discount}")
    case _:
        print("Your Not Eligible")    