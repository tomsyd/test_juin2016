import sys,pandas
from datetime import datetime
import matplotlib.pyplot as plt

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print 'Please provide a search file.'
        sys.exit(0)
    aFile = sys.argv[1]
    aChunks = pandas.read_table(aFile,chunksize=10000,sep='^',usecols=['Date','Destination'],parse_dates=True)
    aData = pandas.DataFrame()
    aData = pandas.concat(chunk for chunk in aChunks)
    aCities = ['MAD','AGP','BCN']
    mData = aData[aData.Destination.isin(aCities)]
    mData['YM'] = mData['Date'].map(lambda x: x[:7])
    mData['counter'] = 1
    mGrouped = mData.groupby(['Destination','YM']).counter.sum().reset_index()
    print mGrouped

    df = pandas.DataFrame({m: mGrouped[mGrouped.Destination.isin([m,])]['counter'] for m in aCities})

    fig = plt.figure(figsize=(15,6))
    ax = fig.add_subplot(1, 1, 1)
    df.plot(ax=ax)
    ax.set_title('Monthly number of search: Malaga, Madrid and Barcelona')
    plt.savefig('test3.svg',bbox_inches='tight')
