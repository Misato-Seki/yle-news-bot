from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    summary = summarizer(text, max_length=120, min_length=80, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    text = input("Enter the text to summarize: ")
    summary = summarize_text(text)
    print(summary)


# from openai import OpenAI
# import os
# from dotenv import load_dotenv

# # Set OpenAI API key
# load_dotenv()
# my_api_key = os.getenv('OPENAI_API_KEY')

# client = OpenAI(api_key=my_api_key)

# def summarize_text(text):
#     prompt = f"Summarize the following text:\n\n{text}\n\nSummary:"
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "user", "content": prompt}
#         ],
#         temperature=0.5,
#         max_tokens=300
#     )
#     return response.choices[0].message['content'].strip()

# if __name__ == "__main__":
#     text = input("Enter the text to summarize: ")
#     summary = summarize_text(text)
#     print(summary)