import streamlit as st
import pandas as pd
import json
import snowflake.snowpark as snowpark
from snowflake.snowpark import Session, DataFrame
import utils as u

# connect to Snowflake
with open('../creds.json') as f:
    connection_parameters = json.load(f)  
session = Session.builder.configs(connection_parameters).create()


def loadInferAndPersist(file) -> snowpark.DataFrame:
    file_df = pd.read_csv(file)
    snowparkDf=session.write_pandas(file_df,file.name,auto_create_table = True, overwrite=True)
    return snowparkDf

st.header("Grandma data uploader")
file = st.file_uploader("Drop your CSV here", type={"csv"})
if file is not None:
    df= loadInferAndPersist(file)
    st.subheader("Great, your data has been uploaded to Snowflake!")
    
    with st.expander("Technical information"):
        
        u.describeSnowparkDF(df)
        st.write("Data loaded to Snowflake:")
        st.dataframe(df)
    
 