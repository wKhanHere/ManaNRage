# All the things that need to happen on load or /reload


#Sculk Mage
team add sculk_mage Sculk_Mage
team modify sculk_mage color dark_blue
scoreboard objectives add PlayerRotationX dummy PlayerRotationX
scoreboard objectives add PlayerRotationY dummy PlayerRotationY
scoreboard objectives add AliveTime dummy AliveTime

#Midnight Spear 
#Fun fact: When enchantments trigger entity effects, they do so in order. In my case, the post attack first calls victim function then attacker function. Don't ask how this works but this is what it is.
scoreboard objectives add TwilightCharges dummy TwilightCharges
scoreboard objectives add MidnightZoneParticleTick dummy MidnightZoneParticleTick
scoreboard objectives add MidnightFangCooldown dummy MidnightFangCooldown

#Highlander Axe
scoreboard objectives add HighlanderAxeRightClickCooldown dummy HighlanderAxeRightClickCooldown
scoreboard objectives add HighlanderStacks dummy HighlanderStacks
scoreboard objectives add HighlanderAxeAttackSpeedCooldown dummy HighlanderAxeAttackSpeedCooldown

#Some variables and constants for general stuff
scoreboard objectives add x dummy x
scoreboard objectives add y dummy y
scoreboard objectives add TheNumberTwentyHundred dummy TheNumberTwentyHundred
scoreboard players set @a TheNumberTwentyHundred 2000

#x and y are used in high lander axe, keep that in mind if using x and y again, or just rebrand to another variable. i ain t doing it rn