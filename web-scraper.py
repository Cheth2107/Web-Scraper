import requests
from bs4 import BeautifulSoup

# URL you want to scrape
url = "https://javascript.info/intro"

# Send a GET request to the URL
res = requests.get(url)

# Get the content of the response
content = res.content

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(content, "html.parser")

# Save the parsed HTML content to a file
with open("output.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())

print("Data has been saved to output.html")




#################################################################

https://github.com/CoreyMSchafer/code_snippets/tree/master/BeautifulSoup

from bs4 import BeautifulSoup
import requests

source = requests.get('https://javascript.info/intro').text

soup = BeautifulSoup(source,'lxml')

content = soup.find("div",class_="content")

main = content.get_text()

print(main)

################################################################


import csv
import requests
from bs4 import BeautifulSoup

# Request the webpage
source = requests.get('https://javascript.info/intro').text

# Parse the webpage with BeautifulSoup
soup = BeautifulSoup(source,'lxml')

# Find the 'important__header' and 'important__content' div classes
content = soup.find("div", class_="important__header")
content2 = soup.find("div", class_="important__content")

# Get the text within the 'important__header' and 'important__content' div classes
header_text = content.get_text()
content2_text = content2.get_text()

# Open a CSV file and write the text to it
with open('output.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([header_text])
    writer.writerow([content2_text])


import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('output.csv')

# Print the data
print(df.to_string(index=False))


import csv
import random
from langchain.chains.question_answering import load_qa_chain
from langchain import HuggingFaceHub

# Initialize the language model
llm = HuggingFaceHub(repo_id="sshleifer/distilbart-cnn-12-6", model_hash="sha1:18e56418238a1bede08d643eebd2e196f18599d6", token="<your_huggingface_token>")

# Initialize the QA chain
ng = load_qa_chain(llm)

# Read the CSV file into a list of rows
rows = []
with open('output.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        rows.append(row)

# Extract the named entities from the answers
named_entities = []
for row in rows:
    entities = ng.extract_entities(row['answer'])
    for entity in entities:
        if entity not in named_entities:
            named_entities.append(entity)

# Define a function to generate a random question
def generate_question(named_entities):
    entity = random.choice(named_entities)
    question = f"Can you tell me something about {entity}?"
    return question

# Generate and print 5 random questions
for i in range(5):
    question = generate_question(named_entities)
    print(question)


https://python.langchain.com/docs/use_cases/csv

https://www.blackbox.ai/share/d864aee4-a96e-430d-b38c-4475332acd51

open ai api - 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

hugging face token - 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
