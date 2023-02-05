import csv
import random
def get_random_quote(quotes_file='quotes.csv'):
    try:    
        with open(quotes_file) as csvfile:
            csvreader=csv.reader(csvfile,delimiter="|")
            quotes=[{'author':line[0],'quote':line[-1]} for line in csvreader]
    except Exception as e:
        quotes=[{'author':'Eric Idle','quote':'Always look on bright side of life'}]
    return random.choice(quotes)
if __name__=='__main__':
    quote=get_random_quote()
    print(f' - Random quote is "{quote["quote"]}" - {quote["author"]}')
