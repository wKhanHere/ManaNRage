execute as @s store result score @s x run attribute @s minecraft:attack_speed get 100
execute as @s store result score @s y run scoreboard players get @s TheNumberTwentyHundred
execute as @s run scoreboard players operation @s y /= @s x
execute as @s unless entity @s[tag=HeldHighlanderAxe] run scoreboard players set @s HighlanderAxeAttackSpeedCooldown 0
execute as @s unless entity @s[tag=HeldHighlanderAxe] run tag @s add HeldHighlanderAxe
execute as @s unless score @s HighlanderAxeAttackSpeedCooldown >= @s y run scoreboard players add @s HighlanderAxeAttackSpeedCooldown 1
