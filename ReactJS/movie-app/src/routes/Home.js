import { useState, useEffect } from "react";
import Movie from "../components/Movie";

function Home() {
  const [loading, setLoading] = useState(true);
  const [movies, setMovies] = useState([]);

  const getMovies = async () => {
    const respJson = await fetch(
      `https://yts.mx/api/v2/list_movies.json?minimum_rating=9&sort_by=year`
    ).then((response) => response.json());
    setMovies(respJson.data.movies);
    setLoading(false);
  };

  useEffect(() => {
    getMovies();
  }, []);

  return <div>{loading ? <h1>Loading...</h1> : <Movie movies={movies} />}</div>;
}

export default Home;
