# HPDS-data-mining
Data mining component of Stanford's Hybrid Physical + Digital Spaces project

We are seeking to study the effect of features of indoor spaces on human wellbeing in a large-scale, systematic manner.
To this end, we are extracting build features and proxies for wellbeing from web datasets. 

# Python Notebooks:
* load_Yelp_data.ipynb
Takes two csv files (a table of businesses and a table of reviews for these businesses) and merges them into one Pandas table. It only includes businesses that are tagged as Shared Office Spaces, Libraries or Internet Cafe.

* tag_reviews.ipynb
This script is used to add tags to reviews that contain words from provided categorized dictionary. It generates a file containing a table with additional boolean columns for each tag. The file also includes a few queries to get useful statistics from the generated tags.

* manual_analysis.ipynb
This script is used to draw random samples from the dataset of specific sizes and tags to be used for manual coding by the researchers

* context_analysis.ipynb
Extracts the sentences in all filtered reviews that contain selected terms and runs sentiment analysis on them to find the sentiment of the contexts that these terms appear in.

# CSV files:
build_features.csv            The dictionary we have developed for build features. Each column is a different category.
feature_contexts.csv          A list of sentences where selected words appear in all filtered reviews.
feature_extracted_reviews.csv A table of reviews with boolean columns corresponding to tags based on our dictoinary.
filtered_Yelp_reviews.pkl     ِA Pandas table of all filtered reviews and their meta-data.

