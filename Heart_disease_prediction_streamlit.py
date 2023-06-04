import  pickle
import streamlit as st
from streamlit_option_menu import option_menu


model = pickle.load(open("Heart_disease_model.pkl","rb"))

st.title('Heart disease prediction using a Machine learning model')
st.header('Description:')
st.write('Welcome to the Heart Disease Predictor, this an interactive application built using Streamlit and powered by a machine learning model. This application aims to assist in the early detection and prediction of heart disease, enabling users to assess their cardiovascular health and make informed decisions regarding their well-being.')
st.header('About ML model')
st.write('The machine learning model is build using Logistic regression algorithm(a popular and effective machine learning algorithm for binary classification tasks.). The model is trained and tested using a kaggle dataset, which contains more than 1000 datas and finally model is build with 85% accuracy.')
st.write('Note: The Heart Disease Predictor is not intended to replace professional medical advice or diagnosis. Always consult with a healthcare professional for accurate assessment and guidance regarding your heart health.')

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Heart Disease Prediction System',
                          ['Predict your disease now...'],
                          default_index=0)
    st.write('Github link:')
    st.markdown('https://github.com/JayaKrishanS/Heart-Disease-Prediction-using-a-Machine-Learning-Model-and-Streamlit-Application..git')
    
                 
# Heart Disease Prediction Page
if (selected == 'Predict your disease now...'):
    
    # page title
    st.header('Kindly enter the details for prediction')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age', value=0, step=1, format="%d" )
        
    with col2:
        gender = st.selectbox('Sex',('Male','Female'))
        if gender == 'Male':
            sex = 1
        else:
            sex = 0
        
    with col3:
        chest_pain = st.selectbox('Chest pain type',('Typical angina','Atypical angina','Non-anginal pain','Asymptomatic'))
        if chest_pain == 'Typical angina':
            cp = 0
        elif chest_pain == 'Atypical angina':
            cp = 1
        elif chest_pain == 'Non-anginal pain':
            cp = 2
        else:
            cp = 3
        
    with col1:
        trestbps = st.number_input('Resting Blood Pressure level', value=0, step=1, format="%d" )
        
    with col2:
        chol = st.number_input('Serum Cholestoral level', value=0, step=1, format="%d" )
        
    with col3:
        blood_sugar = st.selectbox('Fasting Blood Sugar level > 120 mg/dl',('Yes','No'))
        if blood_sugar == 'Yes':
            fbs = 1
        else:
            fbs = 0
        
    with col1:
        resting_electro = st.selectbox('Resting Electrocardiographic results',('Normal','ST-T wave abnormality','Left ventricular hypertrophy'))
        if resting_electro == 'Normal':
            restecg = 0
        elif resting_electro == 'ST-T wave abnormality':
            restecg = 1
        else:
            restecg = 2
        
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved', value=0, step=1, format="%d" )
        
    with col3:
        pain = st.selectbox('Any pain during physical activity?',('Yes','No'))
        if pain == 'Yes':
            exang = 1
        elif pain == 'No':
            exang = 0

    with col1:
        oldpeak = st.number_input('ST depression rate induced by exercise', value=0, step=1, format="%d" )
        
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment', value=0, step=1, format="%d" )
        
    with col3:
        ca = st.number_input('How many Major vessels colored by flourosopy', value=0, step=1, format="%d" )
        
    with col1:
        thallium = st.selectbox('Thallium stress test result',('Normal','Fixed defect','Reversable defect'))
        if thallium == 'Normal':
            thal = 1
        elif thallium == 'Fixed defect':
            thal = 2
        else:
            thal = 3        
        
    # creating a button for Prediction
heart_diagnosis = ''
if st.button('Heart Disease Test Result'):
    heart_prediction = model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
    if (heart_prediction[0] == 1):
      heart_diagnosis = 'The person is having heart disease'
    else:
      heart_diagnosis = 'The person does not have any heart disease'
    
st.success(heart_diagnosis)
