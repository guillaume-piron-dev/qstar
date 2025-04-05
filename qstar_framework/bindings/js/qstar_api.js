bindings/js/qstar_api.js
async function qstarLLM(inputText) {
  const response = await fetch('http://localhost:8000/qstar', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text: inputText })
  });
  const data = await response.json();
  console.log("[JS] Réponse Q-STAR:", data);
}

qstarLLM("Q-STAR : l'IA de demain");
