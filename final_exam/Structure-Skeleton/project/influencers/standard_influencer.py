from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_PERCENTAGE = 0.45
    AVAILABLE_CAMPAIGNS = {
        'HighBudgetCampaign': 1.2,
        'LowBudgetCampaign': 0.9
    }

    def __init__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign: BaseCampaign) -> float:

        payment = float(campaign.budget * StandardInfluencer.INITIAL_PAYMENT_PERCENTAGE)

        return payment

    def reached_followers(self, campaign_type: str) -> int:
        result = (self.followers * self.engagement_rate) * self.AVAILABLE_CAMPAIGNS[campaign_type]

        return int(result)


