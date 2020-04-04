import re
s = input()
letter = re.findall('[a-z]',s)
times = re.findall('[0-9]+',s)
result = ''
for i in range(len(letter)):
    if int(times[i]) % 2 ==0:
        result += letter[i] * int(times[i])
    else:
        result += letter[i]+times[i]
print(result)