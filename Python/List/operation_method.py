#1. Slicing in list

# fruits = ['apple', 'banana', 'cherry', 'elderberry', 'fig','grape']
# print(fruits[1:4])

#2. ommitting indices
# print(fruits[:4])
# print(fruits[4:])
# print(fruits[:])

#2. negative indices
# print(fruits[:-2])


#3. step argument(start, stop,step)
# print(fruits[:])
# print(fruits[::])
# print(fruits[::2])

fruits = ['apple', 'banana', 'jerry', 'elderberry', 'fig','grape','banana']

#4.changing items
fruits[2] = 'mango'
# print(fruits)

# changing multiple items items
fruits[1:3] = ['kiwi', 'lemon']
# 

words = ["A", "B", "C", "F", "Y", "a","b","c","d",]

#5. sort() {they use ASCII table}(they directly sort the original list)
# ascending order(default)
words.sort()
# print(words)

# descending order
words.sort(reverse=True)
# print(words)

#4. sorted() (create a copy of the original list)
sorted_words = sorted(words)
# print(words)


#5. reverse() (change the original list)
fruits.reverse()
# print(fruits)

# couting the occurence of an item
# print(fruits.count('banana'))

# finding the index of an item

# print(fruits.index('fig'))


xyz = ["1", "2", "8","4","5","6","7","8","9","1","1","12"]

#adding the numbers
sum_of_numbers = sum(map(int, xyz))
# print(sum_of_numbers)

#printig the numbers of lowest value
# print(min(map(int, xyz)))

# printing the numbers of highest value
# print(max(map(int, xyz)))
ff


# printing the length of the list
# print(len(xyz))

# removing the last item
xyz.pop()
# print(xyz)