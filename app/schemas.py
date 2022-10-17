from typing import List
from pydantic import BaseModel
from enum import Enum


class InfoModel(BaseModel):
    name: str
    title: str
    email: str
    location: str
    github_profile: str
    headshot: str
    cover: str


class SkillType(str, Enum):
    backend = "backend"
    frontend = "frontend"
    devops = "devops"
    other = "other"


class SkillModel(BaseModel):
    name: str
    type: SkillType


class EducationModel(BaseModel):
    years: str
    major: str
    school: str


class ExperienceModel(BaseModel):
    date: str
    title: str
    company: str
    info: str
    duties: List[str]
    achievements: List[str]


class ProjectModel(BaseModel):
    name: str
    description: str
    urls: List[str]
    tech_used: List[str]
    achievements: List[str]
    screenshots: List[str]


class HobbyModel(BaseModel):
    name: str
    description: str


class ReferenceModel(BaseModel):
    title: str
    name: str


class AllDataModel(BaseModel):
    info: InfoModel
    skills: List[SkillModel]
    education: List[EducationModel]
    experience: List[ExperienceModel]
    projects: List[ProjectModel]
    hobbies: List[HobbyModel]
    references: List[ReferenceModel]


class DebugInput(BaseModel):
    first_name: str
    last_name: str
    ssn: str


class DebugOutput(BaseModel):
    resp: str
