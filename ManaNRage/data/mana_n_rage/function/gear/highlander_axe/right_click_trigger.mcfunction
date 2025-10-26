execute as @s unless score @s HighlanderAxeRightClickCooldown matches 1.. anchored eyes run particle happy_villager ^ ^ ^3 0.1 0.1 0.1 0 10
advancement revoke @s only mana_n_rage:highlander_axe_right_click
advancement revoke @s only mana_n_rage:highlander_axe_cooldown
execute as @s unless score @s HighlanderAxeRightClickCooldown matches 1.. run scoreboard players set @s HighlanderAxeRightClickCooldown 2

execute as @s if score @s HighlanderStacks matches 5..9 run function mana_n_rage:gear/highlander_axe/abil_1
execute as @s if score @s HighlanderStacks matches 10..14 run function mana_n_rage:gear/highlander_axe/abil_2
execute as @s if score @s HighlanderStacks matches 15.. run function mana_n_rage:gear/highlander_axe/abil_3