execute as @a[distance=..9] at @s run effect give @s minecraft:darkness 2 0 true

execute as @e[distance=..9,scores={MidnightFangCooldown=15..},type=!armor_stand,type=!item,type=!experience_orb] at @s if data entity @s Health run summon minecraft:evoker_fangs ~ ~ ~
execute as @e[distance=..9,scores={MidnightFangCooldown=15..},type=!armor_stand,type=!item,type=!experience_orb] if data entity @s Health run scoreboard players set @s MidnightFangCooldown 0
execute as @e[distance=..9,type=!armor_stand,type=!item,type=!experience_orb] at @s if data entity @s Health run scoreboard players add @s MidnightFangCooldown 1

scoreboard players add @s AliveTime 1
execute as @s if score @s AliveTime matches 200.. run function mana_n_rage:gear/midnight_spear/dispose_zone
