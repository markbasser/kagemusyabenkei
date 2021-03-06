from discord.ext import commands
from discord.ext import tasks
import os
import traceback
import discord
from datetime import datetime 
import random  # おみくじで使用

token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID =702778037003092001  #チャンネルID

# 接続に必要なオブジェクトを生成
client = discord.Client()

@client.event
async def on_ready():
    """起動時に通知してくれる処理"""
    print('ログインしました')
    print(client.user.name)  # ボットの名前
    print(client.user.id)  # ボットのID
    print(discord.__version__)  # discord.pyのバージョン
    print('------')


# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    
    
    if now == '00:34':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:hai_kao:699072592987947117><:gm:699792760651120671>')   
        
    if now == '00:14':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
        
    if now == '00:15':
        channel = client.get_channel(731640211733479556)
        await channel.send('rsoak 333.33 @JPYN member  <:rock:732205759462375475> :guitar:') 
        
    if now == '00:16':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 

    if now == '01:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('🥳') 
        
    if now == '01:08':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
        
    if now == '01:10':
        channel = client.get_channel(731640211733479556)
        await channel.send('rsoak 333.33 @JPYN member  <:rock:732205759462375475> :guitar:') 
        
    if now == '01:11':
        channel = client.get_channel(731640211733479556)
        await channel.send('rsoak 333.33 @JPYN member  <:rock:732205759462375475> :guitar:') 
        
    if now == '01:13':
        channel = client.get_channel(731640211733479556)
        await channel.send('rsoak 333.33 @JPYN member  <:rock:732205759462375475> :guitar:')     
        
    if now == '01:14':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475>') 
        
    if now == '01:32':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:hai_kao:699072592987947117>')
        
    if now == '02:14':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
        
    if now == '02:16':
        channel = client.get_channel(731640211733479556)
        await channel.send('rsoak 333.33 @JPYN member  <:rock:732205759462375475> :guitar:')     
        
    if now == '02:18':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475>') 

    if now == '03:29':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:hai_kao:699072592987947117>') 
   
    if now == '04:28':
        channel = client.get_channel(731640211733479556)
        await channel.send('rsoak 333.33 @JPYN member  <:rock:732205759462375475> :guitar:')     
        
    if now == '04:29':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475>')  
        
    if now == '04:30':
        channel = client.get_channel(769753648733225010)
        await channel.send('$soak 0.001') 
        
    if now == '04:31':
        channel = client.get_channel(769283091800916029)
        await channel.send('//dream 0.01')     
        
    if now == '04:32':
        channel = client.get_channel(769753648733225010)
        await channel.send('$soak 0.001') 
        
    if now == '04:33':
        channel = client.get_channel(769283091800916029)
        await channel.send('//dream 0.01')     
        
    if now == '04:34':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001') 
        
    if now == '04:35':
        channel = client.get_channel(769069563094499358)
        await channel.send('//dream 0.01') 
        
    if now == '04:36':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001') 
        
    if now == '04:37':
        channel = client.get_channel(769069563094499358)
        await channel.send('//dream 0.01') 
        
    if now == '05:18':
        channel = client.get_channel(769753648733225010)
        await channel.send('$soak 0.001') 
        
    if now == '05:19':
        channel = client.get_channel(769283091800916029)
        await channel.send('//dream 0.01')     
        
    if now == '05:20':
        channel = client.get_channel(769753648733225010)
        await channel.send('$soak 0.001') 
        
    if now == '05:21':
        channel = client.get_channel(769283091800916029)
        await channel.send('//dream 0.01')     
        
    if now == '05:22':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001') 
        
    if now == '05:23':
        channel = client.get_channel(769069563094499358)
        await channel.send('//dream 0.01') 
        
    if now == '05:24':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001') 
        
    if now == '05:25':
        channel = client.get_channel(769069563094499358)
        await channel.send('//dream 0.01') 
        
    if now == '05:50':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:hai_kao:699072592987947117> <:hello1:713004241131667528>') 
        
    if now == '06:14':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475>') 
        
    if now == '07:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:cafe:699769671234355230>Good morning 🌎everyone.<:hai_kao:699072592987947117> \n Have a nice day today! [omikuji] or [fortune] ← for today is fortune🔮Command')
        
    if now == '07:38':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
        
    if now == '07:52':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
        
    if now == '07:55':
        channel = client.get_channel(731640211733479556)
        await channel.send('rsoak 123.45 @JPYN member  <:rock:732205759462375475> :guitar:') 
        
    if now == '07:56':
        channel = client.get_channel(731640211733479556)
        await channel.send('rsoak 333.33 @JPYN member  <:rock:732205759462375475> :guitar:') 
        
    if now == '07:57':
        channel = client.get_channel(731640211733479556)
        await channel.send('rsoak 333.33 @JPYN member  <:rock:732205759462375475> :guitar:') 
        
    if now == '07:59':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
        
    if now == '08:00':
        channel = client.get_channel(731640211733479556)
        await channel.send('rsoak 333.33 @JPYN member  <:rock:732205759462375475> :guitar:') 
        
    if now == '08:05':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
        
    if now == '08:09':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
    
    if now == '08:10':
        channel = client.get_channel(731640211733479556)
        await channel.send('rsoak 333.33 @JPYN member  <:rock:732205759462375475> :guitar:') 
        
    if now == '08:11':
        channel = client.get_channel(731640211733479556)
        await channel.send('rsoak 333.33 @JPYN member  <:rock:732205759462375475> :guitar:') 
        
    if now == '08:13':
        channel = client.get_channel(731640211733479556)
        await channel.send('rsoak 333.33 @JPYN member  <:rock:732205759462375475> :guitar:')     
        
    if now == '08:14':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475>')
        
    if now == '08:30':
        channel = client.get_channel(769753648733225010)
        await channel.send('$soak 0.001') 
        
    if now == '08:31':
        channel = client.get_channel(769283091800916029)
        await channel.send('//dream 0.01')     
        
    if now == '08:32':
        channel = client.get_channel(769753648733225010)
        await channel.send('$soak 0.001') 
        
    if now == '08:33':
        channel = client.get_channel(769283091800916029)
        await channel.send('//dream 0.01')     
        
    if now == '08:34':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001') 
        
    if now == '08:35':
        channel = client.get_channel(769069563094499358)
        await channel.send('//dream 0.01') 
        
    if now == '08:36':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001') 
        
    if now == '08:37':
        channel = client.get_channel(769069563094499358)
        await channel.send('//dream 0.01') 
        
    if now == '08:18':
        channel = client.get_channel(769753648733225010)
        await channel.send('$soak 0.001') 
        
    if now == '08:19':
        channel = client.get_channel(769283091800916029)
        await channel.send('//dream 0.01')     
        
    if now == '08:20':
        channel = client.get_channel(769753648733225010)
        await channel.send('$soak 0.001') 
        
    if now == '08:21':
        channel = client.get_channel(769283091800916029)
        await channel.send('//dream 0.01')     
        
    if now == '08:22':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001') 
        
    if now == '08:23':
        channel = client.get_channel(769069563094499358)
        await channel.send('//dream 0.01') 
        
    if now == '08:24':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001') 
        
    if now == '08:25':
        channel = client.get_channel(769069563094499358)
        await channel.send('//dream 0.01')
        
    if now == '09:14':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
          
    if now == '10:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:ge:699792780725059664>') 
        
    if now == '10:30':
        channel = client.get_channel(769753648733225010)
        await channel.send('$soak 0.001') 
        
    if now == '10:31':
        channel = client.get_channel(769283091800916029)
        await channel.send('//dream 0.01')     
        
    if now == '10:32':
        channel = client.get_channel(769753648733225010)
        await channel.send('$soak 0.001') 
        
    if now == '10:33':
        channel = client.get_channel(769283091800916029)
        await channel.send('//dream 0.01')     
        
    if now == '10:34':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001') 
        
    if now == '10:35':
        channel = client.get_channel(769069563094499358)
        await channel.send('//dream 0.01') 
        
    if now == '10:36':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001') 
        
    if now == '10:37':
        channel = client.get_channel(769069563094499358)
        await channel.send('//dream 0.01')
        
    if now == '11:14':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
        
    if now == '11:30':
        channel = client.get_channel(769753648733225010)
        await channel.send('$soak 0.001') 
        
    if now == '11:31':
        channel = client.get_channel(769283091800916029)
        await channel.send('//dream 0.01')     
        
    if now == '11:32':
        channel = client.get_channel(769753648733225010)
        await channel.send('$soak 0.001') 
        
    if now == '11:33':
        channel = client.get_channel(769283091800916029)
        await channel.send('//dream 0.01')     
        
    if now == '11:34':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001') 
        
    if now == '11:35':
        channel = client.get_channel(769069563094499358)
        await channel.send('//dream 0.01') 
        
    if now == '11:36':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001') 
        
    if now == '11:37':
        channel = client.get_channel(769069563094499358)
        await channel.send('//dream 0.01')
        
    if now == '12:10':
        channel = client.get_channel(731640211733479556)
        await channel.send('rsoak 333.33 @JPYN member  <:rock:732205759462375475> :guitar:') 
        
    if now == '12:11':
        channel = client.get_channel(731640211733479556)
        await channel.send('rsoak 456.78 @JPYN member  <:rock:732205759462375475> :guitar:') 
        
    if now == '12:13':
        channel = client.get_channel(731640211733479556)
        await channel.send('rsoak 777.77 @JPYN member  <:rock:732205759462375475> :guitar:')     
        
    if now == '12:14':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475>') 
        
    if now == '12:15':
        channel = client.get_channel(698653628176531478)
        await channel.send('/throw JPYN 150 30 EquallyDistributed')
    
    if now == '12:17':
        channel = client.get_channel(709878463733039204)
        await channel.send('/throw JPYN 150 30 EquallyDistributed')

    if now == '12:19':
        channel = client.get_channel(733238114478325790)
        await channel.send('/throw JPYN 150 30 EquallyDistributed')
        
    if now == '12:21':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw JPYN 150 30 EquallyDistributed')

    if now == '12:23':
        channel = client.get_channel(698653628176531478)
        await channel.send('/throw BGPT 333 30 EquallyDistributed')
    
    if now == '12:25':
        channel = client.get_channel(709878463733039204)
        await channel.send('/throw BGPT 333 30 EquallyDistributed')

    if now == '12:27':
        channel = client.get_channel(733238114478325790)
        await channel.send('/throw BGPT 333 30 EquallyDistributed')
        
    if now == '12:29':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw BGPT 333 30 EquallyDistributed')
        
    if now == '12:31':
        channel = client.get_channel(698653628176531478)
        await channel.send('/throw BEN 9 30 EquallyDistributed')
    
    if now == '12:33':
        channel = client.get_channel(709878463733039204)
        await channel.send('/throw BEN 9 30 EquallyDistributed')

    if now == '12:35':
        channel = client.get_channel(733238114478325790)
        await channel.send('/throw BEN 9 30 EquallyDistributed')
        
    if now == '12:37':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw BEN 9 30 EquallyDistributed')
        
    if now == '12:39':
        channel = client.get_channel(698653628176531478)
        await channel.send('/throw KENJ 1000 30 EquallyDistributed')
    
    if now == '12:41':
        channel = client.get_channel(709878463733039204)
        await channel.send('/throw KENJ 1000 30 EquallyDistributed')

    if now == '12:43':
        channel = client.get_channel(733238114478325790)
        await channel.send('/throw KENJ 1000 30 EquallyDistributed')
        
    if now == '12:45':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XPC 1.23456 30 EquallyDistributed')
        
    if now == '12:47':
        channel = client.get_channel(698653628176531478)
        await channel.send('/throw GDRH 1000 30 EquallyDistributed')
    
    if now == '12:49':
        channel = client.get_channel(709878463733039204)
        await channel.send('/throw GDRH 1000 30 EquallyDistributed')

    if now == '12:51':
        channel = client.get_channel(733238114478325790)
        await channel.send('/throw GDRH 1000 30 EquallyDistributed')
        
    if now == '12:53':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XPC 1.23456 30 EquallyDistributed')  
        
    if now == '12:55':
        channel = client.get_channel(698653628176531478)
        await channel.send('/throw SPRTS 777.333333 30 EquallyDistributed')
    
    if now == '12:57':
        channel = client.get_channel(709878463733039204)
        await channel.send('/throw SPRTS 777.333333 30 EquallyDistributed')

    if now == '12:59':
        channel = client.get_channel(733238114478325790)
        await channel.send('/throw SPRTS 777.333333 30 EquallyDistributed')
        
    if now == '13:01':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw SPRTS 789.333333 30 EquallyDistributed') 
        
    if now == '13:02':
        channel = client.get_channel(698653628176531478)
        await channel.send('/throw DOGE 0.000777 30 EquallyDistributed')
    
    if now == '13:03':
        channel = client.get_channel(709878463733039204)
        await channel.send('/throw DOGE 0.000777 30 EquallyDistributed')

    if now == '13:05':
        channel = client.get_channel(733238114478325790)
        await channel.send('/throw DOGE 0.000777 30 EquallyDistributed')
        
    if now == '13:07':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw DOGE 0.000777 30 EquallyDistributed') 
        
    if now == '13:09':
        channel = client.get_channel(698653628176531478)
        await channel.send('/throw XPC 1.7777 30 EquallyDistributed')
    
    if now == '13:11':
        channel = client.get_channel(709878463733039204)
        await channel.send('/throw XPC 1.7777 30 EquallyDistributed')

    if now == '13:13':
        channel = client.get_channel(733238114478325790)
        await channel.send('/throw XPC 1.7777 30 EquallyDistributed')
        
    if now == '13:16':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw DOGE 0.000777 30 EquallyDistributed') 

    if now == '13:18':
        channel = client.get_channel(698653628176531478)
        await channel.send('/throw XEM 0.00007777 30 EquallyDistributed')
    
    if now == '13:20':
        channel = client.get_channel(709878463733039204)
        await channel.send('/throw XEM 0.00007777 30 EquallyDistributed')

    if now == '13:22':
        channel = client.get_channel(733238114478325790)
        await channel.send('/throw XEM 0.00007777 30 EquallyDistributed')
        
    if now == '13:24':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XEM 0.00007891 30 EquallyDistributed')    
        
    if now == '13:25':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
        
    if now == '13:26':
        channel = client.get_channel(731640211733479556)
        await channel.send('rsoak 333.33 @JPYN member  <:rock:732205759462375475> :guitar:') 
        
    if now == '13:28':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
        
    if now == '13:30':
        channel = client.get_channel(769753648733225010)
        await channel.send('$soak 0.001') 
        
    if now == '13:31':
        channel = client.get_channel(769283091800916029)
        await channel.send('//dream 0.01')     
        
    if now == '13:32':
        channel = client.get_channel(769753648733225010)
        await channel.send('$soak 0.001') 
        
    if now == '13:33':
        channel = client.get_channel(769283091800916029)
        await channel.send('//dream 0.01')     
        
    if now == '13:34':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001') 
        
    if now == '13:35':
        channel = client.get_channel(769069563094499358)
        await channel.send('//dream 0.01') 
        
    if now == '13:36':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001') 
        
    if now == '13:37':
        channel = client.get_channel(769069563094499358)
        await channel.send('//dream 0.01')
     
    if now == '14:14':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475>') 
        
    if now == '14:30':
        channel = client.get_channel(769753648733225010)
        await channel.send('$soak 0.001') 
        
    if now == '14:31':
        channel = client.get_channel(769283091800916029)
        await channel.send('//dream 0.01')     
        
    if now == '14:32':
        channel = client.get_channel(769753648733225010)
        await channel.send('$soak 0.001') 
        
    if now == '14:33':
        channel = client.get_channel(769283091800916029)
        await channel.send('//dream 0.01')     
        
    if now == '14:34':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001') 
        
    if now == '14:35':
        channel = client.get_channel(769069563094499358)
        await channel.send('//dream 0.01') 
        
    if now == '14:36':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001') 
        
    if now == '14:37':
        channel = client.get_channel(769069563094499358)
        await channel.send('//dream 0.01')
        
    if now == '15:14':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
        
    if now == '15:15':
        channel = client.get_channel(731640211733479556)
        await channel.send('rsoak 333.33 @JPYN member  <:rock:732205759462375475> :guitar:') 
        
    if now == '15:16':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
        
    if now == '16:50':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:hai_kao:699072592987947117>') 
        
    if now == '16:30':
        channel = client.get_channel(769753648733225010)
        await channel.send('$soak 0.001') 
        
    if now == '16:31':
        channel = client.get_channel(769283091800916029)
        await channel.send('//dream 0.01')     
        
    if now == '16:32':
        channel = client.get_channel(769753648733225010)
        await channel.send('$soak 0.001') 
        
    if now == '16:33':
        channel = client.get_channel(769283091800916029)
        await channel.send('//dream 0.01')     
        
    if now == '16:34':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001') 
        
    if now == '16:35':
        channel = client.get_channel(769069563094499358)
        await channel.send('//dream 0.01') 
        
    if now == '16:36':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001') 
        
    if now == '16:37':
        channel = client.get_channel(769069563094499358)
        await channel.send('//dream 0.01')
        
    if now == '17:01':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:rock:732205759462375475> <:cool:721313054624841838> <:rock:732205759462375475>')
        
    if now == '17:14':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
        
    if now == '17:15':
        channel = client.get_channel(731640211733479556)
        await channel.send('rsoak 333.33 @JPYN member  <:rock:732205759462375475> :guitar:') 
        
    if now == '17:16':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
        
    if now == '19:14':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475>') 

    if now == '20:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:hai_kao:699072592987947117> <:gm:699792760651120671>')
        
    if now == '20:14':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
        
    if now == '20:15':
        channel = client.get_channel(731640211733479556)
        await channel.send('rsoak 333.33 @JPYN member  <:rock:732205759462375475> :guitar:') 
        
    if now == '20:16':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
        
    if now == '20:30':
        channel = client.get_channel(769753648733225010)
        await channel.send('$soak 0.001') 
        
    if now == '20:31':
        channel = client.get_channel(769283091800916029)
        await channel.send('//dream 0.01')     
        
    if now == '20:32':
        channel = client.get_channel(769753648733225010)
        await channel.send('$soak 0.001') 
        
    if now == '20:33':
        channel = client.get_channel(769283091800916029)
        await channel.send('//dream 0.01')     
        
    if now == '20:34':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001') 
        
    if now == '20:35':
        channel = client.get_channel(769069563094499358)
        await channel.send('//dream 0.01') 
        
    if now == '20:36':
        channel = client.get_channel(769718766358757396)
        await channel.send('$soak 0.001') 
        
    if now == '20:37':
        channel = client.get_channel(769069563094499358)
        await channel.send('//dream 0.01')
        
    if now == '20:40':
        channel = client.get_channel(698653628176531478)
        await channel.send('/throw JPYN 150 30 EquallyDistributed')
    
    if now == '20:42':
        channel = client.get_channel(709878463733039204)
        await channel.send('/throw JPYN 150 30 EquallyDistributed')

    if now == '20:44':
        channel = client.get_channel(733238114478325790)
        await channel.send('/throw JPYN 150 30 EquallyDistributed')
        
    if now == '20:46':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw JPYN 150 30 EquallyDistributed')

    if now == '20:48':
        channel = client.get_channel(698653628176531478)
        await channel.send('/throw BGPT 333 30 EquallyDistributed')
    
    if now == '20:50':
        channel = client.get_channel(709878463733039204)
        await channel.send('/throw BGPT 333 30 EquallyDistributed')

    if now == '20:52':
        channel = client.get_channel(733238114478325790)
        await channel.send('/throw BGPT 333 30 EquallyDistributed')
        
    if now == '20:54':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw BGPT 333 30 EquallyDistributed')
        
    if now == '20:56':
        channel = client.get_channel(698653628176531478)
        await channel.send('/throw BEN 9 30 EquallyDistributed')
    
    if now == '20:58':
        channel = client.get_channel(709878463733039204)
        await channel.send('/throw BEN 9 30 EquallyDistributed')

    if now == '21:00':
        channel = client.get_channel(733238114478325790)
        await channel.send('/throw BEN 9 30 EquallyDistributed')
        
    if now == '21:02':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw BEN 9 30 EquallyDistributed')
        
    if now == '21:04':
        channel = client.get_channel(698653628176531478)
        await channel.send('/throw KENJ 1000 30 EquallyDistributed')
    
    if now == '21:06':
        channel = client.get_channel(709878463733039204)
        await channel.send('/throw KENJ 1000 30 EquallyDistributed')

    if now == '21:08':
        channel = client.get_channel(733238114478325790)
        await channel.send('/throw KENJ 1000 30 EquallyDistributed')
        
    if now == '21:10':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XPC 1.23456 30 EquallyDistributed')
        
    if now == '21:12':
        channel = client.get_channel(698653628176531478)
        await channel.send('/throw GDRH 1000 30 EquallyDistributed')
    
    if now == '21:14':
        channel = client.get_channel(709878463733039204)
        await channel.send('/throw GDRH 1000 30 EquallyDistributed')

    if now == '21:16':
        channel = client.get_channel(733238114478325790)
        await channel.send('/throw GDRH 1000 30 EquallyDistributed')
        
    if now == '21:18':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XPC 1.23456 30 EquallyDistributed')  
        
    if now == '21:20':
        channel = client.get_channel(698653628176531478)
        await channel.send('/throw SPRTS 777.333333 30 EquallyDistributed')
    
    if now == '21:22':
        channel = client.get_channel(709878463733039204)
        await channel.send('/throw SPRTS 777.333333 30 EquallyDistributed')

    if now == '21:24':
        channel = client.get_channel(733238114478325790)
        await channel.send('/throw SPRTS 777.333333 30 EquallyDistributed')
        
    if now == '21:26':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw SPRTS 789.333333 30 EquallyDistributed') 
        
    if now == '21:28':
        channel = client.get_channel(698653628176531478)
        await channel.send('/throw DOGE 0.000777 30 EquallyDistributed')
    
    if now == '21:30':
        channel = client.get_channel(709878463733039204)
        await channel.send('/throw DOGE 0.000777 30 EquallyDistributed')

    if now == '21:32':
        channel = client.get_channel(733238114478325790)
        await channel.send('/throw DOGE 0.000777 30 EquallyDistributed')
        
    if now == '21:34':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw DOGE 0.000777 30 EquallyDistributed') 
        
    if now == '21:28':
        channel = client.get_channel(698653628176531478)
        await channel.send('/throw XPC 1.7777 30 EquallyDistributed')
    
    if now == '21:30':
        channel = client.get_channel(709878463733039204)
        await channel.send('/throw XPC 1.7777 30 EquallyDistributed')

    if now == '21:32':
        channel = client.get_channel(733238114478325790)
        await channel.send('/throw XPC 1.7777 30 EquallyDistributed')
        
    if now == '21:34':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw DOGE 0.000777 30 EquallyDistributed') 

    if now == '21:36':
        channel = client.get_channel(698653628176531478)
        await channel.send('/throw XEM 0.00007777 30 EquallyDistributed')
    
    if now == '21:38':
        channel = client.get_channel(709878463733039204)
        await channel.send('/throw XEM 0.00007777 30 EquallyDistributed')

    if now == '21:40':
        channel = client.get_channel(733238114478325790)
        await channel.send('/throw XEM 0.00007777 30 EquallyDistributed')
        
    if now == '21:42':
        channel = client.get_channel(741553045481062461)
        await channel.send('/throw XEM 0.00007891 30 EquallyDistributed') 
       
    if now == '22:04':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
        
    if now == '22:07':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:hai_kao:699072592987947117> <:hello1:713004241131667528>')
        
    if now == '22:14':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
        
    if now == '22:15':
        channel = client.get_channel(731640211733479556)
        await channel.send('rsoak 333.33 @JPYN member  <:rock:732205759462375475> :guitar:') 
        
    if now == '22:16':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
        
    if now == '23:14':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> <:cool:721313054624841838> <:rock:732205759462375475>') 
        
#ループ処理実行
loop.start()


@client.event
async def on_message(message):
    """メッセージを処理"""
    if message.author.bot:  # ボットのメッセージをハネる
        return

    if message.content == "<:hello:699779689127870514> <:hello:699779689127870514> <:hello:699779689127870514>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:hello:699779689127870514><:hello1:713004241131667528>")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "<:hai_kao:699072592987947117> <:ty:699857337980026930>":
        # チャンネルへメッセージを送信
        await message.channel.send(f"<:hai_kao:699072592987947117> <:tok:700489006009286786>")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "!d bump":
        # チャンネルへメッセージを送信
        await message.channel.send(f"rtip {message.author.mention} 25")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "!disboard bump":
        # チャンネルへメッセージを送信
        await message.channel.send(f"rtip {message.author.mention} 25")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "三卍( ﾟ∀ﾟ)･∵":
        # チャンネルへメッセージを送信
        await message.channel.send(f"･∵( ﾟ∀ﾟ）卍三")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "┏○)) ｱﾘﾆ━━━━━━━━ﾝ!":
        # チャンネルへメッセージを送信
        await message.channel.send(f"┏○)) ｱﾘﾍﾞ━━━━━━━━ﾝ<:hai_kao:699072592987947117> ")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "(ﾟ∀ﾟ 三( ﾟ∀ﾟ) 三 ﾟ∀ﾟ)":
        # チャンネルへメッセージを送信
        await message.channel.send(f"(ﾟ∀ﾟ 三 ﾟ∀ﾟ)")  # f文字列（フォーマット済み文字列リテラル）
            
    if message.content == "(　ﾟ∀ﾟ)o彡ﾟみみたん！みみたす！":
        # チャンネルへメッセージを送信
        await message.channel.send(f"(　ﾟ∀ﾟ)o彡ﾟみみたん！みみたす！Go!Go!")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "(　ﾟ∀ﾟ)o彡ﾟみみたん！みみたす！Go!Go!":
        # チャンネルへメッセージを送信
        await message.channel.send(f"(　ﾟ∀ﾟ)o彡ﾟみみたん！みみたす！Go!Go!")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "( ﾟдﾟ)ﾊｯ!":
        # チャンネルへメッセージを送信
        await message.channel.send(f"( ﾟдﾟ)ﾊｯ!")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "((((-(-(-(-(-｡-)-)-)-)-))))":
        # チャンネルへメッセージを送信
        await message.channel.send(f"ｷｬ━━━━(ﾟ∀ﾟ)━━━━!!")  # f文字列（フォーマット済み文字列リテラル）
    
    if message.content == "ヾ(´∀｀)ﾉｷｬｯｷｬ":
        # チャンネルへメッセージを送信
        await message.channel.send(f"(((o(*ﾟ▽ﾟ*)o)))ワロタ")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "ｿｹﾞｷ(､´･ω･)▄︻┻┳═                 :boom: )｀Д)･:∴":
        # チャンネルへメッセージを送信
        await message.channel.send(f"Sniper(､´･ω･)▄︻┻┳═ 　　　　 :boom: :cut_of_meat:)｀Д)･:∴{message.author.mention} \n\n\n/tip 29coin 2929.2929 {message.author.mention} ")  # f文字列（フォーマット済み文字列リテラル）
    
    elif message.content == "r/link":
        # リアクションアイコンを付けたい
        q = await message.channel.send("/link ")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記

    elif message.content == "r/language":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /language EN ")
        [await q.add_reaction(i) for i in ('⭕', '❌')]  # for文の内包表記
              
    elif message.content == "r/accept":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /accept ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記

    elif message.content == "b/benzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info ben ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
        
    elif message.content == "b/jpynzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info jpyn ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記      
        
    elif message.content == "b/bgptzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info bgpt ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
    
    elif message.content == "b/kenjzan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info kenj ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記
             
    elif message.content == "b/sprtszan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info sprts ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記 

    elif message.content == "b/29zan":
        # リアクションアイコンを付けたい
        q = await message.channel.send(" /info 29coin ")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記 
        
    elif message.content == "b/rdeposit":
        # リアクションアイコンを付けたい
        q = await message.channel.send("rdeposit")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記 
        
    elif message.content == "b/rbal":
        # リアクションアイコンを付けたい
        q = await message.channel.send("rbal")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記 
        
    elif message.content == "b/re":
        # リアクションアイコンを付けたい
        q = await message.channel.send("//register")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記 
        
    elif message.content == "b/wallet":
        # リアクションアイコンを付けたい
        q = await message.channel.send("$deposit")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記 
        
    elif message.content == "b/bal":
        # リアクションアイコンを付けたい
        q = await message.channel.send("$soak 0.001")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記 
        
    elif message.content == "b/dt3":
        # リアクションアイコンを付けたい
        q = await message.channel.send("//dream 0.01")
        [await q.add_reaction(i) for i in ('⭕', '🔑')]  # for文の内包表記 



    elif message.content == "/tip bgpt 100 <@&703359665974673484>  ":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="JPYN SLOT:slot_machine:", description=f"{message.author.mention}Reel rotation！",
                              color=0xff1493)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="☆1slot=10 BGPT☆ ",
                        value=random.choice(('---------------------\n| :gem: | :first_place: | :100: |\n---------------------\n--- YOU LOST ---     残念\n--- ▲10BGPT ---\n'
                                             ,'🌟最高【チームに恵まれた日です。チャレンジしたら幸運を招きます☆彡】','やった')), inline=False)
        await message.channel.send(embed=embed)


    elif message.content == "Fortune":
        # Embedを使ったメッセージ送信 と ランダムで要素を選択
        embed = discord.Embed(title="☆OMIKUJI☆Fortune☆", description=f"{message.author.mention}Today!YourFortune!☆",
                              color=0x2ECC69)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.add_field(name="[Today!YourFortune!] ",
                        value=random.choice(('☆☆彡Very🤩VeryGood☆彡☆【Very Good! It ’s a very competitive day.】','☆VeryGoood!☆【It is a good day for the team. 】','Good☆彡！【It will be a convincing day. I can not expect much money.】'
                                             ,'VeryGood【☆☆☆If you work with confidence, you will always get good results. ♡♡♡ Love luck is super berig】', 'GoodDay【☆☆Good chance! There is a result of attacking. ♡♡ For the time being, there is no problem! ?】', 'Good!【☆☆ If you change the usual theory, you will get good results. ♡♡ No change from the current situation】'
                                             ,  'usuallyGood【☆☆Good results with participatory online games ♡ Not only games. Good luck if you go outside to meet】', 'good!【☆The current situation is unchanged ♡ No particular change Let it go！】',  'Good!【☆I do not need any advice】'
                                             , 'It is normal [What is that! ? You probably think that is normal! There is no peony mochi from the shelf', 'Great evil [Great evil [▲▲ I am nauseous!]'
                                             , 'Worst【▲Sorry! There is no opportunity. I think the loss is a win！】', 'Very worst!BAD【▲▲I m nauseous! Useless】')), inline=False)
        await message.channel.send(embed=embed)
        
client.run(token)
