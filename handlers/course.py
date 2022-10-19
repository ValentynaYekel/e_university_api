from models.course import course
from schemas.course import CourseListOut
from handlers.current_user import get_current_user

from db import database
from typing import List

from fastapi import APIRouter, Depends

from schemas.jsend import JSENDOutSchema


router = APIRouter()


@router.get("/courses/", response_model=JSENDOutSchema[List[CourseListOut]], tags=["Admin dashboard"])
async def read_courses_list(auth=Depends(get_current_user)):
    query = course.select()
    return JSENDOutSchema[List[CourseListOut]](
        data=await database.fetch_all(query),
        message="Get all courses"
    )
