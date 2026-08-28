async function analyzeNews() {
  const input = document.getElementById("newsInput");
  const resultBox = document.getElementById("resultBox");
  const badge = document.getElementById("badge");
  const explanation = document.getElementById("resultExplanation");
  const analyzeBtn = document.getElementById("analyzeBtn");

  const text = input.value.trim();
  if (!text) {
    alert("Please enter news text before analyzing.");
    return;
  }

  analyzeBtn.disabled = true;
  analyzeBtn.textContent = "Analyzing...";

  try {
    const response = await fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text: text })
    });

    const data = await response.json();

    resultBox.classList.remove("hidden", "status-true", "status-false");

    if (data.is_real === true) {
      resultBox.classList.add("status-true");
      badge.textContent = "TRUE (Real News)";
      explanation.textContent = "Result: " + data.description;
    } else {
      resultBox.classList.add("status-false");
      badge.textContent = "FALSE (Fake News)";
      explanation.textContent = "Result: " + data.description;
    }
  } catch (err) {
    alert("Error communicating with the prediction server.");
  } finally {
    analyzeBtn.disabled = false;
    analyzeBtn.textContent = "Analyze Text";
  }
}

function clearInput() {
  document.getElementById("newsInput").value = "";
  document.getElementById("resultBox").classList.add("hidden");
}
