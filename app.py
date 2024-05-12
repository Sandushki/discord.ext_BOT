# Discord kütüphanemizi komut dosyamıza yüklemek için import discord kullanırız:
import discord
# discord.ext'dan commands modülüne ulaşım sağlayarak kodlarımızı içeri aktarırız.
from discord.ext import commands

from botLogic import *

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
async def SifreOlustur(ctx):
    await ctx.send(f"Sizin için oluşturduğumuz 16 haneli şifre: "+sifreOlusturucu(15))
@bot.command()
async def rastgeleEmoji(ctx):
    await ctx.send(emoji())
@bot.command()
async def mention(ctx):
    user = ctx.author.name

    await ctx.send(f"Çağrıldınız @{user}")


bot.run('TOKEN (Discord bot API)')