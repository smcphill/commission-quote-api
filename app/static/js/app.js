const API_KEY = "alice";
const form = document.getElementById("quote-form");
const statusEl = document.getElementById("quote-status");
const resultEl = document.getElementById("quote-result");
const submitButton = form.querySelector("button[type=submit]");
const apiKey = document.getElementById("apiKey");
const devView = document.getElementById("dev-mode");
const chaosMode = document.getElementById("chaosMode");


window.addEventListener("load", _event => {
    const params = new URLSearchParams(window.location.search);
    if (params.get("use") === "dev") {
      devView.removeAttribute('hidden');
    }
});

form.addEventListener("submit", async (event) => {
  event.preventDefault();

  const payload = {
    loanAmount: Number(form.loanAmount.value),
    loanTermInMonths: Number(form.loanTermInMonths.value),
    riskBand: form.riskBand.value,
  };

  resultEl.hidden = true;
  statusEl.textContent = "Generating quote…";
  submitButton.disabled = true;

  const baseHeaders = {
        "Content-Type": "application/json",
        "api-key": apiKey.value === "" ? API_KEY : apiKey.value,
  };
  const chaosHeader = chaosMode.checked ? { "X-Bendigo-Chaos": true} : {};

  try {
    const response = await fetch("/api/quote", {
      method: "POST",
      headers: { ...baseHeaders, ...chaosHeader},
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      const error = await response.json().catch(() => ({}));
      throw new Error(error.error ?? `Request failed: ${response.statusText} (${response.status})`);
    }

    const quote = await response.json();

    document.getElementById("quote-id").textContent = quote.quoteId;
    document.getElementById("quote-commission-rate").textContent = quote.commissionRate;
    document.getElementById("quote-total-commission").textContent = quote.totalCommission;

    statusEl.textContent = "";
    resultEl.hidden = false;
  } catch (error) {
    statusEl.textContent = `Failed to generate quote: ${error.message}`;
  } finally {
    submitButton.disabled = false;
  }
});
