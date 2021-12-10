---
# README
Contents List:

+ Title
+ Introduction
+ Prerequisites
+ Installation
+ Getting started tutorial
+ Testing
+ Developer documentation
+ Details

---

## Title
Project Name: ECM1400 Continuous Assessment

---

## Introduction
This purpose of this project is to implement a simple personalised covid dashboard. It can display the current levels of coronavirus cases in a specified area, as well as cases, hospitalisations and total deaths for a specified nation. It can also provide a list of current news articles related to coronavirus.

---

## Prerequisites
This project utilised the Python version 3.10.0.

Here is the link to download Python:
[https://www.python.org/downloads/](https://www.python.org/downloads/)

---

## Installation
You will need to install some external packages:

Flask

        { pip install Flask }
UK Covid API

        { pip install uk-covid19 }
News API

        { pip install newsapi-python }

---

## Getting started tutorial
Firstly you must create an account with the News API and create your own key. Enter it in the config file where it is stated "Enter API Key Here".

After starting the program, you may access the program by going to the address http://127.0.0.1:5000/index on a browser.

In order to customise the program to display the statistics for your given area, you can access the config file and change the values for the keys "location" and "location_type".

---

## Testing
The tests has been placed in the modules called test_covid_data_handler and test_covid_news_handling. These will be called when the webpage is refreshed by the client.

---

## Details
Author: Joshua Weaver

Link to GitHub Page: https://github.com/Joshua-Weaver1/ECM1400-Continuous-Assessment

Licence: MIT Licence