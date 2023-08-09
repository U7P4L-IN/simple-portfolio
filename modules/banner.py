"""
Script : PhoneSploit X
Author : U7P4L 1N (github.com/U7P4L-IN)
"""

from modules import color

version = "v1.6"

menu1 = f"""

    {color.WHITE}1. {color.GREEN}Connect a Device             {color.WHITE}6. {color.GREEN}Get Screenshot                       {color.WHITE}11. {color.GREEN}Install an APK  
    {color.WHITE}2. {color.GREEN}List Connected Devices       {color.WHITE}7. {color.GREEN}Screen Record                        {color.WHITE}12. {color.GREEN}Uninstall an App
    {color.WHITE}3. {color.GREEN}Disconnect All Devices       {color.WHITE}8. {color.GREEN}Download File/Folder from Device     {color.WHITE}13. {color.GREEN}List Installed Apps 
    {color.WHITE}4. {color.GREEN}Scan Network for Devices     {color.WHITE}9. {color.GREEN}Send File/Folder to Device           {color.WHITE}14. {color.GREEN}Access Device Shell
    {color.WHITE}5. {color.GREEN}Mirror & Control Device     {color.WHITE}10. {color.GREEN}Run an App                           {color.WHITE}15. {color.GREEN}Hack Device {color.RED}(Using Metasploit)


   {color.YELLOW} 
  N : Next Page                                      (Page : 1 / 3)"""

menu2 = f"""

    {color.WHITE}16. {color.GREEN}List All Folders/Files      {color.WHITE}21. {color.GREEN}Anonymous Screenshot                {color.WHITE}26. {color.GREEN}Play a Video on Device
    {color.WHITE}17. {color.GREEN}Send SMS                    {color.WHITE}22. {color.GREEN}Anonymous Screen Record             {color.WHITE}27. {color.GREEN}Get Device Information
    {color.WHITE}18. {color.GREEN}Copy WhatsApp Data          {color.WHITE}23. {color.GREEN}Open a Link on Device               {color.WHITE}28. {color.GREEN}Get Battery Information
    {color.WHITE}19. {color.GREEN}Copy All Screenshots        {color.WHITE}24. {color.GREEN}Display a Photo on Device           {color.WHITE}29. {color.GREEN}Restart Device
    {color.WHITE}20. {color.GREEN}Copy All Camera Photos      {color.WHITE}25. {color.GREEN}Play an Audio on Device             {color.WHITE}30. {color.GREEN}Advanced Reboot Options


   {color.YELLOW} 
  P : Previous Page         N : Next Page            (Page : 2 / 3)"""

menu3 = f"""

    {color.WHITE}31. {color.GREEN}Unlock Device               {color.WHITE}36. {color.GREEN}Extract APK from Installed App      {color.WHITE}41. {color.GREEN}Record Mic Audio
    {color.WHITE}32. {color.GREEN}Lock Device                 {color.WHITE}37. {color.GREEN}Stop ADB Server                     {color.WHITE}42. {color.GREEN}Listen Device Audio
    {color.WHITE}33. {color.GREEN}Dump All SMS                {color.WHITE}38. {color.GREEN}Power Off Device                    {color.WHITE}43. {color.GREEN}Record Device Audio
    {color.WHITE}34. {color.GREEN}Dump All Contacts           {color.WHITE}39. {color.GREEN}Use Keycodes (Control Device)       {color.WHITE}44. {color.GREEN}Update PhoneSploit-Pro
    {color.WHITE}35. {color.GREEN}Dump Call Logs              {color.WHITE}40. {color.GREEN}Listen Mic Audio                    {color.WHITE}45. {color.GREEN}Visit PhoneSploit-Pro on GitHub


   {color.YELLOW} 
  P : Previous Page                                  (Page : 3 / 3)"""

menu = [menu1, menu2, menu3]

instruction = f"""

This Attack Will Launch Metasploit-Framework    (msfconsole)

Use 'Ctrl + C' to Stop At Any Point

1. Wait Until You See:
    
    {color.GREEN}Meterpreter >      {color.WHITE}

2. Then Use 'help' Command To See All Meterpreter Commands:

    {color.GREEN}Meterpreter > {color.YELLOW}help       {color.WHITE}

3. To Exit Meterpreter Enter 'exit' or To Exit Metasploit Enter 'exit -y':

    {color.GREEN}Meterpreter > {color.YELLOW}exit       {color.WHITE}

    {color.GREEN}msf6 > {color.YELLOW}exit -y       {color.WHITE}
     
{color.RED}[PhoneSploit X]   {color.WHITE}Press 'Enter' To Continue Attack / '0' to Go Back to Main Menu
    """

banner2 = f"""


   >======>   >=>    >=>     >===>      >==>    >=> >=======>   >=>>=>   >======>   >=>           >===>      >=> >===>>=====>        >=>      >=> 
   >=>    >=> >=>    >=>   >=>    >=>   >> >=>  >=> >=>       >=>    >=> >=>    >=> >=>         >=>    >=>   >=>      >=>             >=>   >=>   
   >=>    >=> >=>    >=> >=>        >=> >=> >=> >=> >=>        >=>       >=>    >=> >=>       >=>        >=> >=>      >=>              >=> >=>    
   >======>   >=====>>=> >=>        >=> >=>  >=>>=> >=====>      >=>     >======>   >=>       >=>        >=> >=>      >=>     >====>     >=>      
   >=>        >=>    >=> >=>        >=> >=>   > >=> >=>             >=>  >=>        >=>       >=>        >=> >=>      >=>              >=> >=>    
   >=>        >=>    >=>   >=>     >=>  >=>    >>=> >=>       >=>    >=> >=>        >=>         >=>     >=>  >=>      >=>             >=>   >=>   
   >=>        >=>    >=>     >===>      >=>     >=> >=======>   >=>>=>   >=>        >=======>     >===>      >=>      >=>            >=>      >=> 

            {color.RED}{version}{color.WHITE}            {color.WHITE}BY github.com/U7P4L-IN
"""

banner3 = f"""


   ><<<<<<<  ><<     ><<    ><<<<     ><<<     ><<><<<<<<<<  ><< <<  ><<<<<<<  ><<          ><<<<     ><<><<< ><<<<<<      ><<      ><<
   ><<    ><<><<     ><<  ><<    ><<  >< ><<   ><<><<      ><<    ><<><<    ><<><<        ><<    ><<  ><<     ><<           ><<   ><<  
   ><<    ><<><<     ><<><<        ><<><< ><<  ><<><<       ><<      ><<    ><<><<      ><<        ><<><<     ><<            ><< ><<   
   ><<<<<<<  ><<<<<< ><<><<        ><<><<  ><< ><<><<<<<<     ><<    ><<<<<<<  ><<      ><<        ><<><<     ><<    ><<<<<    ><<     
   ><<       ><<     ><<><<        ><<><<   >< ><<><<            ><< ><<       ><<      ><<        ><<><<     ><<            ><< ><<   
   ><<       ><<     ><<  ><<     ><< ><<    >< <<><<      ><<    ><<><<       ><<        ><<     ><< ><<     ><<           ><<   ><<  
   ><<       ><<     ><<    ><<<<     ><<      ><<><<<<<<<<  ><< <<  ><<       ><<<<<<<<    ><<<<     ><<     ><<          ><<      ><<
                                                                                                                                    
            {color.RED}{version}{color.WHITE}             {color.WHITE}BY github.com/U7P4L-IN
"""

banner4 = f"""


   8888888b.  888    888  .d88888b.  888b    888 8888888888 .d8888b.  8888888b.  888      .d88888b. 8888888 88888888888    Y88b   d88P 
   888   Y88b 888    888 d88P" "Y88b 8888b   888 888       d88P  Y88b 888   Y88b 888     d88P" "Y88b  888       888         Y88b d88P  
   888    888 888    888 888     888 88888b  888 888       Y88b.      888    888 888     888     888  888       888          Y88o88P   
   888   d88P 8888888888 888     888 888Y88b 888 8888888    "Y888b.   888   d88P 888     888     888  888       888           Y888P    
   8888888P"  888    888 888     888 888 Y88b888 888           "Y88b. 8888888P"  888     888     888  888       888           d888b    
   888        888    888 888     888 888  Y88888 888             "888 888        888     888     888  888       888   888888 d88888b   
   888        888    888 Y88b. .d88P 888   Y8888 888       Y88b  d88P 888        888     Y88b. .d88P  888       888         d88P Y88b  
   888        888    888  "Y88888P"  888    Y888 8888888888 "Y8888P"  888        88888888 "Y88888P" 8888888     888        d88P   Y88b 
                                                                                                                                    
        {color.RED}{version}{color.WHITE}                             {color.WHITE}BY github.com/U7P4L-IN
"""
banner5 = f"""
                                                                                                                        
                                                                                                                        
   ________  ____    ____   ____   ___      _____________   ____  ________  ____       ____   ______________ ____      ___ 
   `MMMMMMMb.`MM'    `MM'  6MMMMb  `MM\     `M'`MMMMMMMMM  6MMMMb\`MMMMMMMb.`MM'      6MMMMb  `MM'MMMMMMMMMM `MM(      )M' 
    MM    `Mb MM      MM  8P    Y8  MMM\     M  MM      \ 6M'    ` MM    `Mb MM      8P    Y8  MM /   MM   \  `MM.     d'  
    MM     MM MM      MM 6M      Mb M\MM\    M  MM        MM       MM     MM MM     6M      Mb MM     MM       `MM.   d'   
    MM     MM MM      MM MM      MM M \MM\   M  MM    ,   YM.      MM     MM MM     MM      MM MM     MM        `MM. d'    
    MM    .M9 MMMMMMMMMM MM      MM M  \MM\  M  MMMMMMM    YMMMMb  MM    .M9 MM     MM      MM MM     MM         `MMd      
    MMMMMMM9' MM      MM MM      MM M   \MM\ M  MM    `        `Mb MMMMMMM9' MM     MM      MM MM     MM          dMM.     
    MM        MM      MM MM      MM M    \MM\M  MM              MM MM        MM     MM      MM MM     MM MMMMMMM d'`MM.    
    MM        MM      MM YM      M9 M     \MMM  MM              MM MM        MM     YM      M9 MM     MM        d'  `MM.   
    MM        MM      MM  8b    d8  M      \MM  MM      / L    ,M9 MM        MM    / 8b    d8  MM     MM       d'    `MM.  
   _MM_      _MM_    _MM_  YMMMM9  _M_      \M _MMMMMMMMM MYMMMM9 _MM_      _MMMMMMM  YMMMM9  _MM_   _MM_    _M(_    _)MM_ 

        {color.RED}{version}{color.WHITE}        {color.WHITE}BY github.com/U7P4L-IN
"""

banner6 = f"""
    888888ba  dP     dP   .88888.  888888ba   88888888b .d88888b   888888ba  dP         .88888.  dP d888888P          dP    dP 
    88    `8b 88     88  d8'   `8b 88    `8b  88        88.    "'  88    `8b 88        d8'   `8b 88    88             Y8.  .8P 
   a88aaaa8P' 88aaaaa88a 88     88 88     88 a88aaaa    `Y88888b. a88aaaa8P' 88        88     88 88    88              Y8aa8P  
    88        88     88  88     88 88     88  88              `8b  88        88        88     88 88    88    88888888 d8'  `8b 
    88        88     88  Y8.   .8P 88     88  88        d8'   .8P  88        88        Y8.   .8P 88    88             88    88 
    dP        dP     dP   `8888P'  dP     dP  88888888P  Y88888P   dP        88888888P  `8888P'  dP    dP             dP    dP 
   oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
     
           {color.RED}{version}{color.WHITE}               {color.WHITE}BY github.com/U7P4L-IN

"""

banner10 = f"""


   :::::::::  :::    :::  ::::::::  ::::    ::: :::::::::: ::::::::  :::::::::  :::        :::::::: ::::::::::: :::::::::::             :::    ::: 
   :+:    :+: :+:    :+: :+:    :+: :+:+:   :+: :+:       :+:    :+: :+:    :+: :+:       :+:    :+:    :+:         :+:                 :+:    :+: 
   +:+    +:+ +:+    +:+ +:+    +:+ :+:+:+  +:+ +:+       +:+        +:+    +:+ +:+       +:+    +:+    +:+         +:+                  +:+  +:+  
   +#++:++#+  +#++:++#++ +#+    +:+ +#+ +:+ +#+ +#++:++#  +#++:++#++ +#++:++#+  +#+       +#+    +:+    +#+         +#+    +#++:++#++:++  +#++:+   
   +#+        +#+    +#+ +#+    +#+ +#+  +#+#+# +#+              +#+ +#+        +#+       +#+    +#+    +#+         +#+                  +#+  +#+  
   #+#        #+#    #+# #+#    #+# #+#   #+#+# #+#       #+#    #+# #+#        #+#       #+#    #+#    #+#         #+#                 #+#    #+# 
   ###        ###    ###  ########  ###    #### ########## ########  ###        ########## ######## ###########     ###                 ###    ### 

            {color.RED}{version}{color.WHITE}                                {color.WHITE}BY github.com/U7P4L-IN

"""

banner11 = f"""


   ooooooooo.   ooooo   ooooo   .oooooo.   ooooo      ooo oooooooooooo  .oooooo..o ooooooooo.   ooooo          .oooooo.   ooooo ooooooooooooo         ooooooo  ooooo 
   `888   `Y88. `888'   `888'  d8P'  `Y8b  `888b.     `8' `888'     `8 d8P'    `Y8 `888   `Y88. `888'         d8P'  `Y8b  `888' 8'   888   `8          `8888    d8'  
    888   .d88'  888     888  888      888  8 `88b.    8   888         Y88bo.       888   .d88'  888         888      888  888       888                 Y888..8P    
    888ooo88P'   888ooooo888  888      888  8   `88b.  8   888oooo8     `"Y8888o.   888ooo88P'   888         888      888  888       888                  `8888'     
    888          888     888  888      888  8     `88b.8   888    "         `"Y88b  888          888         888      888  888       888      8888888    .8PY888.    
    888          888     888  `88b    d88'  8       `888   888       o oo     .d8P  888          888       o `88b    d88'  888       888                d8'  `888b   
   o888o        o888o   o888o  `Y8bood8P'  o8o        `8  o888ooooood8 8""88888P'  o888o        o888ooooood8  `Y8bood8P'  o888o     o888o             o888o  o88888o 
                                                                                                                                                     
            {color.RED}{version}{color.WHITE}                            {color.WHITE}BY github.com/U7P4L-IN

"""

banner12 = f"""


   P)ppppp  H)    hh  O)oooo  N)n   nn E)eeeeee  S)ssss  P)ppppp  L)        O)oooo  I)iiii T)tttttt         X)    xx 
   P)    pp H)    hh O)    oo N)nn  nn E)       S)    ss P)    pp L)       O)    oo   I)      T)             X)  xx  
   P)ppppp  H)hhhhhh O)    oo N) nn nn E)eeeee   S)ss    P)ppppp  L)       O)    oo   I)      T)              X)xx   
   P)       H)    hh O)    oo N)  nnnn E)            S)  P)       L)       O)    oo   I)      T)    #######   X)xx   
   P)       H)    hh O)    oo N)   nnn E)       S)    ss P)       L)       O)    oo   I)      T)             X)  xx  
   P)       H)    hh  O)oooo  N)    nn E)eeeeee  S)ssss  P)       L)llllll  O)oooo  I)iiii    T)            X)    xx 

            {color.RED}{version}{color.WHITE}                            {color.WHITE}BY github.com/U7P4L-IN

"""
banner_list = [
    banner2,
    banner3,
    banner4,
    banner5,
    banner6,
    banner10,
    banner11,
    banner12,
]

instructions_banner = f"""{color.CYAN}

       _____   _________________  __  ______________________  _   _______    
      /  _/ | / / ___/_  __/ __ \/ / / / ____/_  __/  _/ __ \/ | / / ___/    
      / //  |/ /\__ \ / / / /_/ / / / / /     / /  / // / / /  |/ /\__ \     
    _/ // /|  /___/ // / / _, _/ /_/ / /___  / / _/ // /_/ / /|  /___/ /     
   /___/_/ |_//____//_/ /_/ |_|\____/\____/ /_/ /___/\____/_/ |_//____/      

        {color.WHITE}                                                        
"""

hacking_banner = f"""{color.GREEN}


    ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀ ██▓ ███▄    █   ▄████ 
   ▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓██▒ ██ ▀█   █  ██▒ ▀█▒
   ▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒██▒▓██  ▀█ ██▒▒██░▄▄▄░
   ░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ░██░▓██▒  ▐▌██▒░▓█  ██▓
   ░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄░██░▒██░   ▓██░░▒▓███▀▒
    ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒░▓  ░ ▒░   ▒ ▒  ░▒   ▒ 
    ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░ ▒ ░░ ░░   ░ ▒░  ░   ░ 
    ░  ░░ ░  ░   ▒   ░        ░ ░░ ░  ▒ ░   ░   ░ ░ ░ ░   ░ 
    ░  ░  ░      ░  ░░ ░      ░  ░    ░           ░       ░ 
                     ░                 

    {color.WHITE}
"""

keycode_menu = f"""
    {color.WHITE}1. {color.GREEN}Keyboard Text Input                {color.WHITE}11. {color.GREEN}Enter
    {color.WHITE}2. {color.GREEN}Home                               {color.WHITE}12. {color.GREEN}Volume Up
    {color.WHITE}3. {color.GREEN}Back                               {color.WHITE}13. {color.GREEN}Volume Down          
    {color.WHITE}4. {color.GREEN}Recent Apps                        {color.WHITE}14. {color.GREEN}Media Play           
    {color.WHITE}5. {color.GREEN}Power Button                       {color.WHITE}15. {color.GREEN}Media Pause
    {color.WHITE}6. {color.GREEN}DPAD Up                            {color.WHITE}16. {color.GREEN}Tab 
    {color.WHITE}7. {color.GREEN}DPAD Down                          {color.WHITE}17. {color.GREEN}Esc
    {color.WHITE}8. {color.GREEN}DPAD Left           
    {color.WHITE}9. {color.GREEN}DPAD Right
   {color.WHITE}10. {color.GREEN}Delete/Backspace
"""
