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
        c = 0
        for row in csvReader:
            try:
                c += 1
                ret[c] = {'airport':row[0],'nbPax':row[1]}
                if c >= nb:
                    break
            except:
                continue
        return str(json.dumps(ret,sort_keys=True))

if __name__ == "__main__":
    app.run()
