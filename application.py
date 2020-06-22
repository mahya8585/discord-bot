import os
import random
import discord
from flask import Flask
from threading import Thread

app = Flask(__name__)
client = discord.Client()


@client.event
async def on_message(msg):
    """bot動作本体の処理。チャネルにメッセージ送付されたときの処理"""
    message = msg.content
    if message.startswith('/choice'):
        await msg.channel.send('システムテストOK')
        # words = message.split()
        #
        # if (len(words) >= 2) and (words[1].isdecimal()):
        #     # メッセージ第一引数までの数字をランダム選択する
        #     try:
        #         target = [x for x in range(int(words[1]))]
        #     except:
        #         await msg.channel.send('エラーが発生しました。第一引数には半角数字(1以上)を入力してください。')
        #
        #     decide = random.choice(target)
        #     await msg.channel.send(str(decide) + 'でおねがいします!!!')
        #
        # else:
        #     # validation error
        #     await msg.channel.send('いくつまでの数字から選択するのか指定してください。1より大きい数字を入力してください。')


@app.route('/')
def health():
    """アプリ(bot)の生存確認"""
    return 'Bot is alive now.'


def run():
    """Flaskの実行"""
    app.run()


if __name__ == '__main__':
    # アプリ(bot)の起動
    server = Thread(target=run)
    server.start()

    # discordとの接続
    client.run(os.environ('DISCORD_TOKEN'))
