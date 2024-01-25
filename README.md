A Streamlit app for loading data into Snowflake ❄️ 
# Snowshovel 

all credits goes to @ sashamitrovich

This a fork of the locally run Stramlit to be run and hosted directly on your Snowflake instance.
To mitigate the lack of support for file uploads, the csv data is pasted into a text box instead. 

* Accepts a CSV file via the File Uploader component
* Creates a Pandas DataFrame from this file
* Uses Snowpark to create and load a table on Snowflake from this DataFrame

## Setup:
* Setup your Streamlit environment, as described here: https://quickstarts.snowflake.com/guide/getting_started_with_snowpark_for_python_streamlit/index.html?index=..%2F..index#1
* Copy and paste the content of the "main.py" into a new Streamlit App.
* Run
* Copy csv data into the text box
* CTRL+ENTER to submit
* Data is loaded into your target schema under the table name "uploaded_data". 


![image](https://github.com/joldenburgSOLITA/snowshovel/assets/119294091/57455a4d-c5c9-4f58-b7b2-02c4e17ff281)
