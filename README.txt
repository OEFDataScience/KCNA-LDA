#read-me for KCNA-text tool github
I. Script ordering
Python scripts should be run in the following order to recreate analysis:

1. data_clean.py - > 2. LDA_modeling.py -> 3.time_series_weights.py -> 4. topic_weights_visualization.Recreate

Visualization done in R (ggplot2) framework. Shouldn't be much of a problem to produce the visuals in Python if that is more helpful. 

2. Folder info
Assets folder contains a number of visualizations associated with the analysis so far.
NOTE: some data files were too big for GitHub (> 100mb). So you will have to use the .txt files that include dropbox links.
Data folder holds the following: orig_scrape (original KCNA data provided by Arshdeep), 
cleaned_text (initial cleaned text data with non-english removed),
trained_model (contains LDA model objects and dictionary/document term matrix),
final_data (contains final data sheet that has original document information with associated time-series topic weights)

3. Things left to do (as of 4/29/2020)
a. Recreate analysis with Korean language corpus
b. Estimate monthly time series topic weights for both english and korean corpus


Contact Clayton (cbesaw@oneearthfuture.org) for questions and requests



