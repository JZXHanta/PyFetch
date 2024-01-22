class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

windows_logo = """       @@@                              
         @@@                            
         **@@@@@@@                      
     **    ** @@@@@@@@@@@@@@@@@@        
       ** ******@@@@@@@@@@@@@@@@@@@@    
    @@   ***** ****@@@@******@@%%@@@@@@ 
   ++@@@   *******@@@@******%@#====%@@@@
    +++@@@@@@@*** @@@#*****#@@=====*@@@@
 ++    ++ @@@@@@@@@@@#####*@@=====+@@@@ 
   ++ ++++++@@%%@@@@###@@@@@@@*==+@@@@  
@@   +++ ++++++@@@@++++++%@+=*@@@%@@@@  
  @@   +++++++@@@@++++++%@%-----%@@@@   
   @@@@@@@+++#@@@#+++++#@%-----=@@@@    
      @@@@@@@@@@@@@@@@%@@-----=@@@@     
         @@@@@@@@@@@@@@@@@@#--%@@@      
                       @@@@@@@@@@       
                           @@@@@@       
                              @@        
    
"""

windows_logo_colorized = f"""       @@@                              
         @@@                            
         {Bcolors.FAIL}**{Bcolors.ENDC}@@@@@@@                      
     {Bcolors.FAIL}**    **{Bcolors.ENDC} @@@@@@@@@@@@@@@@@@        
       {Bcolors.FAIL}** ******{Bcolors.ENDC}@@@@@@@@@@@@@@@@@@@@    
    @@   {Bcolors.FAIL}***** ****{Bcolors.ENDC}@@@@{Bcolors.FAIL}******{Bcolors.ENDC}@@%%@@@@@@ 
   {Bcolors.OKBLUE}++{Bcolors.ENDC}@@@   {Bcolors.FAIL}*******{Bcolors.ENDC}@@@@{Bcolors.FAIL}******{Bcolors.ENDC}%@#{Bcolors.OKGREEN}===={Bcolors.ENDC}%@@@@
    {Bcolors.OKBLUE}+++{Bcolors.ENDC}@@@@@@@{Bcolors.FAIL}***{Bcolors.ENDC} @@@#{Bcolors.FAIL}*****{Bcolors.ENDC}#@@{Bcolors.OKGREEN}====={Bcolors.ENDC}*@@@@
 {Bcolors.OKBLUE}++    ++{Bcolors.ENDC} @@@@@@@@@@@#####{Bcolors.FAIL}*{Bcolors.ENDC}@@{Bcolors.OKGREEN}====={Bcolors.ENDC}+@@@@ 
   {Bcolors.OKBLUE}++ ++++++{Bcolors.ENDC}@@%%@@@@###@@@@@@@*{Bcolors.OKGREEN}=={Bcolors.ENDC}+@@@@  
@@   {Bcolors.OKBLUE}+++ ++++++{Bcolors.ENDC}@@@@{Bcolors.OKBLUE}++++++{Bcolors.ENDC}%@+=*@@@%@@@@  
  @@   {Bcolors.OKBLUE}+++++++{Bcolors.ENDC}@@@@{Bcolors.OKBLUE}++++++{Bcolors.ENDC}%@%{Bcolors.WARNING}-----{Bcolors.ENDC}%@@@@   
   @@@@@@@{Bcolors.OKBLUE}+++{Bcolors.ENDC}#@@@#{Bcolors.OKBLUE}+++++{Bcolors.ENDC}#@%{Bcolors.WARNING}-----{Bcolors.ENDC}=@@@@    
      @@@@@@@@@@@@@@@@%@@{Bcolors.WARNING}-----{Bcolors.ENDC}=@@@@     
         @@@@@@@@@@@@@@@@@@#{Bcolors.WARNING}--{Bcolors.ENDC}%@@@      
                       @@@@@@@@@@       
                           @@@@@@       
                              @@        
    
"""
