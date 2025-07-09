import streamlit as st
import requests

# Thay bằng URL ngrok backend của bạn
BACKEND_URL = "https://a3d4033514b1.ngrok-free.app"

menu = {
    "Trang chủ": "home.png",
    "Mục tiêu tác chiến": "sources.png",
    "Kho dữ liệu Tiktok": "feeds.png"
}

st.set_page_config(page_title="TikTok_V486", layout="wide")

st.sidebar.title("TIKTOK VIEW")
selection = st.sidebar.radio("Chọn mục:", list(menu.keys()))

filename = menu[selection]

# Gọi API
response = requests.get(f"{BACKEND_URL}/image/{filename}")

if response.status_code == 200:
    st.image(response.content, width=2000)
else:
    st.error(f"Không tải được ảnh: {response.status_code}")
