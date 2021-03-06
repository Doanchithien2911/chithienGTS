n = int(input("nhap n= "))
arr=[]
for i in range(0,n):
    x=int(input("nhap phan tu thu %d: " % (i)))
    arr.append(x)
print('mang da nhap la : ')
print(arr)
arr.sort()
print('mang tang dan la: ')
print(arr)
            