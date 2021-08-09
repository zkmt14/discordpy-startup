from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


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

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
