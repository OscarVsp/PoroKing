# -*- coding: utf-8 -*-
import os

import disnake
from disnake.ext import commands

from bot.bot import Bot


class Info(commands.Cog):
    def __init__(self, bot):
        """Initialize the cog"""
        self.bot: Bot = bot

    @commands.slash_command(name="minecraft", description="Obtenir les infos sur le serveur minecraft communautaire.")
    async def minecraft(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.defer(ephemeral=True)

        embed = (
            disnake.Embed(
                title="__**Serveur minecraft Poroland**__",
                description="Viens nous rejoindre sur le serveur minecraft de la communauté !",
                color=disnake.Colour.blue(),
            )
            .add_field(
                name="__Installation de minecraft__",
                value=f"""
            🔷 Commence par installer le [Launcher Minecraft](https://www.minecraft.net/fr-fr/download) si ce n'est pas encore fait.
            🔷 Ensuite, pour pouvoir rejoindre le seveur **Poroland**, tu dois utiliser la version [Forge de minecraft *1.19.2*](https://files.minecraftforge.net/net/minecraftforge/forge/index_1.19.2.html)
            🔷 Tu peux maintenant te connecter au serveur en utilisant l'addresse suivant : `{str(os.getenv("MINECRAFT_SERV_ADDR"))}`
            """,
                inline=False,
            )
            .add_field(
                name="__Mods et shadders__",
                value="""
            Le serveur permet d'utiliser des mods tel que:
            🔷 [Xearo's Minimap](http://adfoc.us/serve/sitelinks/?id=190660&url=https://chocolateminecraft.com/mods2/minimap/Xaeros_Minimap_23.1.0_Forge_1.19.1.jar) et [Xearo's World Map](http://adfoc.us/serve/sitelinks/?id=190660&url=https://chocolateminecraft.com/mods2/worldmap/XaerosWorldMap_1.28.9_Forge_1.19.1.jar) pour avoir une minimap et avoir la position des autres joueurs.
            🔷 [Distant Horizons](https://www.curseforge.com/minecraft/mc-mods/distant-horizons/download/3923597) pour avoir une distance de vu très largement augmenter.
            🔷 [OptiFine](https://cdn.discordapp.com/attachments/977675456985858089/1061668394883092521/OptiFine_1.19.2_HD_U_H9_MOD.jar) pour pouvoir ajouter des shaders.

            Il te suffit d'ajouter les fichers `.jar` dans dossier `%AppData%\.minecraft\mods` et de relancer le jeu pour ajouter les mods voulut.""",
                inline=False,
            )
        )
        await inter.edit_original_response(embed=embed)

    @commands.slash_command(name="dofus", description="Obtenir les infos sur la guilde dofus communautaire.")
    async def dofus(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.defer(ephemeral=True)

        embed = disnake.Embed(
            title="__**Guilde dofus Arbruti**__",
            description=f"""La guilde **Arbruti** est sur le serveur **Draconiros** (Monocompte) et est ouverte à tous !\nAjoutes <@281401408597655552> sur le jeu (sibannac-ltds) et rejoinds le [serveur discord]({str(os.getenv("DOFUS_DISCORD_SERVER"))}) de la guilde """,
            color=disnake.Colour.blue(),
        )

        await inter.edit_original_response(embed=embed)


def setup(bot: commands.InteractionBot):
    bot.add_cog(Info(bot))
