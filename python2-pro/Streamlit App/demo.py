import numpy as np
import pandas as pd
import streamlit as st

st.title("Demo Page, Hello~~")
st.write("一般文字")
st.write("### ABC")
st.write("#### ABC")
st.write([10,20,30,40,50])
st.write(np.array([10,20,30,40,50]))
st.write(pd.DataFrame({'name':['AA','BB','CC'],
                       'age':[21,19,23]}))
st.table(np.array([10,20,30,40,50]))
st.info("OKOK")

#核取方塊
st.write('核取方塊')
ck = st.checkbox("是否加糖?")
if ck:
    st.info("要加糖")
else:
    st.info("不要加糖")

ck2 = st.checkbox("是否加糖?", key='1111')
if ck2:
    st.info("要加糖")
else:
    st.info("不要加糖")

#選項按鈕
st.write('選項按鈕')
rb = st.radio("請選擇時間", ['AM', 'PM',"None"], key='2222')
st.info(rb)

#下拉選單
st.write('下拉選單')
sb = st.selectbox("請選擇城市",['台北','新北','桃園'], key='3333')
st.info(sb)

#輸入框練習
st.write('輸入框練習')
c1,c2,c3 = st.columns(3)
with c1:
    a = st.number_input("請輸入任意數字")
with c2:
    b = st.number_input("請輸入任意數字", key='4444')
with c3:
    c = st.radio("請選擇任一符號",['＋','—','＊','／'])
    d = 0
    if c == '＋':
        d = a + b
    elif c == '—':
        d = a - b
    elif c == '＊':
        d = a * b
    elif c == '／':
        d = a / b
st.info(f'計算結果={d:.2f}')    

#滑桿
st.write('滑桿')
ss = st.slider("請選擇數量", 1.0, 20.0, step=0.1, value=9.0)
st.info(ss)

#按鈕
st.write('按鈕')
if st.button("確定下單"):
    st.info("送出訂單")
else:
    st.info("尚未下單")

#側邊欄
st.sidebar.write('側邊欄')
x = st.sidebar.radio("請選擇時間", ['AM', 'PM',"None"], key='666')
st.sidebar.info(x)


