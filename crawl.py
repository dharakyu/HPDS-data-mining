import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import argparse

def get_name(soup):
	name = soup.find(class_='sduiv3-hero-title homepage-title').text
	print(name)
	return name

def get_amenities(soup):
	amenities_block = soup.find(class_="sduiv3-amenities-list")

	if amenities_block == None:
		return []

	amenities = []
	for elem in amenities_block.find_all('li'):
		amenities.append(elem.text.strip())

	print(amenities)
	return amenities

def get_reviews(url, driver):
	reviews_url = url+"reviews"
	driver.get(reviews_url)
	reviews_data = driver.find_elements_by_class_name('chat-block')

	reviews = []
	for element in reviews_data:
		full_review = element.text
		review_text = full_review[full_review.find('\n')+1:]
		reviews.append(review_text)
	print(reviews)
	return reviews


if __name__=="__main__":
	#url = 'https://www.sharedesk.net/spaces/view/6043/cybertech/spaces' 

	parser = argparse.ArgumentParser()
	parser.add_argument("url", help="enter url of workspace")
	args = parser.parse_args()
	url = args.url
	print(url)

	# run webdriver from executable path
	driver = webdriver.PhantomJS(executable_path = '/Users/dharakyu/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')

	# get web page
	driver.get(url)

	time.sleep(2)
	# driver.quit()

	soup = BeautifulSoup(driver.page_source, 'html.parser')

	name = get_name(soup)
	amenities = get_amenities(soup)
	reviews = get_reviews(url, driver)
	



