
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException
import time



def generate_keyword_ideas(keywords, language_id="1000", location_ids=["1007788", "1007785", "9040246"]):
    time.sleep(0.1)
    customer_id = "4762156395"
    keyword_client = GoogleAdsClient.load_from_storage('data/google-ads.yaml', version="v15")
    client = GoogleAdsClient.load_from_storage("data/google-ads.yaml")
    service = client.get_service("KeywordPlanIdeaService")
    keyword_plan_network = client.enums.KeywordPlanNetworkEnum.GOOGLE_SEARCH
    googleads_service = keyword_client.get_service("GoogleAdsService")


    # Convert location IDs to resource names
    # location_rns = [client.get_service("GeoTargetConstantService").geo_target_constant_path(location_id) for location_id in location_ids]
    location_rns = []
    language_rn = client.get_service("GoogleAdsService").language_constant_path(language_id)

    request = client.get_type("GenerateKeywordIdeasRequest")
    request.customer_id = customer_id
    request.language = language_rn
    # request.geo_target_constants.extend(location_rns)
    request.geo_target_constants.append(
        googleads_service.geo_target_constant_path("2356")
    )
    request.keyword_plan_network = keyword_plan_network
    request.keyword_seed.keywords.extend(keywords)

    keyword_ideas = []
    try:
        response = service.generate_keyword_ideas(request=request)
        for idea in response:
            if idea.keyword_idea_metrics.avg_monthly_searches > 0:
                keyword_ideas.append({'keyword': idea.text, 'volume': idea.keyword_idea_metrics.avg_monthly_searches})
            # print(f'Keyword idea: "{idea.text}", Avg. Monthly Searches: {idea.keyword_idea_metrics.avg_monthly_searches}, Competition: {idea.keyword_idea_metrics.competition.name}')
    except GoogleAdsException as e:
        print(f'Request failed with errors: {e}')
    
    sorted_keyword_ideas = sorted(keyword_ideas, key=lambda x: x['volume'], reverse=True)

    return sorted_keyword_ideas





def get_keyword_volumes(keywords):
    time.sleep(3)

    # def generate_historical_metrics(client, customer_id):
    keyword_client = GoogleAdsClient.load_from_storage('data/google-ads.yaml', version="v15")
    googleads_service = keyword_client.get_service("GoogleAdsService")
    keyword_plan_idea_service = keyword_client.get_service("KeywordPlanIdeaService")
    request = keyword_client.get_type("GenerateKeywordHistoricalMetricsRequest")
    request.customer_id = "4762156395"

    request.keywords = keywords
    # Geo target constant 2840 is for USA.
    request.geo_target_constants.append(
        googleads_service.geo_target_constant_path("2356")
    )
    request.keyword_plan_network = (
        keyword_client.enums.KeywordPlanNetworkEnum.GOOGLE_SEARCH
    )
    # Language criteria 1000 is for English. For the list of language criteria
    # IDs, see:
    # https://developers.google.com/google-ads/api/reference/data/codes-formats#languages
    request.language = googleads_service.language_constant_path("1000")

    response = keyword_plan_idea_service.generate_keyword_historical_metrics(
        request=request
    )

    results_text = ''
    results_dict = {}
    for result in response.results:
        metrics = result.keyword_metrics
        results_text += f'{result.text} - {metrics.avg_monthly_searches}' + '\n'
        results_dict[result.text] = metrics.avg_monthly_searches
    
    return results_dict



# if __name__ == "__main__":

#     KEYWORDS = [
#   "Second Opinion Medical",
#   "Online Medical Second Opinion",
#   "Second Opinion Consultation",
#   "Cancer Second Opinion",
#   "Surgery Second Opinion",
#   "Second Opinion Doctors",
#   "Telehealth Second Opinion",
#   "Second Opinion Health",
#   "Diagnosis Second Opinion",
#   "Second Opinion Services",
#   "Expert Second Opinion",
#   "Virtual Second Opinion",
#   "Second Opinion Insurance",
#   "Second Opinion International",
#   "Orthopedic Second Opinion",
#   "Cardiology Second Opinion",
#   "Second Opinion Clinic",
#   "Pediatric Second Opinion",
#   "Second Opinion Radiology",
#   "Second Opinion Platform"
# ]

#     # KEYWORDS = ["nose surgery", "eye surgery"]  # Add your seed keywords here
#     keyword_ideas = generate_keyword_ideas(KEYWORDS)
#     # Assuming keyword_ideas is a list of dictionaries with 'keyword' and 'volume' keys

#     sorted_keyword_ideas = sorted(keyword_ideas, key=lambda x: x['volume'], reverse=True)

#     for idea in sorted_keyword_ideas:
#         print(idea['keyword'], '----------', idea['volume'])

    