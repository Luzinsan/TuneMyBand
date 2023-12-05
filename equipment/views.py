from fastapi import APIRouter, Depends

from accounts.models import User
from utils.auth import UserAuthentified
from utils.page import PageRequest, PageResponse, paginate

from .models import Equipment, TypeOfEquipment
from .schemas import CreateEquipmentSchema, EquipmentSchema, TypeOfEquipmentSchema

router = APIRouter()


@router.get("/types_of_equipments", response_model=PageResponse[TypeOfEquipmentSchema])
def list_types_equipments(page: PageRequest = Depends()):
    types = TypeOfEquipment.objects.all()
    return paginate(page, types)


@router.post("/equipment", response_model=EquipmentSchema)
def list_user_equipments(post: CreateEquipmentSchema, user: User = UserAuthentified):
    type_of_equipment = TypeOfEquipment.objects.get(name=post.type)
    post.type = type_of_equipment
    equipment = Equipment.objects.create(owner=user, **post.dict())
    return EquipmentSchema.from_django(equipment)


@router.get("/equipments/mine", response_model=PageResponse[EquipmentSchema])
def list_user_equipments(page: PageRequest = Depends(), user: User = UserAuthentified):
    equipments = Equipment.objects.filter(owner=user)
    return paginate(page, equipments)
