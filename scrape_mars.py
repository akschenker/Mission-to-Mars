# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd
from time import sleep

def scrape():
    mars_results = {}
    # Mars news scraping

    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)

    news_url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(news_url)

    while not browser.is_element_present_by_tag("li", wait_time=5):
        pass

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    # print(soup.prettify())

    news_title = soup.find("li", class_="slide").find("div", class_="content_title").text
    news_p = soup.find("li", class_="slide").find("div", class_="article_teaser_body").text

    mars_results["news_title"] = news_title
    mars_results["news_p"] = news_p

    # Featured image url scraping

    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    featured_img_base = "https://www.jpl.nasa.gov"
    featured_img_url_raw = soup.find("div", class_="carousel_items").find("article")["style"]
    featured_img_url = featured_img_url_raw.split("'")[1]
    featured_img_url = featured_img_base + featured_img_url

    mars_results["featured_img_url"] = featured_img_url

    # Mars weather tweet scraping

    weather_twitter_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(weather_twitter_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    tweets = soup.find("div", class_="stream").find("ol").find_all("li", class_="js-stream-item")
    for tweet in tweets:
        tweet_text = tweet.find("div", class_="js-tweet-text-container").text
        if "Sol " in tweet_text:
                mars_weather = tweet_text.strip()
                break

    mars_results["mars_weather"] = mars_weather

    # Mars facts scraping

    facts_url = "https://space-facts.com/mars/"
    tables = pd.read_html(facts_url)

    facts_df = tables[0]
    facts_df.columns = ["Fact","Value"]

    # get rid of trailing colon
    facts_df["Fact"] = facts_df["Fact"].str[:-1]
    facts_df = facts_df.set_index("Fact")
    facts_df

    facts_html_table = facts_df.to_html()
    facts_html_table = facts_html_table.replace('\n', '')
    
    mars_results["facts_html_table"] = facts_html_table

    # Mars hemispheres photo scraping

    base_hemisphere_url = "https://astrogeology.usgs.gov"
    hemisphere_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(hemisphere_url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    
    hemisphere_image_urls = []

    links = soup.find_all("div", class_="item")

    for link in links:
        img_dict = {}
        title = link.find("h3").text
        next_link = link.find("div", class_="description").a["href"]
        full_next_link = base_hemisphere_url + next_link
        
        browser.visit(full_next_link)
        
        pic_html = browser.html
        pic_soup = BeautifulSoup(pic_html, 'html.parser')
        
        url = pic_soup.find("img", class_="wide-image")["src"]

        img_dict["title"] = title
        img_dict["img_url"] = base_hemisphere_url + url
        
        hemisphere_image_urls.append(img_dict)

    mars_results["hemisphere_image_urls"] = hemisphere_image_urls

    return mars_results