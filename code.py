import csv
import xml.etree.ElementTree as ET 
import pandas as pd
import plotly.express as px
pathh='/Users/supratikvishnu/Library/Mobile Documents/com~apple~CloudDocs/coding/export.xml'
tree = ET.parse(pathh)
root=tree.getroot()
#creating heart.csv file
def createheartfile(date):
    f=open('heart.csv','w')
    csvwriter = csv.writer(f) 
    csvwriter.writerow(['InstantaneousBeatsPerMinute','TIME']) 
    for x in root.iter('Record'):        
        if x.attrib['type']=="HKQuantityTypeIdentifierHeartRateVariabilitySDNN" and (x.attrib['creationDate'][:10]==date or x.attrib['creationDate']==date) :
            for y in x.iter('InstantaneousBeatsPerMinute'):
                #f.write(str(y.attrib['bpm'])+','+str(y.attrib['time'])[:-2])
                csvwriter.writerow([y.attrib['bpm'],str(y.attrib['time'])[:-2]]) 
                #f.write('\n')# dates_list.append(x.attrib['creationDate'])
    
    f.close()
    print('file heart.csv updated!! please plot')
    def plotheart():
        df = pd.read_csv('heart.csv')
        df.head()
        fig = px.line(df, x = 'TIME', y = 'InstantaneousBeatsPerMinute', title='Beats over time ('+date+')')
        fig.show()
    return(plotheart())


def hi():
    print('hello world')


def datelist():

    dates_list=[]
    for x in root.iter('Record'):
        if x.attrib['type']=="HKQuantityTypeIdentifierHeartRateVariabilitySDNN":
            dates_list.append(x.attrib['creationDate'])
    return(dates_list)  

def dateliststep():

    dates_listoo=[]
    for x in root.iter('Record'):
        if x.attrib['type']=="HKQuantityTypeIdentifierStepCount":
            dates_listoo.append(x.attrib['creationDate'])
    return(dates_listoo)  

def createstepsfile(date):

    f=open('steps.csv','w')
    csvwriter = csv.writer(f) 
    csvwriter.writerow(['STEPS','TIME']) 
    for x in root.iter('Record'):        
        if x.attrib['type']=="HKQuantityTypeIdentifierStepCount" and (x.attrib['creationDate'][:10]==date or x.attrib['creationDate']==date ) : #or x.attrib['creationDate'][5:7]==date
            csvwriter.writerow([x.attrib['value'],str(x.attrib['creationDate'])[11:19]]) 
    f.close()
    print('file steps.csv updated!! please plot')

    def plotSteps():
        df = pd.read_csv('steps.csv')
        df.head()
        fig = px.line(df, x = 'TIME', y = 'STEPS', title=('Steps over time'+str(date)))
        fig.show()
    return plotSteps()

def dates():
  alldates=datelist()
  onlydates=[]
  for i in alldates:
    a=i.split()
    if a[0] not in onlydates:
      onlydates.append(a[0])
  return(onlydates)

dates()

def datestep():
  alldates=dateliststep()
  onlydates=[]
  for i in alldates:
    a=i.split()
    if a[0] not in onlydates:
      onlydates.append(a[0])
  return(onlydates)
