from pydantic import BaseModel,ConfigDict
from app.model.models import DepartmentModel
class EmpCreate(BaseModel):
    ename:str 
    email:str
    salary:float
    empid:int
    department_id:int

class EmpUpdate(BaseModel):
    ename:str|None=None
    email:str|None=None
    salary:float|None=None
    empid:int|None=None
    department_id:int|None=None

class EmpResponse(BaseModel):
    eid:int
    ename:str 
    email:str
    salary:float
    empid:int
    department_id:int
    department:DepartmentModel
    model_config = ConfigDict(from_attributes=True)