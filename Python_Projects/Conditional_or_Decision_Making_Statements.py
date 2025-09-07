#runs the code if condition is true 
#syntax

#if condition:

age = 21
if age >= 18:
   print("you can vote")

#if and else condition

age = 17
if age >=18:
    print("you can vote")

else:
    print("you can not vote")        

#elif ladder condition

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("A")
elif marks >= 80:
    print("C")

elif marks >= 70:
    print("C")
elif marks >= 60:
    print("D")
else:
    print("Your Fail")        

#Match-Case (Alternative for elif ladder statement)

choice = int(input("Select any One from These Choice(1-5): "))
match choice:
    case 1:
        print("Java")
    case 2:
        print("python")    
    case 3:
        print("cloud")
    case 4:
        print("Devops") 
    case 5:
        print("aws") 

    case _:
        print("Selecct only valid option")
                      
#Now Comparision bw elif ladder and match case 
#elif ladder
age = int(input("Enter your age: "))
if age == 0 or age == 1 or age == 2 or age == 3 or age == 4 or age == 5:
    category = "Toddler"
elif age == 6 or age == 7 or age == 8 or age == 9 or age == 10:
    category = "child"    
elif age == 15 or age == 17 or age == 19:
    category = "Teenager"
elif age == 20 or age == 21 or age == 22:
    category = "Young" 
else:
    category = "Adults" 
print(category)          

#Now same thing do with the match case 

age = int(input("Enter your age: "))
match age:
    case 0 | 1 | 2 | 3 | 4 | 5:
        category = "Toddler"
    case 6 | 7 | 8 | 9 | 10 | 11 | 12:
        category = "Child"
    case 13 | 14 | 15 | 16 | 17 | 18 | 19:
        category = "Teenage" 
    case 20 | 21 | 22 | 23 | 24 | 25:
        category = "Young" 
    case _:
        category = "Adult" 

print(category)           