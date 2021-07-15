import requests
import json
import re

# https://stackoverflow.com/questions/61364719/how-can-i-scrape-aliexpress-product-data
####
from re import sub
from decimal import Decimal

import pandas as pd
from datetime import date

today = date.today()
metricsFile = '/opt/send-mail-infos/metrics-'+today.strftime("%Y%m%d")+'.xlsx'

money = '$6,150,593.22'
value = Decimal(sub(r'[^\d.]', '', money))
print(value)
###

def money(number):
    number = number.strip('$')
    try:
        [num,dec]=number.rsplit('.')
        dec = int(dec)
        aside = str(dec)
        x = int('1'+'0'*len(aside))
        price = float(dec)/x
        num = num.replace(',','')
        num = int(num)
        price = num + price
    except:
        price = int(number)
    return price


# https://pypi.org/project/PyCurrency-Converter/

#import PyCurrency_Converter
#PyCurrency_Converter.codes()
#PyCurrency_Converter.convert(1, 'USD', 'INR')

target = ["title", "itemDetailUrl", "imagePath"]


def main(url):
    global urls
    global nprices
    r = requests.get(url)
    match = re.search(r'data: ({.+})', r.text).group(1)
    data = json.loads(match)
    #rls.append(url)
    try:
        goal = [data['pageModule'][x] for x in target] + \
            [data['priceModule']['formatedActivityPrice']]
        if len (goal[-1]) < 10:
            #print(goal[-1])
            nprice = goal[-1]
            print (nprice)
            nprices.append(nprice)
            urls.append(url)
        else:
            #print ("US $"+goal[-1].split(" - ")[-1])
            
            nprice = "US $"+goal[-1].split(" - ")[-1]
            print (nprice)
            nprices.append(nprice)
            urls.append(url)
    except:
        print('error:', url)
        nprices.append('--')
        urls.append(url)




def compare_values(lastprices,newprices):
    x = zip(lastprices,newprices)
    global urls
    vals1 =[]
    vals2 = []
    ress = []
    for i , j in x:
        if j == '--':
            vals1.append(float('0'))
            vals2.append(float('0'))
            ress.append(float('0'))

        else:
            val1 = i[1:]
            val1 = val1.replace(",",".")
            val2 = j[4:]
            val2 = val2.replace(",", ".")
            print(val1,val2)
            res = float(val1)/float(val2)
            if res > 1:
                #print ("+++" , val1," -> ",val2 ,"- > ", 1-res)
                vals1.append(val1)
                vals2.append(val2)
                ress.append(("{:.2f}".format(1-res)))
            else:
                #print ("---" , val1," -> ",val2 ,"- > ", 1-res)
                vals1.append(val1)
                vals2.append(val2)
                ress.append(("{:.2f}".format(1-res)))
    d = {'urls':urls ,'my price': vals1, 'actual price': vals2, 'last/new': ress}
    df = pd.DataFrame(data=d)
    print(df)
#    newfile = open("metrics.csv", "rw")
    # create_and_insert_data_to_file()
    save_pd_to_xlsx(df,"./"+metricsFile)
    print ("Alibaba job : FINISHED!")




def save_pd_to_xlsx(pdData,fullPathFile):
    import pandas as pd
    # Create a Pandas dataframe from the data.
    # df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})
    tag = fullPathFile.split("/")[-1]
    print (tag)

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(tag, engine='xlsxwriter')
    # Convert the dataframe to an XlsxWriter Excel object.
    pdData.to_excel(writer, sheet_name='Recommendation')
    # Close the Pandas Excel writer and output the Excel file.

    writer.save()
    print("Data saved to: ",tag )


# start #

global nprices
global prices
global urls
urls = []
nprices = []
links = []
prices = []

def get_cols_fromtab_file(filename):
    afile = open(filename, "r")
    for i in afile.readlines()[1:]:
        i = i.strip()
        
        link = i.split(" ")[0]
       
        
        price = i.split(" ")[1]

        print (link,price)
        links.append(str(link))
        prices.append(str(price))
        y = zip(links,prices)

    return links,prices

datafile = 'plano.txt'
links ,prices = get_cols_fromtab_file(datafile)

for i in links:
    main(i)



compare_values(prices,nprices)
