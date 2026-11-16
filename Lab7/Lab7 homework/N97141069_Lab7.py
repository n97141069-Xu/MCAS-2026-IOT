import numpy as np 
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = np.loadtxt("Bank_Customer.csv", skiprows=1, dtype=str, delimiter=',')

'''
Your work
非數值型資料需轉換成數值型資料 (country, gender)
去除掉無意義的特徵類別 (customer_id)
標準化特徵 (StandardScaler)
'''
# 1. 去除無意義特徵 (customer_id，第 0 欄)
data = data[:, 1:]

# 2. 非數值型資料轉數值
data[:, 2] = np.where(data[:, 2] == 'Female', '0', '1')            # gender: Female=0, Male=1
data[:, 1] = np.where(data[:, 1] == 'France', '0',
             np.where(data[:, 1] == 'Spain', '1', '2'))            # country: France=0, Spain=1, Germany=2
data = data.astype(float)

# 3. 標準化特徵
X = data[:, :-1]
y = data[:, -1]
X = StandardScaler().fit_transform(X)

pre_data = np.column_stack((X, y))

np.savetxt("Bank_Customer_Preprocessed.csv", pre_data, delimiter=",")


from sklearn.linear_model import LogisticRegression 
# 決策分類器
clf = LogisticRegression()

'''
Your work
切割 data 為 x_train, x_test, y_train, y_test
請學習 train_test_split 的使用方法
'''

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=123)

# 使用訓練集來訓練我們的分類器
clf.fit(x_train, y_train)
# 測試資料集中進行預測
pred = clf.predict(x_test)

#print (pred) # 預測分類，即客戶是否流失
#print (y_test) # 分類
print (str(accuracy_score(pred, y_test)*100 ) + "% ")   # 預測精度