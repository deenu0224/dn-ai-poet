# from dotenv import load_dotenv
# load_dotenv()

import streamlit as st
from langchain_openai.chat_models import ChatOpenAI
chat_model = ChatOpenAI()

st.title("인공지능 시인")
title = st.text_input('시의 주제를 제시해주세요')
if st.button('시 쓰기'):
    if not title:
        st.error("주제를 입력해주세요.")
    else:
        with st.spinner("시를 작성하는 중..."):
            # Generate a poem based on the title
            result = chat_model.predict(title + "에 대한 시를 써줘")
            st.write(result)
        


