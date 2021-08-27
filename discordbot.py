from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='!')
token = os.environ['DISCORD_BOT_TOKEN']

un_omikuji = ['大吉','中吉','小吉','小凶','中凶','大凶']
features = ["大きい","小さい","漆黒の","美しい","なんかべとついてる","大量の","おいしそうな","素朴な","豪華な","放置されてる"]
somethings = ["ハンバーガー","テレビのリモコン","小石","お隣さん","ダイヤモンド","月","とんぼの羽","床の埃","ENTERキー","ピンポン球"]

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.event
async def on_message(message):
    
    if message.author.bot:
        return

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
async def z(ctx):
    await ctx.send('ぜっとだよ！')
    
async def hello(ctx):
    await ctx.send('こんにちは！')
    
async def omikuji(ctx):
    await ctx.send('あなたの運勢は' + un_omikuji[random.randrange(5)] + '！')
    
await def item(ctx):
    await ctx.send("今日のラッキーアイテムは" + features[random.randrange(9)] + somethings[random.randrange(9)] + "！")


bot.run(token)
