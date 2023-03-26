#Project Description#
This Python script scrapes content from a given URL, saves it to a file, and then uses OpenAI's GPT-3 to summarize the content. The summarized content is then saved to a separate file.

##Dependencies##
The following Python packages are required to run this script:

_openai_
_os_
_requests_
_beautifulsoup4_

##Installation##
Clone the repository to your local machine.
Install the required Python packages using pip: pip install -r requirements.txt.
Add your OpenAI API key to a text file named openaiapikey.txt in the root directory of the repository.
Usage
Open the Python script in a code editor.
Replace the url variable with the URL you want to scrape.
Replace the contents of the prompt.txt file with your desired prompt for summarization.
Run the Python script.
The scraped content will be saved to a file named webcontent.txt, and the summarized content will be saved to a file named summarycontent.txt.
