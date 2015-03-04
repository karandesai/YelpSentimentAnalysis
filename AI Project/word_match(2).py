import numpy as np
import nltk
import csv

def readFile(file_name):
    count=0;
    read_rows=100;
    
    ins = open( "negative-words.txt", "r" )
    negative = {}
    for line in ins:
        negative[line.strip()]='no'
    ins.close()
    #print(negative)
    negative=dict(negative)


    ins2 = open("positive-words.txt", "r" )
    positive= {}
    for line2 in ins2:
        positive[line2.strip()]='yes'
    ins2.close()
    #print(positive)
    positive=dict(positive)

    output_file=open("yelp_output.csv","a")
    writer = csv.writer(output_file)

    with open(file_name, 'rU') as csvfile:
        datareader = csv.reader(csvfile)
        con=1
        for row in datareader:
            value=0
            adj_count=0
            for i in range(2,len(row)):
                if(i%2!=0):
                    if(row[i] in negative):
                        value=value-1
                        adj_count=adj_count+1
                    elif(row[i] in positive):
                        value=value+1
                        adj_count=adj_count+1
            if(adj_count!=0):
                value=(value/float(adj_count))*2.5+2.5
            else:
                value=-999
            print(str(con)+"->"+str(value))
            con=con+1
            row[1]=value
            writer.writerow(row)

def main():
    countn=readFile('some.csv')

if __name__ == '__main__':
    main()
