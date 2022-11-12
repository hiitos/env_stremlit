import streamlit as st
import face_recognition
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageDraw, Image
from IPython.display import display
from func import func_face_recog

print("-------------app start -------------")

st.title("face recog")

uploaded_file = st.file_uploader("顔が写っている写真をjpgかpngでアップロードしてください。")
submit_button = st.button('顔検出')

if uploaded_file is not None:
    # image = Image.open(uploaded_file)
    # img_array = np.array(image)
    # st.image(
    #     image, caption='upload images',
    #     use_column_width=True
    # )
    if submit_button:
        func_face_recog.img_output(uploaded_file)
    else:
        st.error("顔検出ボタンを押してください")

# st.selectbox('コンボボックス',('選択1','選択2'))
# st.checkbox('チェックボックス')
# st.radio('ラジオボタン',('ラジオボタン1','ラジオボタン2'))
# st.date_input('日付インプット')
# st.text_input('インプットボックス')
# st.text_area('テキストエリア')
# st.selectbox("メニューリスト", ("選択肢1", "選択肢2", "選択肢3")) 
# st.multiselect("メニューリスト（複数選択可）", ("選択肢1", "選択肢2", "選択肢3")) 

print("-------------app end -------------")