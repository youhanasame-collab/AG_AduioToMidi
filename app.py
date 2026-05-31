import streamlit as st
import os

st.title("AG_AudioToMidi Engine")

# هنا بنعمل "Import" داخل الكود عشان لو المكتبة لسه بتحمل، البرنامج ميقعش فوراً
try:
    from basic_pitch.inference import predict_and_save
    basic_pitch_available = True
except ImportError:
    basic_pitch_available = False

audio_file = st.file_uploader("ارفع ملف الصوت (WAV/MP3)", type=['wav', 'mp3'])

if audio_file is not None:
    if not basic_pitch_available:
        st.error("عذراً، مكتبة التحليل لسه بيتم تثبيتها. استنى دقيقة واعمل Refresh.")
    else:
        with open("input.wav", "wb") as f:
            f.write(audio_file.getbuffer())
        
        st.write("جاري التحليل...")
        predict_and_save(
            audio_path_list=["input.wav"],
            output_directory="./",
            save_midi=True,
            save_model_outputs=False,
            save_notes=False
        )
        st.success("تم التحليل!")
        with open("input_basic_pitch.mid", "rb") as f:
            st.download_button("تحميل ملف الـ MIDI", f, "output.mid")
