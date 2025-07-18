import os
import json
import subprocess
import requests
import google.generativeai as genai

# Config
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
model = None

def init_gemini():
    global model
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-pro')

def generate_outline(topic, words):
    prompt = f"""
    Create a professional book outline for: {topic}
    Include:
    - 5 title suggestions
    - 3 subtitle options
    - Full Table of Contents with chapters & subchapters
    - Suggested word count per chapter (total {words} words)
    Return JSON structure.
    """
    response = model.generate_content(prompt)
    with open("outline.json", "w") as f:
        f.write(response.text)
    return json.loads(response.text)

def research_chapter(title):
    prompt = f"""
    Provide research for chapter: {title}
    Include:
    - 5 key facts
    - 2 real-world examples
    - 3 credible sources
    Return JSON format.
    """
    response = model.generate_content(prompt)
    return json.loads(response.text)

def write_chapter(title, research_notes):
    prompt = f"""
    Write a complete chapter titled "{title}" using:
    Research Notes: {research_notes}
    Structure:
    - Intro
    - Main Content with subheadings
    - Examples & Data
    - Key Takeaways
    Style: Professional & engaging.
    """
    response = model.generate_content(prompt)
    os.makedirs("chapters", exist_ok=True)
    path = f"chapters/{title.replace(' ', '_')}.md"
    with open(path, "w") as f:
        f.write(response.text)
    return path

def compile_book():
    subprocess.run("cat chapters/*.md > final_book.md", shell=True)

def export_formats():
    subprocess.run("pandoc final_book.md -o final_book.pdf", shell=True)
    subprocess.run("pandoc final_book.md -o final_book.epub", shell=True)

def generate_audiobook():
    with open("final_book.md", "r") as f:
        text = f.read()
    url = "https://api.elevenlabs.io/v1/text-to-speech/YOUR_VOICE_ID"
    headers = {"xi-api-key": ELEVENLABS_API_KEY, "Content-Type": "application/json"}
    payload = {"text": text[:5000], "voice_settings": {"stability": 0.7, "similarity_boost": 0.8}}
    response = requests.post(url, headers=headers, json=payload)
    with open("audiobook.mp3", "wb") as f:
        f.write(response.content)

def run_pipeline(topic, words, audiobook, export_formats_list):
    init_gemini()
    outline = generate_outline(topic, words)
    for chapter in outline.get("chapters", []):
        title = chapter.get("title")
        research = research_chapter(title)
        write_chapter(title, research)
    compile_book()
    export_formats()
    if audiobook == "yes":
        generate_audiobook()
    print("✅ BookForge Pro: All steps completed!")
