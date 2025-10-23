

# streamlit_surveillance_app.py
# Streamlit frontend for Autonomous Surveillance Car
# -----------------------------------------------
# This app provides a web UI that embeds your Raspberry Pi's Flask video feed
# and sends control commands (forward, backward, left, right, stop, set_mode)
# to the Flask server running on the Pi (surveillance_car.py).
#
# IMPORTANT: This Streamlit app does NOT access GPIO, servo, or the camera
# on the Pi directly. It only acts as a remote control and viewer. For this
# to work when hosted on Streamlit Cloud (or GitHub Pages), your Raspberry Pi
# must expose the Flask endpoints to the internet (via reverse proxy / ngrok /
# Tailscale / port forwarding) or the Streamlit app must run on the same LAN.
#
# Requirements (put in requirements.txt):
# streamlit
# requests
# validators

import streamlit as st
import requests
from urllib.parse import urljoin
import validators

st.set_page_config(page_title="Project ASCar", layout="wide")

st.title(" Autonomous Surveillance Car - RGMCET")

# Sidebar: Raspberry Pi base URL (e.g., http://192.168.0.111:8080 or https://<ngrok>.io)
st.sidebar.header("Raspberry Pi / Server Settings")
pi_base = st.sidebar.text_input("Pi Base URL (include http://)", value="http://192.168.0.111:8080")
if not validators.url(pi_base):
    st.sidebar.error("Enter a valid URL including http:// or https://")

# Helper functions
def post_action(path, data=None, timeout=3):
    try:
        url = urljoin(pi_base, path.lstrip('/'))
        resp = requests.post(url, data=data, timeout=timeout)
        return resp.status_code, resp.text
    except Exception as e:
        return None, str(e)

# Top row: Video (left) and Controls (right)
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Live Camera Feed")
    st.markdown("\n")
    # Embed the Flask MJPEG endpoint using an iframe. If the endpoint supports
    # MJPEG in an <img> tag, the iframe will render it. If not, the raw video
    # may not show in some browsers due to CORS; in that case run Streamlit on
    # the same LAN or use a tunnel that supports CORS.
    video_url = urljoin(pi_base, 'video_feed')
    st.info(f"Video URL: {video_url}")
    st.components.v1.iframe(video_url, height=480)

with col2:
    st.subheader("Manual Controls")
    if not validators.url(pi_base):
        st.warning("Enter a valid Pi Base URL in the sidebar to enable controls.")
    else:
        # Control buttons laid out horizontally
        if st.button("Forward", key='fwd'):
            code, text = post_action('/forward')
            st.write(code, text)
        r1c1, r1c2 = st.columns(2)
        with r1c1:
            if st.button("Left", key='left'):
                code, text = post_action('/left')
                st.write(code, text)
        with r1c2:
            if st.button("Right", key='right'):
                code, text = post_action('/right')
                st.write(code, text)
        if st.button("Backward", key='back'):
            code, text = post_action('/backward')
            st.write(code, text)

        st.markdown("---")
        st.subheader("Mode")
        mode = st.selectbox("Select Mode", options=['autonomous', 'manual'])
        if st.button("Set Mode"):
            code, text = post_action('/set_mode', data={'mode': mode})
            st.write(code, text)

        st.markdown("---")
        if st.button("Stop", key='stop'):
            code, text = post_action('/stop')
            st.write(code, text)

# Bottom: Status and Diagnostics
st.markdown("---")
st.subheader("Diagnostics")
col_a, col_b = st.columns(2)
with col_a:
    st.write("**Ping / Status**")
    try:
        r = requests.get(pi_base, timeout=2)
        st.success(f"Server reachable: {r.status_code}")
    except Exception as e:
        st.error(f"Cannot reach server: {e}")

with col_b:
    st.write("**Camera Device**")
    st.markdown("Use `ls /dev/video*` on the Raspberry Pi to check the USB camera device (e.g., /dev/video0)")

st.markdown("---")
st.info("Notes: If you deploy this app to Streamlit Cloud, remember the Streamlit app must be able to reach your Raspberry Pi's Flask endpoints. Use ngrok / Tailscale / a reverse proxy or run the Streamlit instance on the same LAN.")

# Footer: quick deploy instructions
st.markdown("""
## Quick deployment instructions
1. Create a GitHub repo and add this file as `streamlit_app.py`.
2. Add a `requirements.txt` containing:
```
streamlit
requests
validators
```
3. Sign in to Streamlit Community Cloud (https://streamlit.io/cloud) and connect your GitHub repo.
4. Deploy the app. In the app configuration, set `streamlit_app.py` as the main file.

If you want the Streamlit app to access your Pi behind NAT, consider using:
- Tailscale (recommended) — run tailscale on both Pi and a small VM with Streamlit or enable ACLs.
- Ngrok — start an ngrok tunnel on the Pi: `ngrok http 8080` and use the generated URL in the Streamlit sidebar.
""")
