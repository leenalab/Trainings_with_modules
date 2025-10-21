# Приклад:
"""
student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
mark_counts = {}
for mark in student_marks:
    if mark in mark_counts:
        mark_counts[mark] += 1
    else:
        mark_counts[mark] = 1

print(mark_counts)
"""
import collections

student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
mark_counts = collections.Counter(student_marks)
#print(mark_counts)


 # один з методів Counter - це most_common()

#print(mark_counts.most_common())
# print(mark_counts.most_common(1))
# print(mark_counts.most_common(2))
# print(mark_counts.most_common(3))

from collections import Counter

# Створення Counter з рядка
letter_count = Counter("To be or not to be, that is the question.")
print(letter_count)

sentence = ("To be or not to be, that is the question.")
words = sentence.split()
word_count = Counter(words)

# Виведення слова та його частоти
for word, count in word_count.items():
    print(f"{word}: {count}")