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
   
    if now == '04:13':
        channel = client.get_channel(731640211733479556)
        await channel.send('rsoak 333.33 @JPYN member  <:rock:732205759462375475> :guitar:')     
        
    if now == '04:14':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475>')   
        
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
        
    if now == '09:14':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
          
    if now == '10:00':
        channel = client.get_channel(CHANNEL_ID)
        await channel.send('<:ge:699792780725059664>') 
        
    if now == '11:14':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
        
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
        
    if now == '13:14':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
        
    if now == '13:15':
        channel = client.get_channel(731640211733479556)
        await channel.send('rsoak 333.33 @JPYN member  <:rock:732205759462375475> :guitar:') 
        
    if now == '13:16':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> :guitar: <:rock:732205759462375475>') 
     
    if now == '14:14':
        channel = client.get_channel(731640211733479556)
        await channel.send('<:rock:732205759462375475> <:rock:732205759462375475> <:rock:732205759462375475>') 
        
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
        
    if now == '21:14':
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
        
    if message.content == "ｱﾘﾆﾝﾆﾝﾆﾝﾆﾝ=͟͟͞( 'ω' =͟͟͞( 'ω' =͟͟͞)=͟͟͞=͟͟͞( 'ω' =͟͟͞( 'ω' =͟͟͞)ﾆﾝﾆﾝ":
        # チャンネルへメッセージを送信
        await message.channel.send(f"ｱﾘNinNinNinNin=͟͟͞( 'ω' =͟͟͞( 'ω' =͟͟͞)=͟͟͞=͟͟͞( 'ω' =͟͟͞( 'ω' =͟͟͞)ninnin")  # f文字列（フォーマット済み文字列リテラル）
        
    if message.content == "三卍( ﾟ∀ﾟ)･∵. ｸﾞﾊｯ!!":
        # チャンネルへメッセージを送信
        await message.channel.send(f"三卍( ﾟ∀ﾟ)･∵. ｸﾞﾊｯ!!")  # f文字列（フォーマット済み文字列リテラル）
    
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
