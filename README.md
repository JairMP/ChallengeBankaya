# Documentation

## Installation

Setup a virtualenv and activate.

```sh
pip install virtualenv
virtualenv env
source env/bin/activate
```

Setup the project.

```sh
make setup
```

## Start API

To start the API run.

```sh
make start
```

## Test

Run Tests.

```sh
make tests
```

## Endpoints

To consume de API you can use this endpoints:

```sh
POST http://127.0.0.1:5000/pokemon-in-location
```

You most send a JSON payload with the pokemon locations.

```json
{
  "locations": [
    "viridian-forest",
    "pallet-town",
    "kanto-route-22",
    "digletts-cave",
    "birth-island"
  ]
}
```
