# a='welcome1234'
import re
# print(re.sub('w','W',a))
# print(re.sub('welcom','python',a))
# print(re.split('e',a))
# print((re.findall('e',a)))
# print(re.search('wel',a))
# print(re.search('["1-5"]',a))
# print(re.search('[a-e]',a))
# if re.search('[a-z]',a):
#     print('yes')
# else:
#     print('no')
a='ABcd'
print(re.search('a',a))
print(re.search('a.',a))
print(re.search('a.*',a))
print(re.search('a.+',a))
print(re.search('c.?',a))
print(re.search('[a-z]',a))
print(re.search('[A-C]..',a))