"""This module is responsible for the user interface and the renning of the program"""

#Import Libraries
import sched
import json
from flask import Flask
from flask import render_template
import logging_formatting
import test_covid_news_handling as tcnh
import covid_data_handler as cdh
import covid_news_handling as cnh
import test_covid_data_handler as tcdh
import logging

app = Flask(__name__)

#Create Logger for this module
logger = logging.getLogger(__name__)

#Opening JSON file
j = open('config.json')

#Returns JSON object as a dictionary
data_configuration_json = json.load(j)

#Closing file
j.close()

news = cnh.news_API_request(covid_terms = "Covid COVID-19 coronavirus")
covid_data_exeter = cdh.covid_API_request()
covid_data_england = cdh.covid_API_request(location = data_configuration_json["location"],
                                           location_type = data_configuration_json["location_type"])

@app.route('/')
def redirect():
    """Redirects user to the /index app route"""

    #Logging
    logging.info("The redirect function has been called")

    return rd(url_for('button_responses'))

@app.route('/index')
def run_application():
    """Main function which is responsible for the events produced by the client"""

    #Logging
    logging.info("The run_application function has been called")

    #Perfom Tests
    #Covid Data Handler Tests
    tcdh.test_parse_csv_data()
    tcdh.test_process_covid_csv_data()
    tcdh.test_covid_API_request()
    #Covid News Handling Tests
    tcnh.test_news_API_request()

    news_articles = news['articles']
    cnh.delete_news_article(news_articles)
    return render_template('index.html',
                           title = 'Coronavirus Daily Update',
                           image = 'coronavirus1.jpg',
                           news_articles = news['articles'],
                           location = covid_data_exeter['data'][0]['areaName'],
                           local_7day_infections = 
                           covid_data_exeter['data'][0]['newCasesByPublishDateRollingSum'],
                           nation_location = 
                           covid_data_england['data'][0]['areaName'],
                           national_7day_infections = 
                           covid_data_england['data'][0]['newCasesByPublishDateRollingSum'],
                           hospital_cases = 
                           "Hospital Cases: " + str(covid_data_england['data'][0]['hospitalCases']),
                           deaths_total = "Total Deaths: " + str(covid_data_england['data'][0]['cumDeaths28DaysByPublishDate']))

if __name__ == '__main__':
    app.run()
