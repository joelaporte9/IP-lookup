import shodan

SHODAN_API_KEY = "eoS4KNrwEj88m7GdKssK1qquUVProIGJ"

api = shodan.Shodan(SHODAN_API_KEY)

try:
        # Search Shodan
        results = api.search('apache')

        # Show the results
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
                print('IP: {}'.format(result['ip_str']))
                print(result['data'])
                print('')
except shodan.APIError:
        print('Error: {}'.format())