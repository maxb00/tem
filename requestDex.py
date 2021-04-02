import pandas as pd
import pdb
import requests
import json

def main():
    updateDex()
    #pdb.set_trace()

def updateDex():
    # make request to temtem wiki api
    req = requests.get("https://temtem-api.mael.tech/api/temtems/") # pulls whole dex
    # truncate/isolate cloumns we want
    fi = req.json() # this is raw json of whole dex
    df = pd.DataFrame(fi) # we can cast it all to a DataFrame, (Nx30)
    df = df[['number', 'name', 'types']].copy() # this makes our data frame smaller
    # now, our DataFrame holds just what we want - number, name, types.

    # save new data frame as json that can be read in by no-dep main
    fi = df.to_json(path_or_buf='temdex.json', orient='index') # fi now holds a string containing the new raw json

    #with open('temdex.json', 'w') as outfile:
        #json.dump(fi, outfile)

if __name__ == '__main__':
    main()
