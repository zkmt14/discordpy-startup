# インストールした discord.py を読み込む
import discord

import random

# 自分のBotのアクセストークンに置き換えてください
TOKEN = 'ODczOTIzNDcyNjQ3MTM5MzM4.YQ_eqA.-EqyG7cyv86uOFQzXbeOI-IL1mY'

# 接続に必要なオブジェクトを生成
client = discord.Client()

un_omikuji = ['大吉','中吉','小吉','小凶','中凶','大凶']

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
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

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
