import streamlit as st
import face_recognition
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageDraw, Image
from IPython.display import display
from func import func_face_recog

print("-------------face recog start -------------")

st.title("face recog")
st.write("face recognitionがstreamlit環境にデプロイできない")

# uploaded_file = st.file_uploader("顔が写っている写真をjpgかpngでアップロードしてください。")
# submit_button = st.button('顔検出')

# if uploaded_file is not None:
#     if submit_button:
#         func_face_recog.img_output(uploaded_file)
#     else:
#         st.error("顔検出ボタンを押してください")

print("-------------face recog end -------------")