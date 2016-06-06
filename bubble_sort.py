import datetime

before = datetime.datetime.now()

def bubble_sort(arr, n):
    if (n <= 1):
        return arr
    else:
        for i in range(0, n-1):
            if(arr[i] > arr[i + 1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
        return bubble_sort(arr, n-1)

arr2 = [-965, -950, -937, -908, -900, -879, -872, -868, -847, -846, -825, -819, -812, -797, -793, -767, -732, -724, -720, -713, -706, -701, -669, -656,
 -654, -612, -520, -509, -489, -470, -455, -452, -447, -426, -387, -383, -369, -356, -288, -259, -253, -249, -245, -174, -173, -150, -143, -121, -118,
 -105, -101, -67, -53, -45, -22, 3, 66, 85, 110, 119, 121, 150, 158, 172, 192, 224, 245, 272, 273, 297, 375, 382, 389, 390, 407, 430, 435, 441, 448,
 462, 504, 536, 544, 557, 568, 576, 577, 629, 694, 705, 752, 822, 828, 857, 873, 875, 894, 921, 941, 942]

arr3 = bubble_sort(arr2, len(arr2))

after = datetime.datetime.now()
print arr3
print after.microsecond - before.microsecond, "ms"
