class Ingredient(Model):
    name = CharField()
    description = CharField()
    quantity = DecimalField()
    measurement_type = StringField()
    recipe = ForeignKeyField(Recipe)
