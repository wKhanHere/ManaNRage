execute as @s at @s run ride @s mount @n[tag=sculk_eye_mount,tag=!IsMountedOn,limit=1]
execute as @s at @s run tag @s add IsMounted
execute at @s as @n[tag=sculk_eye_mount,limit=1,distance=..1] run tag @s add IsMountedOn