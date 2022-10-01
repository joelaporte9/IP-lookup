from numpy import empty
import shodan
import sys

def main():
        service = input("Enter the number of the option you'd like to search: (IP = 1, Host = 2, Summary = 3) ")
        if service == '1':
                ShodanSeach()
        elif service == '2':
                HostLookup()
        elif service == '3':
                CollctSummryInfo()
        else:
                print("please enter valid option")

def HostLookup():
        API_KEY = "eoS4KNrwEj88m7GdKssK1qquUVProIGJ"
        api = shodan.Shodan(API_KEY)
        IP = input("Enter IP address: ")

        host = api.host(IP)
        if host == empty:
                print("no data for this IP")

        # Print general info
        print("""
                IP: {}2
                Organization: {}
                Operating System: {}
        """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))

        # Print all banners
        for item in host['data']:
                print("""
                        Port: {}
                        Banner: {}

                """.format(item['port'], item['data']))

def ShodanSeach():
        API_KEY = "eoS4KNrwEj88m7GdKssK1qquUVProIGJ"
        api = shodan.Shodan(API_KEY)

        # Search Shodan
        results = api.search('apache')

        # Show the results
        print('Results found: {}'.format(results['total']))
        for result in results['matches']:
                print('IP: {}'.format(result['ip_str']))
                print(result['data'])
                print('')

#THIS FUNTION IS IN THE WORKS 
def CollctSummryInfo():
        # Configuration / API setup 

        API_KEY = "eoS4KNrwEj88m7GdKssK1qquUVProIGJ"

        # The list of properties we want summary information on

        FACETS = [
        'org',
        'domain',
        'port',
        'asn',

        # We only care about the top 3 countries, this is how we let Shodan know to return 3 instead of the
        # default 5 for a facet. If you want to see more than 5, you could do ('country', 1000) for example
        # to see the top 1,000 countries for a search query.
        ('country', 3),
        ]

        FACET_TITLES = {
        'org': 'Top 5 Organizations',
        'domain': 'Top 5 Domains',
        'port': 'Top 5 Ports',
        'asn': 'Top 5 Autonomous Systems',
        'country': 'Top 3 Countries',
        }

        # Input validation
        # if len(sys.argv) == 1:
        #         print ('Usage: %s <search query>' % sys.argv[0])
        #         sys.exit()

        # Setup the api
        api = shodan.Shodan(API_KEY)

                # Generate a query string out of the command-line arguments
        query = ' '.join(sys.argv[1:])

                # Use the count() method because it doesn't return results and doesn't require a paid API plan
                # And it also runs faster than doing a search().
        result = api.count(query, facets=FACETS)

        print ('Shodan Summary Information')
        print ('Query: %s' % query)
        print ('Total Results: %s\n' % result['total'])

                # Print the summary info from the facets
        for facet in result['facets']:
                print (FACET_TITLES[facet])

                for term in result['facets'][facet]:
                        print ('%s: %s' % (term['value'], term['count']))

                        # Print an empty line between summary info
                print ('')


main()