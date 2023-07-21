
import numpy as np 
import pandas as pd
df_jobs=pd.read_csv("C:\\Users\\mehme\\OneDrive\\Masaüstü\\PYTHON\Assignment2\\jobs.csv",index_col=0)


df_jobs["Ratio"]= np.nan



def critical_ratio(df_jobs):
    que = []
    for i in  range(len(df_jobs)):
       
        df_jobs["Ratio"] =  df_jobs["Due Date"]  / df_jobs["Processing Time"] 
        df_jobs_sorted = df_jobs.sort_values(by=["Ratio"])
        selected_job = df_jobs_sorted.iloc[0]
        que.append(selected_job.name)
        df_jobs = df_jobs_sorted.drop(selected_job.name)
        df_jobs["Due Date"] = df_jobs['Due Date'] - selected_job['Processing Time']

    return list(que)

critical_ratio(df_jobs)
