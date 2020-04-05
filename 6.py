import numpy as np

np.set_printoptions(suppress=True)
np.random.seed(612)
arr1 = np.random.rand(1000)
arr2 = np.arange(1000,dtype='int32')
one = np.ones(1000,dtype='int32')
arr3 = np.stack((arr1,arr2,one),axis=1)
key = int(input("请输入一个1-100间的数字"))
while(key<0 or key>101):
    key = int(input("请输入一个1-100间的数字"))
print('\t序号\t索引值\t随机数')
count=1
for arr in arr3:
    if(int(arr[1]) % key == 0):
        print('\t{}\t\t{}\t\t{}'.format(count, int(arr[1]), arr[0]))
        count += 1