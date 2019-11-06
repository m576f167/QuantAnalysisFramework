from mongoengine import Document
from mongoengine.fields import (
    StringField
)

class AssetUniverseModel(Document):
    """
    A model for asset universe
    """
    symbol = StringField(primary_key = True, required = True)
    meta = {'collection': 'AssetUniverse'}
