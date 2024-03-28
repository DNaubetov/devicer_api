from typing import List
from beanie import PydanticObjectId
from database.connection import Database
from fastapi import APIRouter, HTTPException, status
from models.computers import Computer, ComputerUpdate

computers_router = APIRouter(
    tags=["Computers"]
)

computers_database = Database(Computer)


@computers_router.get("/", response_model=List[Computer])
async def retrieve_all_computers() -> List[Computer]:
    controllers = await computers_database.get_all()
    return controllers


@computers_router.get("/{id}", response_model=Computer)
async def retrieve_computer(id: PydanticObjectId) -> Computer:
    controller = await computers_database.get(id)
    if not controller:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Computers with supplied ID does not exist"
        )
    return controller


@computers_router.post("/new")
async def create_computer(body: Computer) -> dict:
    data = list()
    user_all_data_db = await Computer.find(Computer.user_name == body.user_name).to_list()
    for user in user_all_data_db:
        setattr(user, 'id', None)
    print(user_all_data_db[-1] == body)
    if body in user_all_data_db:
        return {"message": "Данный пользователь уже в системе есть"}

    # await computers_database.save(body)
    return {
        "message": "Computers created successfully"
    }


@computers_router.put("/{id}", response_model=Computer)
async def update_computer(id: PydanticObjectId, body: ComputerUpdate) -> Computer:
    updated_controller = await computers_database.update(id, body)
    if not updated_controller:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Computers with supplied ID does not exist"
        )
    return updated_controller


@computers_router.delete("/{id}")
async def delete_computer(id: PydanticObjectId) -> dict:
    controller = await computers_database.delete(id)
    if not controller:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Computers with supplied ID does not exist"
        )
    return {
        "message": "Computers deleted successfully."
    }
