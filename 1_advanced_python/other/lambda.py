students = [
    {'name': 'Mary', 'grade': 92},
    {'name': 'Bob', 'grade': 85},
    {'name': 'John', 'grade': 78}
]

print(sorted(students, key=lambda student: student['grade'], reverse=True))
words = ['cat', 'dog', 'elephant', 'mash']
print(max(words, key=lambda word: len(word)))

# print(list(map(lambda value: (value*9/5)+32, [25, 30, 0, 11, 44, 12])))

# nums = [15, 5, 11, 25, 6, 11, 2, 3, 4, 0, 16]
# bigger_filtered =
# print(bigger_filtered)
# squared =
# print(list(map(lambda value: pow(value, 2), list(filter(lambda value: value > 10, nums)))))