from datetime import datetime
from typing import Dict, Union
from components.exceptions import BackendException
from pydantic import BaseModel, validator


class StudentCheckExistanceIn(BaseModel):   # TODO syntax error
    full_name: str
    telephone_number: str


class StudentCheckExistanceOut(BaseModel):
    student: int
    token: str
    expires: datetime


class CreateStudentIn(BaseModel):
    full_name: str
    telephone_number: str
    course_id: int
    faculty_id: int
    speciality_id: int
    gender: str

    @validator('full_name')
    def validate_full_name(value):  # TODO may be there is need to use staticmethod decorator
        full_name = value.split()   # TODO use hint or so
        if not full_name or len(full_name) < 2:
            raise BackendException(message="The student's name and surname are mandatory!")
        return value
    
    @validator('telephone_number')
    def validate_telephone_number(value):   # TODO may be there is need to use staticmethod decorator
        if not value:
            raise BackendException(message='The phone number cannot be empty!')
        elif len(str(value)) != 12:
            raise BackendException(message='The phone number must contain 12 digits!')
        return value

    @validator('course_id')
    def validate_course_id(value):  # TODO may be there is need to use staticmethod decorator
        if not value:
            raise BackendException(message='The course cannot be empty!')
        elif value not in range(1, 7):
            raise BackendException(message='The course must be between 1 and 6!')
        return value

    @validator('speciality_id')
    def validate_speciality_id(value):
        if not value:
            raise BackendException(message='The specialty cannot be empty!')
        return value

    @validator('faculty_id')
    def validate_faculty_id(value):
        if not value:
            raise BackendException(message='The faculty cannot be empty!')
        return value

    @validator('gender')
    def validate_gender(value):
        exists_genders = ['Ч', 'М']
        if not value: 
            raise BackendException(message='The student gender cannot be empty!')
        if value.upper() not in exists_genders:     # TODO use hint or so
            raise BackendException(message='Choose your gender from the list provided.')
        return value


class CreateStudentOut(BaseModel):
    student_id: int       


class StudentsListOut(BaseModel):
    student_id: int       
    student_full_name: str
    telephone_number: str
    user_id: int = None
    university_id: int
    faculty_id: int
    speciality_id: int
    course_id: int
    gender: str


class DeleteStudentIn(BaseModel):
    student_id: int