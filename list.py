[16:32, 1/17/2022] sandy krish😎: MERAKI QUESTIONS@
numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
a=0
i=0
while i<len(numbers):
	if numbers[i]>a:
		a=numbers[i]
	i+=1
print(a)
O/p:70
Maximum numbers
[17:00, 1/17/2022] sandy krish😎: a='my name is laxmi'
count=0
c1=0
i=0
while i<len(a):
		if a[i]==' ':
			count+=1
		else:
			c1+=1
		i+=1
print('total space:',count)
print('total chtr:',c1)
O/p:total space:3
         total chtr:14
[17:01, 1/17/2022] sandy krish😎: Number of spaces
Total chtr
[12:07, 1/18/2022] sandy krish😎: numbers =[50,40,23,70,56,12,5,10,7]
count=0
while numbers[count:]:
	count+=1
print(count)
O/p:9
Without using Len()print how many elements
[15:49, 1/18/2022] sandy krish😎: numbers=[50,40,23,70,56,12,5,10,7]
count=0
i=0
while i<len(numbers):
	if 20<=numbers[i]<=40:
		count+=1
	i+=1
print(count)
    numbers between 20 and 40
[15:53, 1/18/2022] sandy krish😎: numbers=[50,40,23,70,56,12,5,10,7]
count=0
while numbers[count:]:
	count+=1
print(count)
O/p:9
How many elements in a list
[16:18, 1/18/2022] sandy krish😎: places=["delhi","gujarat","rajasthan","punjab","kerala"]
i=0
while i<len(places):
	places.reverse( )
	print(places[i])
	i+=1
	reverses the order of the items
[16:22, 1/18/2022] sandy krish😎: *
Check whether the list is palindrome or not? 
name=[ 'n', 'i', 't', 'i', 'n' ]
rev=name[: :-1]
i=0
while i<len(name):
		if name==rev:
			i+=1
			print("Haan! palindrome hai")
			break
		else:
			print("nahi ! palindrome nahi hai")
		Output:-Haan! palindrome hai

[Program finished]
[16:34, 1/19/2022] sandy krish😎: numbers=[50,40,23,70,56,12,5,10,7]
i=0
a=0
while i<len(numbers):
	if numbers[i]>a:
		a=numbers[i]
	i+=1
j=0
max2=0
while j<len(numbers):
	if numbers[j]<a:
		if numbers[j]>max2:
			max2=numbers[j]
	j+=1
print("second max numbers",max2)
print(max2)
Second maximum element
[16:45, 1/19/2022] sandy krish😎: list1=[1,2,3,4,5,6]
list2=[2,3,1,0,6,7]
list3=[ ]
i=0
while i<len(list1):
	if i not in list2:
		list3.append(i)
	i+=1
print(list3)
   which number are not present in second array
[09:24, 1/20/2022] sandy krish😎: marks=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,52,49]]
sum=sum(marks[0]+marks[1]+marks[2])
print(sum)
Sum of students total marks
[10:11, 1/21/2022] sandy krish😎: marks=[[78,76,94,86,88],[91,71,98,65,76],[95,45,78,53,49]]
i=0
avg=0
while i<len(marks):
	j=0
	while j<len(marks):
		avg0=sum(marks[0])/len (marks[0])
		avg1=sum(marks[1])/len (marks[1])
		avg2=sum(marks[2])/len (marks[2])
		j+=1
	i+=1
print(avg0)
print(avg1)
print(avg2)
Average marks of each year
[11:39, 1/21/2022] sandy krish😎: n = [10, 11, 12, 13, 14, 17, 18, 19]
i=0
list1=[]
while i<len(n):
	list2=[]
	j=i
	while j<len(n):
		if n[i]+n[j]==30:
			list2.append(n[j])
			list2.append(n[i])
			list1.append(list2)
		j+=1
	i+=1
print(list1)
All pairs in an array of integers whose sum is equal
[12:07, 1/21/2022] sandy krish😎: elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
a=[ ]
b=[ ]
while i<len(elements): 
    if elements[i]%2==0:
        a.append(elements[i])
    else:
        b.append(elements[i])
    i+=1
print("even=",a)
print("odd=",b)
    
    odd and even
[12:49, 1/21/2022] sandy krish😎: elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
sum1=0
while i<len(elements):
	if elements[i]%2==0:
		sum=sum+(elements[i])
	else:
		sum1=sum1+(elements[i])
	i+=1
print("sum of even=",sum,"sum of odd=",sum1)
Sum of even and odd
[13:21, 1/21/2022] sandy krish😎: elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
avg=0
avg1=0
while i<len(elements):
	if elements[i]%2==0:
		avg=avg+(elements[i])/len(elements)
	else:
		avg1=avg1+(elements[i])/len(elements)
	i+=1
print("avg of even=",avg,"avg of odd=",avg1)
Average of even and odd
[11:02, 1/25/2022] sandy krish😎: elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
c=0
c1=0
sum=0
sum1=0
while i<len(elements):
	if elements[i]%2==0:
		sum=sum+elements[i]
		c=c+1
	else:
		sum1=sum1+elements[i]
		c1=c1+1
	i+=1
aver1=sum//c
aver2=sum1//c1
	
print("avg of even=",aver1)
print("avg of odd=",aver2)

avg of even and odd
[13:17, 1/25/2022] sandy krish😎: char = ["a", "n", "t", "a", "a", "t", "n", "n", "a", "x", "u", "g", "a", "x", "a"]
i=0
m=[]
while i<len(char):
    count=0
    n=[]
    j=0
    while j<len(char):
        if char[i]==char[j]:
            count=count+1
        j=j+1
    n.append(char[i])
    n.append(count)
    if n not in m:
        m.append(n)
    i=i+1
print(m)
How many characters and words are there
[13:18, 1/25/2022] sandy krish😎: * 
Even numbers
Odd numbers
Sum of even numbers
Sum of odd numbers
Average of even numbers
Average of odd numbers
Length of the list
Count of even numbers
Count of odd numbers? 

elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
even=[ ]
odd=[ ]
sum=0
sum1=0
count=0
count1=0
avg=0
avg1=0
while i<len(elements):
	if elements[i]%2==0:
		even.append(elements[i])
		sum=sum+(elements[i])
		avg=avg+(elements[i])/len(elements)
		count+=1
	else:
		odd.append(elements[i])
		sum1=sum1+(elements[i])
		avg1=avg+(elements[i])/len(elements)
		count1+=1
		
	i+=1
print("sum of even num=",sum)
print("sum of odd num=",sum1)
print("sum of all num=",sum+sum1)
print("average of even num=",avg)
print("average of odd num=",odd)
print("avg of all num=",avg+avg1)
print("even…
[15:11, 1/25/2022] sandy krish😎: list=[19,17,12,17,17,18,10,17,14,12,19,17,12,13,11]
i=0
a=[ ]
while i<len(list):
	if list[i]not in a:
		a.append(list[i])
	i+=1
print(a)
Duplicate question
[15:48, 1/27/2022] sandy krish😎: grocery_list=["flour","cheese","carrots"]
print(grocery_list[0])
print(grocery_list[1])
print(grocery_list[2])
Print the list flour
                        Cheese
                         Carrots
[15:48, 1/27/2022] sandy krish😎: Doc questions
[16:31, 1/27/2022] sandy krish😎: list=[['g','f','g'],['i','s'],['b','e','s','t']]
list1=['g','f','g']
list2=['i','s']
list3=['b','e','s','t']
list4=list1+list2+list3
i=0
while i<len(list4):
	print(list4[i],end="")
	i+=1
2.add the characters
[09:48, 1/28/2022] sandy krish😎: a=[6,1,3,5,6,3,1]
i=0
b=[ ]
while i<len(a):
	h=a[i]
	if h not in b:
		b.append(h)
	i+=1
print(b)
i=0
product=1
while i<len(b):
	product=product*b[i]
	i+=1
print(product)
3.product the duplicate numbers
[10:01, 1/28/2022] sandy krish😎: list=[1,2,2,5,8,4,4,8]
f=[ ]
i=0
while i<len(list):
	if list[i]not in f:
		f.append (list[i])
	i+=1
print(f)
5.count unique values
[10:23, 1/28/2022] sandy krish😎: a=[9,1,1,9]
i=0
s=' '
while i<len(a):
	s=s+(str(a[i]**2))
	i+=1
print(s)
Print given square
[10:25, 1/28/2022] sandy krish😎: a=[9,1,1,9]
i=0
s=' '
while i<len(a):
	s=s+(str(a[i]**2))
	i+=1
print(s)
Print square of 9118
[10:29, 1/28/2022] sandy krish😎: a=[9,1,1,9]
i=0
s=[ ]
while i<len(a):
	s.append(a[i]**2)
	i+=1
print(s)
11.Single number square
[10:58, 1/28/2022] sandy krish😎: num=[50,40,23,70,56,12,5,7,10]
max=0
i=0
while i<len(num):
	if num[i]>max:
		max=num[i]
	i+=1
max1=0
j=0
while j<len(num):
	if num[j]>max1:
		if num[j]!=max:
			max1=num[j]
	j+=1
max2=0
k=0
while k<len(num):
	if num[k]>max2:
		if num[k]!=max and num[k]!=max1:
			max2=num[k]
	k+=1
print(max)
print(max1)
print(max2)
9.first,second,third maximum
[15:51, 1/28/2022] sandy krish😎: a=[1,2,3,4,5,6,7,8,9,10]
l=len(a)
b=[ ]
i=0
for i in range(l):
	diff=1+a[i]-a[i]
	b.append(diff)
print(b)
16.find the difference
[15:59, 1/28/2022] sandy krish😎: a=[[0],[1,3],[5,7],[9,11],[13,15,17]]
i=0
maxl=0
minl=0
while i<len(a):
	if len(a[i])>maxl:
		maxl=len(a[i])
		minl=a[i]
		print(maxl,minl)
	i+=1
	15.min and max
[16:01, 1/28/2022] sandy krish😎: 14
[17:00, 1/28/2022] sandy krish😎: a=[2,4,6,8]
i=1
b=[ ]
while i<len(a):
	c=a[-i]-a[-i-1]
	b.append(c)
	i+=1
print(b)
16.difference
[09:25, 1/29/2022] sandy krish😎: a=[1,2,3,4,5,6,7,8,9,10]
i=1
b=[ ]
while i<len(a):
	c=a[-i]-a[-i-1]
	b.append(c)
	i+=1
print(b)
A)16.difference
[09:30, 1/29/2022] sandy krish😎: list=[1,2,3,1,2,2]
i=0
a=[ ]
while i<len(list):
	if list[i]not in a:
		a.append(list[i])
	i+=1
print(a)
24)remove  duplicate numbers
[10:18, 1/29/2022] sandy krish😎: n=[4,6,4,3,3,4,3,4,3,8]
i=0
a=[ ]
while i<len(n):
	j=0
	c=0
	while j<=i:
		if n[i]==n[j]:
			c+=1
		j+=1
	if c>3:
		a.append(n[i])
	i+=1
print(a)
25)a)elements of frequency greater than k
[10:20, 1/29/2022] sandy krish😎: n=[4,6,4,3,3,4,3,4,6,6]
k=2
a=[ ]
while k<len(n):
	if n[k] not in a:
		a.append(n[k])
	k+=1
print(a)

25)b) elements of frequency greater than k
[10:45, 1/29/2022] sandy krish😎: n=[1,1,1,64,23,64,22,22,22]
i=2
a=[ ]
while i<len(n):
	if n[i] not in a:
		a.append(n[i])
	i+=4
print(a) 
n=[4,5,5,3,8]
i=2
a=[ ]
while i<len(n):
	if n[i] not in a:
		a.append(n[i])
	i+=4
print(a)
26)which occur 3 consecutive times
[11:10, 1/29/2022] sandy krish😎: list=[5,6,[],3,[ ],[ ],9]
b=[ ]
for i in list:
	if i!=[ ]:
		b.append(i)
print(b)
29)remove empty list
[18:42, 1/29/2022] sandy krish😎: a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
count=0
max=[ ]
while i<len(a):
	if a[i]>max:
		max=a[i]
		count+=1
	i+=1
j=0
count1=0
min=a[j]
while j<len(a):
	if a[j]>max:
		min=a[j]
		count1+=1
	j+=1
print((count,max))
print((count1,min))
14)min and max
[18:42, 1/29/2022] sandy krish😎: 30.Given a list of numbers, write a Python program to count positive and negative numbers in a List.
Example:

list1 = [2, -7, 5, -64, -14]

Output: pos = 2, neg = 3


Iist2 = [-12, 14, 95, 3]

Output: pos = 3, neg = 1

A. 
list1 = [2, -7, 5, -64, -14]
i=0
count=0
count1=0
while i<len(list1):
	if list1[i]>0:
		count+=1
	else:
		count1+=1
	i+=1
print('positive',count)
print('negative',count1)


B. 
list2= [-12,14,95,3]
i=0
count=0
count1=0
while i<len(list2):
	if list2[i]>0:
		count+=1
	else:
		count1+=1
	i+=1
print('positive',count)
print('negative',count1)
[19:45, 1/29/2022] sandy krish😎: list= [15,81,11,234]
i=0
b=[]
while i<len(list):
	j=list[i]
	sum=0
	while j>0:
		rem=j%10
		sum=sum+rem
		j=j//10
	b.append(sum)	
	i+=1
print(b)
33)b)sum of number digits
[19:46, 1/29/2022] sandy krish😎: list= [12, 67, 98, 34]
i=0
b=[]
while i<len(list):
	j=list[i]
	sum=0
	while j>0:
		rem=j%10
		sum=sum+rem
		j=j//10
	b.append(sum)	
	i+=1
print(b)
33)a)
[20:18, 1/29/2022] sandy krish😎: 36.
Write a Python program to join adjacent members of a given list.
Original list:

['1', '2', '3', '4', '5', '6', '7', '8']

Join adjacent members of a given list:

['12', '34', '56', '78']

Original list:

['1', '2', '3']

Join adjacent members of a given list:

['12']

A. 
list=['1', '2', '3', '4', '5', '6', '7', '8']
i=0
a=[ ]
while i<len(list)-1:
	b=(list[i])+(list[i+1])
	a.append(b)
	i+=2
print(a)

B. 

list=['1', '2', '3']
i=0
a=[ ]
while i<len(list)-1:
	b=(list[i])+(list[i+1])
	a.append(b)
	i+=2
print(a)
[20:44, 1/29/2022] sandy krish😎: 37.
Write a Python program to pair up the consecutive elements of a given list.
Original lists:

[1, 2, 3, 4, 5, 6]

Pair up the consecutive elements of the said list:

[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]]

Original lists:

[1, 2, 3, 4, 5]

Pair up the consecutive elements of the said list:

[[1, 2], [2, 3], [3, 4], [4, 5]]

A. 

list=[1, 2, 3, 4, 5, 6]
i=0
a=[ ]
while i<len(list)-1:
	b=[list[i],list[i+1]]
	a.append(b)
	i+=1
print(a)


B. 

list=[1, 2, 3, 4, 5, ]
i=0
a=[ ]
while i<len(list)-1:
	b=[list[i],list[i+1]]
	a.append(b)
	i+=1
print(a)
[10:47, 1/30/2022] sandy krish😎: list=[34.67,12,-94.89,"python",0,"c#"]
i=0
b=[]
while i<len(list):
	if type(list[i])==int:
		b.append(list[i])
	i+=1
print(b)
	
	34. Write a Python program to remove all the values except integer values from a given
array of mixed values.
Original list: [34.67, 12, -94.89, 'Python', 0, 'C#']
After removing all the values except integer values from the said array of mixed values:
[12, 0]
[10:56, 1/30/2022] sandy krish😎: 31. Given the start and end of a range, write a Python program to print all negative numbers in a given
range.
Example:
Input: start = -4, end = 5
Output: -4, -3, -2, -1
Input: start = -3, end = 4
Output: -3, -2, -1

A .

list=[-4,-3,-2,-1,0,1,2,3,4,5]
i=0
while i<len(list):
	if -4<=list[i]<5:
		if list[i]<0:
			print(list[i],end=" ")
	i+=1

O/p:[-4,-3,-2,-1]


B.

list=[-3,-2,-1,0,1,2,3,4,]
i=0
while i<len(list):
	if -4<=list[i]<5:
		if list[i]<0:
			print(list[i],end=" ")
	i+=1

O/p:[-3,-2,-1]
[11:38, 1/30/2022] sandy krish😎: 32.Given start and end of a range, write a Python program to print all positive numbers in given range.
Example:

Input: start = -4, end = 5

Output: 0, 1, 2, 3, 4, 5


Input: start = -3, end = 4

Output: 0, 1, 2, 3, 4


A. 
list=[-4,-3,-2,-1,0,1,2,3,4,5]
i=0
while i<len(list):
	if -4<=list[i]<=5:
		if list[i]>=0:
			print(list[i],end=" ")
	i+=1

Output:-0,1, 2, 3, 4, 5

B. 

list=[-3,-2,-1,0,1,2,3,4,]
i=0
while i<len(list):
	if -4<=list[i]<=5:
		if list[i]>=0:
			print(list[i],end=" ")
	i+=1

Output:-0, 1,2,3,4
[11:51, 1/30/2022] sandy krish😎: 44.Write a Python program to add a number to each element in a given list of numbers.
Original lists:

[3, 8, 9, 4, 5, 0, 5, 0, 3]

Add 3 to each element in the said list:

[6, 11, 12, 7, 8, 3, 8, 3, 6]

Original lists:

[3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0]

Add 0.51 to each element in the said list:

[3.71, 8.51, 10.41, 4.71, 5.51, 0.61, 5.51, 3.62, 0.51]

A. 
list=[3, 8, 9, 4, 5, 0, 5, 0, 3]
i=0
sum=0
a=[ ]
while i<len(list):
	sum=list[i]+3
	a.append(sum)
	i+=1
print(a)

Output:-[6, 11, 12, 7, 8, 3, 8, 3, 6]

[Program finished]


B. 

list=[3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0]
i=0
sum=0
a=[ ]
while i<len(list):
	sum=list[i]+0.51
	a.append(sum)
	i+=1
print(a)


Output:-[3.71, 8.51, 10.41, 4.71, 5.51, 0.61, 5.51, 3.62, 0.51]

[Program finished]
[12:22, 1/30/2022] sandy krish😎: 43.Write a Python program to insert a specified element in a given list after every nth element.
Original list:

[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]

Insert 20 in said list after every 4 th element:

[1, 3, 5, 7, 20, 9, 11, 0, 2, 20, 4, 6, 8, 10, 20, 8, 9, 0, 4, 20, 3, 0]

Original list:

['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']

Insert Z in said list after every 3 th element:

['s', 'd', 'f', 'Z', 'j', 's', 'a', 'Z', 'j', 'd', 'f', 'Z', 'd']

A. 

list=[1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
i=0
a=4
list1=[]
while i<len(list):
	if i==a:
		list1.append(20)
		a+=4
	list1.append(list[i])
	i+=1
print(list1)

Output:-[1, 3, 5, 7, 20, 9, 11, 0, 2, 20, 4, 6, 8, 10, 20, 8, 9, 0, 4, 20, 3, 0]

[Program finished]

B. 

…
[16:20, 1/30/2022] sandy krish😎: 45. Write a Python program to remove the last N number of elements from a given list.

Original lists:

[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]

Remove the last 3 elements from the said list:

[2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34]

A.

list=[2,3,9,8,2,0,39,84,2,2,34,2,34,5,3,5]
i=0
a=[ ]
while i<len(list)-3:
	if list[i]!=0:
		a.append(list[i])
	i+=1
print(a)

B.

list=[2,3,9,8,2,0,39,84,2,2,34,2,34,5,3,5]
i=0
a=[ ]
while i<len(list)-3:
	if list[i]!=0:
		a.append(list[i])
	i+=1
print(a)
[09:40, 1/31/2022] sandy krish😎: 46.Write a Python program to concatenate element-wise three given lists.
Original lists:

['0', '1', '2', '3', '4']

['red', 'green', 'black', 'blue', 'white']

['100', '200', '300', '400', '500']

Concatenate element-wise three said lists:

['0red100', '1green200', '2black300', '3blue400', '4white500']

list=[['0', '1', '2', '3', '4'],['red', 'green', 'black', 'blue', 'white'],['100', '200', '300', '400', '500']]
i=0
a=list[0]
b=list[1]
c=list[2]
d=[ ]
while i<len(a):
	j=0
	while j<len(b):
		k=0
		while k<len(c):
			e=a[i]+b[j]+c[k]
			d.append(e)

			k+=1
			j+=1
			i+=1
print(d)

Output:-['0red100', '1green200', '2black300', '3blue400', '4white500']

[Program finished]
[10:29, 1/31/2022] sandy krish😎: 47.write a python program to convert a given list of strings in to list of lists.

1 a=['red','maroon','yellow','white']
i=0
b=[ ]
while i<len(a):
	j=0
	while j<len(a[i]):
		b.append(a[i][j])
		j+=1
	i+=1
print(b)
[14:50, 1/31/2022] sandy krish😎: #even 
#Odd
#Even prime
#Odd prime

a=[1,2,3,4,5,6,7,8,9,10]
i=0
odd=[]
even=[]
even_prime=[]
odd_prime=[]
while i<len(a):
	if a[i]%2==0:
		even.append(a[i])
		if a[i]==2:
			even_prime.append(2)
	else:
		odd.append(a[i])
		j=2
		while j<a[i]:
			if a[i]%j==0:
				break
			else:
				j+=1
		if a[i]==j:
			odd_prime.append(a[i])
	i+=1
print("odd list is ",odd)
print("odd prime list is" ,odd_prime);
print("even list is ",even);
print("even prime lsit is ",even_prime);

⁉️In the given list find even,odd,even prime,odd prime❓
[15:16, 1/31/2022] sandy krish😎: #a=[0,[3,5,[4,7,[10]]]]
print(a[1][2][2])
O/p:10
[15:21, 1/31/2022] sandy krish😎: #a=[4,5]
i=0
s=0
while i<len(a):
	s=s+a[i]
	i+=1
print(s)
O/p: 9
[13:48, 2/1/2022] sandy krish😎: #MAGIC NUMBER
ms=[
[8,3,4],
[1,5,9],
[6,7,2]
]
i=0
r1=0
r2=0
r3=0
c1=0
c2=0
c3=0
d1=0
d2=0
while i<len(ms):
	r1+ms[i][0]
	r2+ms[i][1]
	r3+ms[i][2]
	c1+ms[i][0]
	c2+ms[i][1]
	c3+ms[i][2]
	d1+ms[i][0]
	d2+ms[i][1]
	i+=1
	if r1==r2==r3==c1==c2==c3==d1==d2:
		print('its magic square')
		break
	else:
		print('its not magic square')
		break
O/P:it's a magic number
[13:53, 2/1/2022] sandy krish😎: #MAGIC NUMBER
ms=[
[8,3,4],
[1,5,9],
[6,7,2]
]
i=0
r1=0
r2=0
r3=0
c1=0
c2=0
c3=0
while i<len(ms):
	r1+ms[i][0]
	r2+ms[i][1]
	r3+ms[i][2]
	c1+ms[i][0]
	c2+ms[i][1]
	c3+ms[i][2]
	i+=1
	if r1==r2==r3==c1==c2==c3:
		print('its magic square')
		break
	else:
		print('its not magic square')
		break
O/P:it's a magic number
[15:22, 2/4/2022] sandy krish😎: a=[5,3,3,2,7,10,6,2,2,10,1]
i=0
while i<len(a):
	j=0
	while j<len(a):
		if (a[i]<a[j]):
			a[i],a[j]=a[j],a[i]
		j+=1
	i+=1
print(a)
				
			👉👉👉Write a program to print in ascending order of the list❓❓❓ and decending order also
[15:22, 2/4/2022] sandy krish😎: a=[" pr iya"," lax m i","hi ma bin du"]
i=0
space=[ ]
while i<len(a):
	j=0
	st=' '
	while j<len(a[i]):
		if a[i][j]!=' ':
			st+=a[i][j]
		j+=1
	space.append(st)
	i+=1
print(space)

👉👉remove the space❓
[15:22, 2/4/2022] sandy krish😎: print("hello everyone")
print("_welcome to KBC_")
print("* very good luck for your game***")
print("so lets play the game")
question_list=["what is the capital of India?","How many colours in rainbow?",
"How many girls in navgurukul ? ","which course we are doing in navgurukul?"]
options_list=[["bihar","delhi","kolkata","canada"],["8","9","7","10"],["118","120","100","104"],["beaty palour","swimming course","fashion designer","engineering course"]]
life_line=[["delhi","bihar"],["7","10"],["120","118"],["engineering course","beaty palour"]]
solution_list2=[1,1,2,1]
solution_list=[2,3,1,4]
i=0
count=0
while i<len(question_list[i]):
	print("Q.",i+1,question_list[i])
	j=0
	while j<len(options_list[i]):
		print(j+1,options_list[i][j])
		j=j+1
	user=int(input("cho…
[15:22, 2/4/2022] sandy krish😎: 50.Write a Python program to join two given list of lists of same length, element wise.
Original lists:

[[10, 20], [30, 40], [50, 60], [30, 20, 80]]

[[61], [12, 14, 15], [12, 13, 19, 20], [12]]

Join the said two lists element wise:

[[10, 20, 61], [30, 40, 12, 14, 15], [50, 60, 12, 13, 19, 20], [30, 20, 80, 12]]

Original lists:

[['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]

[['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]

Join the said two lists element wise:

[['a', 'b', 'p', 'q'], ['b', 'c', 'd', 'p', 's', 't'], ['e', 'f', 'u', 'v', 'w']]

A. 
list=[[10, 20], [30, 40], [50, 60], [30, 20, 80]]

list1=[[61], [12, 14, 15], [12, 13, 19, 20], [12]]
i=0
a=[ ]
while i<len(list):
	b=list[i]+list1[i]
	a.append(b)
	i+=1
print(a)

Output:-[[10, 20, 61], [30, 40, 12, …
[13:46, 2/5/2022] sandy krish😎: a=[23,4,6,5,0,7]
i=0
b=[ ]
while i<len(a):
	x=a[i-1]+a[-i]
	b.append(x)
	i+=2
print(b)
O/p:30,4,11
[13:53, 2/5/2022] sandy krish😎: a=[[3,5,67],[3,45,5],[5,67,28]]
i=0
b=[ ]
while i<len(a):
	j=0
	c=a[i][j]
	while j<len(a[i]):
		if a[i][j]>c:
			c=a[i][j]
			b.append(c)
		j+=1
	print(c,end=' ')
	i+=1
[14:53, 2/5/2022] sandy krish😎: *
Total sum of list? 
a=[[23, 45], [4, 5[6]]]

Output:-83

a=[[23,45],[4,5,[6]]]
i=0
b=[ ]
while i<len(a):
	if type(a[i])==list:
		j=0
		while j<len(a[i]):
			if type(a[i][j])==list:
				k=0
				while k<len(a[i][j]):
					b.append(a[i][j][k])
					k+=1
			else:
				b.append(a[i][j])
			j+=1
	else:
		b.append(a[i])
	i+=1
print(b)
i=0
s=0
while i<len(b):
	s=s+b[i]
	i+=1
print(s)

Output:-[23, 45, 4, 5, 6]
83

[Program finished]
[14:53, 2/5/2022] sandy krish😎: *
a=[9, 2,4,6,7,9]
Output:-[18, 9,10]

a=[9,2,4,6,7,9]
i=0
b=[ ]
while i<len(a):
	x=a[i-1]+a[-i]
	b.append(x)
	i+=2
print(b)
[14:53, 2/5/2022] sandy krish😎: a=[[23,45,6],[23,4,5],[20,5,1]]
i=0
b=[ ]
while i<len(a):
	j=0
	c=a[i][j]
	while j<len(a[i]):
		if a[i][j]<c:
			c=a[i][j]
			b.append(c)
		j+=1
	print(c,end=' ')
	i+=1

👉👉find the minimum numbers??

O/p: 6 4 1
[14:53, 2/5/2022] sandy krish😎: n=[[4,5,[6],8,9,[23]]]
i=0
b=[ ]
while i<len(n):
	if type(n[i])==list:
		j=0
		while j<len(n[i]):
			if type(n[i][j])==list:
				k=0
				while k<len(n[i][j]):
					b.append(n[i][j][k])
					k+=1
			else:
				b.append(n[i][j])
			j+=1
	else:
			b.append(n[i])
	i+=1
print(b)
i=0
sum=0
while i<len(b):
		sum=sum+b[i]
		i+=1
print(sum)

👉👉find the total sum❓❓