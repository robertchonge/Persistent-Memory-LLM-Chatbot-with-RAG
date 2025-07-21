from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_text(text, max_length=150):
    return summarizer(text, max_length=max_length, min_length=30, do_sample=False)[0]['summary_text']
