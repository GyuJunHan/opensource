myList = [30,10,20]
print("현재 리스트 : %s" % myList)

myList.append(40)
print("append(40) 후의 리스트 : %s" % myList)
print("pop()으로 추출한 값 : %s" % myList.pop())
print("pop() 후의 리스트 : %s" % myList)
#List는 Stack과 같은 LIFO구조를 지니고 있음
myList.sort()
print("sort 후의 리스트 : %s" % myList)

myList.reverse()
print("reverse()후의 리스트 : %s" % myList)

print("20값의 위치 : %d" % myList.index(20))

myList.insert(2,222)
print("insert(2,222)후의 리스트 : %s" % myList)

myList.remove(222)
print("remove(222) 후의 리스트 : %s" % myList)

myList.extend([77,88,77])
print("extend([77, 88, 77]) 후의 리스트 : %s" % myList)

print("77값의 개수 : %d" % myList.count(77))

list1 = []
list2 = []
value = 1
for i in range(0,3) :
    for j in range(0,4) :
        list1.append(value)
        value+=1
    list2.append(list1)
    list1 = []
# List로 만들어본 행렬..?
for i in range(0,3) :
    for k in range(0,4) :
        print("%3d" % list2[i][k], end = " ")
    print("")