import openai
import os
import requests
from bs4 import BeautifulSoup

####################


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


def save_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)


openai.api_key = open_file('../openaiapikey.txt')
####################


def gpt_3(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=600,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    text = response['choices'][0]['text'].strip()
    return text

# scrape content function


def scrape_content(url):
    # fetch content
    page_content = requests.get(url)
    # parse scraped content
    soup = BeautifulSoup(page_content.text, 'html.parser')
    # extract text from page
    content = soup.get_text()
    # remove white space
    content = content.strip()

    return content


# find a url to scrape
url = 'insert your url here'

# run scrape function
webinfo = repr(scrape_content(url))
save_file("webcontent.txt", webinfo)
print(webinfo)

# summarize content
output = open_file("prompt.txt").replace('<<INFO>>', webinfo)
output2 = gpt_3(output)
print(output2)
save_file("summarycontent.txt", output2)
