# 1. Write a function to return the grade based on percentage
def grade(marks_perc):
    if 90 <= marks_perc <= 100:
        return "A"
    elif 80 <= marks_perc <= 89:
        return "B"
    elif 70 <= marks_perc <= 79:
        return "C"
    elif 60 <= marks_perc <= 69:
        return "D"
    else:
        return "F"


marks_perc1 = 90
marks_perc2 = 70
marks_perc3 = 50

print(f"The grade for {marks_perc1} is: {grade(marks_perc1)}")
print(f"The grade for {marks_perc2} is: {grade(marks_perc2)}")
print(f"The grade for {marks_perc3} is: {grade(marks_perc3)}")
# print(grade(marks_perc2))
# grade(marks_perc3)

# 2. Write a function that return a list of common elements from two different sets
def common_elements(set1,set2):
    common=set1.intersection(set2)
    return list(common)

set_1={1,2,3,4,5}
set_2={4,5,6,7,8}

print(common_elements(set_1,set_2))

#another way to solve question2:
def common_elements(set1,set2):
    common=set1 & set2
    return common
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(common_elements(set1,set2))

#to get unique elements between two sets:
def Unique_elements(set1,set2):
    unique=set1 | set2
    return unique
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(Unique_elements(set1,set2))

#to get elements that are present in set1 and not in set2
def unique_elements_in_set1(set1, set2):
    unique = set1 - set2  # Subtraction to get elements in set1 but not in set2
    return unique

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(unique_elements_in_set1(set1, set2))  # Output: {1, 2, 3}


# 3. Convert a String to a List of Characters
str1 = "etlqalabs"
# output=['e','t','l','q','a','l','a','b','s']
list1 = []
for i in str1:
    list1.append(i)
print(list1)

# 4. Write a function to check if list contains any duplicate element and return True or False as
# applicable
def dup_check(lista):
    if len(lista)!=len(set(lista)):
        print ("True")
    else:
        print ("False")

list1=[1,2,3,2,1,4]
list2=[1,4,3,8,7]

dup_check(list1)
dup_check(list2)

# 5. Given a list, write a function that provide the occurrence of element against each element in
# the list.
# e.g. List = [1,2,3,4,5,1,3]
# Expected Output:
# 1: 2
# 2:1
# 3: 2
# 4: 1
# 5: 1
def occurences(input_list):
    occurences={}
    for element in input_list:
        if element in occurences:
            occurences[element]+=1
        else:
            occurences[element]=1
    for element,count in occurences.items():
        print(f"{element}: {count}")

list1=[1,2,3,4,5,1,3]
occurences(list1)


# 6. Write a function return a substring where it starts from 2rd occurrence of ‘a’ and end at
# occurrent of ‘b’
# e.g. s = "abracadabra"
# start_char = 'a'
# end_char = 'b'
# Expected output: acadab
def substring(s):
    start_index = s.find('a', s.find('a') + 1)
    end_index = s.rfind('b')

    if start_index != -1 and end_index != -1 and start_index < end_index:
        return s[start_index:end_index + 1]  # include end character
    else:
        return ""


s = 'abracadabra'
print(substring(s))



