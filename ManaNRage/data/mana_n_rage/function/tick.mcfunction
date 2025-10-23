# What makes this datapack tick


#Sculk Mage

#Sculk Mage - Eyes
execute as @e[tag=sculk_eye_mount,tag=IsMountedOn] at @s run function mana_n_rage:mob/sculk_mage/eyes/mount_tick
execute as @e[tag=sculk_eye,tag=IsMounted] at @s run function mana_n_rage:mob/sculk_mage/eyes/eye_tick

