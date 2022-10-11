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

## Endpoint

To consume de API you can use this endpoint:

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

## Responses

### 200 - Success

```json
{
   "bestLocation": {
        "pokemonTypes": "Number of pokemons types in the best location",
        "location": "Best location name"
    }
    "locations": [
      "location": "Location name",
      "pokemons": "List of pokemons you can catch in the location"
    ]
}
```

### 400 - Location payload length

```json
{
  "errors": {
    "locations": ["Shorter than minimum length 1."]
  }
}
```

### 400 - Wrong Location

```json
{
  "error": "canalave-city is not located on Kanto region"
}
```

### 400 - Pokemon API Error

```json
{
  "error": "Pokemon API call fail"
}
```
