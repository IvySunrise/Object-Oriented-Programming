from Objectorientedprogramming import Enemy
Herbert = Enemy("Herbert", 0)
n = 0
wants_to_prod = str(input("You wanna prod him? Press the enter button"))
while wants_to_prod == "" and n < 5:
    Herbert.prod(n)
    Herbert.increase()
    n = n + 1
    wants_to_prod = str(input(""))

