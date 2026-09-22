import operator
from typing import Annotated, List, Optional, Literal
from pydantic import BaseModel, Field



class Evidence(BaseModel):
    claim: Optional[str]=Field(default=None)
    description: Optional[str]=Field(default=None)

    method: Optional[str]=Field(default=None)
    dataset: Optional[str]=Field(default=None)
    metric: Optional[str]=Field(default=None)
    limitation: Optional[str]=Field(default=None)

    source_id: Optional[str]=Field(default=None)
    related_subtask_id: Optional[str]=Field(default=None)

class Source(BaseModel):
    id: Optional[str]=Field(default=None)
    title: Optional[str]=Field(default=None)
    url: Optional[str]=Field(default=None)
    year: Optional[int]=Field(default=None)
    doi: Optional[str]=Field(default=None)

class Scope(BaseModel):
    task_type: Optional[Literal["domain_review","other"]]=Field(default=None)   # 任务类型，当前只有领域调研
    focus:Optional[str]=Field(default=None) # 聚焦点
    dimensions:Optional[List[str]]=Field(default=None)  # 维度

class SubTask(BaseModel):
    id: Optional[str]=Field(default=None)
    question: Optional[str]=Field(default=None)
    status: Optional[Literal["done","doing","todo"]]=Field(default=None)


class SearchResult(BaseModel):
    info: Optional[str]=Field(default=None)



"""
    
"""

class ResearchStateIn(BaseModel):
    question: Optional[str]=Field(default=None)  # 研究问题

class ResearchStateOut(BaseModel):

    question:Optional[str]=Field(default=None)  # 用户原始问题
    answer:Optional[str]=Field(default=None)    # 完整回答

    key_findings:List[str]=Field(default_factory=list)      # 关键发现
    key_evidences:List[Evidence]=Field(default_factory=list)    # 核心证据
    sources:List[Source]=Field(default_factory=list)        # 来源



class ResearchState(BaseModel):

    question: Optional[str]=Field(default=None)     # 研究问题

    # 问题分析
    research_topic:Optional[str]=Field(default=None)    # 研究问题的主题
    research_scope:Optional[Scope]=Field(default=None)   #

    # 研究计划
    research_subtasks:Annotated[
        List[SubTask],
        Field(max_length=5,description="规划的子任务最多为5个"),
        Field(min_length=1,description="最少要有1个子任务")
    ]=Field(default_factory=list)                                   # 需要完成的子任务
    current_subtask_id:Optional[int]=Field(default=None)            # 当前正在处理的子任务

    # 检索过程
    search_queries:Annotated[List[str],operator.add]=Field(default_factory=list)  #检索的query
    search_results:Annotated[List[SearchResult],operator.add]=Field(default_factory=list)   # 检索的结果
    sources_gathered:Annotated[List[Source],operator.add]=Field(default_factory=list)   # 获取的来源

    # 证据和反思
    evidences: Annotated[List[Evidence],operator.add]=Field(default_factory=list)
    is_sufficient:Optional[bool]=Field(default=False)
    search_loop_count:Optional[int]=Field(default=0)










