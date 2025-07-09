import streamlit as st
import requests

# Thay bằng URL ngrok backend của bạn
BACKEND_URL = "https://abc1234.ngrok.io"

menu = {
    "Trang chủ": "home.png",
    "Mục tiêu tác chiến": "sources.png",
    "Kho dữ liệu Tiktok": "feeds.png"
}

st.set_page_config(page_title="Dashboard", layout="wide")

st.sidebar.title("Dashboard")
selection = st.sidebar.radio("Chọn mục:", list(menu.keys()))

filename = menu[selection]

# Gọi API
st.write(f"## {selection}")
response = requests.get(f"{BACKEND_URL}/image/{filename}")

if response.status_code == 200:
    st.image(response.content, use_column_width=True)
else:
    st.error(f"Không tải được ảnh: {response.status_code}")
