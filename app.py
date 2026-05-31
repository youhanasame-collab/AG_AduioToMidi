import streamlit as st
from basic_pitch.inference import predict_and_save
import os

st.title("AG_AduioToMidi Engine")

audio_file = st.file_uploader("ارفع ملف الصوت (WAV/MP3)", type=['wav', 'mp3', 'ogg'])

if audio_file is not None:
    # حفظ الملف مؤقتاً عشان الـ Engine يقرأه
    with open("input.wav", "wb") as f:
        f.write(audio_file.getbuffer())
    
    st.write("جاري التحليل... اصبر ثانية، احنا بنحلل كل النوتات!")
    
    # تنفيذ الـ Basic Pitch لتحويل الصوت لـ MIDI
    output_directory = "./"
    predict_and_save(
        audio_path_list=["input.wav"],
        output_directory=output_directory,
        save_midi=True,
        save_model_outputs=False,
        save_notes=False
    )
    
    st.success("تم التحليل بنجاح!")
    
    # رابط تحميل ملف الـ MIDI
    with open("input_basic_pitch.mid", "rb") as f:
        st.download_button("تحميل ملف الـ MIDI", f, "output.mid")
