
import streamlit as st
import numpy as np
from PIL import ImageDraw, Image
from IPython.display import display
from func import func_classifier
import torch
import os

path = "./"

files = os.listdir(path)
print(files)        # ['dir1', 'dir2', 'file1', 'file2.txt', 'file3.jpg']

print("-------------classifier start -------------")

st.title("classifier")

uploaded_file = st.file_uploader("画像をjpgかpngでアップロードしてください。")
# ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
submit_button = st.button('画像を分類する')

if (uploaded_file is not None):
    if submit_button:
        
        st.success("読み込み成功")
        st.image(uploaded_file)
        
        # モデルパス　app.pyと同じディレクトリに入れる
        model_path = "model_cnn.pth"
        model = torch.load(model_path, map_location=torch.device("cpu"))
        st.write(func_classifier.result(uploaded_file,model))
    else:
        st.error("画像を分類するボタンを押してください")

# "model_cnn.pth"
print("-------------classifier end -------------")