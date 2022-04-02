import { Link } from "react-router-dom";

function Movie({ movies }) {
  return (
    <div>
      {movies.map((movie) => {
        return (
          <div key={movie.id}>
            <h2>
              <Link to={`/movie/${movie.id}`}>{movie.title}</Link>
            </h2>
            <img src={movie.medium_cover_image} alt="movieCoverImage" />
            <p>
              {movie.summary.length
                ? `${movie.summary.slice(0, 235)}...`
                : movie.summary}
            </p>
            <ul>
              {movie.genres.map((genre, idx) => (
                <li key={idx}>{genre}</li>
              ))}
            </ul>
          </div>
        );
      })}
    </div>
  );
}

export default Movie;
