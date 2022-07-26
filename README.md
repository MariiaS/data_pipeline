## Architecture
Main application is in the _data_pipeline_ folder.
The settings for the Docker to connect to database are stored in _database_ folder.
The selected database is postgreSQL because it's free, works well with Docker and can be easily maintained.

The Pipeline class is responsible for creating the structure for the data pipeline, it contains the main stages which can be reused during the pipeline run depending on the needs. 
In order to initialize the pipeline, input arguments needed: game name and the date in the format "YYYY-MM-DD"
The tests are stored in the tests folder and contains basic checks of the function. 

Main principles followed: 
1. Clean code - code should speak for itself, not comments
2. KISS - simple and clear code
3. PEP8 whenever possible.
4. Functional programming - create pure functions whenever possible

## Installation

### Docker installation
    docker-machine start default
    docker-machine env default
    eval $(docker-machine env default)


### Running Docker Compose
    docker-compose up --build

## Concerns
1. As the index is not unique and is mocked in data, the combination of state and city can give more precise information about the country
2. It is hard to find free libraries returning country code and country from zipcode or city. Google Maps API could help, but it requires paid user. I'm aware that current library is not perfect and returns country in the original language - search of the needed library is not the key of the task
3. I'm taking a sample of 10 record to decrease the time, as each request obtaining country code from ip address requires time. Possible improvements: create database that matches country and postal code, find a fast api that returns country name from the ip address.
4. The json file has a nested structure, and parsing of json into not-nested dataframe/sql is not covered, can be done more accurate without conversion to dataframe.
5. db could be done much better, for instance turn to lower case main fields such as gender, to have unified information in the tables
6. Also, the architecture of the database can be dome much more accurate - collect the user data at the same table from both games, create separate field for the game name

## Questions
1. Could you find what is the gender ratio in each game? -> The test is written an is executed during the application running
2. Try to list the youngest and oldest player per country. -> The test is written an is executed during the application running
3. If you suddenly had millions of new events for the accounts to process per day, how would
you make the data pipeline faster and more scalable and more reliable? 
Bonus) Can you summarize a list of principles you would follow when developing an event pipeline?
   A: I would create a scheduled pipeline, which would be executed with some time interval throughout the day, whereas before it is executed the data is stored into the files 
   with the limit of lines written, 1000 per file. The name of the file will include the timestamp as well, so that the application could execute files one by one.
