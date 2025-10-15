import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import StandarScaler
from sklearn.decomposition import PCA


st.title("IRIS資料集展示")

# 載入IRIS
iris=datasets.load_iris()
df=pd.DataFrame(iris.data,columns=iris.feature_names)
st.write(df.head())

colors = ['r','g','b']
#上半部是資料
#下半部是pca 散點圖