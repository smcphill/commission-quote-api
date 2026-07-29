const form = document.getElementById("quote-form");
const statusEl = document.getElementById("quote-status");
const resultEl = document.getElementById("quote-result");
const submitButton = form.querySelector("button[type=submit]");
const apiKey = document.getElementById("apiKey");

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

  try {
    const response = await fetch("/api/quote", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "api-key": apiKey.value,
      },
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
