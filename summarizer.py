import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def chunk_text(text, chunk_size=3000):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield " ".join(words[i:i + chunk_size])

def summarize_text(text):
    summaries = []

    for chunk in chunk_text(text):
        prompt = f"""
        Summarize this YouTube transcript clearly in bullet points:

        {chunk}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that summarizes text clearly."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        summaries.append(response.choices[0].message.content)

    combined_summary = "\n".join(summaries)

    final_prompt = f"""
    Combine these summaries into one clean final summary:

    {combined_summary}
    """

    final_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Create a clean final structured summary."},
            {"role": "user", "content": final_prompt}
        ],
        temperature=0.3
    )

    return final_response.choices[0].message.content