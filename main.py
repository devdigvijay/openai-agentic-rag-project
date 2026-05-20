from dotenv import load_dotenv
from src.openai import ChatOpenAIAssistace,OpenAIAssistace,OPEN_AI_GPT_3_TURBO



load_dotenv()

def main():
    
    last_converstion = ChatOpenAIAssistace(CHAT_OPEN_AI_MODEL)
    print('last converstion :',last_converstion)

    query = input('Question : ')
    llm_response=OpenAIAssistace(query=query,model=OPEN_AI_GPT_3_TURBO)
    print('llm resoponse : ',llm_response)

if __name__ == "__main__":
    main()