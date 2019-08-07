import requests
import json
import googlemaps
import pandas as pd
import csv
import time


def get_cities(filename):
	cities = []
	with open(filename, 'r') as f:
		reader = csv.reader(f)
		for entry in reader:
			cities.append(entry[0])

	cities[0] = "New York"
	return cities

def get_place_ids(cities, api_key):
	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

	place_ids = []

	for city in cities:
		print(city)
		query = "coworking in " + city
		r = requests.get(url + 'query=' + query + '&key=' + api_key)
		x = r.json()
		results = x['results']

	
		for entry in results:
			place_ids.append(entry["place_id"])
			print(entry["place_id"])

		
		curr_x = x
		if('next_page_token' in curr_x):

			next_page_token = curr_x['next_page_token']
			print("next page...")

			time.sleep(2)
			r1 = requests.get(url + 'pagetoken=' + next_page_token + '&key=' + api_key)
			x1 = r1.json()
			results1 = x1['results']
	
			for entry in results1:
				place_ids.append(entry["place_id"])
				print(entry["place_id"])

			curr_x = x1

			if('next_page_token' in curr_x):

				next_page_token = curr_x['next_page_token']
				print("next page...")

				time.sleep(2)
				r2 = requests.get(url + 'pagetoken=' + next_page_token + '&key=' + api_key)
				x2 = r2.json()
				results2 = x2['results']
	
				for entry in results2:
					place_ids.append(entry["place_id"])
					print(entry["place_id"])

	print(len(place_ids))
	as_df = pd.DataFrame(place_ids)
	print(as_df.nunique())
	return place_ids
	

def build_df(place_ids):
	gmaps = googlemaps.Client(key=api_key, queries_per_second=10)

	place_cols = ["place_id", "business_name", "formatted_address", "overall_rating"]
	business_df = pd.DataFrame(columns=place_cols)

	review_cols = ["place_id", "text", "user_rating"]
	review_df = pd.DataFrame(columns=review_cols)

	for id in place_ids:
		result = gmaps.place(place_id=id, fields=["name", "formatted_address", "rating", "review"])["result"]
		if "rating" in result.keys() and "reviews" in result.keys():
			print(result["name"])
			#print(result.keys())

			business_entry = pd.DataFrame([[id, result["name"], result["formatted_address"], result["rating"]]], 
							columns=place_cols)
			business_df = business_df.append(business_entry)

		if "reviews" in result:
			for entry in result["reviews"]:
				#print(entry["text"])
				review_entry = pd.DataFrame([[id, entry["text"], entry["rating"]]], columns=review_cols)
				review_df = review_df.append(review_entry)

	business_and_review_df = pd.merge(business_df, review_df, on='place_id', how='inner')
	business_and_review_df.to_csv("50_cities_google_businesses_and_reviews_updated.csv")
	return business_and_review_df

if __name__=="__main__":
	api_key = "redacted"
	cities = get_cities('cities.csv')
	place_ids = get_place_ids(cities, api_key)
	
	df = build_df(place_ids)
	print(df)

