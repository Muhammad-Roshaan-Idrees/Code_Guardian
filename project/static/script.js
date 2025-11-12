const API_BASE = "";

const codeInput = document.getElementById("code");
const reviewOutput = document.getElementById("reviewOutput");
const loadingOverlay = document.getElementById("loading");
const apiStatus = document.getElementById("apiStatus");
const lastReview = document.getElementById("lastReview");

async function checkAPI() {
    try {
        const res = await fetch(`${API_BASE}/health`);
        if (res.ok) {
            const data = await res.json();
            apiStatus.textContent = `Connected (${data.status})`;
            apiStatus.style.color = "limegreen";
        } else {
            throw new Error("Unhealthy response");
        }
    } catch (err) {
        apiStatus.textContent = "Disconnected";
        apiStatus.style.color = "red";
    }
}
checkAPI();

function showLoading(show) {
    loadingOverlay.style.display = show ? "flex" : "none";
}

function clearCode() {
    codeInput.value = "";
    reviewOutput.innerHTML = `
        <div class="placeholder">
            <i class="fas fa-code"></i>
            <h4>Your Code Review Awaits</h4>
            <p>Write or paste your code and click "Review Code" to get started</p>
        </div>`;
}

function clearReview() {
    reviewOutput.innerHTML = "";
}

function displayReview(result) {
    if (!result.success) {
        reviewOutput.innerHTML = `<p style="color:red;">Error: ${result.error}</p>`;
        return;
    }

    const review = result.review || result.feedback || result.security_review || result.performance_review;
    if (typeof review === "string") {
        reviewOutput.innerHTML = `<pre>${review}</pre>`;
    } else {
        reviewOutput.innerHTML = `
            <h4>Summary</h4>
            <p>${review.summary || result.feedback || "No summary provided"}</p>

            ${review.quality_metrics ? `
                <h4>Quality Metrics</h4>
                <ul>
                    ${Object.entries(review.quality_metrics).map(([k,v]) => `<li>${k}: ${v}/10</li>`).join("")}
                </ul>` : ''
            }

            ${review.critical_issues?.length ? `
                <h4>Critical Issues</h4>
                <ul>${review.critical_issues.map(i => 
                    `<li><b>${i.type}</b> (${i.severity}) - ${i.description}<br><em>${i.suggestion}</em></li>`
                ).join('')}</ul>` : ''
            }

            ${review.improvement_suggestions?.length ? `
                <h4>Improvement Suggestions</h4>
                <ul>${review.improvement_suggestions.map(s => 
                    `<li>${s.suggestion} (Impact: ${s.impact}, Effort: ${s.effort})</li>`
                ).join('')}</ul>` : ''
            }

            ${review.positive_aspects?.length ? `
                <h4>Positive Aspects</h4>
                <ul>${review.positive_aspects.map(p => `<li>${p}</li>`).join('')}</ul>` : ''
            }
        `;
    }

    lastReview.textContent = new Date().toLocaleTimeString();
}

async function reviewCode() {
    const code = codeInput.value.trim();
    const language = document.getElementById("language").value;
    const focusAreas = Array.from(document.querySelectorAll('input[name="focus"]:checked')).map(i => i.value);

    if (!code) return alert("Please enter your code first");

    showLoading(true);
    try {
        const res = await fetch(`${API_BASE}/review`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code, language, focus_areas: focusAreas })
        });
        const data = await res.json();
        displayReview(data);
    } catch (err) {
        reviewOutput.innerHTML = `<p style="color:red;">Error: ${err.message}</p>`;
    } finally {
        showLoading(false);
    }
}

async function getQuickFeedback() {
    const code = codeInput.value.trim();
    const language = document.getElementById("language").value;
    if (!code) return alert("Please enter your code first");

    showLoading(true);
    try {
        const res = await fetch(`${API_BASE}/quick-feedback`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ code, language })
        });
        const data = await res.json();
        displayReview(data);
    } catch (err) {
        reviewOutput.innerHTML = `<p style="color:red;">Error: ${err.message}</p>`;
    } finally {
        showLoading(false);
    }
}

function exportReview() {
    const content = reviewOutput.innerText;
    const blob = new Blob([content], { type: "text/plain" });
    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = `code_review_${Date.now()}.txt`;
    link.click();
}
