import streamlit as st
import pandas as pd

st.title('年齢調整MAC計算用')
st.caption('年齢を入力してください')

age = st.text_input('年齢')

MAC_40 = 1.8

if not age == "":
    if int(age) > 4 and int(age) < 101:

        age_related_MAC = MAC_40*10**((-0.00269)*(int(age) - 40))
        st.text(f'セボフルランにおける{age}歳の年齢調整MACは')
        st.text(f'1 MAC = {round(age_related_MAC,3)}')
        st.text(f'0.5 MAC = {round(0.5 * age_related_MAC,3)}')
        st.text(f'0.2 MAC = {round(0.2 * age_related_MAC,3)}')
    else:
        st.text('5から100の整数を半角で入力してください')

if age == "":
    st.caption('セボフルランの年齢調整MACです')
    df = pd.read_csv('streamlit_test\sevoMAC0205.csv',index_col="年齢")
    st.dataframe(df)
