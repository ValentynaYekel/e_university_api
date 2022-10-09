from models.course import course
from schemas.course import CourseListOut
from handlers.current_user import get_current_user

from db import database
from typing import List

from fastapi import APIRouter, Depends

import logging
from logging.config import dictConfig

from e_university_api.loggers import dict_config

dictConfig(dict_config)

logger = logging.getLogger('root-logger')

router = APIRouter()


@router.get("/courses/", response_model=List[CourseListOut], tags=["Admin dashboard"])
# async def read_courses_list(auth = Depends(get_current_user)):
async def read_courses_list():
    logger.debug('Debug')
    query = course.select()
    return await database.fetch_all(query)
