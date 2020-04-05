import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


boston_housing = tf.keras.datasets.boston_housing

(train_x, train_y),(test_x,test_y) = boston_housing.load_data(test_split=0)

plt.rcParams['font.sans-serif']="SimHei"
plt.rcParams['axes.unicode_minus']=False

title = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B-1000", "LSTAT"]

plt.figure(figsize=(12,12))

for i in range(13):
    plt.subplot(4, 4, (i+1))
    plt.scatter(train_x[:, i], train_y)
    plt.xlabel(title[i])
    plt.ylabel("Price($1000's)")
    plt.title(str(i+1)+ "," + title[i]+ "-- Price")

plt.tight_layout()
plt.suptitle("各个属性与房价的关系", x=0.5, y=1.02, fontsize=20)
plt.show()

for i in range(len(title)):
    print("{} -- {}".format(i+1,title[i]))

choice = int(input("请选择属性"))-1
plt.subplot(111)
plt.scatter(train_x[:, choice], train_y)
plt.xlabel(title[choice])
plt.ylabel("Price($1000's)")
plt.title(str(choice+1)+ "," + title[choice]+ "-- Price")
plt.tight_layout()
plt.show()