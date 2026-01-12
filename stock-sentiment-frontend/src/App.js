import { useState } from "react";

function App() {
  const [ticker, setTicker] = useState("");
  const [result, setResult] = useState(null);

  const checkStock = async () => {
    const res = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ticker }),
    });

    const data = await res.json();
    setResult(data);
  };

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Stock Sentiment Predictor</h1>
      <input
        type="text"
        value={ticker}
        onChange={(e) => setTicker(e.target.value)}
        placeholder="Enter stock symbol"
      />
      <button onClick={checkStock}>Check</button>

      {result && (
        <div style={{ marginTop: "2rem" }}>
          <p><b>Ticker:</b> {result.ticker}</p>
          <p><b>Latest Price:</b> ${result.last_price}</p>
          <p><b>Daily Sentiment Score:</b> {result.daily_score.toFixed(2)}</p>
          <p><b>Suggested Action:</b> {result.action}</p>
          <p><b>Headlines:</b></p>
          <ul>
            {result.headlines.map((h, idx) => (
              <li key={idx}>{h}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
