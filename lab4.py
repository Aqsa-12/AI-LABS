#Implementing Stack using Python
stack=[]
#push
stack.append('A')
stack.append('B')
stack.append('C')
print("Stack",stack)
#pop
element=stack.pop()
print('pop : ',element)
element=stack.pop()
print('pop : ',element)

#peek
topelement=stack[-1]
print('TOP :',topelement)
#isempty
isEmpty=not bool(stack)
print("IS EMPTY : ",isEmpty)
#size
print("len : ",len(stack))

#Implementing queue using Python
queue = []

# Enqueue
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue: ", queue)

# Dequeue
element = queue.pop(0)
print("Dequeue: ", element)

# Peek
frontElement = queue[0]
print("Peek: ", frontElement)

# isEmpty
isEmpty = not bool(queue)
print("isEmpty: ", isEmpty)

# Size
print("Size: ", len(queue))


#Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2 

    
        if arr[mid] == target:
            return mid  
        # 
        elif arr[mid] > target:
            high = mid - 1
        
        else:
            low = mid + 1

    return -1 

sorted_array = [6, 12, 17, 23,38, 45, 77,84,90]
target_value = 17
result = binary_search(sorted_array, target_value)

if result != -1:
    print("Target found at index:",result)
else:
    print("Target not found in the array.")