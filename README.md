# discord-bot

## ソースコード上に無い設定
### DISCORD_TOKEN の設定
Discord botのアクセストークンはソースコード上に設定していません。   
本コードはAzure WebApps上で動かすことを想定しているため、Azure WebAppsの application設定から環境変数として設定しています。   
他のシステムを使う場合はこのアクセストークン設定・取得部分の変更をお願いします。