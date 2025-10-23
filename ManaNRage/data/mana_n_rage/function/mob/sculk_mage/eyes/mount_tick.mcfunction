execute as @p[limit=1,sort=nearest] store result score @s PlayerRotationX run data get entity @s Rotation[0] 1000
execute as @p[limit=1,sort=nearest] store result score @s PlayerRotationY run data get entity @s Rotation[1] 1000

execute as @p[limit=1,sort=nearest] run scoreboard players add @s PlayerRotationX 180000
execute as @p[limit=1,sort=nearest] run execute if score @s PlayerRotationX matches 180001.. run scoreboard players remove @s PlayerRotationX 360000

execute as @s store result entity @s Rotation[0] double 0.001 run scoreboard players get @p PlayerRotationX
execute as @s store result entity @s Rotation[1] double -0.001 run scoreboard players get @p PlayerRotationY

execute as @n[tag=IsMounted] store result entity @s Rotation[0] double 0.001 run scoreboard players get @p PlayerRotationX
execute as @n[tag=IsMounted] store result entity @s Rotation[1] double -0.001 run scoreboard players get @p PlayerRotationY


execute as @s at @s unless entity @n[type=minecraft:player,distance=..3] run tp @s ^ ^ ^0.3
execute as @s at @s unless entity @n[type=minecraft:player,distance=..3] run tp @s ^ ^ ^0.3
execute as @s at @s unless entity @n[type=minecraft:player,distance=..3] run tp @s ^ ^ ^0.3

execute anchored eyes run particle electric_spark ~0.4 ~ ~0.0 0 0 0 0 0 force
execute anchored eyes run particle electric_spark ~0.32 ~ ~0.24 0 0 0 0 0 force
execute anchored eyes run particle electric_spark ~0.12 ~ ~0.38 0 0 0 0 0 force
execute anchored eyes run particle electric_spark ~-0.12 ~ ~0.38 0 0 0 0 0 force
execute anchored eyes run particle electric_spark ~-0.32 ~ ~0.24 0 0 0 0 0 force
execute anchored eyes run particle electric_spark ~-0.4 ~ ~0.0 0 0 0 0 0 force
execute anchored eyes run particle electric_spark ~-0.32 ~ ~-0.24 0 0 0 0 0 force
execute anchored eyes run particle electric_spark ~-0.12 ~ ~-0.38 0 0 0 0 0 force
execute anchored eyes run particle electric_spark ~0.12 ~ ~-0.38 0 0 0 0 0 force
execute anchored eyes run particle electric_spark ~0.32 ~ ~-0.24 0 0 0 0 0 force

execute as @s run scoreboard players add @s AliveTime 1

execute as @s at @s if score @s AliveTime matches 100.. run function mana_n_rage:mob/sculk_mage/eyes/explosion

