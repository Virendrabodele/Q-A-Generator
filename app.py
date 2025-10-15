import streamlit as st
import whisper
import pandas as pd

# Load Whisper model (tiny / base / small / medium / large)
model = whisper.load_model("base")

st.title("🎥 Video to Training Module (Q&A Generator)")

# File uploader
uploaded_file = st.file_uploader("Upload your training video (MP4)", type=["mp4"])

if uploaded_file:
    st.video(uploaded_file)

    # Save uploaded video temporarily
    with open("temp_video.mp4", "wb") as f:
        f.write(uploaded_file.read())

    st.info("⏳ Transcribing video...")
    result = model.transcribe("temp_video.mp4")
    transcript = result["text"]

    st.success("✅ Transcription Completed!")
    st.text_area("Transcript", transcript, height=300)

    # Split transcript into sentences/steps
    steps = transcript.split(". ")
    qa_data = []

    for i, step in enumerate(steps, 1):
        step = step.strip()
        if not step:
            continue

        # Create question from the first few words
        words = step.split()
        if len(words) > 6:
            question = " ".join(words[:6]) + "?"
        else:
            question = step + "?"

        qa_data.append({
            "Step": f"Step {i}",
            "Question": question,
            "Answer": step
        })

    # Convert to DataFrame
    df = pd.DataFrame(qa_data)
    st.dataframe(df)

    # Export to Excel
    df.to_excel("Training_Module.xlsx", index=False)
    with open("Training_Module.xlsx", "rb") as f:
        st.download_button("📥 Download Training Module (Excel)", f, file_name="Training_Module.xlsx")
