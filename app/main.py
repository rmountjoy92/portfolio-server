from typing import Any, Dict, AnyStr, List, Union
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .schemas import (
    AllDataModel,
    InfoModel,
    SkillModel,
    EducationModel,
    ExperienceModel,
    ProjectModel,
    HobbyModel,
    ReferenceModel,
    DebugInput,
    DebugOutput
)
from .resume import (
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
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


JSONObject = Dict[AnyStr, Any]
JSONArray = List[Any]
JSONStructure = Union[JSONArray, JSONObject]


@app.post(
    "/debug",
    tags=["Testing"],
    name="Debug",
)
async def debug(debug_input: JSONStructure = None):
    """
    Print and return the data posted
    """
    print(debug_input)
    return {"resp": debug_input}
