import joblib
import pandas as pd
import streamlit as st

tree_model = joblib.load("model/housing_model_tree.pkl")

st.write("""
# Housing Price Prediction App
This app predicts the **median house value** in California based on various features.
""")

st.sidebar.header('User Input Features')

longitude =  st.sidebar.slider('longitude', -180.0, 180.0, -122.23)
latitude = st.sidebar.slider('latitude', -90.0, 90.0, 37.88)
housing_median_age = st.sidebar.slider('housing_median_age', 0, 100, 41)
total_rooms = st.sidebar.slider('total_rooms', 0, 10000, 880)
total_bedrooms = st.sidebar.slider('total_bedrooms', 0, 5000, 129)
population = st.sidebar.slider('population', 0, 50000, 322)
households = st.sidebar.slider('households', 0, 5000, 126)
median_income = st.sidebar.number_input('median_income', min_value=0.0,value=40.0, step=1.0)
ocean_proximity = st.sidebar.selectbox('ocean_proximity', ('NEAR BAY', 'INLAND', '<1H OCEAN', 'NEAR OCEAN', 'ISLAND'))

data = {
    'longitude': longitude,
    'latitude': latitude,
    'housing_median_age': housing_median_age,
    'total_rooms': total_rooms,
    'total_bedrooms': total_bedrooms,
    'population': population,
    'households': households,
    'median_income': median_income,
    'ocean_proximity': ocean_proximity
}
features = pd.DataFrame(data, index=[0])

result = tree_model.predict(features)

st.write('User Input Features:')
st.write(features)

st.metric(label='Predicted Median House Value ($)', value=f'{result[0]:,.2f}')

