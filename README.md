## Concerns
1. As the index is not unique, the combination of state and city can give more precise information about the country
2. It is hard to find free libraries returning country code and country from zipcode or city. Google Maps API could help, but it requires paid user. I'm aware that current library is not perfect and returns country in the original language - search of the needed library is not the key of the task
3. I'm taking a sample of 10 record to decrease the time, as each request obtaining country code from ip address requires time. Possible improvements: create database that matches country and postal code, find a fast api that returns country name from the ip address.
4. The json file has a nested structure, and parsing of json into not-nested dataframe/sql is not covered.
