# from openai import OpenAI
from dotenv import load_dotenv
import openai
import os

load_dotenv('.env.local')
api_key = os.getenv('OPENAI_API_KEY')

openai.api_key_path = api_key

def analyze_text(text_to_analyze):

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant and you give answers in a list. People generally ask about text and books."},
            {"role": "user", "content": "Now, about this following text: " + text_to_analyze}
        ]
    )
    analysis = response['choices'][0]['message']['content']
    return analysis

 


def read_text_from_files(root_dir):
    text_data = ""
    for company_dir in os.listdir(root_dir):
        company_path = os.path.join(root_dir, company_dir)
        if os.path.isdir(company_path):
            for year_dir in os.listdir(company_path):
                year_path = os.path.join(company_path, year_dir)
                if os.path.isdir(year_path):
                    for subdir, _, files in os.walk(year_path):
                        for filename in files:
                            if filename == "full-submission.txt":
                                file_path = os.path.join(subdir, filename)
                                with open(file_path, 'r') as file:
                                    text_data += file.read() + "\n"
    return text_data

# Example usage
root_directory = "./filings/sec-edgar-filings"
text_data = read_text_from_files(root_directory)
print("Insight:", analyze_text(text_data))