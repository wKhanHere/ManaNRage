execute as @s at @s unless entity @n[tag=sculk_eye_mount,distance=..1] run kill @s 
#kill mechanism if mount is dead is actually handled here lmao, dont delete this line

execute as @n[tag=IsMountedOn] at @n[tag=IsMountedOn] if entity @n[type=minecraft:player,distance=..3] run function mana_n_rage:mob/sculk_mage/eyes/explosion