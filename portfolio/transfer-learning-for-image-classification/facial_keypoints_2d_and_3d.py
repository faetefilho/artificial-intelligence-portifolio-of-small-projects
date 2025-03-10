# -*- coding: utf-8 -*-
"""facial-keypoints-2d-and-3d.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K3CuJGfa3hVCQGKi4IqXsuOLw6ym7DqS
"""

!pip install -qU face-alignment torch_snippets
import face_alignment
from torch_snippets import read, show

!wget https://www.dropbox.com/s/2s7xjto7rb6q7dc/Hema.JPG

fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._2D, flip_input=False, device='cpu')

input = read('Hema.JPG', 1)
preds = fa.get_landmarks(input)[0]
print(preds.shape)

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
# %matplotlib inline
fig,ax = plt.subplots(figsize=(5,5))
show(read('Hema.JPG',1), ax=ax)
ax.scatter(preds[:,0], preds[:,1], marker='+', c='r')
plt.show()

fa = face_alignment.FaceAlignment(face_alignment.LandmarksType._3D, flip_input=False, device='cpu')
input = read('Hema.JPG', 1)
preds = fa.get_landmarks(input)[0]
import pandas as pd
df = pd.DataFrame(preds)
df.columns = ['x','y','z']
import plotly.express as px
fig = px.scatter_3d(df, x = 'x', y = 'y', z = 'z')
fig.show()