#import pandas as pd
import numpy as np
import pickle
import streamlit as st
#from PIL import Image

# loading in the model to predict on the data
pickle_in = open('model.pkl', 'rb')
classifier = pickle.load(pickle_in)

def welcome():
    return 'welcome all'

# defining the function which will make the prediction using
# the data which the user inputs
def prediction(gender, stream, intern, cgpa,backlogs):
    prediction = classifier.predict([[stream, stream, intern, cgpa,backlogs]])
    print(prediction)
    return prediction
	

# this is the main function in which we define our webpage
def main():
    # giving the webpage a title
    st.title("Student Placement Predition Application")
    # here we define some of the front end elements of the web page like
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit Student Placement Classifier ML App </h1>
    </div>
    """
	
    # this line allows us to display the front end aspects we have
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)	
    # the following lines create text boxes in which the user can enter
    # the data required to make the prediction
    gender = st.number_input("Enter Gender(Female=0, Male=1)", step=1, value=0)
    stream = st.number_input("Enter Stream(Civil=0, CSE=1, Electronics=2,EnTC=3, IT=4, Mechanical=5)",step=1, value=0)
    intern = st.number_input("Enter Previous Internships",step=1, value=0)
    cgpa = st.number_input("Enter CGPA",step=1, value=0)
    backlogs = st.number_input("Enter backlogs",step=1, value=0)	
    result =""
    # the below line ensures that when the button called 'Predict' is clicked,
    # the prediction function defined above is called to make the prediction
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(gender, stream, intern, cgpa,backlogs)
        print(result)
        if(result==1):
            st.success("'You're Placed")
        else:
            st.success("'You're Not Placed")
            st.success('The output is {}'.format(result))
	
if __name__=='__main__':
    main()
