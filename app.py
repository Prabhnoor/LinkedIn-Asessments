import requests
import pyperclip
from bs4 import BeautifulSoup
import os
import openai

# Set up the OpenAI API credentials using an API key
openai.api_key = "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"

# Load the HTML file into memory
with open('index.html', 'r') as file:
    html = file.read()

# Create a BeautifulSoup object from the HTML file
soup = BeautifulSoup(html, 'html.parser')

# Find the <body> tag in the HTML file
body_tag = soup.body

# Get the text from the clipboard
clipboard_text = pyperclip.paste()

# Create a new BeautifulSoup object from the clipboard text
new_soup = BeautifulSoup(clipboard_text, 'html.parser')

# Append the new content to the <body> tag
body_tag.append(new_soup)

# Save the updated HTML file
with open('index.html', 'w') as file:
    file.write(str(soup))

# Open the HTML file and read its contents
HTMLFileToBeOpened = open("index.html", "r")
contents = HTMLFileToBeOpened.read()

# Create a BeautifulSoup object from the HTML file contents
soup = BeautifulSoup(contents, 'html.parser')

# Extract the text contents of the HTML file
data=soup.text

# Remove any existing files with the same name as temp.txt and file.txt
os.remove('temp.txt')
os.remove('file.txt')

# Open temp.txt in write mode and write the text contents of the HTML file to it
with open('temp.txt', 'w') as wf:
    data=str(data)    
    wf.write(str(data))

# Create an empty string variable called result
result=''

# Open temp.txt in read mode and iterate over each line in the file
with open('temp.txt', 'r') as file:
    # Check if the line is not empty and add it to the result string variable if it's not
    for line in file:
            if not line.isspace():
                result += line
    
    # Move the file pointer back to the beginning of the file
    file.seek(0)  
    # Open file.txt in write mode and write the result string to it
    with open('file.txt','w') as wf:
        wf.write(result)

# Open file.txt in read mode and read its contents into a variable called text
with open('file.txt', 'r') as f:
    text = f.read()

# Copy the contents of the text variable to the clipboard
pyperclip.copy(text)

# Get the text from the clipboard
text = pyperclip.paste()

# Set up the OpenAI API request
prompt = "I will ask a question and give you four options. Please respond with the correct option. Do not say anything but the answer:\n\n" + text + "\n\n"
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=100,
    n=1,
    stop=None,
    temperature=0.5,
)

# Print the generated text
print(response.choices[0].text)

# Load the HTML file into memory
with open('index.html', 'r') as file:
    html = file.read()

# Create a BeautifulSoup object from the HTML file
soup = BeautifulSoup(html, 'html.parser')

# Find the <body> tag in the HTML file
body_tag = soup.body

# Delete all the contents of the <body> tag
body_tag.clear()

# Save the updated HTML file
with open('index.html', 'w') as file:
    file.write(str(soup))