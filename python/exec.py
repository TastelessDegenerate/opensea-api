from client import RestAPIClientBase
from prettytable import PrettyTable

__rest_client = RestAPIClientBase()

def get_collection_stats(collection_slug):
    url = f"https://api.opensea.io/api/v1/collection/{collection_slug}/stats"
    response = __rest_client.get(url).json()
    # print(f"Response Dict: \n {response.__dict__}")
    return response

if __name__ == "__main__":
    projects = [
        'kaiju-kingz',
        "boredapeyachtclub",
        "doodles-official"
    ]
    table_header = [ 'project', 'floor_price', 'total_supply', 'owners', 'total_volume' ]
    t = PrettyTable(table_header)

    for collection_slug in projects:
        response = get_collection_stats(collection_slug)
        stats = response['stats']
        row = [ collection_slug, stats['floor_price'], stats['total_supply'], stats['num_owners'], stats['total_volume'] ]
        t.add_row(row)

    print("@TastelessDegen")
    print("https://github.com/TastelessDegenerate/opensea-api")
    print(t)