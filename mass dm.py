import discord, colorama, os
from colorama import Fore
from discord.ext import commands

class utils:
    def rename(name):
        os.system(f'title MASS-DMER - {name}')

token = input("ODg4ODQ3NDI3MzU5MDg0NTQ0.YUYprA.tw372PJ8cSjD_NFLJYQFORlGPuA")
os.system('cls')


class massdm:
    client = discord.Client()
    client = commands.Bot(command_prefix='!', self_bot=True)
    client.remove_command('help')
    utils.rename(f"Connected to account, waiting for input...")
    def banner():
        print(f"""{Fore.LIGHTBLUE_EX}
                   ███╗   ███╗ █████╗ ███████╗███████╗    ██████╗ ███╗   ███╗███████╗██████╗ 
                   ████╗ ████║██╔══██╗██╔════╝██╔════╝    ██╔══██╗████╗ ████║██╔════╝██╔══██╗
                   ██╔████╔██║███████║███████╗███████╗    ██║  ██║██╔████╔██║█████╗  ██████╔╝
                   ██║╚██╔╝██║██╔══██║╚════██║╚════██║    ██║  ██║██║╚██╔╝██║██╔══╝  ██╔══██╗
                   ██║ ╚═╝ ██║██║  ██║███████║███████║    ██████╔╝██║ ╚═╝ ██║███████╗██║  ██║
                   ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
                                        -- Created by mythic#9999 --
                   {Fore.RESET}                                                             
           """)

    @client.event
    async def on_connect():
        friends = []
        for i in massdm.client.user.friends:
            friends.append(i)
        massdm.banner()
        input(f"{Fore.LIGHTGREEN_EX}Press any button to continue..")
        messagetosend = input(f"{Fore.LIGHTGREEN_EX}Insert message to send: ")
        print("Starting...")
        utils.rename(f"Sending message to {len(friends)} friends..")
        for i in friends:
            try:
                await i.send(messagetosend)
                print(f"{Fore.LIGHTCYAN_EX}Message sent to: {i.name}{Fore.RESET}")
            except Exception as err:
                print(f"{Fore.RED} Error sending DM to {i.name}: {err}{Fore.RESET}")
        input(f"{Fore.GREEN}Message have been dmed to {len(friends)} friends! Press any button to exit..")
        utils.rename("Done sending messages")

    def run(ODg4ODQ3NDI3MzU5MDg0NTQ0YUYprAtw372PJ8cSjD_NFLJYQFORlGPuA):
        massdm.client.run(ODg4ODQ3NDI3MzU5MDg0NTQ0YUYprAtw372PJ8cSjD_NFLJYQFORlGPuA, bot=False)

massdm.run(ODg4ODQ3NDI3MzU5MDg0NTQ0YUYprAtw372PJ8cSjD_NFLJYQFORlGPuA)
