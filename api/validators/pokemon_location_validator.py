from marshmallow import Schema, fields, validate


class PokemonLocationPayloadSchema(Schema):
    locations = fields.List(fields.String(), required=True,
                            validate=validate.Length(min=1))


class LocationSchema(Schema):
    location = fields.String()
    pokemons = fields.List(fields.String())


class BestLocationSchema(Schema):
    location = fields.String()
    pokemon_types = fields.Number(
        attribute="pokemonTypes", data_key="pokemonTypes")


class PokemonLocationResponseSchema(Schema):
    best_location = fields.Nested(
        BestLocationSchema, data_key="bestLocation", attribute="bestLocation")
    locations = fields.List(fields.Nested(LocationSchema))
