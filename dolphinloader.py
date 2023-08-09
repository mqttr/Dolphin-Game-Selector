import os, random

# Add path of Dolphin.exe  Win+R "SystemPropertiesAdvanced" > "Eviorment Variables" > "System Variables" > "Path" > EDIT > New "add Path/To/Dolphin.exe" 

# Tally up all the RoMs
rom_path="D:\My Games\.Emulators\Dolphin-x64\.EmuGames\\"
dir_list = os.listdir(rom_path)

game_path = ""
game_name = ""
ext=".dasd"

print("Everything in \"" + rom_path + "\" :")
print(dir_list)

for name in dir_list:
    if not name.endswith(ext):
        dir_list.remove(name)
        print(name + " removed")

print(dir_list)


# # Random selection of RoM in path
# game_name = random.choice(dir_list)
# game_path = rom_path+game_name


# print("Game: \"" + game_path + "\" Selected.")

# Command = " Dolphin.exe --batch --exec="Path\To\Game" "
game_path="Dolphin.exe --batch --exec=\"" + game_path + "\""
os.system(game_path)

# exit()