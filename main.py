from db import database
from tags_metadata import metadata
from handlers import faculty
from handlers.authorization import check_student_existance 
from handlers.authorization import registration
from handlers.authorization import auth
from handlers import me, user, user_request, bed_places, role, hostel, course, speciality, student

import logging
from logging.config import dictConfig
from loggers import dict_config

dictConfig(dict_config)

logger = logging.getLogger('root-logger')



from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

router = APIRouter()

app = FastAPI(openapi_tags=metadata)


@app.get('/test-log/')
async def test_log():
    logger.debug('Log starts')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoints registration
app.include_router(faculty.router)
app.include_router(check_student_existance.router)
app.include_router(registration.router)
app.include_router(auth.router)
app.include_router(me.router)
app.include_router(user.router)
app.include_router(user_request.router)
app.include_router(bed_places.router)
app.include_router(role.router)
app.include_router(hostel.router)
app.include_router(course.router)
app.include_router(speciality.router)
app.include_router(student.router)
app.include_router(router)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
