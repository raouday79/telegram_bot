import pandas as pd
import json
#from flask_sqlalchemy import SQLAlchemy
#from flask_marshmallow import Marshmallow
from sqlalchemy import create_engine

def loadData():
    df = pd.read_csv('../user.csv')
    return df

def checkUser(id,df,obj):
    ob  = json.load(temp)
    print(ob)
    df_temp = df[df['id']==id]
    if len(df_temp<1):
        #temp_dict =
        print('Hii')

df = loadData()
checkUser(1,df,3)