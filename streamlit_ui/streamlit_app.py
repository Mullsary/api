import streamlit as st
import requests

API_URL = "http://api:8000"

st.title("Сокращатель ссылок")


with st.form("create"):
    long_url = st.text_input("Длинная ссылка:")
    submitted = st.form_submit_button("Создать короткую")
    
    if submitted and long_url:
        resp = requests.get(f"{API_URL}/link", params={"link": long_url})
        if resp.status_code == 200:
            short = resp.json()["link"]
            st.success(f"Короткая ссылка: {short}")
            st.markdown(f"[Перейти]({short})")
        else:
            st.error("Ошибка")

