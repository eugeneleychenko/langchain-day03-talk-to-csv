import streamlit as st
from langchain.agents import create_csv_agent, create_pandas_dataframe_agent
from langchain.llms import OpenAI
from langchain.agents import AgentType
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import pandas as pd
from io import StringIO



def main():
    load_dotenv()
    st.set_page_config("Ask your CSV Anything!")
    st.title("Ask your CSV Anything!")
    csv_upload = st.file_uploader("Upload your CSV!", type="csv")
    st.write(csv_upload)
    
    
    

    if csv_upload:
            # stringio = StringIO(csv_upload.getvalue().decode("utf-8"))
            question  = st.text_input("What would you like to know about:")
            llm = ChatOpenAI(temperature=0)
            agent = create_csv_agent(
            llm=llm, path=csv_upload.name, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)  # Pass file name to function

            if csv_upload is not None and question != "":
                answer = agent.run(question)
                st.write(answer)
        



if __name__ == '__main__':
    main()