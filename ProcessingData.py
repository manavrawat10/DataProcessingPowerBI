# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 18:13:39 2018

@author: Manav
"""

import os
import pandas as pd
from deletefiles import delete
raw="G:\\PowerBI\\Raw"
proc="G:\\PowerBI\\Processed"
unproc="G:\\PowerBI\\Unprocessed"
for filename in os.listdir(raw):
    #reading each file one by one
    readFile=raw+"\\"+str(filename)
    df=pd.read_csv(readFile)
    print(filename)
    # fill -99999 in place of blank values
    #df.fillna("-99999", inplace=True)
    # convert kilobytes column to float value
    try:
        df.Kilobytes.astype(float).fillna(-99999.0)
        df.to_csv(proc+"\\"+str(filename))
    except Exception as e:
        print(e)
        df.to_csv(unproc+"\\"+str(filename))
    #print(df.Kilobytes)
    #print(df['Kilobytes'].str.isnumeric())
    #print(df.head())
delete(raw)
    