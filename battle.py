from fighter import Fighter
import time

run = True
fighter_1 = Fighter(12, 10, 100)
fighter_2 = Fighter(15, 5, 100)

while run:
    time.sleep(0.5)
    print('======')
    if fighter_1.hp > 0:
        damage = fighter_1.strike()
        computed_damage = fighter_2.get_damage(damage)
        print(f'Fighter 1 strikes for {computed_damage} hit points')
        print(f'Fighter 2 has {fighter_2.hp} hp')
    else:
        run = False
        print(f'Fighter 2 Wins !')
        break

    time.sleep(0.5)
    print('======')
    if fighter_2.hp > 0:
        damage = fighter_2.strike()
        computed_damage = fighter_1.get_damage(damage)
        print(f'Fighter 2 strikes for {computed_damage} hit points')
        print(f'Fighter 1 has {fighter_1.hp} hp')
    else:
        run = False
        print(f'Fighter 1 Wins !')
        break
