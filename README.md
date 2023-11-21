# movie-blog-automation
![blogger-autom](https://user-images.githubusercontent.com/59218902/220018801-24f25cc9-2a56-4fe8-957c-179355a42fbb.png)

### Blog Automation Project

This project is designed to fetch the `top 250` movies from `IMDb`, search for their corresponding Wikipedia pages, extract the plot and poster image, and finally upload the information to a Blogger account using the `Blogger API`.

## MoviePlotzz

**Website :  https://movieplotzz.blogspot.com/**


![image](https://github.com/pj8912/movie-blog-automation/assets/59218902/f6c19c67-3669-4f22-aeba-bdf0a54efde5)


## Getting Started
These instructions will help you get started with the project.

## Prerequisites

Before getting started with the project, you will need the following:

- A Google account to access the Blogger API
- A valid API key, client credentials to access the Blogger API
- A Python environment with the following packages installed:
    - requests
    - bs4 (BeautifulSoup)
    - wikipedia
    - IMDbPY(Cinemagoer)



## Install

- Clone repo
```
git clone https://github.com/pj8912/movie-blog-automation.git
```

- Install `requirements.txt`


```
pip install -r requirements.txt
```


## Configuration

- Create a project in the Google API Console.
- Enable the Blogger API for your project.
- Create an API key for your project.
- Create OAuth 2.0 Client ID(clientid, client credentials)
- Add `CLIENT_ID` and `CLIENT_SECRET` to `.env` file
- Go to `code-token/` run `get_code_token.py` to generate `access token` that will be used to upload `post` to blogger.
- Add generated `ACCESS_TOKEN` to .env file.

## Start 

1. Run the main.py file to start the project.
```
python main.py
```
2. The project will fetch the top 250 movies from IMDb, search for their corresponding Wikipedia pages, extract the plot and poster image, and finally upload the information to a Blogger account using the Blogger API.

## Support

<a href="https://www.buymeacoffee.com/gjohnpinto" target="_blank" align="center"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>


## Conclusion
This project is a useful tool for anyone looking to extract and upload movie information from IMDb and Wikipedia to a Blogger account. With a few simple steps, you can easily fetch the top 250 movies from IMDb, extract their plots and poster images, and upload them to your Blogger account.
