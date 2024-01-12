#!/usr/bin/env python3

"""Python app for testing pythagoras approximations"""

from getpass import getpass
from tqdm import trange

from src import pythagorean


LOGO:str = """
 (   The one and only (or at least better than Denton's one)
 )\ )        )   )                                                                                    )         
(()/((    ( /(( /(    ) (  (     (     (    )            )             (          ) (     )      ) ( /(    (    
 /(_))\ ) )\())\())( /( )\))( (  )(   ))\( /(  (      ( /( `  )  `  )  )(   (  ( /( )\   (    ( /( )\())(  )(   
(_))(()/((_))((_)\ )(_)|(_))\ )\(()\ /((_)(_)) )\ )   )(_))/(/(  /(/( (()\  )\ )\()|(_)  )\  ')(_)|_))/ )\(()\  
| _ \)(_)) |_| |(_|(_)_ (()(_|(_)((_|_))((_)_ _(_/(  ((_)_((_)_\((_)_\ ((_)((_|(_)\ (_)_((_))((_)_| |_ ((_)((_) 
|  _/ || |  _| ' \/ _` / _` / _ \ '_/ -_) _` | ' \)) / _` | '_ \) '_ \) '_/ _ \ \ / | | '  \() _` |  _/ _ \ '_| 
|_|  \_, |\__|_||_\__,_\__, \___/_| \___\__,_|_||_|  \__,_| .__/| .__/|_| \___/_\_\ |_|_|_|_|\__,_|\__\___/_|   
     |__/              |___/                              |_|   |_|        By Koodarimpi :3     
"""

diffs:list = []
diff_percents:list = []


def main() -> None:
    """Main function""" 
    print('\033[?25l\033[2J', end="")      # Hide the cursor and clear the terminal
    print(LOGO)
    getpass("           [Press enter to start]\n")
    for i in trange(1,5000):
        for j in range(1,5000):
            calc = pythagorean.calc((i,j))
            diff = abs(calc - pythagorean.approx((i,j)))

            diffs.append(diff)
            diff_percents.append((diff/calc)*100)

    avg_err:float = round(sum(diffs)/len(diffs),2)
    avg_err_percent:float = round(sum(diff_percents)/len(diff_percents),2)
    print(
        f'Avg error: {avg_err} \nAvg error percent: {avg_err_percent}%'
    )
    print('\033[?25h', end="")              # Show the cursor again

if __name__=="__main__":
    main()
