from pydantic import BaseModel, Field, ConfigDict, StringConstraints
from typing import Annotated

QuestionText = Annotated[str, StringConstraints(strip_whitespace=True, min_length=5, max_length=100)]

class QuestionBase(BaseModel):
    text: QuestionText


class  QuestionCreate(QuestionBase):
    pass


class QuestionRead(QuestionBase):
    model_config = ConfigDict(from_attributes=True)
    id: Annotated[int,  Field(..., alias="id")]



class QuestionUpdate(QuestionBase):
    text: QuestionText | None = None