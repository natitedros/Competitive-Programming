def gradingStudents(grades):
    # Write your code here
    newGrades = []
    for grade in grades:
        if grade < 38:
            newGrades.append(grade)
        else :
            num = grade//5
            nextMulOf5 = num+1
            nextMul = nextMulOf5*5
            if nextMul-grade < 3:
                newGrades.append(nextMul)
            else:
                newGrades.append(grade)
    return newGrades
