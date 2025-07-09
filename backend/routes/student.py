from fastapi import APIRouter, HTTPException, Path
from pydantic import BaseModel, EmailStr, Field
from uuid import uuid4
from uuid import UUID
from typing import Dict
from services.ollama import generate_summary_for_student
import asyncio

router = APIRouter(prefix="/student", tags=["Students"])
students_lock = asyncio.Lock()

# -------------------------
# In-memory storage
# -------------------------
students: Dict[str, dict] = {}

# -------------------------
# Pydantic models
# -------------------------
class StudentCreateDTO(BaseModel):
    name: str
    age: int = Field(..., ge=0, le=150)
    email: EmailStr

class StudentResponseDTO(StudentCreateDTO):
    id: str


#Create a Student
@router.post("/", response_model=StudentResponseDTO)
async def create_student(student: StudentCreateDTO):
    async with students_lock:
        for s in students.values():
            if s["email"] == student.email:
                raise HTTPException(status_code=400, detail="Student with this email already exists")
        
        student_id = str(uuid4())
        students[student_id] = student.dict()
    
    return {**student.dict(), "id": student_id}



#Get all Students
@router.get("/", response_model=list[StudentResponseDTO])
async def get_all_students():
    return [{**s, "id": sid} for sid, s in students.items()]


#Get Student by ID
@router.get("/{student_id}", response_model=StudentResponseDTO)
async def get_student_by_id(student_id: UUID):
    sid = str(student_id)
    student = students.get(sid)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return {**student, "id": sid}

#Update Student by ID
@router.put("/{student_id}", response_model=StudentResponseDTO)
async def update_student(student_id: UUID, updated: StudentCreateDTO):
    sid = str(student_id)
    async with students_lock:
        if sid not in students:
            raise HTTPException(status_code=404, detail="Student not found")
        students[sid] = updated.dict()
    return {**updated.dict(), "id": sid}




#Delete Student by ID
@router.delete("/{student_id}", status_code=204)
async def delete_student(student_id: UUID):
    sid = str(student_id)
    async with students_lock:
        if sid not in students:
            raise HTTPException(status_code=404, detail="Student not found")
        del students[sid]



#Summary of Student with Ollama
@router.get("/{student_id}/summary")
async def get_student_summary(student_id: UUID):
    sid = str(student_id)
    student = students.get(sid)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    summary = generate_summary_for_student(
        name=student["name"],
        age=student["age"],
        email=student["email"]
    )
    return {"summary": summary}

