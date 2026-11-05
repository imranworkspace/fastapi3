from app.crud.dept import (create_single_dept,create_bulk_dept,get_all_dept,
                           get_dept_by_depid,update_dept_by_depid,delete_dept_by_depid)
from app.schemas.dept import DeptUpdate,DeptResponse,DeptCreate
from fastapi import Depends,APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import getdb

router = APIRouter(prefix='/dept',tags=['dept'])

@router.post('/',response_model=DeptCreate)
async def insert_single_dept(dept_data:DeptCreate,db:AsyncSession=Depends(getdb)):
    return await create_single_dept(db,dept_data)

@router.post('/bulk',response_model=list[DeptCreate])
async def insert_multiple_dept(dept_data:list[DeptCreate],db:AsyncSession=Depends(getdb)):
    return await create_bulk_dept(db,dept_data)

@router.get('/',response_model=list[DeptResponse])
async def retrive_all_dept(db:AsyncSession=Depends(getdb)):
    return await get_all_dept(db)

@router.get('/{dept_id}')
async def retrive_all_dept(dept_id:int,db:AsyncSession=Depends(getdb)):
    return await get_dept_by_depid(db,dept_id)

@router.put('/{dept_id}',response_model=DeptUpdate)
async def put_(dept_id:int,dept_model:DeptUpdate,db:AsyncSession=Depends(getdb)):
    return await update_dept_by_depid(db,dept_id,dept_model)

@router.delete('/{dept_id}')
async def delete_by_deptid(dept_id:int,db:AsyncSession=Depends(getdb)):
    return await delete_dept_by_depid(db,dept_id)
