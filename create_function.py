# 설정 불러오기
from settings import *


# create_maze.mcfunction
with open("create_maze.mcfunction", "w") as f:
    # 이전 미로 제거
    # for x in range(TO, END, STEP):
    #     for z in range(TO, END, STEP):
    #         f.write(f"execute @e[type=armor_stand, name=maze] ~{x} -60 ~{z} fill ~{WIDTH-1} -60 ~{WIDTH-1} ~-{WIDTH-1} {-60+(HEIGHT+2)} ~-{WIDTH-1} air\n")
    #         f.write(f"execute @e[type=armor_stand, name=maze] ~{x} -60 ~{z} fill ~{WIDTH-1} -61 ~{WIDTH-1} ~-{WIDTH-1} -61 ~-{WIDTH-1} grass\n")
    
    # 미로 생성
    for x in range(TO, END, STEP):
        for z in range(TO, END, STEP):
            f.write("scoreboard players random @a[tag=private] direct 1 3\n")
            f.write(f"execute @a[tag=private, scores={{direct=1}}] ~~~ execute @e[type=armor_stand, name=maze] ~{x} -60 ~{z} detect ~ {-60+(HEIGHT+1)} ~ air 0 fill ~{WIDTH-1} ~{HEIGHT-1} ~  ~ ~ ~ {WALL}\n")
            f.write(f"execute @a[tag=private, scores={{direct=2}}] ~~~ execute @e[type=armor_stand, name=maze] ~{x} -60 ~{z} detect ~ {-60+(HEIGHT+1)} ~ air 0 fill ~ ~{HEIGHT-1} ~{WIDTH-1}  ~ ~ ~ {WALL}\n")
            f.write(f"execute @a[tag=private, scores={{direct=3}}] ~~~ execute @e[type=armor_stand, name=maze] ~{x} -60 ~{z} detect ~ {-60+(HEIGHT+1)} ~ air 0 fill ~-{WIDTH-1} ~{HEIGHT-1} ~  ~ ~ ~ {WALL}\n")
            f.write(f"execute @e[type=armor_stand, name=maze] ~{x} -60 ~{z} detect ~ {-60+(HEIGHT+1)} ~ air 0 fill ~{WIDTH-1} -61 ~{WIDTH-1} ~-{WIDTH-1} -61 ~-{WIDTH-1} {FLOOR}\n")
            f.write(f"execute @e[type=armor_stand, name=maze] ~{x} -60 ~{z} detect ~ {-60+(HEIGHT+1)} ~ air 0 fill ~{WIDTH-1} {-60+HEIGHT} ~{WIDTH-1} ~-{WIDTH-1} {-60+HEIGHT} ~-{WIDTH-1} {CEILLING}\n")
            f.write(f"execute @e[type=armor_stand, name=maze] ~{x} -60 ~{z} setblock ~ {-60+(HEIGHT+1)} ~ structure_void\n")
