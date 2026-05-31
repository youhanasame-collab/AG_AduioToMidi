import streamlit as st
import subprocess
import sys

# نحاول تثبيت المكتبة أثناء تشغيل التطبيق إذا لم تكن موجودة
try:
    from basic_pitch.inference import predict_and_save
except ImportError:
    st.write("جاري إعداد محرك التحليل... يرجى الانتظار دقيقة.")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "basic-pitch"])
    from basic_pitch.inference import predict_and_save

st.title("AG_AudioToMidi Engine")

audio_file = st.file_uploader("ارفع ملف الصوت (WAV/MP3)", type=['wav', 'mp3'])

if audio_file is not None:
    with open("input.wav", "wb") as f:
        f.write(audio_file.getbuffer())
    
    st.write("جاري التحليل... اصبر ثانية، احنا بنحلل كل النوتات!")
    
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
