import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

st.write("MY FIRST WEBAPP")
df = pd.read_table('https://storage.googleapis.com/kagglesdsdata/datasets/9590/13660/fruit_data_with_colors.txt?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20210118%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210118T184625Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=83388a8ddbcc779d09c8f24c4d9a0fc63f48534ecb8db88ddeaa0dc745b1414398887b40db78edec143fa1fe7aa13a363246cbd0bfc3c60092fd21b1f165fb17711a224132dbf5e649046ec0c1af4bda1512a712649df4284f13d9a5d6b5b7e1778ecb02102ee7f1e369773dfe08235ac36a4b3df18e1902800b2a25f4c430112d066fa0d7a572400d3fff2778a6075bffb4738643931390c0118851c3006de4ecf223e55138fbf5ce8bcb457161f08e496c2cbdd73ab17fc8c140850b4384d3d3c9e67f277b5bc824ba102eebfa08d96abb480dbd715b46b1801938e03a914de2b6eb7da2c11e4f1004ad75d5a55ed3689aefe525dc6834148b2a160b794ff9')
st.sidebar.dataframe(df)
fruit = df["fruit_name"].value_counts()
chart_list = ['Bar graph','Pie chart','Scatter']
select = st.sidebar.selectbox('CHARTS (SELECT ONE)',chart_list)

if select == "Bar graph":
  plt.bar(fruit.index,fruit)
  st.pyplot()

elif select == "Pie chart":
  plt.pie(fruit,labels=fruit.index,autopct = '%.2f%%')
  st.pyplot()

elif select == "Scatter":
  plt.scatter(df["width"],df["height"])
  plt.xlabel("WIDTH")
  plt.ylabel("HEIGHT")
  st.pyplot()
