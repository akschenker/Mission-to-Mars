# Mission-to-Mars

In this assignment, I used BeautifulSoup to scrape data from several websites containing Mars news. Different types of data included were images of Mars, tweets about the current Mars weather, a table of Mars facts, and headlines with the latest Mars news. After scraping the data, I stored the data in MongoDB and then loaded it into an HTML file using a Flask/Jinja template that interfaces with Python. Finally, I formatted the HTML using Bootstrap and configured the app such that clicking a button on the webpage would re-scrape and load the data.

## Prerequisites

The Python libraries `flask`, `flask_pymongo`, `BeautifulSoup`, and `splinter` must be installed in order for the code to run. The initial data scraping can be run either in a Jupyter Notebook or in Python.

## Built With

* Python / Jupyter Notebook
* Pandas
* BeautifulSoup
* Flask
* Splinter / Selenium
* MongoDB
* HTML 5.0
* [Bootstrap](https://getbootstrap.com/)

## Authors

* Arley Schenker