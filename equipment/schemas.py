# forum/schemas.py
from djantic import ModelSchema

from .models import Equipment, TypeOfEquipment

__all__ = ["CreateEquipmentSchema", "EquipmentSchema", "TypeOfEquipmentSchema"]


class TypeOfEquipmentSchema(ModelSchema):

    class Config:
        model = TypeOfEquipment
        exclude = ("equipment_set", "musicpart_set",)


class EquipmentSchema(ModelSchema):
    type: object

    class Config:
        model = Equipment
        exclude = ("id",)


class CreateEquipmentSchema(ModelSchema):
    type: str

    class Config:
        model = Equipment
        include = (
            "name",
            "type",
            "state",
            "description",
            "register_date",
        )

