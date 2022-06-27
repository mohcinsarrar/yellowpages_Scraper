<div id="top"></div>
<div align="center">
  <h1 align="center">Yellow Pages Scraper</h1>
</div>

is a simple and functional solution to extract data from [yellowpages.com](https://www.yellowpages.com). The program carefully processes the pages from the yellowpages website, saving their data on your computer, with this program you can information for Local businesses, like name, phone, adresse and website
<br>This program built with the python Requests and BeautifulSoup

## Requirements

- Python 3.8
- BeautifulSoup 4

<!-- GETTING STARTED -->
## Installation

1. Clone the repo
   ```sh
   git clone https://github.com/mohcinsarrar/yellowpages_Scraper.git
   ```
2. Install BeautifulSoup
   ```sh
   pip install beautifulsoup4
   ```

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

to start extract Local businesses from yellowpages, go to the project directory, and use this command
  ```sh
     python scraper.py -q "coffee shops" -g "chicago" -l 30 -f "out.csv"
  ```
- "coffee shops" is the search query
- "chicago" is the search geo location
- "out.csv" is the file name where the data stored



<p align="right">(<a href="#top">back to top</a>)</p>
