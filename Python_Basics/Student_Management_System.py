student_name = 'kumar'
student_age = 26
student_id = 7013
#scores
quiz_score = 80
assignment_score = 75
exam_score = 90
#attendence
student_Attendece = 60
#lets start with caluclation part
total_score = quiz_score + assignment_score + exam_score
#avarege score
avg_score = total_score/3
#student passing 
student_passed = avg_score > 75
#Increment attendence 
student_Attendece += 1
#awaard eligibility
award_eligibility = student_Attendece >= 90 and student_passed

#Now print the output

print("=====STUDENT REPORT=====")
print(f"Student Name: {student_name}")
print(f"Student Age:{student_age}")
print(f"Student ID:{student_id}")
print(f"Student Total Score:{total_score}")
print(f"Student Avg Score:{avg_score}")
print(f"Student Current Attendence:{student_Attendece}")
print(f"Student Award Eligibility:{award_eligibility}")