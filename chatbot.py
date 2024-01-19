from chatterbot import chatbot
from chatterbottrainers import chatterbotcorpusTrainer
chatbot=chatbot('clonebot')
trainer=chatterbotcorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')
while True:
    user_typ=input("you:")
    response=chatbot.get_response(user_input)
    print("clonebot:",response)
