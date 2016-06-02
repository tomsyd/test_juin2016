import sys,os,pandas,csv
from GeoBases import GeoBase

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
        aChunks = pandas.read_table(aFile,chunksize=10000,sep='^',usecols=['arr_port','pax'])
        aData = pandas.DataFrame()
        aData = pandas.concat(chunk for chunk in aChunks)
        grouped = aData.groupby(aData['arr_port']).sum()
        sgrouped = grouped.sort_values(by='pax',ascending=False)
        geo = GeoBase(data='ori_por',verbose=False)
        for i in range(10):
            try:
                item = sgrouped.ix[i]
                print geo.get(item.name.strip(),'name'),item.pax
            except:
                print 'no more airports...'
                sys.exit(0)