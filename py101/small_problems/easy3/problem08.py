# Write a function that determines the mean (average) of the three
# scores passed to it, and returns the letter associated with that
# grade.

# Numerical score letter grade list:

# 90 <= score <= 100: 'A'
# 80 <= score < 90: 'B'
# 70 <= score < 80: 'C'
# 60 <= score < 70: 'D'
# 0 <= score < 60: 'F'

# Tested values are all between 0 and 100. There is no need to check
# for negative values or values greater than 100.

def get_grade(score1, score2, score3):
    score = (score1 + score2 + score3) / 3
    if score >= 90:
        return 'A'
    if score >= 80:
        return 'B'
    if score >= 70:
        return 'C'
    if score >= 60:
        return 'D'
    else:
        return 'F'

print(get_grade(95, 90, 93) == "A")      # True
print(get_grade(50, 50, 95) == "D")      # True
