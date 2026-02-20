import numpy as np

# ✅Step 2 – Create Array from Python List
arr = np.array([2,5,7,9])
print(arr)
print(type(arr))
print(arr.dtype)
print(arr.shape)

# ✅Step 3 – Create 2D Array (Matrix) from List of Lists
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)
print(arr2.shape)

# ✅Step 4 – Special Arrays: Zeros, Ones, Full
zeros = np.zeros((3,2))
ones= np.ones((2,3))
full = np.full((2,3),7)
print("Zeros:\n", zeros)
print("Ones:\n", ones)
print("Full:\n", full)

# ✅Step 4 – Special Arrays: Zeros, Ones, Full
a = np.arange(0,10,2) # start, stop (exclusive), step
print(a)
b = np.linspace(0,1,5)# start, stop (inclusive), num points
print(b)

#  tuple
arr = np.array((1, 2, 3, 4, 5))
print(arr)

# 0-D Arrays
arr = np.array(42)
print(arr)

# 1-D Arrays
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# 2-D arrays
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

# 3-D arrays
arr = np.array([[1, 2, 3], [4, 5, 6], [1, 2, 3]])
print(arr)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) #with 2 2ds
print(arr)


# Check Number of Dimensions?
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)

arr = np.array(({'a':10}, {'b':20}))# dict inside list or tuple work
# arr = np.array([{'a':10}, {'b':20}])
print(arr)
print("Dtype:", arr.dtype)

# ✅NumPy Array Indexing
arr = np.array([1, 2, 3, 4])
print(arr[2])

arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3])# index2 = 3 + index3 = 4

# ✅Access 3-D Arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])

# ✅Negative Indexing
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])

# ✅NumPy Array Slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[:4])

# ✅Negative Slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])

# ✅STEP for slicing
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2])

# ✅Slicing 2-D Arrays
arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10]])
print(arr[0, 1:4]) # first array and 1:4

arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10]])
print(arr[0:2, 2])#  rows, column

arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10]])
print(arr[0:2, 1:4])

# ✅Checking the Data Type of an Array
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='i4')# when we want  data output  as i4 type or any means that symbol
print(arr)
print(arr.dtype)

# ✅Converting Data Type on Existing Arrays
arr = np.array([1.1, 2.1, 3.1])
print(arr)
print(arr.dtype)
newarr = arr.astype(int)#AStype will do copy of the array and i is int float to int changing
print(newarr)
print(newarr.dtype)

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)# int to bool
print(newarr)
print(newarr.dtype)

# ✅NumPy Array Copy vs View
# The copy SHOULD NOT be affected by the changes made to the original array.
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
x[0] = 42
print(arr)
print(x)

# The view SHOULD be affected by the changes made to the original array.
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 42
print(arr)
print(x)

# ✅NumPy Array Shape
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)

# ✅NumPy Array Reshaping
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
# Reshape From 1-D to 3-D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)#Pass -1 as the value, and NumPy will calculate this number for you.
print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)

# ✅NumPy Array Iterating
arr = np.array([1, 2, 3])
for x in arr:
  print(x)

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    print(x)

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  for y in x:
    print(y)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
  print(x)

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
 for y in x:
    for z in y:
      print(z)
#(both are same up and down)
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
  print(x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:,::2]):
    print(x)

arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
    print(idx,x)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
  print(idx, x)

# ✅NumPy Joining Array
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1,arr2))
print(arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1,arr2), axis = 0)
print(arr)
arr = np.concatenate((arr1,arr2), axis = 1)
print(arr)

#✅Joining Arrays Using Stack Functions
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))# rows
print(arr)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))# columns
print(arr)




arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.dstack((arr1, arr2))# height same as rows
print(arr)

# ✅NumPy Splitting Array
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr,2) # 2parts splited
print(newarr)
print(newarr[0])# split value got through index

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)
print(newarr[2])

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)#rows split
print(newarr)


# ✅NumPy Searching Arrays
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.array(arr == 7)# search number if not there false
print(x)
x = np.array(arr == 4)
print(x)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)

# ✅Search Sorted
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr,7) # where 7 is index no?
print(x)

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side='right')
print(x)

arr = np.array([1, 3, 15, 7])
arr_sorted = np.sort(arr)
x = np.searchsorted(arr_sorted, [2, 4, 8])
print(x)

# ✅NumPy Sorting Arrays
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

arr = np.array([True, False, True])
print(np.sort(arr))

rr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(rr))

# ✅NumPy Filter Array
arr = np.array([41, 42, 43, 44])
x = [True, False, False, True]# true there false delete
newarr = arr[x]
print(newarr)

arr = np.array([41, 42, 43, 45])
filter_arr = []
for i in arr:
    if i > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

print(filter_arr)
newarr = arr[filter_arr]
print(newarr)


arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)


# ✅Step 2 – NumPy Array Operations
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([1, 2, 3, 4])
print("arr1 + arr2 =", arr1 + arr2)
print("arr1 - arr2 =", arr1 - arr2)
print("arr1 * arr2 =", arr1 * arr2)
print("arr1 / arr2 =", arr1 / arr2)

# ✅2️⃣ Universal Functions (ufuncs)
print(np.sqrt(arr1))
print(np.exp([1,2,3]))
print("Sine values:", np.sin([0, np.pi/2, np.pi]))

# ✅3️⃣ Aggregate Functions
arr = np.array([10, 20, 30, 40])
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Max:", np.max(arr))
print("Min:", np.min(arr))
print("Standard deviation:", np.std(arr))

# ✅Generate Random Number
# ✅ 1D array
x = np.random.randint(100)
print(x)
x = np.random.rand()
print(x)
num = np.random.randint(1, 191)  # high is exclusive → 191
print(num)
#randint(low, high, size)
arr = np.random.randint(1, 191, 3)  # 5 random numbers
print(arr)

# ✅ 2D array
print(np.random.rand(2,3))

# ✅4️⃣ seed() → Fix Random Output
np.random.seed(10)
print(np.random.rand(5))

# ✅5️⃣ choice() → Random Sampling
arr = np.array([10,20,30,40, 50])
print(np.random.choice(arr, 2))

#  ✅6️⃣ shuffle() → Shuffle Original Array
arr = np.array([1,2,3,4,5])
np.random.shuffle(arr)
print(arr)

# ✅7️⃣ uniform() → Random Float in Range
print(np.random.uniform(5, 10, 5))

# ✅8️⃣ normal() → Custom Normal Distribution
print(np.random.normal(50, 5, 5))

print('thank you')