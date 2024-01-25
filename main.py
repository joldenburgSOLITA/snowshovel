import streamlit as st
import pandas as pd
import random
import io
import snowflake.snowpark as snowpark
from snowflake.snowpark.context import get_active_session
import snowflake.snowpark.types as T

# Use the active Snowflake session
session = get_active_session()

# Function to describe the Snowpark DataFrame
def describeSnowparkDF(snowpark_df: snowpark.DataFrame):
    st.write("Here's some stats about the loaded data:")
    numeric_types = [T.DecimalType, T.LongType, T.DoubleType, T.FloatType, T.IntegerType]
    numeric_columns = [c.name for c in snowpark_df.schema.fields if type(c.datatype) in numeric_types]

    # Get categorical columns
    categorical_types = [T.StringType]
    categorical_columns = [c.name for c in snowpark_df.schema.fields if type(c.datatype) in categorical_types]

    st.write("Relational schema:")
    columns = [c for c in snowpark_df.schema.fields]
    st.write(columns)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write('Numeric columns:', numeric_columns)
    with col2:
        st.write('Categorical columns:', categorical_columns)
    
    # Calculate statistics for the dataset
    st.dataframe(snowpark_df.describe().sort('SUMMARY'), use_container_width=True)

# Function to load and persist data
def loadInferAndPersist(csv_content: str) -> snowpark.DataFrame:
    try:
        # Attempt to parse the CSV content
        file_df = pd.read_csv(io.StringIO(csv_content))
        snowpark_df = session.write_pandas(file_df, "uploaded_data", auto_create_table=True, overwrite=True)
        return snowpark_df
    except Exception as e:
        st.error(f"Failed to parse CSV: {e}")
        return None

bowling_gifs = [
    "https://media.tenor.com/ZvLM36xOKVsAAAAM/amf-animation.gif",
    "https://media.tenor.com/a9zjShK0KFQAAAAM/bowling-strike.gif",
    "https://media.tenor.com/lM-JzbAJ_mUAAAAM/bowling-bowler.gif",
    "https://media.tenor.com/d0peeTKTX4YAAAAM/bowling-ball.gif"
    # Add more URLs as needed
]

st.header("Data uploader")
csv_content = st.text_area("Paste your CSV content here")

if csv_content:
    df = loadInferAndPersist(csv_content)
    if df is not None:
        st.subheader("Great, your data has been uploaded to Snowflake!")
        
        # Display a random bowling alley GIF
        selected_gif = random.choice(bowling_gifs)
        st.image(selected_gif, caption="Success!")

        with st.expander("Technical information"):
            # Describe the Snowpark DataFrame
            describeSnowparkDF(df)
            st.write("Data loaded to Snowflake:")
            st.dataframe(df)
