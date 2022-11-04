# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 08:20:20 2022

@author: hpatel80
Full Name : Hanee Haresh Patel
"""
import pandas as pd
import sys
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename= 'output.log',
                    filemode='a')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# add the handler to the root logger
logging.getLogger().addHandler(console)

try:
    if len(sys.argv)<2:
        logging.error("No command entered")
    log_file, timestamp = sys.argv[2], sys.argv[4]
    df = pd.read_csv(log_file)
    df=df.dropna()
    date=[]
    for _,row in df.iterrows():
        date.append(row['timestamp'][:10])
    df['date']=date
    cookie_occurance=df[df['date'].isin([timestamp])]['cookie'].value_counts().to_dict()
    if not cookie_occurance:
        logging.error("No cookie for the date {}".format(timestamp))
    max_occurance = 0
    for key, value in cookie_occurance.items():
        if value > max_occurance:
            max_occurance = value
    for key, value in cookie_occurance.items():
        if value == max_occurance:
            logging.info(key)
except (IndexError, FileNotFoundError) as exception:
    logging.error(exception)