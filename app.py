import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="👨‍⚕️")

# Load the saved models safely
def load_model(file_path):
    try:
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        st.error(f"Error loading model {file_path}: {e}")
        return None

# Use relative paths or ensure paths exist
base_path = r"D:\Amarjeet Admission\2 Year\4th semester\Internship project\training_models"

diabetes_model = load_model(os.path.join(base_path, "diabetes_model.sav"))
heart_disease_model = load_model(os.path.join(base_path, "heart_disease_model.sav"))
parkinsons_model = load_model(os.path.join(base_path, "parkinsons_model.sav"))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Prediction of Disease Outbreak System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction'],
                           menu_icon=['activity', 'heart', 'person'],
                           default_index=0)

# Helper function to convert input safely
def safe_float_conversion(value):
    try:
        return float(value)
    except ValueError:
        return None

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')

    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    with col2:
        Age = st.text_input('Age')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [safe_float_conversion(x) for x in user_input]

        if None in user_input:
            st.error("Please enter valid numerical values for all fields.")
        elif diabetes_model:
            diab_prediction = diabetes_model.predict([user_input])
            diab_diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
            st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.subheader('Heart Disease Prediction')

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex (0: Female, 1: Male)')
    with col3:
        cp = st.text_input('Chest Pain Type')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholesterol (mg/dl)')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl (1: Yes, 0: No)')
    with col1:
        restecg = st.text_input('Resting ECG Results')
    with col2:
        thalach = st.text_input('Max Heart Rate Achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina (1: Yes, 0: No)')
    with col1:
        oldpeak = st.text_input('ST Depression Induced by Exercise')
    with col2:
        slope = st.text_input('Slope of the Peak Exercise ST Segment')
    with col3:
        ca = st.text_input('Major Vessels Colored by Fluoroscopy')
    with col1:
        thal = st.text_input('Thal (0: Normal, 1: Fixed Defect, 2: Reversible Defect)')

    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [safe_float_conversion(x) for x in user_input]

        if None in user_input:
            st.error("Please enter valid numerical values for all fields.")
        elif heart_disease_model:
            heart_prediction = heart_disease_model.predict([user_input])
            heart_diagnosis = 'The person has heart disease' if heart_prediction[0] == 1 else 'The person does not have heart disease'
            st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.subheader("Parkinson's Disease Prediction")

    col1, col2, col3, col4, col5 = st.columns(5)
    features = ['name','MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)', 'MDVP:Jitter(Abs)',
                'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP', 'MDVP:Shimmer', 'MDVP:Shimmer(dB)',
                'Shimmer:APQ3', 'Shimmer:APQ5', 'MDVP:APQ', 'Shimmer:DDA', 'NHR',
                'HNR', 'RPDE', 'DFA', 'spread1', 'spread2', 'D2', 'PPE']

    inputs = []
    for i, feature in enumerate(features):
        col = [col1, col2, col3, col4, col5][i % 5]
        inputs.append(col.text_input(feature))

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        user_input = [safe_float_conversion(x) for x in inputs]

        if None in user_input:
            st.error("Please enter valid numerical values for all fields.")
        elif parkinsons_model:
            parkinsons_prediction = parkinsons_model.predict([user_input])
            parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
            st.success(parkinsons_diagnosis)

# Footer Section
import streamlit as st

def set_bg_from_url():
    footer = """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            
            color: white;
            text-align: center;
            padding: 10px 0;
        }
        .footer a {
            color: white;
            text-decoration: none;
            margin: 0 10px;
        }
        .footer svg {
            vertical-align: middle;
        }
    </style>
    <footer class="footer">
        <p style="font-size:1.1rem;">
            Made by <strong>Amarjeet Usnale</strong>
        </p>
    </footer>
    """
    
    st.markdown(footer, unsafe_allow_html=True)

# Call the function to display the footer
set_bg_from_url()

    
