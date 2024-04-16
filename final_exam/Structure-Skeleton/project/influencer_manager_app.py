from typing import List

from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:

    VALID_CAMPAIGN_TYPES = {
        'LowBudgetCampaign': LowBudgetCampaign,
        'HighBudgetCampaign': HighBudgetCampaign
    }
    VALID_INFLUENCER_TYPES = {'PremiumInfluencer': PremiumInfluencer,
                            'StandardInfluencer': StandardInfluencer
                            }


    def __init__(self):

        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):

        if influencer_type not in self.VALID_INFLUENCER_TYPES:
            return f"{influencer_type} is not an allowed influencer type."

        try:
            next(filter(lambda infl: infl.username == username, self.influencers))
            return f"{username} is already registered."
        except StopIteration:

            influencer = self.VALID_INFLUENCER_TYPES[influencer_type](username, followers, engagement_rate)
            self.influencers.append(influencer)
            return f"{username} is successfully registered as a {influencer_type}."


    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in self.VALID_CAMPAIGN_TYPES:
            return f"{campaign_type} is not a valid campaign type."

        try:
            next(filter(lambda camp: camp.campaign_id == campaign_id, self.campaigns))
            return f"Campaign ID {campaign_id} has already been created."
        except StopIteration:

            campaign = self.VALID_CAMPAIGN_TYPES[campaign_type](campaign_id, brand, required_engagement)
            self.campaigns.append(campaign)
            return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        try:
            influencer = next(filter(lambda inf: inf.username == influencer_username, self.influencers))
        except StopIteration:
            return f"Influencer '{influencer_username}' not found."

        try:
            campaing = next(filter(lambda camp: camp.campaign_id == campaign_id, self.campaigns))
        except StopIteration:
            return f"Campaign with ID {campaign_id} not found."

        if not campaing.check_eligibility(influencer.engagement_rate):
            return (f"Influencer '{influencer_username}' does not meet "
                    f"the eligibility criteria for the campaign with ID {campaign_id}.")

        calculated_payment = influencer.calculate_payment(campaing)

        if calculated_payment > 0.0:
            campaing.approved_influencers.append(influencer)
            campaing.budget -= calculated_payment
            influencer.campaigns_participated.append(campaing)

            return (f"Influencer '{influencer_username}' has successfully participated "
                    f"in the campaign with ID {campaign_id}.")

    def calculate_total_reached_followers(self):
        pass

    def influencer_campaign_report(self, username: str):
        user = next(filter(lambda u: u.username == username, self.influencers))

        return user.display_campaigns_participated()

    def campaign_statistics(self):
        result = "$$ Campaign Statistics $$"

        sorted_campaings = sorted(self.campaigns, key=lambda x: (len(x.approved_influencers), -x.budget))
        for camp in sorted_campaings:
            total_reached_followers = 0

            for influencer in camp.approved_influencers:
                total_reached_followers += influencer.reached_followers(camp.__class__.__name__)

            result += (f"\n  * Brand: {camp.brand}, Total influencers: {len(camp.approved_influencers)}, Total budget: "
                       f"${camp.budget:.2f}, Total reached followers: {total_reached_followers}")


        return result