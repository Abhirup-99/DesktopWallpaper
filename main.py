from scraper import scrape
from setWallpaper import setWallpaper
import argparse
from random import randint

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=\
        "Helper methods")
    parser.add_argument("--term",type=str,nargs="+")
    parser.set_defaults(term=[])
    args =  parser.parse_args()
    if(len(args.term)==0):
        scrape("")
    else:
        randomGuess = randint(0,len(args.term)-1)
        scrape(args.term[randomGuess])
    setWallpaper()
