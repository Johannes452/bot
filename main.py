import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True  # Wichtig, um auf Member-Events zuzugreifen

bot = commands.Bot(command_prefix="!", intents=intents)

# IDs hier anpassen
ADMIN_ROLE_ID = 1383861917092675737  # ID der Admin-Rolle
WHITELIST_USER_IDS = [742372118980853801]  # IDs der erlaubten Benutzer

@bot.event
async def on_ready():
    print(f"Bot ist online als {bot.user}")

@bot.event
async def on_member_join(member):
    if member.id in WHITELIST_USER_IDS:
        role = member.guild.get_role(ADMIN_ROLE_ID)
        if role:
            await member.add_roles(role)
            print(f"Adminrolle an {member.name} vergeben.")
        else:
            print("Adminrolle nicht gefunden.")

bot.run("MTM4Mzg2MjUyNjY5NzI3NTU0Mw.Ge6I1K.YwbhIo_0VddNgzP_Bxm0GD-SgYswKxAcCGj6_w")
