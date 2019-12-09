import numpy as np      # numpy 별명 np

def seq_array():
    data1 = list(range(0,10))
    print(type(data1), data1)
    a1 = np.array(data1)
    print(type(a1), a1.dtype, a1)

    data2 = [0.1, 5, 4, 12, 0.5]
    a2 = np.array(data2)
    print(a2.dtype, a2)


def two_dimension_array():
    a3 = np.array([[1, 2, 3], [4, 5, 6,], [7, 8, 9]])
    print(a3.dtype, a3)


def range_array():
    print(np.arange(0, 10, 2))
    print(np.arange(5))
    print(np.arange(12).reshape((4,3)))
    b1 = np.arange(12).reshape(4,3)
    print(b1.shape)

    b2 = np.arange(5)
    print(b2.shape)


def num_array():
    print(np.linspace(1, 10, 5))
    print(np.linspace(0, np.pi, 20))
    arr_zero_n = np.zeros(5)
    arr_zero_mxn = np.zeros((5, 5))
    arr_one_n = np.ones(5)
    arr_one_mxn = np.ones((5, 5))
    print(arr_one_n, arr_one_mxn, arr_zero_n, arr_zero_mxn)

    print(np.eye(2))


def type_conversion():
    str_array = np.array(['1.51', '0.62', '2', '3.14', '3.141592'])
    print(str_array, str_array.dtype)
    float_array = str_array.astype(float)
    print(float_array, float_array.dtype)


def rand_array():
    print(np.random.rand(2,3))
    print(np.random.rand())
    print(np.random.rand(2,3,4))
    print(np.random.randint(10, size=(3,4)))
    print(np.random.randint(1,30))


def calculate_array():
    arr1 = np.array([10, 20, 30, 40])
    arr2 = np.array([1, 2, 3, 4])
    print(arr1+arr2, arr1-arr2, arr2*2, arr2**2, arr1*arr2, arr1/arr2, arr1/(arr2**2))
    print(arr1 > 20)

    arr3 = np.arange(5)
    print(arr3)
    print([arr3.sum(), arr3.mean()])
    print([arr3.std(), arr3.var()])
    print([arr3.min(), arr3.max()])

    arr4 = np.arange(1,5)
    print(arr4, arr4.cumsum(), arr4.cumprod())

    A = np.array([0, 1, 2, 3,]).reshape(2,2)
    print(A)
    B = np.array([3, 2, 0, 1]).reshape(2,2)
    print(B)

    print(A.dot(B))
    print(np.dot(A,B))

    print(np.transpose(A))
    print(A.transpose())

    print(np.linalg.inv(A))
    print(np.linalg.det(A))


def array_indexing():
    # a1 = np.array([0, 10, 20, 30, 40, 50])
    a1 = np.arange(0,60,10)
    print(a1, a1[0], a1[4])
    print(a1[[1, 3, 4]])
    a2 = np.arange(10, 100, 10).reshape((3,3))
    print("a2값: {}".format(a2))
    print(a2[0,2])
    a2[2,2]=95
    print(a2)

    print(a2[1])
    a2[1] = np.array([45, 55, 65])
    print(a2)

    a2[1] = [47, 57, 67]
    print(a2)

    print(a2[[0,2],[0,1]])
    a = np.array([1, 2, 3, 4, 5, 6])
    print(a[a>3])
    print(a[(a%2)==0])


def array_slicing():
    b1 = np.array([0, 10, 20, 30, 40, 50])
    print(b1[1:4], b1[:3], b1[2:])
    b1[2:5] = np.array([25, 35, 45])
    print(b1)

    b1[3:6] = 60
    print(b1)

    b2 = np.arange(10, 100, 10).reshape(3,3)
    print(b2)

    print(b2[1:3, 1:3])
    print(b2[:3,1:])

    print(b2[1][0:2])


    b2[0:2, 1:3] = np.array([[25, 35], [55, 65]])
    print(b2)



if __name__ == "__main__":
    # seq_array()
    # two_dimension_array()
    # range_array()
    # num_array()
    # type_conversion()
    # rand_array()
    # calculate_array()
    # array_indexing()
    array_slicing()

