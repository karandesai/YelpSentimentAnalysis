import numpy as np
import nltk
import csv
import codecs

def readFile(file_name):
    count=0;
    read_rows=100;
    
    ins = open( "negative-words.txt", "r" )
    negative = {}
    for line in ins:
        negative[line.strip().lower()]='no'
    ins.close()
    #print(negative)
    negative=dict(negative)


    ins2 = open("positive-words.txt", "r" )
    positive= {}
    for line2 in ins2:
        positive[line2.strip().lower()]='yes'
    ins2.close()
    #print(positive)
    positive=dict(positive)


    ins3 = open("users.txt", "rU" )
    users={}
    usersNo=1
    for line3 in ins3:
        users[usersNo]=line3.strip()
        usersNo=usersNo+1
    ins3.close()
    users=dict(users)
    #print users

    ins4 = open( "negative-adverbs.txt","rU")
    negative_ad = {}
    for line4 in ins4:
        negative_ad[line4.strip().replace('\xe2\x80\x99', "'").lower()]='no'
    ins4.close()

    negative_ad=dict(negative_ad)
    negative_ad.pop('', None)
    #print(negative_ad)


    ins5 = open( "positive-adverbs.txt","rU")
    positive_ad = {}
    for line5 in ins5:
        positive_ad[line5.strip().replace('\xe2\x80\x99', "'").lower()]='no'
    ins5.close()

    positive_ad=dict(positive_ad)
    positive_ad.pop('', None)
    print(positive_ad)

    output_file=open("yelp_output__adverb_test.csv","a")
    writer = csv.writer(output_file)

    with open(file_name, 'rU') as csvfile:
        datareader = csv.reader(csvfile)
        con=1
        for row in datareader:
            value=0
            adj_count=0
            for i in range(5,len(row)):   ##### PLEASE MAKE SURE THIS INDEX IS CORRECt, SHOULD BE START FROM 5?  ######

                adv_sign=1
                if(row[i] in ['RB']):
                    if(i+2<len(row)):
                        i=i+1
                        row[i].replace("'","");
                        row[i].replace('\xe2\x80\x99', "'")
                        if(row[i].lower() in negative_ad):
                            adv_sign=-1
                            #print row[i] +"->" + row[i+2]+":"+str(adv_sign)
                        if(row[i].lower() in positive_ad):
                            adv_sign=2
                            #print row[i] +"->" + row[i+2]+":"+str(adv_sign)
                        i=i+2
                
            
                if(i%2==0):
                    if(row[i].lower() in negative):
                        value=value-(1*adv_sign)
                        if(adv_sign==2):
                            adj_count=adj_count+1
                        adj_count=adj_count+1
                    elif(row[i].lower() in positive):
                        value=value+(1*adv_sign)
                        if(adv_sign==2):
                             adj_count=adj_count+1
                        adj_count=adj_count+1
                    if(adv_sign!=1):
                        print(row[i-2]+"->"+row[i]+":"+str(adv_sign))
                            
        
            #End of line for-loop.
            if(adj_count!=0):
                value=(value/float(adj_count))*2.5+2.5
            else:
                value=-999
            #print(str(con)+"->"+str(value))
            row[1]=value
            row[2]=users[con]
            con=con+1
            if(con==330071):
                return
            writer.writerow(row)

def main():
    countn=readFile('new_some.csv')

if __name__ == '__main__':
    main()
