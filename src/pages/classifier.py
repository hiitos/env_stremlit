
import streamlit as st
import numpy as np
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

if (uploaded_file is not None):
    # モデルパス　app.pyと同じディレクトリに入れる
    try:
        model_path = "data/model_cnn1.pth"
        torch.load(model_path, map_location=torch.device("cpu"))
    except FileNotFoundError:
        eroor_message = True
        model_path = st.file_uploader("modelをアップロードしてください。")

    if model_path is not None:
        st.success("モデル読込成功")
    else:
        st.error("modelの読み込みに失敗したため、モデルをアップロードしてください")
        
    submit_button = st.button('画像を分類する')

    if submit_button:
        
        st.success("読み込み成功")
        st.image(uploaded_file)
        model = torch.load(model_path, map_location=torch.device("cpu"))
        st.write(func_classifier.result(uploaded_file,model))
    else:
        st.error("画像を分類するボタンを押してください")

print("-------------classifier end -------------")