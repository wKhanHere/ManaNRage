#Minecraft calculates attack speed tick req as 20/speed; so probably rounding is just how java normally does it



#Sculk Mage

#Sculk Mage - Eyes
execute as @e[tag=sculk_eye_mount,tag=IsMountedOn] at @s run function mana_n_rage:mob/sculk_mage/eyes/mount_tick
execute as @e[tag=sculk_eye,tag=IsMounted] at @s run function mana_n_rage:mob/sculk_mage/eyes/eye_tick

#Frenzied Earthling

#Midnight Spear
#Too lazy to make another scoreboard for tracking how long target has been tagged by midnight target, so i just killed it
execute as @e[tag=midnight_spear_hit] at @s run scoreboard players add @s AliveTime 1
execute as @e[tag=midnight_spear_hit,scores={AliveTime=20..}] at @s run kill @s
execute as @e[tag=midnight_zone] at @s run function mana_n_rage:gear/midnight_spear/midnight_zone_tick
execute as @e[tag=midnight_zone] at @s run function mana_n_rage:gear/midnight_spear/midnight_zone_tick_particle

#Rose Armour
execute as @a[tag=RoseArmorOn] at @s run function mana_n_rage:gear/rose_armour/armour_tick

#HighlanderAxe
execute as @e[tag=HeldHighlanderAxe] if predicate mana_n_rage:isnotholdinghighlanderaxe run tag @s remove HeldHighlanderAxe