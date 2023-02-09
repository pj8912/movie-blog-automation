# wiki-blog-automation
Blogging Automation Project

IMDb Top 250 Movie Plot Scraper & Poster Uploader
This project is designed to fetch the top 250 movies from IMDb, search for their corresponding Wikipedia pages, extract the plot and poster image, and finally upload the information to a Blogger account using the Blogger API.

## Getting Started
These instructions will help you get started with the project.

## Prerequisites

Before getting started with the project, you will need the following:

- A Google account to access the Blogger API
- A valid API key, client id and client credentials to access the Blogger API
- A Python environment with the following packages installed:
    - requests
    - bs4 (BeautifulSoup)
    - wikipedia
    - IMDbPY(Cinemagoer)



## Installing

- Clone the repository to your local machine.

`git clone https://github.com/<your-username>/imdb-top-250-movie-plot-scraper-poster-uploader.git`

- Install the required packages.

`pip install -r requirements.txt`


## Configuration

- Create a project in the Google API Console.
- Enable the Blogger API for your project.
- Create an API key for your project.
- Create OAuth 2.0 Client ID(clientid, client credentials)
- Add `CLIENT_ID` and `CLIENT_SECRET` to `.env` file
- Go to `code-token/` run `get_code_token.py` to generate `access token` that will be used to upload `post` to blogger.
- Add generated `ACCESS_TOKEN` to .env file.

## Usage

1. Run the main.py file to start the project.

` python main.py`


2. The project will fetch the top 250 movies from IMDb, search for their corresponding Wikipedia pages, extract the plot and poster image, and finally upload the information to a Blogger account using the Blogger API.


## Conclusion


This project is a useful tool for anyone looking to extract and upload movie information from IMDb and Wikipedia to a Blogger account. With a few simple steps, you can easily fetch the top 250 movies from IMDb, extract their plots and poster images, and upload them to your Blogger account.