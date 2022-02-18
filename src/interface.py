from tracemalloc import start
from pyfiglet import Figlet
import imdb

def clear_scr():
    # Clear the screen "ctrl + l" 
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

def greetings():
    print(Figlet().renderText("RMovieInfo"))
    
    
def show_search_result(search: list) -> int:
    for i,  s in enumerate(search):
        if (s['kind'] == 'movie' or s['kind'] ==  'tv series' or s['kind'] ==  'tv mini series' or s['kind'] ==  'video game' or s['kind'] ==  'video movie' or s['kind'] ==  'tv movie') and 'year' in s:
            print(f"[{i}] {s['title']} ({s['year']} {s['kind']})")
        elif s['kind'] == 'episode' and 'year' in s:
            print(f"[{i}] {s['title']} ({s['year']} {s['series title']} {s['kind']})")
        else:
            search.pop(i)
    
    return int(input("\n>> "))



def print_movie_info(movie):
    clear_scr()
    print(Figlet().renderText(f"{movie['title']}  ( {movie['year']} )" ), end="\n\n\n")
    
    print(Figlet().renderText(f"IMDb: {movie['rating']} / 10"), end="\n\n\n")
    
    print()
        
    print(f"\nPlot: {movie['plot'][0]}")
    
    print()
        
    print("\n")
    print("Director(s):", end='')
    for i, d in enumerate(movie['director']):
        if i == len(movie['director'])-1:
            print(f" {d}")
        else:
            print(f" {d},", end='')
    print("Writer(s):", end='')
    # print(movie['writer'])
    for i, w in enumerate(movie['writer']):
        if len(w) < 1:
            continue
        if i == len(movie['writer'])-1:
            print(f" {w}")
        else:
            print(f" {w},", end='')
            
    print("\nMain Cast:")
    for i, c in enumerate(movie['cast']):
        if i > 10:
            break
        print(f"\t{c} as {c.currentRole}")
    
    
    