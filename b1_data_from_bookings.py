import sys,os,pandas,csv

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Please provide a booking file.'
        sys.exit(0)
    aFile = sys.argv[1]
    aData = None
    if not os.path.exists(aFile):
        print 'Please check if the booking file', aFile, 'does exist'
        sys.exit(0)
    else:
        # extract data from file
        aChunks = pandas.read_table(aFile,chunksize=10000,sep='^',usecols=['pos_oid  ','dep_port','arr_port','cre_date           ','brd_time           '])
        aData = pandas.DataFrame()
        aData = pandas.concat(chunk for chunk in aChunks)
        aData.to_csv('bkg4b1.csv',sep='^')
