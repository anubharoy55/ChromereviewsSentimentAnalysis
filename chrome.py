# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
import pandas as pd

import streamlit as st

import ChromeReviewsSentimentAnalysisCopyy

def welcome():
    return "HELLO WORLD"

def Analyzer(df):
    
    #putput=classifier.predict(df)
    output=classifier.fileOperations(df)
    print(output)
    return output

def main():
    st.title('Chrome Reviews Sentiment Analysis')
    html_temp='''
    <div style="background-color:tomato;padding:10x">
    <h2 style="color:white;text-align:center;">Streamlit Chrome Reviews Sentiment Analysis>
    </div>
    '''
    st.markdown(html_temp,unsafe_allow_html=True)
    
    
    #uploadFile=
    #uploadedFile = st.file_uploader('fileUploadLabel', type=['csv'],accept_multiple_files=False,key=None)
    
    #st.text("Upload a csv File")
    st.subheader("Dataset")
    data_file = st.file_uploader("Upload a CSV",type=["csv"])
        
    if data_file is not None:

        file_details = {"filename":data_file.name, "filetype":data_file.type,
                        "filesize":data_file.size}

        st.write(file_details)
        df = pd.read_csv(data_file)
        #print(st.dataframe(df))
    #result=fileOperations(df)
    
    #output=[]
    if st.button("Show the Mismatch"):
        output=Analyzer(df)
        st.success('\t\tOUTPUT\n')
        st.dataframe(output)
    if st.button('About'):
        st.text("Thanks for visiting")
        
if __name__=='__main__':
    
    with open('classifier.pkl','rb') as read_file:
        classifier=pickle.load(read_file)
    main()