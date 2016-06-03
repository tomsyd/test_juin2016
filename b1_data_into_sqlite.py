import pandas,sys,os.path
from sqlalchemy import create_engine

data_engine = create_engine('sqlite:///bkg.db')

if __name__ == '__main__':
    # load bkg4b1.csv into sqlite db
    bFile = 'bkg4b1.csv'
    for df in pandas.read_csv(bFile,sep='^',chunksize=10000,iterator=True):
        df = df.rename(columns={c: c.replace(' ', '') for c in df.columns})
        df.to_sql('bkg_data',data_engine,if_exists='append')
