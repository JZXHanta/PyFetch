class bcolors:
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
         {bcolors.FAIL}**{bcolors.ENDC}@@@@@@@                      
     {bcolors.FAIL}**    **{bcolors.ENDC} @@@@@@@@@@@@@@@@@@        
       {bcolors.FAIL}** ******{bcolors.ENDC}@@@@@@@@@@@@@@@@@@@@    
    @@   {bcolors.FAIL}***** ****{bcolors.ENDC}@@@@{bcolors.FAIL}******{bcolors.ENDC}@@%%@@@@@@ 
   {bcolors.OKBLUE}++{bcolors.ENDC}@@@   {bcolors.FAIL}*******{bcolors.ENDC}@@@@{bcolors.FAIL}******{bcolors.ENDC}%@#{bcolors.OKGREEN}===={bcolors.ENDC}%@@@@
    {bcolors.OKBLUE}+++{bcolors.ENDC}@@@@@@@{bcolors.FAIL}***{bcolors.ENDC} @@@#{bcolors.FAIL}*****{bcolors.ENDC}#@@{bcolors.OKGREEN}====={bcolors.ENDC}*@@@@
 {bcolors.OKBLUE}++    ++{bcolors.ENDC} @@@@@@@@@@@#####{bcolors.FAIL}*{bcolors.ENDC}@@{bcolors.OKGREEN}====={bcolors.ENDC}+@@@@ 
   {bcolors.OKBLUE}++ ++++++{bcolors.ENDC}@@%%@@@@###@@@@@@@*{bcolors.OKGREEN}=={bcolors.ENDC}+@@@@  
@@   {bcolors.OKBLUE}+++ ++++++{bcolors.ENDC}@@@@{bcolors.OKBLUE}++++++{bcolors.ENDC}%@+=*@@@%@@@@  
  @@   {bcolors.OKBLUE}+++++++{bcolors.ENDC}@@@@{bcolors.OKBLUE}++++++{bcolors.ENDC}%@%{bcolors.WARNING}-----{bcolors.ENDC}%@@@@   
   @@@@@@@{bcolors.OKBLUE}+++{bcolors.ENDC}#@@@#{bcolors.OKBLUE}+++++{bcolors.ENDC}#@%{bcolors.WARNING}-----{bcolors.ENDC}=@@@@    
      @@@@@@@@@@@@@@@@%@@{bcolors.WARNING}-----{bcolors.ENDC}=@@@@     
         @@@@@@@@@@@@@@@@@@#{bcolors.WARNING}--{bcolors.ENDC}%@@@      
                       @@@@@@@@@@       
                           @@@@@@       
                              @@        
    
"""
