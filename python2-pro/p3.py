import streamlit as st
import joblib
import numpy as np
import pandas as pd
from sklearn import datasets

st.title("Iris 品種預測")
svm = joblib.load("svm.joblib")
RF = joblib.load("rf.joblib")
knn = joblib.load("knn.joblib")
LR = joblib.load("lr.joblib")

# 側邊欄選擇模型
m = st.sidebar.selectbox(
    "選擇分類模型",
    ["支援向量機(SVM)", "隨機森林(RF)", "K近鄰(KNN)", "邏輯回歸(LR)"])
    
if m == "支援向量機(SVM)":
    model = svm
elif m == "隨機森林(RF)":
    model = RF
elif m == "K近鄰(KNN)":
    model = knn
elif m == "邏輯回歸(LR)":
    model = LR

# 接收預測資料
iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
se1 = st.slider("#### 花萼長度 (cm)", 
                float(df['sepal length (cm)'].min()), 
                float(df['sepal length (cm)'].max()), 
                float(df['sepal length (cm)'].mean()))
se2 = st.slider("#### 花萼寬度 (cm)", 
                float(df['sepal width (cm)'].min()),
                float(df['sepal width (cm)'].max()),
                float(df['sepal width (cm)'].mean()))
se3 = st.slider("#### 花瓣長度 (cm)",
                float(df['petal length (cm)'].min()),
                float(df['petal length (cm)'].max()),
                float(df['petal length (cm)'].mean()))
se4 = st.slider("#### 花瓣寬度 (cm)",
                float(df['petal width (cm)'].min()),
                float(df['petal width (cm)'].max()),
                float(df['petal width (cm)'].mean()))

st.image('iris.png')

# 預測結果
labels =['Setosa', 'Versicolor', 'Virginica']

if st.button("進行預測"):
    X = [[se1, se2, se3, se4]]
    y_pred = model.predict(X)
    st.write(y_pred)
    st.success(f'#### 預測品種為:,{labels[y_pred[0]]}')

#st.write("請輸入花萼與花瓣的長寬(cm)來預測Iris的品種")
#sepal_length = st.number_input("花萼長度", 0.0, 10.0, 5.0)
#sepal_width = st.number_input("花萼寬度", 0.0, 10.0, 3.0)
#petal_length = st.number_input("花瓣長度", 0.0, 10.0, 1.5)
#petal_width = st.number_input("花瓣寬度", 0.0, 10.0, 0.2)

#input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])