# Web Content Summarization with OpenAI's GPT-3

This Python script uses OpenAI's GPT-3 language model to summarize the content of a web page. It also includes a function to scrape the content of a given URL using the `requests` and `BeautifulSoup` libraries.

## Usage

To use this script, follow these steps:

1. Clone this repository to your local machine.
2. Add your OpenAI API key to a file called `openaiapikey.txt` in the root directory of the repository.
3. Replace the value of the `url` variable in the script with the URL of the web page you want to summarize.
4. Create a file called `prompt.txt` in the root directory of the repository, and include the following text: `Summarize the following information: <<INFO>>`. This text will be used as the prompt for the GPT-3 language model, with `<<INFO>>` replaced by the scraped content of the web page.
5. Run the script using Python 3: `python3 summarize.py`
6. The summarized content will be saved to a file called `summarycontent.txt` in the root directory of the repository.

## Dependencies

This script requires the following Python libraries to be installed:

- `openai`
- `requests`
- `bs4`

## License

This code is licensed under the MIT license. See the `LICENSE` file for more information.
