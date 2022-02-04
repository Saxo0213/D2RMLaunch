# Diablo II Resurrected / D2R / MLunch

You can open D2R Game without ProcessExplorer / handler64

Start the program, you can input your gamename for program to close the Multilimit (ex:D2R,D2RB,D2RC.....Use "," separate )

![Process properties](https://github.com/Saxo0213/D2RMLunch/blob/main/image/03.PNG)

When program find new game, the word will be red color

![Process properties](https://github.com/Saxo0213/D2RMLunch/blob/main/image/04.PNG)

You can press mouse rightbutton to be transparent 

![Process properties](https://github.com/Saxo0213/D2RMLunch/blob/main/image/05.PNG)


# Diablo II Resurrected / D2R / MLunch
- Download EXE Program
  - Download from GoogleDrive ==> [GoogleDrive](https://drive.google.com/file/d/1jKt1eKyVklDpK5nt6-196NnIuphAlTsL/view?usp=sharing)
  - Password: ShareBySaxo

###

"My antivirus flagged this as a virus! Are you trying to steal my account!?"

No. python are often flagged as malicious or trojans. Feel free to download [python](https://www.python.org/) and compile it yourself from source. 
# Instruction 
- The Same D2R Folder Method
  - 1、Start D2Rprocess
  - 2、copy D2R.exe for another name EX: D2RB.exe
  - loop↓
  - 3、Login Battle Account
  - 4、Start Game
  - 5、When in Lobby ,Close the game and Run D2RB.exe in Lobby
  - 6、Logout Battle Account and start another account

![Process properties](https://github.com/Saxo0213/D2RMLunch/blob/main/image/01.PNG)

- Different D2R Folder Method
  - 1、Start D2Rprocess
  - 2、Copy D2R Folder
  - 3、In the BattleNet setting, Allow open another Battle.net
  - 4、Use 1st Folder D2RLunch, Login(Account A)、start game
  - 5、when in lobby
  - 5、when in lobby Use next Folder D2RLunch to Login(Account B) and start game
![Process properties](https://github.com/Saxo0213/D2RMLunch/blob/main/image/02.PNG)

# About pywinhandle different
  because system only have one keyword, so I change the code out function when find it
- before
        
        result.append(dict(process_id=process_id, handle=handle, name=handle_name, type=handle_type))

- after 
        
        result=(dict(process_id=process_id, handle=handle, name=handle_name, type=handle_type))
        if keyname in result['name']:
          return result
  
# Process Utilities
- [pywinhandle](https://github.com/yihleego/pywinhandle) By yihleego
- [Handle](https://docs.microsoft.com/en-us/sysinternals/downloads/handle)
- [Process Explorer](https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer)

# ThanK
- Thank [yihleego](https://github.com/yihleego) solved the code problem
