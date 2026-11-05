from app.database import Base
from sqlalchemy.orm import mapped_column,Mapped,relationship
from sqlalchemy import ForeignKey,String,Integer,Float


class DepartmentModel(Base):
    __tablename__="dept"
    did:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    dname:Mapped[str]=mapped_column(String(25),nullable=False,unique=True)
    emps:Mapped[list['EmployeeModel']] = relationship(
        back_populates="dep"
    )

class EmployeeModel(Base):
    __tablename__='emp'
    eid:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True)
    ename:Mapped[str]=mapped_column(String(75),nullable=False)
    email:Mapped[str]=mapped_column(String(100),nullable=False,unique=True)
    salary:Mapped[float]=mapped_column(Float,nullable=False)
    empid : Mapped[int]=mapped_column(ForeignKey("dept.did"),nullable=False)
    dep:Mapped[DepartmentModel] = relationship(
        back_populates="emps"
    )

