# Четность
# from isOdd import isOdd
# print(isOdd(1)) 
# print(isOdd(4)) 

# Прогресс
# from progress.bar import Bar
# import time

# bar = Bar('Processing', max=20)
# for i in range(20):
#     # Do some work
#     time.sleep(1)
#     bar.next()
# bar.finish()

# Эмоджи
# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))
# print(emoji.emojize('Python is :thumbsup:', language='alias'))
# print(emoji.demojize('Python is 👍'))
# print(emoji.emojize("Python is fun :red_heart:"))
# print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
# #red heart, not black heart
# print(emoji.is_emoji("👍"))

# Математические графики
# import matplotlib.pyplot as plt
# import numpy as np

# list = [1,2,3,2,7]
# plt.plot(list)

# plt.show()

# Телеграм-бот
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_comands import *

app = ApplicationBuilder().token("5618054654:AAF35ko-OlsnC7D0HIPQ8HFXOtHQJpOQehA").build()

app.add_handler(CommandHandler("hi", hi_comand))
app.add_handler(CommandHandler("time", time_comand))
app.add_handler(CommandHandler("help", help_comand))
app.add_handler(CommandHandler("sum", sum_comand))
print('server start')
app.run_polling()
