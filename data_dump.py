import pymongo
import pandas as pd 
import json 


client = pymongo.MongoClient("mongodb+srv://gazalsobti:gazal2002@cluster0.tgt6jdx.mongodb.net/?retryWrites=true&w=majority")
DATA_FILE_PATH=(r"C:\Users\91702\OneDrive\Documents\python_industry project\medical-insurance\insurance.csv")
DATABASE_NAME="INSURANCE"
COLLECTION_NAME="INSURANCE_PROJECT"

if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: ",{df.shape})

    df.reset_index(drop=True,inplace=True)

#taking transpose of df and converting it into key - value pair 
# and then storing in the list 
    json_record=list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

