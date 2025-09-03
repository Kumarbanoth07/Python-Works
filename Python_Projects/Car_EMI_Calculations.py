#Car EMI Details
Actual_Car_Value = 1700000
Annual_Interest = 10
Tenure_EMI_Months = 36

#Convert Interest Rate To Monthly
Monthly_Interest_Rate = (Annual_Interest / 12) / 100

#EMI Calculations 
emi = (Actual_Car_Value * Monthly_Interest_Rate * (1 + Monthly_Interest_Rate) ** Tenure_EMI_Months) / \
((1 + Monthly_Interest_Rate) ** Tenure_EMI_Months - 1)

#Total Payment
Total_Payment = emi * Tenure_EMI_Months

#Total interest
Total_Interest = Total_Payment - Actual_Car_Value

#Output

print("=====Car EMI Details=====")
print(f"Loan Amount (Actual Car Value): ₹{Actual_Car_Value}")
print(f"Annual Interest Rate (%): {Annual_Interest}")
print(f"Loan Tensure (Months): {Tenure_EMI_Months}")
print(f"Monthly EMI: ₹{emi:.2f}")
print(f"Total Paymet: ₹{Total_Payment:.2f}")
print(f"Total Interest: ₹{Total_Interest:.2f}")