from langchain_openai import ChatOpenAI,OpenAI,OpenAIEmbeddings
from langchain_core.messages import HumanMessage, AIMessage,SystemMessage  


def ChatOpenAI_Assistace(model :str) -> str:
    """* these is ChatOpenAIAssistace() function for chat histry context *"""
    llm_chat_model : ChatOpenAI = ChatOpenAI(model= model)
    chat_history: list[SystemMessage | HumanMessage | AIMessage] = [SystemMessage(content='you are helpfull assistance.')]
    while True:
        user_query: str = input('Human : ')
        if user_query == 'exit':
            break
        chat_history.append(HumanMessage(content=user_query))
        response: AIMessage = llm_chat_model.invoke(chat_history)
        print(f'AI : {response.content}')
        chat_history.append(AIMessage(content=response.content))
    return chat_history 

def OpenAI_Assistace(query:str,model:str)->str:
    """this is OPEN AI LLM for query """
    llm = OpenAI(model=model,temperature=0.1)
    llm_response:str = llm.invoke(query)
    return llm_response

def Generate_Embbedings_From_Query(query:str,model:str,dim:int)->any:
    """This is for genrating embbedings from your query"""
    embedding_model = OpenAIEmbeddings(model=model,dimensions=dim)
    return  embedding_model.embed_query(query)