# 1)Given a string , write a python code to reverse the string using for loop and slice
# operator both ways?
# Input: city = "ETLQALabs"
# expected output: “sbaL AQ LTE”

city="ETLQALabs"
l=len(city)
for i in range(l):
    result=city[::-1]
    result1=result[0:4] + ' ' + result[4:6] + ' ' +  result[6:9]
print(result1)


# 2. Extract a substring form character "Q" and ends at "b"
# Input: city = "ETLQALabs"
# Expected O/P : QAlab

city="ETLQALabs"
result1=city[3:5]
result2=city[5:8].lower()
final=result1 + result2
print(final)

# 3. Write a python code to check if the given list contains duplicate elements and print yes
# or no as per input
# e.g.
# list1 =[1,2,3,4,3] => Yes
# list2 =[1,2,3,4] => No

def dup_check(list):
    if len(list)!=len(set(list)):
        print ("Yes")
    else:
        print ("No")

#Examples#
list1=[1,2,3,4,3]
list2=[1,2,3,4]
print(f"For list1 {list1} duplicate presence is:")
dup_check(list1)
print(f"For list2 {list2} duplicate presence is:")
dup_check(list2)

# 4. How would you use slicing to create a new list containing only the odd-indexed elements of a
# given list?
Input : list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Expected output : [1, 3, 5, 7, 9]
list=[0,1,2,3,4,5,6,7,8,9]
list2=list[1:10:2]
print(f"The new list is: {list2}")


# 5. How would you use slicing to create a new list containing only the even-indexed elements of a
# given list?
# Input : list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected output : [0, 2, 4, 6, 8]

list=[0,1,2,3,4,5,6,7,8,9]
even_List=list[0:10:2]
print(f"The new list containing only the even-indexed elements of the given list {list} is: {even_List}")
