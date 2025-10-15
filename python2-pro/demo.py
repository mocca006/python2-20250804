import numpy as np
import pandas as pd
import streamlit as st

st.title("demo Page --- Hello")
st.write("This is the demo page of the python2-pro project.")
st.write("This is a simple demo to show how to use Streamlit.")
st.write("You can add more content here as you like.")

st.write(pd.DataFrame({'name':['aa','bb','cc'],'age':[21,18,16]}))
st.info("okok")

st.table(np.array([10,20,30,40,50]))

# 核取
st.write('方塊')

ck = st.checkbox("add?")
if ck:
    st.info("add")
else:
    st.info("no add")

ck2 = st.checkbox("add?", key='1111') # 兩組以上要手動加上key=***
if ck2:
    st.info("add")
else:
    st.info("no add")

# 選取按鈕
st.write('button')
rb = st.radio("select Time",['AM','PM',"none"],key = '2222')
st.info(rb)

#下拉選單

st.write('menu')
sb = st.selectbox("區域",['台北','台中','高雄'],key = '3333')

# 輸入框練習
st.write('輸入框練習')
c1,c2,c3=st.columns(3)
with c1:
    a=st.number_input("輸入數字")
with c2:
    b=st.number_input("輸入數字",key = '4444')
with c3:
    c= st.radio("select",['+','-','*','/'])
    d = 0
    if c == '+':
        d = a+b
    elif c == '-':
        d = a-b
    elif c == '*':
        d = a*b
    elif c == '/':
        d = a/b
st.info(d)
st.info(f'結果={d:.2f}')

# https://tw.piliapp.com/symbol/
# 全形字體庫

# 滑桿
st.write('滑桿')
ss = st.slider("選擇數量", 1, 20, step=1, value=9)
st.info(ss)

ss1 = st.slider("選擇數量", 1.0, 20.0, step=0.1, value=9.0, key='5555')
st.info(ss1)

# 按鈕
st.write('按鈕')
if st.button("下單"):
    st.info("送出訂單")
else:
    st.info("尚未")

# 側邊攔
st.write('側邊欄')
sb = st.sidebar.radio("select Time",['AM','PM',"none"],key = '6666')
st.sidebar.info(sb)

#首頁
#側邊欄---資料集挑選
#main---資料是否縮放/降維
#側邊欄2---挑選模型與參數
#main---模型

#ipynb 匯出模型 ---> py 導入模型
#streamit 連結Github ---> 上傳雲端
