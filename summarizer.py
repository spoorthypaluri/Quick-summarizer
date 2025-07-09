from transformers import pipeline

# Load summarizer model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def chunk_text(text, max_chunk_size=800):
    words = text.split()
    chunks = []
    current_chunk = []

    for word in words:
        current_chunk.append(word)
        if len(current_chunk) >= max_chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = []

    # Add remaining words
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

def summarize_text(text):
    chunks = chunk_text(text)
    final_summary = ""

    for chunk in chunks:
        summary = summarizer(chunk, max_length=180, min_length=50, do_sample=False)
        final_summary += summary[0]['summary_text'] + " "

    return final_summary.strip()
