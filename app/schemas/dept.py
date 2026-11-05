from pydantic import BaseModel

class DeptCreate(BaseModel):
    dname:str 

class DeptUpdate(BaseModel):
    did:int|None=None
    dname:str|None=None

class DeptResponse(BaseModel):
    did:int 
    dname:str