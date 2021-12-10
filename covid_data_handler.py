"""All the Covid data handling functionality"""

#Import Libraries
import json
import csv
import logging
from uk_covid19 import Cov19API
import pandas
import logging_formatting

#Opening JSON file
f = open('config.json')

#Returns JSON object as a dictionary
data_configuration_json = json.load(f)

#Closing file
f.close()

#Create Logger for this module
logger = logging.getLogger(__name__)

#Define Global Variables
csv_filename = data_configuration_json["csv_filename"]

def parse_csv_data(csv_filename: str) -> list:
    """Returns a list of strings for the rows in the file"""

    #Logging
    logging.info("The parse_csv_data function has been called")

    with open(csv_filename, newline='') as f:
        reader = csv.reader(f)
        covid_csv_data = list(reader)
        return covid_csv_data


def process_covid_csv_data(covid_csv_data: list) -> int:
    """Returns three variables; the number of cases in the last 7 days, the current number
of hospital cases and the cumulative number of deaths"""

    #Logging
    logging.info("The process_covid_csv_data function has been called")

    read_file = pandas.read_csv('nation_2021-10-28.csv')

    #Return the number of cases in the last 7 days
    last7days_cases = read_file.iloc[2:9,6].sum()
    #Return the current number of hospital cases
    current_hosptial_cases = read_file.iloc[0,5]
    #Return the cumulative number of deaths
    total_deaths = read_file.iloc[13,4]
    return [last7days_cases, current_hosptial_cases, total_deaths]

def covid_API_request(location: str = "Exeter", location_type: str = "ltla") -> dict:
    """Returns up-to-date Covid data as a dictionary"""

    #Logging
    logging.info("The covid_API_request function has been called")

    #Construct the value of the filters parameter
    area = [
    f'areaName={location}',
    f'areaType={location_type}'
    ]

    #Construct the value of the structure parameter
    cases_and_deaths = {
    "date": "date",
    "areaName": "areaName",
    "areaCode": "areaCode",
    "newCasesByPublishDate": "newCasesByPublishDate",
    "cumCasesByPublishDate": "cumCasesByPublishDate",
    "newDeaths28DaysByDeathDate": "newDeaths28DaysByDeathDate",
    "cumDeaths28DaysByDeathDate": "cumDeaths28DaysByDeathDate",
    "newCasesByPublishDateRollingSum": "newCasesByPublishDateRollingSum",
    "hospitalCases": "hospitalCases",
    "cumDeaths28DaysByPublishDate": "cumDeaths28DaysByPublishDate"
    }

    #Instantiating the API object
    api = Cov19API(
        filters=area,
        structure=cases_and_deaths,
        latest_by="newCasesByPublishDate"
    )

    #Extract the data
    data = api.get_json()

    return data
