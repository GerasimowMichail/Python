# 7 Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат..
a=[0,1]
for x in a:
    for y in a:
        for z in a:
            if not(x or y or z ) == (not x and not y and not z  ):
                print(x, y, z)   