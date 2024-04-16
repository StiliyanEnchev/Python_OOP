from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_PERCENTAGE = 0.85
    AVAILABLE_CAMPAIGNS = {
        'HighBudgetCampaign': 1.5,
        'LowBudgetCampaign': 0.8
    }

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign: BaseCampaign) -> float:

        payment = float(campaign.budget * PremiumInfluencer.INITIAL_PAYMENT_PERCENTAGE)

        return payment

    def reached_followers(self, campaign_type: str) -> int:
        result = (self.followers * self.engagement_rate) * self.AVAILABLE_CAMPAIGNS[campaign_type]

        return int(result)


