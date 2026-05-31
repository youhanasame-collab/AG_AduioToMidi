import streamlit as st
st.title("AG_AduioToMidi Tool")
audio_file = st.file_uploader("ارفع ملف الصوت هنا", type=['wav', 'mp3'])
if audio_file is not None:
    st.write("تم رفع الملف بنجاح!")
