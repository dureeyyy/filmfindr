import streamlit as st
import os
import request as req
from dotenv import load_dotenv
from tweaker import st_tweaker

with open('src/styles/style.css') as style:
    st.markdown(f'<style>{style.read()}</style>', unsafe_allow_html=True)

def main():

    load_dotenv()

    url = os.environ.get('URL')
    apikey = os.environ.get('APIKEY')

    st.title('FilmFindr')

    query = st.text_input('Movie Title', label_visibility="hidden", placeholder='Enter movie title')
    print(f'Query : {query}')

    if query != "":

        parameter = f't : {query}'

        print(f'PARAMETER : {parameter}')
    
        json_response = req.send_request(url, apikey, parameter)

        movie = req.handle_response(json_response)        

        st.subheader(movie.get_title())
        st.image(movie.get_poster())
        st.write(movie.get_year())
        st.write(movie.get_rated())
        st.write(movie.get_genre())
        st.write(movie.get_actors())
        st.write(movie.get_director())
        st.write(movie.get_writers())
        st.write(movie.get_plot())

    else:

        col1, col2, col3 = st.columns(3)

        with col1:
            st_tweaker.image(
                "https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SX300.jpg",
                id='movie1'
                )
            st_tweaker.image(
                "https://m.media-amazon.com/images/M/MV5BMTQ5NjQ0NDI3NF5BMl5BanBnXkFtZTcwNDI0MjEzMw@@._V1_SX300.jpg",
                id='movie2'
                )
            st_tweaker.image(
                "https://m.media-amazon.com/images/M/MV5BMzU3NTYxM2MtNjViMS00YmNlLWEwM2MtYWI2MzgzNTkxODFjXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg",
                id='movie3')

        with col2:
            st_tweaker.image(
                "https://m.media-amazon.com/images/M/MV5BNzc1OWY5MjktZDllMi00ZDEzLWEwMGItYjk1YmRhYjBjNTVlXkEyXkFqcGc@._V1_SX300.jpg",
                id='movie4')
            st_tweaker.image(
                "https://m.media-amazon.com/images/M/MV5BMjIxMjgxNTk0MF5BMl5BanBnXkFtZTgwNjIyOTg2MDE@._V1_SX300.jpg",
                id='movie5')
            st_tweaker.image(
                "https://m.media-amazon.com/images/M/MV5BNzc3Mzg1OGYtZjc3My00Y2NhLTgyOWUtYjRhMmI4OTkwNDg4XkEyXkFqcGdeQXVyMTU3NDU4MDg2._V1_SX300.jpg",
                id='movie6')

        with col3:
            st_tweaker.image(
                "https://m.media-amazon.com/images/M/MV5BNDdjZGQ5YzEtNTc2My00Mjc0LWFlMTctYzkwMzZlNzdiZWYzXkEyXkFqcGc@._V1_SX300.jpg",
                id='movie7')
            st_tweaker.image(
                "https://m.media-amazon.com/images/M/MV5BMmNkODhkYjctMDMyOC00ZTNjLTkwZTItM2ExMTAxMGU1ZGQ1XkEyXkFqcGc@._V1_SX300.jpg",
                id='movie8')
            st_tweaker.image(
                "https://m.media-amazon.com/images/M/MV5BNjY5YWJjODYtNDUzNy00ZGMyLTk3NTQtN2EzZmFhZTFmMDNiXkEyXkFqcGc@._V1_SX300.jpg",
                id='movie9')



if __name__ == "__main__":
    main()
