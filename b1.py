import pandas,sys,os.path
from sqlalchemy import create_engine

data_engine = create_engine('sqlite:///bkg.db')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Please provide a search file.'
        sys.exit(0)
    aFile = sys.argv[1]
    if not os.path.exists(aFile):
        print 'Please check if the search file', aFile, 'does exist'
        sys.exit(0)
    else:
        # create new csv file (by chunk)
        for df in pandas.read_csv(aFile,sep='^',chunksize=10000,iterator=True):
            df = df.rename(columns={c: c.replace(' ', '') for c in df.columns})
            # default value of match is 0, i.e. no booking was done for the search
            df['match'] = 0
            for idx,row in df.iterrows():
                print idx
                #print row
                depPort = row['Seg1Departure']
                arrPort = row['Seg1Arrival']
                bkgs = pandas.read_sql_query("SELECT * FROM bkg_data WHERE dep_port='" + depPort + "' AND arr_port='" + arrPort + "' LIMIT 1",data_engine)
                if bkgs.empty:
                    row['match'] = 1
            df.to_csv('test.csv',sep='^')
