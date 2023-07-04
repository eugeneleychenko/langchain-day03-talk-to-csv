import streamlit as st
from langchain.agents import create_csv_agent, create_pandas_dataframe_agent
from langchain.llms import OpenAI
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import pandas as pd
from io import StringIO
import time



def main():
    load_dotenv()
    st.set_page_config("Ask your CSV Anything!")
    st.title("Ask your CSV Anything!")
    csv_upload = st.file_uploader("Upload your CSV!", type="csv")
    
    # st.write(df)
    
    
    

    if csv_upload:
        # stringio = StringIO(csv_upload.getvalue().decode("utf-8"))
        df = pd.read_csv(csv_upload)
        question  = st.text_input("What would you like to know about:")
        llm = ChatOpenAI(temperature=0, model="gpt-4")
        agent = create_pandas_dataframe_agent(
        llm=llm, df=df, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)  # Pass file name to function

        
        if csv_upload is not None and question != "":
            with st.spinner('Thinking'):
                time.sleep(5)
            answer = agent.run(question)
            with st.spinner('Looking for answers'):
                time.sleep(5)
            st.write(answer)
        



if __name__ == '__main__':
    main()