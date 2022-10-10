execute @e[type=armor_stand, name=maze] ~6 -60 ~6 execute @a[r=3, tag=player] ~~~ tag @e[type=armor_stand, name=maze] add chunk
execute @e[tag=chunk] ~~~ tp @s ~6 ~ ~6
execute @e[tag=chunk] ~~~ function create_maze
tag @e remove chunk

execute @e[type=armor_stand, name=maze] ~6 -60 ~ execute @a[r=3, tag=player] ~~~ tag @e[type=armor_stand, name=maze] add chunk
execute @e[tag=chunk] ~~~ tp @s ~6 ~ ~
execute @e[tag=chunk] ~~~ function create_maze
tag @e remove chunk

execute @e[type=armor_stand, name=maze] ~ -60 ~6 execute @a[r=3, tag=player] ~~~ tag @e[type=armor_stand, name=maze] add chunk
execute @e[tag=chunk] ~~~ tp @s ~ ~ ~6
execute @e[tag=chunk] ~~~ function create_maze
tag @e remove chunk

execute @e[type=armor_stand, name=maze] ~-6 -60 ~6 execute @a[r=3, tag=player] ~~~ tag @e[type=armor_stand, name=maze] add chunk
execute @e[tag=chunk] ~~~ tp @s ~-6 ~ ~6
execute @e[tag=chunk] ~~~ function create_maze
tag @e remove chunk

execute @e[type=armor_stand, name=maze] ~6 -60 ~-6 execute @a[r=3, tag=player] ~~~ tag @e[type=armor_stand, name=maze] add chunk
execute @e[tag=chunk] ~~~ tp @s ~6 ~ ~-6
execute @e[tag=chunk] ~~~ function create_maze
tag @e remove chunk

execute @e[type=armor_stand, name=maze] ~-6 -60 ~-6 execute @a[r=3, tag=player] ~~~ tag @e[type=armor_stand, name=maze] add chunk
execute @e[tag=chunk] ~~~ tp @s ~-6 ~ ~-6
execute @e[tag=chunk] ~~~ function create_maze
tag @e remove chunk

execute @e[type=armor_stand, name=maze] ~-6 -60 ~ execute @a[r=3, tag=player] ~~~ tag @e[type=armor_stand, name=maze] add chunk
execute @e[tag=chunk] ~~~ tp @s ~-6 ~ ~
execute @e[tag=chunk] ~~~ function create_maze
tag @e remove chunk

execute @e[type=armor_stand, name=maze] ~ -60 ~-6 execute @a[r=3, tag=player] ~~~ tag @e[type=armor_stand, name=maze] add chunk
execute @e[tag=chunk] ~~~ tp @s ~ ~ ~-6
execute @e[tag=chunk] ~~~ function create_maze
tag @e remove chunk

execute @e[name=maze, type=armor_stand] ~~~ tp @s ~ -30 ~