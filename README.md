[![Coverage Status](https://coveralls.io/repos/github/Joshuakemboi/Politic_API/badge.svg?branch=develop)](https://coveralls.io/github/Joshuakemboi/Politic_API?branch=develop)
[![Build Status](https://travis-ci.org/Joshuakemboi/Politic_API.svg?branch=develop)](https://travis-ci.org/Joshuakemboi/Politic_API)

# Politic_API
## Summary

Politico-api is a backend application that implements the voting process of country where users politicians can run for different political offices and be voted in by the users. The admin can create political parties and offices

This project is managed by pivotal tracker board. view the board [here]
https://www.pivotaltracker.com/n/projects/2242376


## The following are API endpoints enabling one to:
  -  Create account and log in
  -  Create a political party
  -  Fetch a specific political party
  -  Fetch all political parties
  -  Edit a specific political party
  -  Delete a specific political party
  -  Create a political office
  -  Fetch all political offices
  -  Create candidate for a specific office election
  -  Vote for a candidate for a specific office election

## Pre-requisites
  -  Postman
  -  Git
  -  Python3

## Testing

  -  Clone this repository to your computer:

git clone: https://github.com/Joshuakemboi/Politic_API.git

  -  cd into this folder:

Politico-api

  -  Create a virtual environment

python3 -m venv venv

  -  Activate the virtual environment

source venv/bin/activate

  -  Switch to 'develop' branch

git checkout develop

  -  Install requirements

pip3 install -r requirements.txt

  -  Run app

python3 run.py

  - Run tests

pytest

## Deployment

1.https://joshpoliticapi-api-heroku.herokuapp.com/api/v1/party

2.https://joshpoliticapi-api-heroku.herokuapp.com/api/v1/office

3.https://joshpoliticapi-api-heroku.herokuapp.com/api/v1/user

## Party endpoints
For the endpoint it only takes the following data

  {

   "party_logo_url":string,

   "party_name":string,

   "party_headquarters_address":string

  }
## office endpoints

For the endpoint it only takes the following data

  {

    "office_name" : String, 

    "office_type" : String
  }



## Use Postman to test following working Endpoinsts


| Endpoint  | Functionality |
| ------------- | ------------- |
| POST/users  | Create a user record  |
| GET/users/<user_id>  | Fetch a specific user record  |
| PUT /users/<user_id>/  | Edit a user  |
| DELETE /users/<users_id>  | Delete a user  |
| POST/party  | Create a politcal party record  |
| GET/party/<party-id>  | Fetch a specific politcal party record  |
| GET/party/<party-id>  | Fetch a all politcal party record  |
| PUT /party/<party_id>  | Edit a political party  |
| DELETE /party/<party-id>  | Delete a politcal party  |
| POST/office  | Create a political office  |
| GET/office/<office-id>  | Fetch a specific politcal office record  |
| GET /offices  | Fetch all political offices records  |

## Authors
kemboijoshua- Github-[kemboijoshua](https://github.com/Joshuakemboi/Politic_API)

## License

This project is licensed under the MIT license. See [LICENSE](https://github.com/Joshuakemboi/Politic_API/blob/develop/LICENSE)

## Contribution

Fork this repository, contribute, and create a pull request to this repo's gh-pages branch.

## Acknowledgements
  -  Andela workshops.
  -  Andela Bootcamp Team 9members
