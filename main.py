from scraper import scrape
import argparse
from random import randint
import urllib.request


def connect():
    try:
        urllib.request.urlopen('https://www.google.com/') #Python 3.x
        return True
    except:
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=\
        "Helper methods")
    parser.add_argument("--term",type=str,nargs="+")
    parser.set_defaults(term=[])
    args =  parser.parse_args()

    #checks if its connected to the internet
    print("starting")
    isInternetConnected = connect()
    if isInternetConnected:
        if(len(args.term)==0):
            print("starting scraping")
            scrape("")
        else:
            randomGuess = randint(0,len(args.term)-1)
            scrape(args.term[randomGuess])
        print("setting wallpaper")
