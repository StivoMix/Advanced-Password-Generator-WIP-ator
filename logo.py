from pystyle import Colorate, Colors
def logo():
    logo = """
    ____                                          __
   / __ \____ ____________      ______  _________/ /
  / /_/ / __ `/ ___/ ___/ | /| / / __ \/ ___/ __  / 
 / ____/ /_/ (__  |__  )| |/ |/ / /_/ / /  / /_/ /  
/_/ __ \____/____/______|__/___/\____/_/   \__,_/   
   /  |/  /___ ______/ /_  (_)___  ___              
  / /|_/ / __ `/ ___/ __ \/ / __ \/ _ \             
 / /  / / /_/ / /__/ / / / / / / /  __/             
/_/  /_/\__,_/\___/_/ /_/_/_/ /_/\___/                    
"""
    return Colorate.Vertical(Colors.blue_to_purple, logo)