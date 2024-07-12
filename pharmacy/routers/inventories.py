from fastapi import APIRouter, status
from fastapi.exceptions import HTTPException
import sqlalchemy.exc
from sqlalchemy import select

from pharmacy.dependencies.database import Database, AnnotatedInventory
from pharmacy.database.models.inventories import Inventory
from pharmacy.schemas.inventories import InventoryCreate, InventorySchema

router = APIRouter()



@router.post("/inventory", response_model =InventorySchema)
def create_inventory( inventory_data: InventoryCreate, db: Database ,)->Inventory:
    
   inventory= Inventory(**inventory_data.model_dump())



   try:
    db.add(inventory)
    db.commit()
    db.refresh(inventory)

    return inventory
   except sqlalchemy.exc.IntegrityError:
    db.rollback()

    
    



@router.get("/inventory", response_model=list[InventorySchema])
def get_list_of_inventory(db: Database) -> list[Inventory]:
    return db.scalars(select(Inventory)).all()
    

@router.get("/inventory/{inventory_id}", response_model=InventorySchema)
def get_inventory(inventory: AnnotatedInventory) -> Inventory:
    return inventory
    
    

@router.delete("/inventory/{inventory_id}")
def delete_inventory(inventory: AnnotatedInventory, db:Database)-> None:
        db.delete(inventory) 
        db.commit()
    