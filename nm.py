#import libraries
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
#matplotlib.use('Agg')
import seaborn as sns 
#Remove Warnings
st.balloons()
st.set_option('deprecation.showPyplotGlobalUse', False)
from PIL import Image 
img = Image.open("download.jpeg")
st.image(img,width=300)
st.title("World Happiness Report 2021")
#import dataset
df = pd.read_csv('world-happiness-report-2021.csv')
#First thirty rows
data = df.head(10)
#Display the table
st.table(data)

#data=pd.read_csv('world-happiness-report-2021.csv')
total_rows=df.shape[0]
#1. the total number of countries in dataset
st.markdown("Total number of countries in dataset:  " + str(total_rows))
st.header("Position of India in the list")
grp1=df.groupby('Country name')
grp1_data=grp1.get_group('India')
st.table(grp1_data)
st.header("Countries with more Social Support")
grp1=data.groupby('Social support')
#grp1_data=grp1.get_group('India')
st.table(grp1.max())
#Displot
st.subheader("Displot showing Social Support")
sns.distplot(df['Social support'])
st.pyplot()
#barplot
st.subheader("Barplot showing Health Life Expectancy")
sns.barplot(x='Country name',y='Explained by: Healthy life expectancy',data=df)
st.pyplot()