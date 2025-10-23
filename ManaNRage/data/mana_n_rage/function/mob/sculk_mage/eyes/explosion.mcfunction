execute as @p run tell @a "You have triggered the sculk eye explosion!"

execute as @s at @s anchored eyes run particle minecraft:sonic_boom ~ ~ ~ 2 2 2 0 10 force

execute as @s at @s run effect give @e[distance=..3] darkness 5 0 true
execute as @s at @s run effect give @e[distance=..3] wither 5 2 true

execute as @s at @s run playsound minecraft:event.mob_effect.raid_omen hostile @a ~ ~ ~ 2 1

execute as @s at @s run summon armor_stand ~ ~ ~ {Tags:["sculk_eye_explosion"],Invisible:1b,Invulnerable:1b,equipment:{feet:{id:sculk,components:{"minecraft:enchantments":{"mana_n_rage:sculk_eye_explosion":1}}}}}
execute as @s at @s run kill @s