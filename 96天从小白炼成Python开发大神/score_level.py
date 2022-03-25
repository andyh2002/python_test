def score_level(score):
    if score >= 90:
        return 'A'
    elif 80 <= score <90:
        return 'B'
    elif 70 <= score <80:
        return 'C'
    elif 60 <= score <70:
        return 'D'
    else:
        return 'E'

n = int(input("请输入学生分数："))    
level = score_level(n)
print(level)
