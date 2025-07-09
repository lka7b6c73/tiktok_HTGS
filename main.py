import streamlit as st
import requests

# Thay bằng URL ngrok backend của bạn
BACKEND_URL = "https://c87126cd32d5.ngrok-free.app"

menu = {
    "Trang chủ": "home.png",
    "Mục tiêu tác chiến": "sources.png",
    "Kho dữ liệu Tiktok": "feeds.png"
}


st.set_page_config(
    page_title="TikTok V486",
    page_icon="https://static.vecteezy.com/system/resources/previews/018/930/574/non_2x/tiktok-logo-tikok-icon-transparent-tikok-app-logo-free-png.png",
    layout="wide"
)

st.sidebar.image(
    "https://static.vecteezy.com/system/resources/previews/018/930/574/non_2x/tiktok-logo-tikok-icon-transparent-tikok-app-logo-free-png.png",
    use_container_width=True
)
st.sidebar.title("TIKTOK VIEW")
selection = st.sidebar.radio("Chọn mục:", list(menu.keys()))

filename = menu[selection]

# Gọi API
response = requests.get(f"{BACKEND_URL}/image/{filename}")
time_resp = requests.get(f"{BACKEND_URL}/time")

if time_resp.status_code == 200:
    capture_time = time_resp.json().get("capture_time", "N/A")
    st.caption(f"📸 Capture at: {capture_time}")
else:
    st.caption("📸 Capture time: N/A")
if response.status_code == 200:
    st.image(response.content, width=2000)
else:
    st.error(f"Không tải được ảnh: {response.status_code}")
