library(ggplot2)
library(plyr)
require(maps)
library(tidyverse)
library(ggthemes)
library(haven)
library(scales)
library(ggpubr)
library(ggalt)
library(zoo)

#import data 
df <- read.csv("year_topic_weights.csv",
               header = TRUE)
df2 <- df[df$topic_label=="Juche/Ideology" | df$topic_label=="Nuclear" | df$topic_label=="Positive ROK"
          | df$topic_label=="Historical Grievance" | df$topic_label=="Industy/Science", ]
df3 <- df[df$topic_label=="Art/Sport" | df$topic_label=="Foreign Relations" | df$topic_label=="Negative ROK"
          | df$topic_label=="Military/Patriotism" | df$topic_label=="Diplomacy", ]
df4 <- df[df$topic_label=="Nuclear" | df$topic_label=="Positive ROK" | df$topic_label=="Negative ROK"
          | df$topic_label=="Historical Grievance" | df$topic_label=="Diplomacy", ]

df_docs <- read.csv("total_doc_year.csv",
                    header = TRUE)



#graph
plot1 <- ggplot(df2, aes(x = year, y = average_weight, colour = topic_label)) +
  geom_smooth() +
  geom_hline(yintercept = 0.09579, size = 1, colour="#333333") +
  labs(title = "DPRK Corpus Topic Presence (1996 - 2020)",
       subtitle = "Top-5 topics in entire corpus") +
  xlab("Date") + ylab("Average Yearly Topic Weight") + 
  theme_hc()

plot1

plot2 <- ggplot(df3, aes(x = year, y = average_weight, colour = topic_label)) +
  geom_smooth() +
  geom_hline(yintercept = 0.09579, size = 1, colour="#333333") +
  labs(title = "DPRK Corpus Topic Presence (1996 - 2020)",
       subtitle = "Bottom-5 topics in entire corpus") +
  xlab("Date") + ylab("Average Yearly Topic Weight") + 
  theme_hc()

plot2

plot3 <- ggplot(df4, aes(x = year, y = average_weight, colour = topic_label)) +
  geom_smooth() +
  geom_hline(yintercept = 0.09579, size = 1, colour="#333333") +
  labs(title = "DPRK Corpus Topic Presence (1996 - 2020)",
       subtitle = "Topics related to nuclear and threat perception") +
  xlab("Date") + ylab("Average Yearly Topic Weight") + 
  theme_hc()

plot3

plot4 <- ggplot(df_docs, aes(x = year, y = total_docs)) +
  geom_bar(stat = "identity") +
  geom_hline(yintercept = 4596, size = 1, colour="#333333") +
  labs(title = "DPRK Corpus Document Output (1996 - 2020)",
       subtitle = "Total number of documents put out each year (in our corpus)\nBlack line represents median output") +
  xlab("Year") + ylab("Total Docs") + 
  theme_hc()

plot4


