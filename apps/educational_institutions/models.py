from sqlalchemy import (MetaData, Column, INTEGER, VARCHAR, ForeignKey, Table, JSON)
from sqlalchemy.orm import relationship

from apps.common.db import Base

metadata_obj = MetaData()


class University(Base):
    __tablename__ = "university"

    university_id = Column(INTEGER, primary_key=True, nullable=False)
    university_name = Column(VARCHAR(length=255), nullable=False)
    logo = Column(VARCHAR(length=255))
    rector_id = Column(INTEGER, ForeignKey("rector.rector_id"))

    rector = relationship("Rector", back_populates="university")
    faculties = relationship("Faculty", back_populates="university")
    hostels = relationship("Hostel", back_populates="university")
    requisites = relationship("Requisites", back_populates="university")
    user_request_reviews = relationship("UserRequestReview", back_populates="university")
    user_request = relationship("UserRequest", back_populates="university")

    def __repr__(self):
        return f'{self.__class__.__name__}(university_id="{self.university_id}", university_name="{self.university_name}",' \
               f'logo="{self.logo}", rector_id="{self.rector_id}")'


class Faculty(Base):
    __tablename__ = 'faculty'

    faculty_id = Column(INTEGER, primary_key=True, nullable=False)
    name = Column(VARCHAR(length=255), nullable=False)
    shortname = Column(VARCHAR(length=20))
    main_email = Column(VARCHAR(length=50))
    dekan_id = Column(INTEGER, ForeignKey('dekan.dekan_id'))
    university_id = Column(INTEGER, ForeignKey("university.university_id"), nullable=False)

    dekan = relationship("Dekan", back_populates="faculties")
    university = relationship("University", back_populates="faculties")
    speciality = relationship("Speciality", back_populates="faculties")
    student = relationship("Student", back_populates="faculties")
    faculty = relationship("UserFaculty", back_populates="faculties")
    user_request = relationship("UserRequest", back_populates="faculties")

    def __repr__(self):
        return f'{self.__class__.__name__}(faculty_id="{self.faculty_id}", name="{self.name}", shortname="{self.shortname}", ' \
               f'main_email="{self.main_email}", dekan_id="{self.dekan_id}", university_id="{self.university_id}")'


class Speciality(Base):
    __tablename__ = 'speciality'

    speciality_id = Column(INTEGER, primary_key=True, nullable=False)
    code = Column(INTEGER, nullable=False)
    name = Column(VARCHAR(length=255), nullable=False)
    faculty_id = Column(INTEGER, ForeignKey("faculty.faculty_id"), nullable=False)

    faculties = relationship("Faculty", back_populates="speciality")
    student = relationship("Student", back_populates="specialties")

    def __repr__(self):
        return f'{self.__class__.__name__}(speciality_id="{self.speciality_id}",code="{self.code}",name="{self.name}",' \
               f'faculty_id="{self.faculty_id}")'


class Dekan(Base):
    __tablename__ = 'dekan'

    dekan_id = Column(INTEGER, primary_key=True, nullable=False)
    full_name = Column(VARCHAR(length=255), nullable=False)

    faculties = relationship("Faculty", back_populates="dekan")

    def __repr__(self):
        return f'{self.__class__.__name__}(dekan_id="{self.dekan_id}", full_name="{self.full_name}")'


class Rector(Base):
    __tablename__ = 'rector'

    rector_id = Column(INTEGER, primary_key=True, nullable=False)
    full_name = Column(VARCHAR(length=255), nullable=False)

    university = relationship("University", back_populates="rector")

    def __str__(self):
        return f'{self.__class__.__name__}(rector_id="{self.rector_id}",full_name="{self.full_name}")'


class Course(Base):
    __tablename__ = 'course'

    course_id = Column(INTEGER, primary_key=True, nullable=False)
    value = Column(INTEGER, nullable=False)

    student = relationship('Student', back_populates='courses')

    def __repr__(self):
        return f'{self.__class__.__name__}(course_id="{self.course_id}", value="{self.value}")'


faculty_list_view = Table('faculty_list_view', metadata_obj,
                          Column('faculty_id', INTEGER),
                          Column('name', VARCHAR(255)),
                          Column('shortname', VARCHAR(20)),
                          Column('main_email', VARCHAR(50)),
                          Column('university_id', INTEGER),
                          Column('dekan_id', INTEGER),
                          Column('dekan_full_name', VARCHAR(255)))

speciality_list_view = Table('speciality_list_view', metadata_obj,
                             Column('faculty_id', INTEGER),
                             Column('speciality_id', INTEGER),
                             Column('university_id', INTEGER),
                             Column('speciality_info', JSON))
