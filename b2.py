import web,sys,os,pandas,csv,json

urls = (
    '/airports/(.*)', 'getJsonOutput'
)

app = web.application(urls, globals())

class getJsonOutput:
    def GET(self, nb):
        nb = int(nb)
        if nb <= 0:
            return '' # only accept positive number
        # extract data from file
        aFile = './test2_result.csv'
        csvReader = csv.reader(open(aFile,'rb'))
        ret = dict()
        counter = 0
        for row in csvReader:
            try:
                airport,n = row
                n = int(n)
                counter += 1
                ret[counter] = {'airport':airport,'nbPax':n}
                if counter >= nb:
                    break
            except:
                continue
        print ret
        return str(json.dumps(ret,sort_keys=True))

if __name__ == "__main__":
    app.run()
