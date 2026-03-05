# YouTube Video Summarizer

An AI powered web application that extracts transcripts from YouTube videos and generates clean summaries using a large language model.

---

## Features

* Extracts captions from YouTube videos
* Handles long videos using chunking
* Generates structured bullet point summaries
* Simple Streamlit interface
* Secure API key management using environment variables

---

## Project Structure

```
youtube-video-summarizer/
│
├── app.py
├── transcript.py
├── summarizer.py
├── requirements.txt
├── .env
└── README.md
```

---

## Installation Guide

### 1 Install Python

Make sure Python 3.9 or newer is installed.

Check version:

```
python --version
```

---

### 2 Clone or Create Project Folder

```
youtube-video-summarizer
```

Open it in your editor.

---

### 3 Install Dependencies

Inside the project folder run:

```
pip install -r requirements.txt
```

If you do not have the file yet, install manually:

```
pip install youtube-transcript-api openai streamlit python-dotenv
```

---

### 4 Add Your OpenAI API Key

Create a file named:

```
.env
```

Inside it add:

```
OPENAI_API_KEY=your_api_key_here
```

Do not share this file publicly.

---

## Running The Application

From inside the project folder run:

```
streamlit run app.py
```

Your browser will open automatically.

Paste a YouTube link that has captions enabled and click Summarize.

---

## How It Works

1 User provides YouTube URL
2 Transcript is extracted using youtube transcript api
3 Text is split into chunks for long videos
4 Each chunk is summarized using OpenAI
5 Final summary is combined and displayed

---

## Common Errors

### Transcript Not Found

The video must have captions enabled.

### OpenAI 429 Error

This means your account has no available quota.

Check billing and usage in your OpenAI dashboard.

---

## Security Note

Never upload your `.env` file to GitHub.
Add this to your `.gitignore` file:

```
.env
```

---

## Future Improvements

* Export summary as PDF
* Add timestamped summaries
* Add blog post generator
* Deploy to cloud
* Add authentication
* Convert into Chrome extension

---

## License

This project is for educational purposes.
