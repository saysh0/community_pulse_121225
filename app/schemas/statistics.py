from typing import Annotated
from pydantic import BaseModel, Field, computed_field


class StatisticsBase(BaseModel):
    pass


class StatisticsRead(StatisticsBase):
    question_id: int
    agree_count: int
    disagree_count: int


    @computed_field
    @property
    def total_count(self) -> int:
        return self.agree_count + self.disagree_count