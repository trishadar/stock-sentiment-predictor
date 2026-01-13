async function analyze() {
  const ticker = document.getElementById("ticker").value;
  const result = document.getElementById("result");
  const headlinesList = document.getElementById("headlines");

  result.innerText = "Analyzing...";
  headlinesList.innerHTML = "";

  const res = await fetch("https://stock-sentiment-predictor.onrender.com/analyze", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ ticker })
  });

  const data = await res.json();

  if (data.error) {
    result.innerText = `Error: ${data.error}`;
    return;
  }
  result.innerText = `${data.ticker}: ${data.action} (sentiment: ${data.daily_score}, price: $${data.price})`;

  data.headlines.forEach(h => {
    const li = document.createElement("li");
    li.innerText = `${h.title} → ${h.sentiment}`;
    headlinesList.appendChild(li);
  });
}
