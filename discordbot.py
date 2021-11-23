from discord.ext import commands
import os
import traceback
import random
bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

un_omikuji = ['大吉','中吉','小吉','小凶','中凶','大凶']
features = ["大きい","小さい","漆黒の","美しい","なんかべとついてる","大量の","おいしそうな","のりしおの匂いがする","しめった","放置されてる","カビくさい","青白く光り輝く","妖艶な","超絶怒涛の","アメリカ在住"]
somethings = ["回すメン"."テレビのリモコン","小石","お隣さん","ダイヤモンド","月","とんぼの羽","床の埃","ENTERキー","ピンポン球","カレーライス","ぜっと","カマドウマ","吉野家の牛丼","三ツ矢サイダー"]

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '!hello':
        await message.channel.send('こんにちは。')
    if message.content == '!z':
        await message.channel.send('ぜっとだよ！')

    if message.content == '!omikuji':
        await message.channel.send('あなたの運勢は' + un_omikuji[random.randrange(5)] + '！')

    if message.content == "!item":
        await message.channel.send("今日のラッキーアイテムは" + features[random.randrange(15)] + somethings[random.randrange(15)] + "！")

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
bot.run(token)
