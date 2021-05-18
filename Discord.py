import discord
from discord.ext import commands
import json
import requests
from pprint import pprint



bot = commands.Bot(command_prefix = '#', description = "Bot Test")


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("Hello Team!"))
    print("Ready!")


@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name='général')
    await channel.send(f'Welcome {member.mention}!')
    

@bot.command()
async def Bonjour(ctx):
    await ctx.send("Bonjour !")


@bot.command()
async def InfoServeur(ctx):
    serveur = ctx.guild
    nomDuServeur = serveur.name
    nbDePersonnes = serveur.member_count
    message = f"Le serveur **{nomDuServeur}** contient **{nbDePersonnes}** personnes."      # 1*:en italique ,2*: en gras
    await ctx.send(message)

#Donne les coordonnées géographiques de la ville voulue pour pouvoir avoir les prévisions météo de cette même ville
def coordonnées(city, long_or_lat):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=c21a9f12441f8209ffb56153f5be52b2'.format(city)
    res = requests.get(url)
    data = res.json()
    if long_or_lat == "longitude":
        position = data['coord']['lon']
    elif long_or_lat == "latitude":
        position = data['coord']['lat']
    return position

#Donne la météo d'une ville jusqu'à 1 semaine à l'avance
@bot.command()
async def météo(ctx, city, moment, compteur_jour_heure):
    latitude = coordonnées(city, "latitude")
    longitude = coordonnées(city, "longitude")
    url = 'https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=&appid=c21a9f12441f8209ffb56153f5be52b2'.format(latitude,longitude)
    res = requests.get(url)
    data = res.json()
    if compteur_jour_heure == "now" or compteur_jour_heure == "today":
        compteur_jour_heure = 0

    #Cette condition donne la m�t�o � l'instant o� elle est demand�e
    if moment == "current":
        température = "%.1f" % (float(data[moment]['temp']) - 273.15)       #data[moment]['temp'] donne la temp�rature en kelvin / converti en �C et donn� avec 1 chiffre significatif 
        humidité = float(data[moment]['humidity'])      #humidit� en %      
        wind = "%.1f" % (float(data[moment]['wind_speed']) * 3.6)       #float(data[moment]['wind_speed'] donne la vitesse du vent en m/s / converti en m/s
        description = data[moment]['weather'][0]['description']     
        message = f"Température: **{température}°C** \nTaux d'humidité: **{humidité}%** \nVitesse du vent:  **{wind} km/h** \nEtat du ciel: **{description}**"
        await ctx.send(message)      
    #Cette condition donne la m�t�o par heure jusqu'� 48 heures � l'avance
    elif moment == "hourly":
        if -1 < int(compteur_jour_heure) < 48:
          température = "%.1f" % (float(data[moment][int(compteur_jour_heure)]['temp']) - 273.15)
          humidité = float(data[moment][int(compteur_jour_heure)]['humidity']) 
          wind = "%.1f" % (float(data[moment][int(compteur_jour_heure)]['wind_speed']) * 3.6)
          description = data[moment][int(compteur_jour_heure)]['weather'][0]['description']
          message = f"Température: **{température}°C** \nTaux d'humidité: **{humidité}%** \nVitesse du vent:  **{wind} km/h** \nEtat du ciel: **{description}**"
          await ctx.send(message)
        else:
          message = f"Erreur valeur.\nVeuillez donner une valeur correct (entre 0 et 47)."
          await ctx.send(message)
    #Cette condition donne la m�t�o par jour jusqu'� 7 jours � l'avance
    elif moment == "daily":
        if -1 < int(compteur_jour_heure) < 8:
          température_jour = "%.1f" % (float(data[moment][int(compteur_jour_heure)]['temp']['day']) - 273.15)
          température_nuit = "%.1f" % (float(data[moment][int(compteur_jour_heure)]['temp']['night']) - 273.15)
          humidité = float(data[moment][int(compteur_jour_heure)]['humidity']) 
          wind = "%.1f" % (float(data[moment][int(compteur_jour_heure)]['wind_speed']) * 3.6)
          description = data[moment][int(compteur_jour_heure)]['weather'][0]['description']
          message = f"Température dans la journée: **{température_jour}°C** \nTempérature dans la nuit: **{température_nuit}éC** \nTaux d'humidité: **{humidité}%** \nVitesse du vent:  **{wind} km/h** \nEtat du ciel: **{description}**"
          await ctx.send(message)
        else:
          message = f"Erreur valeur.\nVeuillez donner une valeur correct (entre 0 et 7)."
          await ctx.send(message)
    else:
        message = f"Erreur message.\nVeuillez donner le moment correct (current, hourly ou daily)."
        await ctx.send(message)


bot.run("")
