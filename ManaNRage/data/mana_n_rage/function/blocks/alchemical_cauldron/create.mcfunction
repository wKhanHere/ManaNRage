execute as @s at @s align xyz run tp ~0.5 ~0.5 ~0.5
execute as @s at @s run summon armor_stand ~0.24 ~-0.6 ~0.24 {NoGravity:1b,Invulnerable:1b,ShowArms:1b,HasVisualFire:0b,Small:1b,Invisible:1b,Tags:["alchemical_cauldron","undeployed","alcCNo1"],DisabledSlots:4079166}
execute as @s at @s run summon armor_stand ~-0.24 ~-0.6 ~0.24 {NoGravity:1b,Invulnerable:1b,ShowArms:1b,HasVisualFire:0b,Small:1b,Invisible:1b,Tags:["alchemical_cauldron","undeployed","alcCNo2"],DisabledSlots:4079166}
execute as @s at @s run summon armor_stand ~0.24 ~-0.6 ~-0.24 {NoGravity:1b,Invulnerable:1b,ShowArms:1b,HasVisualFire:0b,Small:1b,Invisible:1b,Tags:["alchemical_cauldron","undeployed","alcCNo3"],DisabledSlots:4079166}
execute as @s at @s run summon armor_stand ~-0.24 ~-0.6 ~-0.24 {NoGravity:1b,Invulnerable:1b,ShowArms:1b,HasVisualFire:0b,Small:1b,Invisible:1b,Tags:["alchemical_cauldron","undeployed","alcCNo4"],DisabledSlots:4079166}
execute as @e[tag=undeployed,limit=4,sort=nearest] at @s run tp @s ~ ~ ~ facing entity @n[type=item, nbt = {Item: {id: "minecraft:nether_star"}}] eyes
execute as @e[tag=undeployed,limit=4,sort=nearest] run tag @s remove undeployed
execute as @s run kill @s 