import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

st.title("IRIS資料集展示")
iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
st.write(df.head())

colors = ['r', 'g', 'b']

#上半部是資料
#下半部是pca 散點圖
# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html

df['target'] = iris.target #加入目標欄位,方便查看,X+y
# st.subheader("IRIS資料集前五筆資料")
# st.write(df.head())
mapping = {'setosa':0,'versicolor':1,'virginica':2}
# df['target'] = df['target'].map(mapping)

# 分頁
tab1, tab2 = st.tabs(["依花萼的長寬", "依花瓣的長寬"])
fig, ax = plt.subplots()
with tab1:
    for i, s in mapping.items():
        subset = df[df['target'] == s]
        ax.scatter(subset['sepal length (cm)'], subset['sepal width (cm)'], 
                   label=i, c=colors[s])
    ax.set_xlabel('Sepal Length (cm)')
    ax.set_ylabel('Sepal Width (cm)')
    ax.set_title('IRIS Sepal Length vs Width')
    ax.legend()
    st.pyplot(fig)

fig2, ax2 = plt.subplots()
with tab2:
    for i, s in mapping.items():
        subset = df[df['target'] == s]
        ax2.scatter(subset['petal length (cm)'], subset['petal width (cm)'], 
                   label=i, c= colors[s])    
    ax2.set_xlabel('Petal Length (cm)')
    ax2.set_ylabel('Petal Width (cm)')
    ax2.set_title('IRIS Petal Length vs Width')
    ax2.legend()
    st.pyplot(fig2)
    
#PCA 降維
st.write("### PCA:將全部特徵轉換成二維")
X = iris.data
scaler = StandardScaler()
X_scaler = pd.DataFrame(scaler.fit_transform(X), columns=iris.feature_names)

pca = PCA(n_components=2, random_state=42)
X_pca = pca.fit_transform(X_scaler)

fig3, ax3 = plt.subplots()
y= df['target']
for i, name in enumerate(y.unique()):
    m = (y.values == i)
    ax3.scatter(X_pca[m, 0], X_pca[m, 1], c=colors[i], label=name)

ax3.set_xlabel('PCA 1')
ax3.set_ylabel('PCA 2')
ax3.set_title('PCA of IRIS Dataset')
ax3.legend()
st.pyplot(ax3.figure)

st.write("PCA降維後的資料點分佈如上圖所示，不同顏色代表不同的IRIS品種。")
st.write("PCA（主成分分析）是一種降維技術，可以將高維資料投影到低維空間，同時保留資料的主要特徵。")
st.write("在此例中，我們將4維的IRIS資料集降維到2維，並使用散點圖展示不同品種的分佈情況。")
st.write("從圖中可以看出，不同品種的IRIS在PCA空間中有一定的分離度，這表明PCA能夠有效地捕捉資料中的變異性。")
st.write("這對於後續的分類任務非常有幫助，因為良好的分離度通常意味著分類器能夠更準確地識別不同的類別。")
st.write("總結來說，PCA是一個強大的工具，可以幫助我們理解和可視化高維資料，並為機器學習任務提供有價值的特徵。")
##
