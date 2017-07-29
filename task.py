class Ingredient(Model):
    name = CharField()
    description = CharField()
    quantity = DecimalField()
    measurement_type = CharField()
    recipe = ForeignKeyField(Recipe)
