import streamlit as st
import face_recognition
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np
from PIL import ImageDraw, Image
# from IPython.display import display
# def draw_faces(img, locs):
    
def img_output(uploaded_file):

    # 画像を読み込む。
    # img = face_recognition.load_image_file("images/my_picture.jpg")
    img = face_recognition.load_image_file(uploaded_file)

    # CNN を使った顔検出
    face_locations = face_recognition.face_locations(img,model="cnn",number_of_times_to_upsample=2)

    # HOG 特徴量を使った顔検出
    # face_locations3 = face_recognition.face_locations(img,model="hog")

    # 顔の各部位を検出する。
    facial_landmarks = face_recognition.face_landmarks(img, face_locations)
    # print(facial_landmarks)

    # draw_faces(img, face_locations)
    img = Image.fromarray(img)
    draw = ImageDraw.Draw(img, mode="RGBA")

    for top, right, bottom, left in face_locations:
        draw.rectangle((left, top, right, bottom), outline="lime", width=2)

    # 日本語訳
# jp_names = {'nose_bridge': '鼻筋',
#             'nose_tip': '鼻先',
#             'top_lip': '上唇',
#             'bottom_lip': '下唇',
#             'left_eye': '左目',
#             'right_eye': '左目',
#             'left_eyebrow': '左眉毛',
#             'right_eyebrow': '右眉毛',
#             'chin': '下顎'}

    for face in facial_landmarks:
        for name, points in face.items():
            print(name)
            print(points)
            print("")
            points = np.array(points)
            draw.point(points, fill='red')
            # draw.line(points, fill='red', width=2) 
    #         ax.plot(points[:, 0], points[:, 1], 'o-', ms=3, label=jp_names[name])

    st.image(img, caption='サンプル',use_column_width=True)