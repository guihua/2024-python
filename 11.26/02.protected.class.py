from protcted_student import Student

bart = Student('Bart Simpson', 'male', 59)
print('bart.get_name() =', bart.get_name())
bart.set_score(60)
print('bart.get_score() =', bart.get_score())

print('DO NOT use bart._Student__name:', bart._Student__name)

if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')

    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')