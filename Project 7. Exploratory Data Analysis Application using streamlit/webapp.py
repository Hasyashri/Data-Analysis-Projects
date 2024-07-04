# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 19:36:35 2024

@author: habha
"""

# 1. imports
import streamlit as st
import pandas as pd
import seaborn as sns


# 2. Title and Subheader
st.title('Exploratory Data Analysis App')
st.subheader("EDA using Python and Streamlit")

# 3.  Upload Dataset

upload=st.file_uploader("Upload Your Dataset in any Format")
if upload is not None:
    #data=pd.read_csv(upload)
    file_extension = upload.name.split('.')[-1]
    
    if file_extension == 'csv':
        data = pd.read_csv(upload)
    elif file_extension == 'json':
        data = pd.read_json(upload)
    elif file_extension in ['xls', 'xlsx']:
        data = pd.read_excel(upload)
    else:
        st.error("Unsupported file format")
   
   
# 4. Show Dataset
if st.checkbox("Priview Of The Dataset"):
    if st.button("Head"):
        st.write(data.head())
    if st.button("Tail"):
        st.write(data.tail())     
# 5. Check Datatype of Each Columns
if upload is not None:
    if st.checkbox("Check Datatypes of the all columns"):
        st.text("Datatypes of the columns")
        st.write(data.dtypes)
# 6. Find Shape of the Dataset(Number of Rows and Number of Columns)
if upload is not None:
    data_shape=st.radio("What Dimension Do You Want To Check?",('Rows','Columns'))
    
    if data_shape=='Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape=='Columns':
        st.text("Number of Columns")
        st.write(data.shape[1])
# 7. Find Null Values in The Dataset
if upload is not None:
    Null_values=data.isnull().values.any()
    if Null_values==True:
        if st.checkbox("Null Values in the Dataset"):
            sns.heatmap(data.isnull())
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()
        else:
            st.success("The Dataset does not have Null Values, Let's Go to the Next step")
# 8. Find Duplicate Values in the Dataset
if upload is not None:
      test=data.duplicated().any()
      if test==True:
          st.warning("This Dataset contains Duplicated values")
          dup=st.selectbox("Do You Want To Remove Duplicated ValuesArithmeticError)",\
                           ("Select One","Yes","No"))
          if dup=="Yes":
              data=data.drop_duplicates()
              st.text("Duplicated Values from the Dataset are removed")
          if dup=="No":
              st.text("Okay")    
# 9.Get Overall Statistics
if upload is not None:
   if st.checkbox("Summary Of The Dataset Statistics"):
       st.write(data.describe(include='all'))
# 10. About 

if st.button("About This App"):
    st.text("This application to the Exploratory Data Analysis of the uploaded dataset in just few clicks")
    st.text("This app built using Python and Streamlit")
    
# 11. By
if st.button("By"):
    st.success("Hasyashri Upadhyay")