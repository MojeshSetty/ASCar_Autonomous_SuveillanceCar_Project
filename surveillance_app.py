# surveillance_app.py
import streamlit as st
import requests
from PIL import Image
import cv2
import threading

# ==============================
# CONFIGURATION
# ==============================
st.set_page_config(page_title="Surveillance Car", page_icon="🚗", layout="centered")

# Backend Flask server URL (change IP to your Pi's address)
FLASK_URL = "http://192.168.0.111:8080"

# ==============================
# STREAMLIT UI
# ==============================
st.title("🤖 Autonomous Surveillance Car")
st.markdown("Control and monitor your Raspberry Pi-based surveillance car remotely.")

# --- Video Feed ---
st.subheader("📹 Live Video Feed")
frame_window = st.image([])

# --- Control Buttons ---
st.subheader("🎮 Manual Controls")
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("⬆️ Forward"):
        requests.get(f"{FLASK_URL}/move?dir=forward")

col_left, col_stop, col_right = st.columns([1, 1, 1])
with col_left:
    if st.button("⬅️ Left"):
        requests.get(f"{FLASK_URL}/move?dir=left")
with col_stop:
    if st.button("🛑 Stop"):
        requests.get(f"{FLASK_URL}/move?dir=stop")
with col_right:
    if st.button("➡️ Right"):
        requests.get(f"{FLASK_URL}/move?dir=right")

col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("⬇️ Backward"):
        requests.get(f"{FLASK_URL}/move?dir=backward")

# --- Mode Toggle ---
st.subheader("⚙️ Operation Mode")
mode = st.radio("Select Mode", ["Manual", "Autonomous"], horizontal=True)

if mode == "Autonomous":
    requests.get(f"{FLASK_URL}/mode?set=auto")
    st.success("Autonomous mode activated 🤖")
else:
    requests.get(f"{FLASK_URL}/mode?set=manual")
    st.info("Manual mode enabled 🎮")

# --- System Status ---
st.subheader("📊 System Status")
status_placeholder = st.empty()

# ==============================
# CAMERA STREAM HANDLER
# ==============================
def video_stream():
    cap = cv2.VideoCapture(f"{FLASK_URL}/video_feed")  # Flask MJPEG stream
    while True:
        ret, frame = cap.read()
        if not ret:
            continue
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_window.image(frame)

threading.Thread(target=video_stream, daemon=True).start()

# --- Simulated status (you can replace with API call) ---
st.markdown("---")
st.markdown("🟢 **Connected to Raspberry Pi**")
st.markdown("📡 Status: Monitoring distance and camera feed...")

st.success("System ready ✅")

