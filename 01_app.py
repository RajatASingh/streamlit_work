import pandas as pd
import numpy as np
import plotly.express as ppx
import streamlit as st

st.header('Load & Analyse')
st.markdown('This app will give you flexibility to upload the dataset and work with it withour writting a code')

# Create a file uploader widget
uploaded_file = st.file_uploader("Choose a csv file", type="csv")

# If a file is uploaded
if uploaded_file is not None:
    # Read the file contents into a Pandas DataFrame
    df = pd.read_csv(uploaded_file)

    # Display the DataFrame
    rows = st.number_input('Give number of rows you want to see from the dataset' , value= 0 , step=1)
    st.write(df.head(rows))
    st.write('datatype of column\n',df.dtypes)


# Get the list of columns in the dataframe
columns = list(df.columns)

# Create a selectbox for the columns
selected_column = st.selectbox('Select a column', columns)

# Get the list of data types
data_types = ['int', 'float', 'str']

# Create a selectbox for the data types
selected_data_type = st.selectbox('Select a data type', data_types)

# Convert the data in the selected column to the selected data type
if selected_data_type == 'int':
    df[selected_column] = df[selected_column].apply(int)
elif selected_data_type == 'float':
    df[selected_column] = df[selected_column].apply(float)
elif selected_data_type == 'str':
    df[selected_column] = df[selected_column].apply(str)

# Display the dataframe with the updated data type
st.write(df.head(2))

st.markdown('**Make a chart based on requirement**')
x_axis = st.selectbox('select a column name to set on x_axis', df.columns)
y_axis = st.selectbox('select a column name to set on y_axis', df.columns)

chart_types = ['Bar chart', 'Line chart']
selected_chart_type = st.selectbox('Select a chart type', chart_types)

# Display the selected chart
if selected_chart_type == 'Bar chart':
    st.bar_chart(data= df , x= x_axis , y= y_axis )
elif selected_chart_type == 'Line chart':
    st.line_chart(data= df , x= x_axis , y= y_axis )
