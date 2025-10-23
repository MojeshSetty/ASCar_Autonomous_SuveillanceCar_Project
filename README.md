


# 🚘 Autonomous Surveillance Car — Streamlit Control Dashboard

An **AI-powered autonomous surveillance system** built using **Raspberry Pi**, **Python**, and **Streamlit**, designed to perform real-time monitoring, remote control, and autonomous navigation.
This project combines **computer vision**, **Flask streaming**, and a **modern Streamlit web interface** for intuitive human–robot interaction.

---

## 🧠 Project Overview

The **Autonomous Surveillance Car** is capable of:

* Detecting and avoiding obstacles using **ultrasonic sensors**
* Capturing and streaming **live video feed** from the Pi Camera
* Operating in both **Manual** and **Autonomous** modes
* Controlling motion (Forward, Backward, Left, Right, Stop) via the web UI
* Displaying **system status** and control logs in real-time

The new **Streamlit-based dashboard** offers a modern, mobile-friendly, and cloud-deployable interface — ideal for remote monitoring.

---

## ⚙️ Tech Stack

| Component     | Technology                                                  |
| ------------- | ----------------------------------------------------------- |
| Hardware      | Raspberry Pi 4, Ultrasonic Sensors, Motor Driver, Pi Camera |
| Backend       | Python, OpenCV, Flask                                       |
| Web Interface | Streamlit                                                   |
| Communication | HTTP/Flask Stream                                           |
| Deployment    | Streamlit Cloud / GitHub                                    |

---

## 🖥️ Features

* 🎥 **Live video feed** from Raspberry Pi camera
* 🎮 **Manual control buttons** (Forward, Backward, Left, Right, Stop)
* 🤖 **Autonomous mode toggle** for self-navigation
* ⚡ **Real-time system status** (camera, sensors, connection, uptime)
* 🌐 **Streamlit web dashboard** with Tailwind-inspired design

---

## 📁 Project Structure

```
Autonomous_Surveillance_Car_Project/
│
├── surveillance_app.py           # Streamlit web interface
├── surveillance_car.py           # Core Raspberry Pi control logic
├── static/                       # CSS, JS, or media files (optional)
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## 🚀 How to Run Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/autonomous-surveillance-car.git
   cd autonomous-surveillance-car
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Raspberry Pi control code**

   ```bash
   python3 surveillance_car.py
   ```

4. **Launch the Streamlit dashboard**

   ```bash
   streamlit run surveillance_app.py
   ```

5. **Open in browser**

   ```
   http://localhost:8501
   ```

---

## ☁️ Deployment

You can deploy the Streamlit dashboard directly on **[Streamlit Cloud](https://share.streamlit.io)** or any web hosting platform linked to your GitHub repository.

---

## 📷 Preview
![Dashboard Preview](preview.png)

---
---
## MY Team 

I am very greatful to my team for being so supportive and encouragment in this project . Here is my Team 
* Sai Pawan Kummari
* Jaya Naveen Singh Bondili
* Bharathi Chantimalla
* And I am also very thankful to my department : HOD Sir Dr. Kishore, and all faculty members and Gopi Sir
---

## 🤝 Contributions

Contributions are welcome!
Feel free to open issues or submit pull requests to improve UI, add sensor integration, or enhance performance.

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and share.

---
