def run_nian(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


# 断言,测试用例
assert run_nian(2004) == True
assert run_nian(2005) == False
assert run_nian(2010) == False
assert run_nian(2100) == False

print(run_nian(2000))
