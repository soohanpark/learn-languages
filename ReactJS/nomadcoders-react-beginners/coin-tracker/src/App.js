import { useEffect, useState } from "react";
function App() {
  const [loading, setLoading] = useState(true);
  const [coins, setCoins] = useState([]);
  useEffect(() => {
    fetch("https://api.coinpaprika.com/v1/tickers")
      .then((response) => {
        return response.json();
      })
      .then((json) => {
        setCoins(json);
        setLoading(false);
      });
  }, []);
  return (
    <div>
      <h1>Coin!</h1>
      {loading ? <strong>Loading...</strong> : null}
      <ul>
        {coins.map((val, idx) => (
          <li>
            {val.name} ({val.symbol}): {val.quotes.USD.price} USD
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
