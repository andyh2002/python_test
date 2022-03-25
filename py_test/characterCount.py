import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print('区分大小写统计结果：', count)

countLower = {}
for character in message:
    countLower.setdefault(character.lower(), 0)
    countLower[character.lower()] = countLower[character.lower()] + 1

print('不区分大小写统计结果：', countLower)

# 美观输出格式
pprint.pprint(countLower)
