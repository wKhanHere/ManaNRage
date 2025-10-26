execute at @s as @s run summon armor_stand ~ ~ ~ {Tags:["midnight_zone"],Invisible:1b,Marker:1b,NoGravity:1b}
execute at @s as @n[tag=midnight_zone,sort=nearest,limit=1] run scoreboard players add @s MidnightZoneParticleTick 0
kill @s