## 🎥 Video to Training Module (Q&A Generator)
I’ve developed a small tool that lets you train your bot locally without sharing your video data with any external LLM. You can use this tool by feeding it your own video — it will process the content and generate questions and answers based on that data. You can then use this output to train your local LLM or internal chatbot securely.

## 🎥 Video to Training Module (Q&A Generator)

### 🧠 Overview

This tool helps you **generate training datasets from your own videos — completely locally**.
If you want to train your chatbot or internal LLM without uploading sensitive video data to external servers, this app is for you.

Simply upload a training video (e.g., explainer, meeting recording, tutorial), and the tool will:

1. **Transcribe** the video using [OpenAI Whisper](https://github.com/openai/whisper).
2. **Generate** questions and answers automatically from the transcript.
3. **Export** the generated Q&A as an Excel file for easy training or fine-tuning your local chatbot.

---

### 🚀 Features

* 💻 100% Local — no data leaves your machine.
* 🗣️ Automatic speech-to-text transcription.
* ❓ Auto-generated question-answer pairs.
* 📂 Export ready-to-train Excel file.
* 🎨 Simple and interactive Streamlit interface.

---

### 🧰 Tech Stack

* **Python 3.9+**
* **Streamlit** — for the web interface
* **Whisper** — for transcription
* **Pandas** — for data formatting and export

---

### ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/video-to-training-module.git
cd video-to-training-module

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**Example `requirements.txt`:**

```
streamlit
openai-whisper
pandas
```

---

### ▶️ Run the App

```bash
streamlit run app.py
```

Then open the link shown in your terminal (usually `http://localhost:8501`) in your browser.

---

### 📘 How It Works

1. Upload any `.mp4` training video.
2. The app transcribes the speech into text.
3. It automatically splits the text into meaningful steps.
4. For each step, it generates a **Question** and an **Answer**.
5. You can view and download all Q&A pairs as an Excel file.

---

### 🧩 Output Example

| Step   | Question                  | Answer                                                                  |
| ------ | ------------------------- | ----------------------------------------------------------------------- |
| Step 1 | How to install Streamlit? | To install Streamlit, open your terminal and run pip install streamlit. |
| Step 2 | What is Whisper model?    | Whisper is an automatic speech recognition model developed by OpenAI.   |

---

### 🔒 Why Use This Tool?

✅ Keep your company data **completely private**.
✅ Generate chatbot training data **quickly**.
✅ Works on **any local machine** with Python.
✅ Great for **HR onboarding, training videos, tutorials**, and more.

---

### 📦 Future Enhancements

* [ ] Add support for multiple file formats (e.g., `.wav`, `.mov`)
* [ ] Auto-topic detection and better Q&A phrasing
* [ ] Integration with local LLMs (e.g., Ollama, LM Studio)

