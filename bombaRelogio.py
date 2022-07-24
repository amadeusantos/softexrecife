from time import sleep

print("Iniciando contagem regressiva.")
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print("BUM!")
