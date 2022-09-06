from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from schemas import (
    AllDataModel,
    InfoModel,
    SkillModel,
    EducationModel,
    ExperienceModel,
    ProjectModel,
    HobbyModel,
    ReferenceModel,
)
from resume import (
    all_data,
    info,
    skills,
    education,
    experience,
    projects,
    hobbies,
    references,
)

app = FastAPI(
    title="Ross Mountjoy's Portfolio Api",
)

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://mountjoy.tech"
    "https://api.mountjoy.tech"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/info", tags=["Resume"], response_model=InfoModel)
async def contact_info():
    """
    Get my contact info
    """
    return info


@app.get("/skills", tags=["Resume"], name="Skills", response_model=List[SkillModel])
async def resume_skills():
    """
    Get my skills
    """
    return skills


@app.get(
    "/education", tags=["Resume"], name="Education", response_model=List[EducationModel]
)
async def resume_skills():
    """
    Get my education
    """
    return education


@app.get(
    "/experience",
    tags=["Resume"],
    name="Experience",
    response_model=List[ExperienceModel],
)
async def resume_experience():
    """
    Get my experience
    """
    return experience


@app.get(
    "/projects",
    tags=["Resume"],
    name="Projects",
    response_model=List[ProjectModel],
)
async def resume_projects():
    """
    Get my coding projects
    """
    return projects


@app.get(
    "/hobbies",
    tags=["Resume"],
    name="Hobbies",
    response_model=List[HobbyModel],
)
async def resume_hobbies():
    """
    Get my hobbies
    """
    return hobbies


@app.get(
    "/references",
    tags=["Resume"],
    name="References",
    response_model=List[ReferenceModel],
)
async def resume_references():
    """
    Get my references
    """
    return references


@app.get(
    "/",
    tags=["Resume"],
    name="All Data",
    response_model=AllDataModel,
)
async def get_all():
    """
    Get my whole resume as a single JSON object
    """
    return all_data
