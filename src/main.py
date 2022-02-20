import imdb
import interface

def main():
    ia = imdb.Cinemagoer()
    interface.clear_scr()
    interface.greetings()
        
    search = input("\n\nSearch: ")    
    search_result = ia.search_movie(search)    
    search_index = interface.show_search_result(search_result)
    
    movie = ia.get_movie(search_result[search_index].movieID)
    if movie['kind'] == 'movie':
        interface.print_movie_info(movie)
    
    
if __name__ == '__main__':
    main()