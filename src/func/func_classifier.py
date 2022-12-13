import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms

import os
import shutil
from PIL import Image
import numpy as np
import streamlit as st

# UPLOAD_FOLDER = "./static/images/"

labels = ["飛行機", "自動車", "鳥", "猫", "鹿", "犬", "カエル", "馬", "船", "トラック"]
n_class = len(labels)
img_size = 32
n_result = 3  # 上位3つの結果を表示

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16*5*5, 256)
        self.dropout = nn.Dropout(p=0.5)
        self.fc2 = nn.Linear(256, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16*5*5)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x

def result(uploaded_file,model):
    # 画像の読み込み
    image = Image.open(uploaded_file)
    image = image.convert("RGB")
    image = image.resize((img_size, img_size))
    # return image

    normalize = transforms.Normalize(
        (0.0, 0.0, 0.0), (1.0, 1.0, 1.0))  # 平均値を0、標準偏差を1に
    to_tensor = transforms.ToTensor()
    transform = transforms.Compose([to_tensor, normalize])

    x = transform(image)
    x = x.reshape(1, 3, img_size, img_size)

    # 予測
    net = Net()
    net.load_state_dict(model)
    net.eval()  # 評価モード

    y = net(x)
    y = F.softmax(y, dim=1)[0]
    sorted_idx = torch.argsort(-y)  # 降順でソート
    print(sorted_idx)
    result = []
    for i in range(n_result):
        idx = sorted_idx[i].item()
        ratio = y[idx].item()
        label = labels[idx]
        result.append(str(round(ratio*100, 1)) + "%の確率で" + label + "です")
        
    print(result)
    return result