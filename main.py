from dotenv import load_dotenv
from src.openai import ChatOpenAI_Assistace,OpenAI_Assistace,Generate_Embbedings_From_Query,OPEN_AI_GPT_3_TURBO,OPEN_AI_GPT_5_MINI,OPEN_AI_EMBEDDING_MODEL_SMALL



load_dotenv()

def main():
    
    last_converstion = ChatOpenAI_Assistace(OPEN_AI_GPT_3_TURBO)
    print('last converstion :',last_converstion)

    query = input('Question : ')
    llm_response = OpenAI_Assistace(query=query,model=OPEN_AI_GPT_3_TURBO)
    print('llm resoponse : ',llm_response)

    query = input('Question : ')
    response = Generate_Embbedings_From_Query(query=query,model=OPEN_AI_EMBEDDING_MODEL_SMALL,dim=32)
    print(response)


if __name__ == "__main__":
    main()