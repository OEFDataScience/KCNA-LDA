# -*- coding: utf-8 -*-
"""
Time-series topic weight extraction
Created on Wed Apr 29 11:21:55 2020
@author: Claytonious
"""
#modules
import gensim
import gensim.test.utils 
import pickle
import pandas as pd
import tqdm


##############################################################################
#Extract topic frequencies
#load lda model
lda_model = gensim.models.LdaModel.load("lda_baseline.pkl")
#load corpus/DTM
with open("corpus.pkl", "rb") as fp:
    corpus = pickle.load(fp)
###################################################################################
#identify topics in lda model object. they could be in a different order than 
#the web dashboard.
topics = lda_model.show_topics(num_words = 30, formatted = True)
#0 = positive ROK, 1 = industry and science, 2 = juche/ideology, 3 = art/games,
#4 = negative ROK, 5 = military/patriotism, 6 = nuclear, 7 = historical grievance (japan/rok),
#8 = diplomacy, 9 = foreign relations?
##############################################################################
#Part 1: Extract weights by document. Can take up to three hours depending on
#corpus size
#########################################################################
weights_output = pd.DataFrame(columns = ['topic', 'prob_weight', 'doc_id'])
pbar = tqdm.tqdm(total = len(corpus))
for i in range(0, len(corpus)):
    doc_weights = lda_model[corpus[i]][0]
    weights_df = pd.DataFrame(doc_weights, columns = ['topic', 'prob_weight'])
    weights_df['doc_id'] = i
    weights_output = weights_output.append(weights_df)
    pbar.update(1)
pbar.close()

#save topic weights by document
weights_output.to_csv("topic_weights_bydoc.csv")
weights_output.to_pickle("topic_weights_bydoc.pkl")
###########################################################################################
#setup weights dataset for visualization
df2 = pd.read_pickle("dprk_cleaned.pkl")
df = pd.read_pickle("topic_weights_bydoc.pkl")
#merge info from base data into weight data
df3 = df2.reset_index()
df3['doc_id'] = df3.index
df3['year'] = pd.DatetimeIndex(df3['Date']).year

df11 = pd.merge(df,df3[['doc_id','year', 'Title', 'Text', 'URL', 'Date']],on='doc_id', how='left')

#yearly average weight by topic
total_docs = df11.groupby('year')['doc_id'].apply(lambda x: len(x.unique())).reset_index()
total_docs.columns = ['year', 'total_docs']
total_docs.to_csv("total_doc_year.csv")

df_avg = df11.groupby(['year', 'topic']).agg({'prob_weight':'sum'}).reset_index()
df_avg = df_avg.merge(total_docs, on='year', how="left")
df_avg['average_weight'] = df_avg['prob_weight'] / df_avg['total_docs']

#create topic labels for dataset
topic_labels = ['Positive ROK', "Industy/Science", "Juche/Ideology", "Art/Sport", "Negative ROK", "Military/Patriotism", 
                "Nuclear", "Historical Grievance", "Diplomacy", "Foreign Relations"]
topic_id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
data_tuple = list(zip(topic_id, topic_labels))
df_labels = pd.DataFrame(data_tuple, columns = ['topic', 'topic_label'])

df_avg2 = df_avg.merge(df_labels, on='topic')
df_avg2.to_csv("year_topic_weights.csv")

##########
#create final dataset and export
df12 = pd.merge(df11,df_avg2[['year', 'topic', 'average_weight', 'total_docs', 'topic_label']],on=['year', 'topic'], how='left')
df12.to_csv("FULL_DPRK_PROCESSED.csv")
df12.to_pickle("FULL_DPRK_PROCESSED.pkl")


