from pydantic import BaseModel, Field
from typing import List, Optional
from enum import Enum

class IssueSeverity(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class IssueType(str, Enum):
    BUG = "bug"
    SECURITY = "security"
    PERFORMANCE = "performance"
    STYLE = "style"
    BEST_PRACTICE = "best_practice"
    DOCUMENTATION = "documentation"

class SuggestionImpact(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class SuggestionEffort(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class CriticalIssue(BaseModel):
    type: IssueType
    severity: IssueSeverity
    line: str
    description: str
    suggestion: str
    code_example: Optional[str] = None

class ImprovementSuggestion(BaseModel):
    category: str
    suggestion: str
    impact: SuggestionImpact
    effort: SuggestionEffort

class QualityMetrics(BaseModel):
    readability: int = Field(ge=0, le=10)
    maintainability: int = Field(ge=0, le=10)
    security: int = Field(ge=0, le=10)
    performance: int = Field(ge=0, le=10)
    documentation: int = Field(ge=0, le=10)

class CodeReviewResponse(BaseModel):
    overall_score: int = Field(ge=0, le=100)
    summary: str
    quality_metrics: QualityMetrics
    critical_issues: List[CriticalIssue]
    improvement_suggestions: List[ImprovementSuggestion]
    positive_aspects: List[str]
    language_specific_notes: List[str]

class QuickFeedbackResponse(BaseModel):
    key_points: List[str]
    overall_impression: str
    priority_actions: List[str]