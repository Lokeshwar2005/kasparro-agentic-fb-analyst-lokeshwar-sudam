from pydantic import BaseModel, Field
from typing import List

# --- INSIGHTS.JSON Schema ---
class Hypothesis(BaseModel):
    """A single, data-driven explanation for a performance change."""
    driver: str = Field(description="The potential driver of the ROAS change.")
    hypothesis: str = Field(description="The specific hypothesis to be validated.")
    confidence: float = Field(description="A numerical confidence score from 0.0 to 1.0 before validation.", ge=0.0, le=1.0)
    validation_evidence: str = Field(description="The quantitative evidence found by the Evaluator Agent.")
    final_confidence: float = Field(description="The numerical confidence score from 0.0 to 1.0 after validation.", ge=0.0, le=1.0)

class Insights(BaseModel):
    """The structured output for all hypotheses and their validation."""
    summary_of_change: str = Field(description="A concise summary of the ROAS fluctuation.")
    hypotheses: List[Hypothesis]

# --- CREATIVES.JSON Schema ---
class CreativeIdea(BaseModel):
    """A recommended creative message for a low-CTR campaign."""
    campaign_name: str = Field(description="The name of the low-CTR campaign this creative targets.")
    original_message_theme: str = Field(description="The thematic core of the original, underperforming creative message.")
    new_headline: str = Field(description="A proposed new, high-impact headline (max 8 words).")
    new_primary_message: str = Field(description="A proposed new primary message/body text, grounded in existing creative messaging themes.")
    new_cta: str = Field(description="A proposed new Call-to-Action (CTA).")
    reasoning: str = Field(description="Explain why this new creative direction is expected to improve CTR.")

class CreativeRecommendations(BaseModel):
    """The structured output for all creative recommendations."""
    low_ctr_campaigns_analyzed: List[str]
    recommendations: List[CreativeIdea]
