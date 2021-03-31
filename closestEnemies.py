
# def closest_enemies(tuple(int,int), list1(tuple(int, int))):
#     pass

def get_distance(a,b):
    return ((((b[0]-a[0])**2) + ((b[1]-a[1])**2) )**(1/2))


def closest_enemies(hero_pos, enemy_pos): #(tuple, list(tuples))
    n = len(enemy_pos)
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, n - 1):
            if get_distance(hero_pos, enemy_pos[i]) > get_distance(hero_pos, enemy_pos[i+1]):
                enemy_pos[i],enemy_pos[i+1] = enemy_pos[i+1], enemy_pos[i]
                swapped = True
    # return enemy_pos #For testing

def test(val1,val2):
    if val1 != val2:
        print(f'Test Failed! \n\tActual: {val1} \n\tExpected: {val2}')
    else:
        print(f'Test PASSED! \n\tActual: {val1}  \n\tExpected: {val2}')

heropos1 = (0,0)
heropos2 = (-5,-2)


enemylsit = [(2,6),(4,8),(1,3),(1,4),(8,8),(1,3),(8,7),(8,6),(2,2),(22,29),(1,1),(3,3),(3,1)]  #for testing only 

def main():
        # test(closest_enemies((0,0), enemylsit),[(1, 1), (2, 2), (1, 3), (1, 3), (3, 1), (1, 4), (3, 3), (2, 6), (4, 8), (8, 6), (8, 7), (8, 8), (22, 29)])
        closest_enemies(heropos1,enemylsit)
        print(enemylsit)
        test(enemylsit,[(1, 1), (2, 2), (1, 3), (1, 3), (3, 1), (1, 4), (3, 3), (2, 6), (4, 8), (8, 6), (8, 7), (8, 8), (22, 29)])
        closest_enemies(heropos2, enemylsit)
        print(enemylsit)


if __name__ == '__main__':
    main()
    

