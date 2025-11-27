document.getElementById("quoteBtn").onclick = async function () {
    const response = await fetch("/quote");
    const data = await response.json();
    document.getElementById("quoteText").textContent = data.quote;
};
