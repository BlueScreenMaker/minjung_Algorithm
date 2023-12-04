sum_score = 0
sum_grade = 0
for i in range(20) :
    subject, score, grade = input().split()
    if grade == "A+" :
        sum_grade += (float(score) * 4.5)
    elif grade == "A0" :
        sum_grade += (float(score) * 4.0)
    elif grade == "B+" :
        sum_grade += (float(score) * 3.5)
    elif grade == "B0" :
        sum_grade += (float(score) * 3.0)
    elif grade == "C+" :
        sum_grade += (float(score) * 2.5)
    elif grade == "C0" :
        sum_grade += (float(score) * 2.0)
    elif grade == "D+" :
        sum_grade += (float(score) * 1.5)
    elif grade == "D0" :
        sum_grade += (float(score) * 1.0)
    elif grade == "F" :
        sum_grade += (float(score) * 0.0)
    else :
        continue
    sum_score += float(score)

print(sum_grade/sum_score)