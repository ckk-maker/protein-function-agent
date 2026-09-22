"""
    9.22:
    - 图的构建
    - 完成到任务规划node
"""
from src.protein_researcher.state import ResearchState,ResearchStateIn,ResearchStateOut
from langgraph.graph import START, END, StateGraph
from typing_extensions import Literal




# TODO: 各个node的函数定义

# 问题分析
def analyze_question(state:ResearchState):
    """
        对问题进行分析，得到所要研究的topic和具体的scope
    :param
        state: 当前只有question
    :return:
        research_topic和research_scope，包括任务类型、聚焦点、具体维度
    """
    pass


# 任务规划
def plan_subtask(state:ResearchState):
    """
        依据topic和scope去规划具体的子任务，并初始化当前正在处理的子任务
    :param
        state: research_topic和research_scope
    :return:
        一系列subtask
    """
    pass


# 任务执行
def subtask(state:ResearchState):
    pass


# 检索生成
def generate_query(state:ResearchState):
    pass


# 检索执行
def search(state:ResearchState):
    pass


# 证据生成
def extract_evidence(state:ResearchState):
    pass


# 反思
def reflect(state:ResearchState):
    pass


# 答案总结
def summarize(state:ResearchState):
    pass


def route_reflect(state:ResearchState)\
        -> Literal["subtask","generate_query","summarize"]:
    pass




def build_graph():
    builder=StateGraph(
        ResearchState,
        input_schema=ResearchStateIn,
        output_schema=ResearchStateOut,
    )

    builder.add_node("analyze_question",analyze_question)
    builder.add_node("plan_subtask",plan_subtask)
    builder.add_node("subtask",subtask)
    builder.add_node("generate_query",generate_query)
    builder.add_node("search",search)
    builder.add_node("extract_evidence",extract_evidence)
    builder.add_node("reflect",reflect)
    builder.add_node("summarize",summarize)

    builder.add_edge(START,"analyze_question")
    builder.add_edge("analyze_question","plan_subtask")
    builder.add_edge("plan_subtask","subtask")
    builder.add_edge("subtask","generate_query")
    builder.add_edge("generate_query","search")
    builder.add_edge("search","extract_evidence")
    builder.add_edge("extract_evidence","reflect")
    builder.add_conditional_edges("reflect",route_reflect)
    builder.add_edge("summarize",END)

    return builder.compile()


graph = build_graph()


