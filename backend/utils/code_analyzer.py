import openai
import os
import json
from typing import Dict, List
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import PydanticOutputParser

from .prompt_templates import CodeReviewTemplates
from .schemas import CodeReviewResponse, QuickFeedbackResponse

class AdvancedCodeAnalyzer:
    def __init__(self):
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is required")
        
        self.llm = ChatOpenAI(
            model="gpt-4",
            temperature=0.1,
            max_tokens=4000,
            api_key=api_key
        )
        
        self.llm_quick = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.3,
            max_tokens=1000,
            api_key=api_key
        )
        
        self.review_parser = PydanticOutputParser(pydantic_object=CodeReviewResponse)
        self.feedback_parser = PydanticOutputParser(pydantic_object=QuickFeedbackResponse)
        self.templates = CodeReviewTemplates()

    def _get_reviewer_perspective(self, focus_areas: List[str]) -> str:
        if 'security' in focus_areas:
            return "security_expert"
        elif 'performance' in focus_areas:
            return "performance_analyst"
        else:
            return "senior_engineer"

    def _get_system_role(self, perspective: str) -> str:
        return self.templates.SYSTEM_ROLES.get(perspective, self.templates.SYSTEM_ROLES["senior_engineer"])

    def analyze_code(self, code: str, language: str, focus_areas: List[str]) -> Dict:
        try:
            perspective = self._get_reviewer_perspective(focus_areas)
            system_role = self._get_system_role(perspective)
            
            prompt = self.templates.COMPREHENSIVE_REVIEW.format_prompt(
                system_role=system_role,
                language=language,
                focus_areas=", ".join(focus_areas),
                code=code,
                reviewer_perspective=perspective
            )
            
            response = self.llm.invoke(prompt.to_messages())
            
            try:
                review_data = self._parse_json_response(response.content)
                validated_review = self.review_parser.parse(json.dumps(review_data))
                
                return {
                    "success": True,
                    "review": validated_review.dict(),
                    "metadata": {
                        "model_used": "gpt-4",
                        "reviewer_perspective": perspective,
                        "focus_areas": focus_areas
                    }
                }
                
            except Exception as e:
                review_data = self._extract_and_parse_json(response.content)
                return {
                    "success": True,
                    "review": review_data,
                    "metadata": {
                        "model_used": "gpt-4",
                        "reviewer_perspective": perspective,
                        "note": "Response was manually parsed due to format issues"
                    }
                }
                
        except Exception as e:
            return {
                "success": False,
                "error": f"Analysis failed: {str(e)}",
                "suggestion": "Please try again with a smaller code snippet or different focus areas."
            }

    def get_quick_feedback(self, code: str, language: str) -> Dict:
        try:
            prompt = self.templates.QUICK_FEEDBACK.format_prompt(
                language=language,
                code=code,
                focus_areas="quick assessment"
            )
            
            response = self.llm_quick.invoke(prompt.to_messages())
            
            return {
                "success": True,
                "feedback": response.content,
                "metadata": {
                    "model_used": "gpt-3.5-turbo",
                    "type": "quick_feedback"
                }
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Quick feedback failed: {str(e)}"
            }

    def security_analysis(self, code: str, language: str) -> Dict:
        try:
            prompt = self.templates.SECURITY_REVIEW.format_prompt(
                system_role=self.templates.SYSTEM_ROLES["security_expert"],
                language=language,
                code=code
            )
            
            response = self.llm.invoke(prompt.to_messages())
            
            return {
                "success": True,
                "security_review": response.content,
                "metadata": {
                    "model_used": "gpt-4",
                    "analysis_type": "security"
                }
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Security analysis failed: {str(e)}"
            }

    def performance_analysis(self, code: str, language: str) -> Dict:
        try:
            prompt = self.templates.PERFORMANCE_REVIEW.format_prompt(
                system_role=self.templates.SYSTEM_ROLES["performance_analyst"],
                language=language,
                code=code
            )
            
            response = self.llm.invoke(prompt.to_messages())
            
            return {
                "success": True,
                "performance_review": response.content,
                "metadata": {
                    "model_used": "gpt-4",
                    "analysis_type": "performance"
                }
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": f"Performance analysis failed: {str(e)}"
            }

    def _parse_json_response(self, content: str) -> Dict:
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return self._extract_and_parse_json(content)

    def _extract_and_parse_json(self, content: str) -> Dict:
        import re
        
        json_match = re.search(r'```(?:json)?\s*(.*?)\s*```', content, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                pass
        
        json_like_match = re.search(r'\{.*\}', content, re.DOTALL)
        if json_like_match:
            json_str = json_like_match.group(0)
            try:
                return json.loads(json_str)
            except json.JSONDecodeError:
                pass
        
        return {
            "overall_score": 50,
            "summary": "Analysis completed with formatting issues",
            "quality_metrics": {
                "readability": 5,
                "maintainability": 5,
                "security": 5,
                "performance": 5,
                "documentation": 5
            },
            "critical_issues": [],
            "improvement_suggestions": [
                {
                    "category": "formatting",
                    "suggestion": "The analysis encountered formatting issues. Consider reviewing the code manually.",
                    "impact": "low",
                    "effort": "low"
                }
            ],
            "positive_aspects": ["Code was successfully processed for analysis"],
            "language_specific_notes": ["Review completed with basic assessment"]
        }