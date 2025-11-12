// API Configuration
const API_BASE_URL = 'http://localhost:5000';

// DOM Elements
const codeInput = document.getElementById('code');
const languageSelect = document.getElementById('language');
const reviewBtn = document.getElementById('reviewBtn');
const quickBtn = document.getElementById('quickBtn');
const reviewOutput = document.getElementById('reviewOutput');
const loadingOverlay = document.getElementById('loading');
const apiStatus = document.getElementById('apiStatus');
const lastReview = document.getElementById('lastReview');

// Initialize
document.addEventListener('DOMContentLoaded', function() {
    checkAPIStatus();
    loadLastReviewTime();
});

// Check API Status
async function checkAPIStatus() {
    try {
        const response = await fetch(`${API_BASE_URL}/health`);
        if (response.ok) {
            apiStatus.innerHTML = '<i class="fas fa-check"></i> Connected';
            apiStatus.style.color = 'var(--success)';
        } else {
            throw new Error('API not responding');
        }
    } catch (error) {
        apiStatus.innerHTML = '<i class="fas fa-times"></i> Disconnected';
        apiStatus.style.color = 'var(--error)';
        console.error('API connection failed:', error);
    }
}

// Main Code Review Function
async function reviewCode() {
    const code = codeInput.value.trim();
    const language = languageSelect.value;
    const focusAreas = getSelectedFocusAreas();

    if (!code) {
        showError('Please enter some code to review');
        return;
    }

    showLoading(true);
    
    try {
        const response = await fetch(`${API_BASE_URL}/review`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                code: code,
                language: language,
                focus_areas: focusAreas
            })
        });

        const data = await response.json();

        if (data.success) {
            displayReviewResults(data.review);
            updateLastReviewTime();
        } else {
            showError(data.error || 'Failed to analyze code');
        }
    } catch (error) {
        showError('Network error: ' + error.message);
    } finally {
        showLoading(false);
    }
}

// Quick Feedback Function
async function getQuickFeedback() {
    const code = codeInput.value.trim();
    const language = languageSelect.value;

    if (!code) {
        showError('Please enter some code to review');
        return;
    }

    showLoading(true);
    
    try {
        const response = await fetch(`${API_BASE_URL}/quick-feedback`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                code: code,
                language: language
            })
        });

        const data = await response.json();

        if (data.success) {
            displayQuickFeedback(data.feedback);
            updateLastReviewTime();
        } else {
            showError(data.error || 'Failed to get quick feedback');
        }
    } catch (error) {
        showError('Network error: ' + error.message);
    } finally {
        showLoading(false);
    }
}

// Display Review Results
function displayReviewResults(review) {
    let html = '<div class="review-content">';
    
    // Overall Score
    html += `
        <div class="score-display">
            <div class="score-circle">${review.overall_score}</div>
            <h3>Overall Score</h3>
            <p>${review.summary}</p>
        </div>
    `;

    // Issues
    if (review.issues && review.issues.length > 0) {
        html += '<div class="issues-list">';
        html += '<h4><i class="fas fa-exclamation-triangle"></i> Issues Found</h4>';
        
        review.issues.forEach(issue => {
            html += `
                <div class="issue-item ${issue.severity}">
                    <div class="issue-header">
                        <span class="issue-type">${issue.type.replace('_', ' ')}</span>
                        <span class="issue-severity severity-${issue.severity}">${issue.severity}</span>
                    </div>
                    <div class="issue-line">Location: ${issue.line}</div>
                    <div class="issue-description">${issue.description}</div>
                    <div class="issue-suggestion">
                        <strong>Suggestion:</strong> ${issue.suggestion}
                    </div>
                </div>
            `;
        });
        
        html += '</div>';
    }

    // Strengths
    if (review.strengths && review.strengths.length > 0) {
        html += '<div class="strengths-list">';
        html += '<h4><i class="fas fa-check-circle"></i> Strengths</h4>';
        html += '<ul>';
        review.strengths.forEach(strength => {
            html += `<li>${strength}</li>`;
        });
        html += '</ul></div>';
    }

    // Recommendations
    if (review.recommendations && review.recommendations.length > 0) {
        html += '<div class="recommendations-list">';
        html += '<h4><i class="fas fa-lightbulb"></i> Recommendations</h4>';
        html += '<ul>';
        review.recommendations.forEach(rec => {
            html += `<li>${rec}</li>`;
        });
        html += '</ul></div>';
    }

    html += '</div>';
    reviewOutput.innerHTML = html;
}

// Display Quick Feedback
function displayQuickFeedback(feedback) {
    const html = `
        <div class="review-content">
            <div class="score-display">
                <div class="score-circle"><i class="fas fa-bolt"></i></div>
                <h3>Quick Feedback</h3>
            </div>
            <div class="quick-feedback">
                ${feedback.replace(/\n/g, '<br>')}
            </div>
        </div>
    `;
    reviewOutput.innerHTML = html;
}

// Utility Functions
function getSelectedFocusAreas() {
    const checkboxes = document.querySelectorAll('input[name="focus"]:checked');
    return Array.from(checkboxes).map(cb => cb.value);
}

function showLoading(show) {
    loadingOverlay.style.display = show ? 'flex' : 'none';
    reviewBtn.disabled = show;
    quickBtn.disabled = show;
}

function showError(message) {
    reviewOutput.innerHTML = `
        <div class="error-message">
            <i class="fas fa-exclamation-circle"></i>
            <h4>Error</h4>
            <p>${message}</p>
        </div>
    `;
}

function clearCode() {
    codeInput.value = '';
    codeInput.focus();
}

function clearReview() {
    reviewOutput.innerHTML = `
        <div class="placeholder">
            <i class="fas fa-code"></i>
            <h4>Your Code Review Awaits</h4>
            <p>Write or paste your code and click "Review Code" to get started</p>
        </div>
    `;
}

function exportReview() {
    const reviewText = reviewOutput.innerText;
    const blob = new Blob([reviewText], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `code-review-${new Date().toISOString().split('T')[0]}.txt`;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
}

function updateLastReviewTime() {
    const now = new Date();
    lastReview.textContent = now.toLocaleTimeString();
    localStorage.setItem('lastReviewTime', now.toISOString());
}

function loadLastReviewTime() {
    const lastTime = localStorage.getItem('lastReviewTime');
    if (lastTime) {
        const time = new Date(lastTime);
        lastReview.textContent = time.toLocaleTimeString();
    }
}

// Example code loader (for demo purposes)
function loadExampleCode() {
    const examples = {
        python: `def calculate_average(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total / len(numbers)

def find_duplicates(items):
    seen = set()
    duplicates = []
    for item in items:
        if item in seen:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates`,

        javascript: `function calculateAverage(numbers) {
    let total = 0;
    for (let i = 0; i < numbers.length; i++) {
        total += numbers[i];
    }
    return total / numbers.length;
}

function findDuplicates(items) {
    const seen = new Set();
    const duplicates = [];
    for (const item of items) {
        if (seen.has(item)) {
            duplicates.push(item);
        } else {
            seen.add(item);
        }
    }
    return duplicates;
}`
    };

    const lang = languageSelect.value;
    if (examples[lang]) {
        codeInput.value = examples[lang];
    }
}

// Add event listener for language change to load examples
languageSelect.addEventListener('change', loadExampleCode);

// Load Python example by default
window.addEventListener('load', loadExampleCode);