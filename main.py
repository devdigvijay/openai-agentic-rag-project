from dotenv import load_dotenv
from src.openai import ChatOpenAIAssistace, CHAT_OPEN_AI_MODEL



load_dotenv()

def main():
    
    last_converstion = ChatOpenAIAssistace(CHAT_OPEN_AI_MODEL)
    print('last converstion :',last_converstion)

if __name__ == "__main__":
    main()