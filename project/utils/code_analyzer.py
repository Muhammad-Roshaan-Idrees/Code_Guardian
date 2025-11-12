import os
from typing import Dict, List
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env file
load_dotenv()


class AdvancedCodeAnalyzer:
    def __init__(self):
        """Initialize Gemini model"""
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY environment variable is required")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash")

    # ---------------------------------------------------------------------
    # Comprehensive Code Review
    # ---------------------------------------------------------------------
    def analyze_code(self, code: str, language: str, focus_areas: List[str]) -> Dict:
        """Performs a detailed code review using Gemini."""
        try:
            focus_text = ", ".join(focus_areas)
            prompt = f"""
You are a senior software engineer performing a detailed code review.

Language: {language}
Focus areas: {focus_text}

Review the following code:
```{language}
{code}
```

Provide a detailed analysis covering the focus areas. Structure your response as a JSON object with keys: 'issues' (list of strings), 'suggestions' (list of strings), 'rating' (string out of 10).
"""
            response = self.model.generate_content(prompt)
            # Assuming the response is valid JSON text
            import json
            result = json.loads(response.text)
            return result
        except Exception as e:
            return {"error": str(e)}

