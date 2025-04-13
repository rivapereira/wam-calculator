# 🎓 UOWD WAM & GPA Calculator

This is a lightweight web app to help University of Wollongong Dubai (UOWD) students calculate their **Weighted Average Mark (WAM)** and **Grade Point Average (GPA)** using just their transcript text.

Built with **Streamlit** and hosted on **Hugging Face Spaces**.

---

## 📌 Features

- ✅ Automatically parses your transcript text (no formatting needed!)
- 📊 Calculates WAM using:  
  `WAM = (subject credit × mark) / total credit`
- 🎓 Calculates GPA using UOWD-style grade conversions:
  - HD = 4.0
  - DI = 3.7
  - CR = 3.0
  - PS = 2.0
  - FL = 0.0
- 🔢 Credit point breakdown for 100, 200, and 300-level subjects
- ☁️ Runs entirely in the browser with no installation needed

---

## 🚀 Try it now

🧠 [Launch the app on Hugging Face Spaces](https://huggingface.co/spaces/rivapereira123/wam-calculator)  
*(Change the link above to your actual space if different)*

---

## 📂 File Structure
├── app.py # Streamlit app with full logic ├── requirements.txt # Python dependencies └── README.md # You are here

## ✍️ Example Transcript Format

Just copy and paste your subject records directly from SOLS — no headers needed!

2025	DXB UG Winter 	Dubai/ On Campus	CSCI203	6	 	 	Enrolled


## 👩🏻‍💻 About the Creator

Made with ❤️ by **Riva Pereira**, a third-year student at UOWD.  
Connect with me on [LinkedIn](https://linkedin.com/in/riva-pereira/)

---

## 📜 License

MIT License – feel free to fork and build your own version!
