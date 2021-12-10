"""This module is resonsible for covid news handling"""

#Import Libraries
import json
from flask import request
import logging_formatting
import logging
from newsapi import NewsApiClient

#Create Logger for this module
logger = logging.getLogger(__name__)

#Opening JSON file
f = open('config.json')

#Returns JSON object as a dictionary
data_configuration_json = json.load(f)

#Closing file
f.close()

newsapi = NewsApiClient(api_key= data_configuration_json["API-Key"])

def news_API_request(covid_terms = "Covid COVID-19 coronavirus"):
    """Retrieve all articles"""

    #Logging
    logging.info("The news_API_request function has been called")

    all_articles = newsapi.get_everything(q=covid_terms,
                                          sources='bbc-news,the-verge',
                                          domains='bbc.co.uk,techcrunch.com',
                                          from_param='2021-12-01',
                                          language='en',
                                          sort_by='relevancy',
                                          page_size=10
                                          )
    return all_articles

all_articles = news_API_request(covid_terms = "Covid COVID-19 coronavirus")

def delete_news_article(news_articles):
    """Permenantly delete news article fromm feed"""

    #Logging
    logging.info("The delete_news_article has been called")

    text_field = request.args.get('notif')

    for i in range (len(news_articles)):
        if text_field == news_articles[i]['title']:
            del news_articles[i]

            #Log article being deleted
            logging.info("Permenantly deleted news article fromm feed")

            file = open("deleted_news_articles", "a")
            file.write(news_articles[i]['title'])
            file.close()
            return news_articles

def update_news(all_articles):
    """Update atricles in feed"""

    #Log articles being updates
    logging.info("Aticles being updataed")

    new_articles = delete_news_article(all_articles)
    return new_articles
