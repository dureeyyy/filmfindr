class Movie: 
    def __init__(self): 
        self._title = "" 
        self._year = "" 
        self._rated = "" 
        self._genre = "" 
        self._plot = "" 
        self._poster = "" 
        self._director = "" 
        self._actors = "" 
        self._writers = "" 

    # getter method 
    def get_title(self): 
        return self._title 
    
    def get_year(self): 
        return self._year
    
    def get_rated(self): 
        return self._rated 
    
    def get_genre(self): 
        return self._genre
    
    def get_plot(self): 
        return self._plot
    
    def get_poster(self): 
        return self._poster
    
    def get_director(self): 
        return self._director
    
    def get_actors(self): 
        return self._actors
    
    def get_writers(self): 
        return self._writers
      
    # setter method 
    def set_title(self, t): 
        self._title = t

    def set_year(self, y): 
        self._year = y  

    def set_rated(self, r): 
        self._rated = r

    def set_genre(self, g): 
        self._genre = g

    def set_plot(self, pl): 
        self._plot = pl
    
    def set_poster(self, ps): 
        self._poster = ps 

    def set_director(self, ps): 
        self._director = ps 

    def set_actors(self, ps): 
        self._actors = ps 

    def set_writers(self, ps): 
        self._writers = ps 