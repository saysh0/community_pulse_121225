from pydantic import BaseModel

from app.schemas import *


class QuestionCreateRequest(QuestionCreate):
    pass


class QuestionUpdateRequest(QuestionUpdate):
    pass


class QuestionReadResponse(QuestionRead):
    pass


class QuestionDetailResponse(QuestionRead):
    statistics: StatisticsRead | None = None


class QuestionListResponse(QuestionRead):
    pass


class QuestionResponse(BaseModel):
    items: list
    count: int


