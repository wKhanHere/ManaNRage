execute as @s at @s run scoreboard players add @s TwilightCharges 1
execute as @s at @s if score @s TwilightCharges matches 10.. run scoreboard players set @s TwilightCharges 10
execute as @n[tag=midnight_spear_hit,sort=nearest] at @s if entity @p[scores={TwilightCharges=10..}] run function mana_n_rage:gear/midnight_spear/midnight_zone
execute as @s if entity @s[scores={TwilightCharges=10..}] run scoreboard players set @s TwilightCharges 0