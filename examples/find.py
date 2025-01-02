import thotpy as th

th.call.here()

file = 'sample.txt'
key = 'key'
key_regex = r'key\s*\d*'
number_of_matches = 0
additional_lines = 2
split_additional_lines = False
regex = False

if regex:
    keyword = key_regex
else:
    keyword = key

matches = th.find.lines(keyword, file, number_of_matches, additional_lines, split_additional_lines, regex)
print(matches)
for match in matches:
    print(match)

test_1 = th.find.lines('line', file, 3, 1, True, False)
print(test_1)  # ['line 1', 'line 2', 'line 2', 'line 3', 'line 3', 'line 4']

test_2 = th.find.lines('line', file, -3, 0, True, False)
print(test_2)  # ['line 18', 'line 19', 'line 20']

test_3 = th.find.lines('line', file, -3, 1, True, False)
print(test_3)  # ['line 18', 'line 19', 'line 19', 'line 20', 'line 20']

test_4 = th.find.lines('line', file, -2, -1, True, False)
print(test_4)  # ['line 18', 'line 19', 'line 19', 'line 20']

test_5 = th.find.lines('line', file, -2, 1, True, False)
print(test_5)  # ['line 19', 'line 20', 'line 20']

