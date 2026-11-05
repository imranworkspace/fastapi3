from app.model.models import DepartmentModel
from app.schemas.dept import DeptCreate,DeptResponse,DeptUpdate
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select

async def create_single_dept(db:AsyncSession,dept_data:DepartmentModel):
    dept = DepartmentModel(
        dname=dept_data.dname
    )
    try:
        db.add(dept)
        await db.commit()
        await db.refresh(dept)
        return dept     
    except IntegrityError as esc:
        await db.rollback()
        raise HTTPException(
            status_code=409,
            detail='dept already exists into db'
        )
    
async def create_bulk_dept(db:AsyncSession,dept_data:list[DepartmentModel]):
    departments =[
         DepartmentModel(
        dname=dept.dname
    )
    for dept in dept_data
    ]
    try:
        db.add_all(departments)
        await db.commit()
        for dept in departments:
            await db.refresh(dept)
        return departments     
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=409,
            detail='dept already exists into db'
        )

async def get_all_dept(db:AsyncSession):
    depts =await db.execute(select(DepartmentModel).order_by(DepartmentModel.did))
    r = depts.scalars().all()
    if r == []:
        raise HTTPException(
            status_code=404,
            detail='department not available in database'
        )
    return r 

async def get_dept_by_depid(db:AsyncSession,dept_id:int):
    r = await db.execute(select(DepartmentModel).where(DepartmentModel.did == dept_id))
    id=r.scalar_one_or_none()
    if id is None:
        raise HTTPException(
            status_code=404,
            detail='department not available in database'
        )
    return id

async def update_dept_by_depid(db:AsyncSession,dept_id,dept_model:DeptUpdate):
    id =await get_dept_by_depid(db,dept_id)
    
    update_dept_ = dept_model.model_dump(
        exclude_unset=True
    )

    for field,value in update_dept_.items():
        setattr(id,field,value)

    await db.commit()
    await db.refresh(id)
    return id

async def delete_dept_by_depid(db:AsyncSession,dept_id):
    id =await get_dept_by_depid(db,dept_id)
    await db.delete(id)
    await db.commit()
    return HTTPException(
        status_code=200,
        detail='record deleted from db'
    )