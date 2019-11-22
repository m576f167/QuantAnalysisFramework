from mongoengine import Document
from mongoengine.fields import (
    BooleanField,
    StringField
)

class AssetUniverseModel(Document):
    """
    A model for asset universe
    """
    symbol = StringField(unique = True, required = True)
    asset_class = StringField()
    easy_to_borrow = BooleanField()
    exchange = StringField()
    asset_id = StringField()
    marginable = BooleanField()
    name = StringField()
    shortable = BooleanField()
    status = StringField()
    tradable = BooleanField()
    meta = {'collection': 'AssetUniverse'}
