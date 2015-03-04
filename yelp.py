import numpy as np
import nltk
import csv

def readFile(file_name):
    count=0;
    read_rows=10;
        
    f=open('new_some.csv', 'a')
    writer = csv.writer(f)
    
    with open(file_name, 'rU') as csvfile:
        spamreader = csv.reader(csvfile)
        
        for row in spamreader:
                    if(count%100==0):
                        print(count)
                    text = nltk.word_tokenize(row[1])
                    index=0
                    final_write=[]
                    final_write.append(row[0])
                    final_write.append(0)
                    final_write.append(1)
                    final_write.append(2)
                    final_write.append(3)
                    word_before=''
                    symbol_before=''
                    for word, pos in nltk.pos_tag(text): # remove the call to nltk.pos_tag if `sentence` is a list of tuples as described above
                        word=word.rstrip('\n')
                        word=word.replace(r'\n', '')
                        word=word.replace('.','')
                        word=word.strip()
                        if pos in ['JJ']: # JJ-adjective, RB-adverb feel free to add any other tags
                            if symbol_before in ['RB']:
                                final_write.append(symbol_before)
                                final_write.append(word_before)
                            final_write.append(pos)
                            final_write.append(word)
                        if pos in ['RB']:
                            word_before=word
                            symbol_before=pos
                        else:
                            word_before=''
                            symbol_before=''
                    writer.writerow(final_write)
                    final_write=[]
                    count=count+1

def main():
    countn=readFile('yelp_new.csv')

if __name__ == '__main__':
    main()
