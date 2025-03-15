import discord
from discord.ext import commands
import random

intents = discord.Intents.default() 
intents.message_content = True  
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event 
async def on_ready():
    print (f'Logged in as {bot.user}')
                          
@bot.command() 
async def hi(ctx):
    await ctx.send('Hello!')

@bot.command()
async def love(ctx):
    percentage = random.randint(0, 100)
    if percentage == 100:
        response = f'❤️ Love probability: {percentage}% - you two are a perfect match! ❤️'
    elif percentage >=90:
        response = f'❤️ Love probability: {percentage}% - you two are meant to be. period.❤️'
    elif percentage >= 70:
        response = f'❤️ Love probability: {percentage}% - I can picture you two together 😘'
    elif percentage >=50:
        response = f'❤️ Love probability: {percentage}% - there is a chance maybe 😍'
    elif percentage >=30:
        response = f'❤️ Love probability: {percentage}% - could be worse 😊'
    elif percentage <= 10:
        response = f'❤️ Love probability: {percentage}% - there is no chance for you two 😭'
    await ctx.send(response)

@bot.command()
async def rain(ctx):
    percentage = random.randint(0, 100)
    if percentage == 100:
        response = f'☔ Rain probability: {percentage}% - hide inside! ☔'
    elif percentage >=90:
        response = f'☔ Rain probability: {percentage}% - it will rain for sure! ☔'
    elif percentage >= 70:
        response = f'☔ Rain probability: {percentage}% - it will probably rain ☔'
    elif percentage >=50:
        response = f'🌧️ Rain probability: {percentage}% - it might rain ☔'
    elif percentage >=30:
        response = f'🌧️ Rain probability: {percentage}% - there is a small chance it will rain ☔'
    elif percentage <= 10:
        response = f'🌧️ Rain probability: {percentage}% - I dont think its raining today ☔'
    await ctx.send(response)

@bot.command()
async def exam(ctx):
    percentage = random.randint(0, 100)
    if percentage == 100:
        response = f'📚 Exam passing probability: {percentage}% - you will definitely pass 💅'
    elif percentage >=90:
        response = f'📚 Exam passing probability: {percentage}% - you will pass for sure 💅'
    elif percentage >= 70:
        response = f'📚 Exam passing probability: {percentage}% - you have a high chance of passing 📚'
    elif percentage >=50:
        response = f'📚 Exam passing probability: {percentage}% - you might pass 📚'
    elif percentage >=30:
        response = f'📚 Exam passing probability: {percentage}% - you have a small chance of passing 📚'
    elif percentage <= 10:
        response = f'📚 Exam passing probability: {percentage}% - prepare better, you will take the exam again anyway💅'
    await ctx.send(response)




bot.run('TOKEN') #replace TOKEN with your bot token