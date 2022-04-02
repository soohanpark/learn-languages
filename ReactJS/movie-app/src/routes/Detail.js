import { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

function Detail() {
  const { id } = useParams();

  const [loading, setLoading] = useState(true);
  const [movie, setMovie] = useState([]);

  const getMovie = async () => {
    const respJson = await fetch(
      `https://yts.mx/api/v2/movie_details.json?movie_id=${id}`
    ).then((resp) => resp.json());
    // TODO
    console.log(respJson);
    setMovie(respJson.data.movie);
    setLoading(false);
  };

  useEffect(() => {
    getMovie();
  }, []);
  return (
    <h1>{loading ? <h1>Loading...</h1> : <MovieDetail movie={movie} />}</h1>
  );
}

function MovieDetail({ movie }) {
  return (
    <div>
      <h1>{movie.title}</h1>
      <img src={movie.medium_cover_image} alt={movie.title} />
      <p>{movie.description_intro}</p>
      <ul>
        {movie.genres.map((genre, idx) => {
          return <li key={idx}>{genre}</li>;
        })}
      </ul>
    </div>
  );
}

export default Detail;
