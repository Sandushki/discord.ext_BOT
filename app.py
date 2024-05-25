# Discord kütüphanemizi komut dosyamıza yüklemek için import discord kullanırız:
import discord
# discord.ext'dan commands modülüne ulaşım sağlayarak kodlarımızı içeri aktarırız.
from discord.ext import commands

from botLogic import *

# {os} ve {random} kütüphanelerini bilgisayara aktarırız.
import os, random 

# Botumuzun ayrıcalıklarını depolayalım
intents = discord.Intents.default()
intents.message_content = True


# Bot adında bir değişken oluşturarak bot objesi ile bir bot oluştururuz, fakat işimiz bu sefer orada bitmez.
# commands sınıfındaki Bot objesini kullanırız

# Komutlarımızın prefixini command_prefix'ten ayarlarız.
# bot = commands.Bot(command_prefix='!', intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

# Deklaratör, @ ile başlar, ve fonksiyonları otomatik olarak belirli koşullarda çalıştırılmasını sağlaırız.
@bot.event
async def on_ready():
    print(f"{bot.user} olarak Discord'dayız!")


# @bot.command() deklaratörü, oluşturduğumuz fonksiyonu bir bot komutuna dönüştürür
@bot.command()
# Bu fonksiyonun içinde ctx --> context adını verdiğimiz objeyi kullanırız.
async def hello(ctx):
    await ctx.send(f"Merhaba! {bot.user} bir bot!")

@bot.command()
async def YaziTura(ctx):
    await ctx.send("Paranın, "+yaziTura()+" yüzü yukarıda kaldı.")
@bot.command()
async def sifreOlustur(ctx):
    await ctx.send(f"Sizin için oluşturduğumuz 15 haneli şifre: "+sifreOlusturucu(15))
@bot.command()
async def rastgeleEmoji(ctx):
    await ctx.send(emoji())
@bot.command()
async def mention(ctx):
    user = ctx.author.name

    await ctx.send(f"@{user} çağrıldınız!")
@bot.command()
async def clear(ctx):
    await ctx.send(temizle())
@bot.command()
async def bye(ctx):
    await ctx.send("Gitme, geri gel!")
@bot.command()
async def komutlar(ctx):
    await ctx.send(komutCikar())

@bot.command()
async def resim(ctx):
    """"
        Bilgisayarımızda bulunan herhangi bir dosya ile çalışmak istiyorsak open() fonksiyonu kullanılır.
        Open kelimesinin Türkçesi, açmak ve açık anlamlarına gelir.

        text() --> Metin, görseller, exe...

        open() fonksiyonunun altında bir sürü argüman kullanırız:
        open() fonksiyonunun ilk argümanında dosya yolunu belirleriz.

        Metin dosyalarını açmak istediğinizde ek bir argüman olarak bu metin dosyalarının karakter setini belritmeniz gerekir.
        Bunu yapabilmek için encoding='utf-8' komutunu yazarız.

        'wb' ==> yazmak için metin dışında bir dosya açar.
        'rb' ==> okunması için metin dışında bir dosya açar.
"""
    randomPicture = random.choice(os.listdir('img'))

    with open(f'img\{randomPicture}', 'rb') as f:
        # METİN OLMAYAN bir dosyayı Discord dosyasına dönüştürür.
        resim = discord.File(f)
    # Resmi gönderelim.
    await ctx.send(file=resim)
