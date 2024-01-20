import urllib.request
urllib.request.urlretrieve("https://www.fdic.gov/bank/individual/failed/banklist.csv", "/Users/deepak/Desktop/FDIC_Failed_Bank_List/data/raw/banklist.csv")
urllib.request.urlretrieve("https://catalog.data.gov/harvest/object/cb22fea9-0c90-43e9-94bf-903eacd37c92", "/Users/deepak/Desktop/FDIC_Failed_Bank_List/data/raw/banklist.json")