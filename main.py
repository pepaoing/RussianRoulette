# Imports = Imortar Liberias
import random
from time import sleep

# Made by pepa#7928 and Ryevk#6003

# Variables = Variables
lifes = 6

#code
banner = """


┬─┐┬ ┬┌─┐┌─┐┬┌─┐┌┐┌  ┬─┐┌─┐┬ ┬┬  ┌─┐┌┬┐┌┬┐┌─┐
├┬┘│ │└─┐└─┐│├─┤│││  ├┬┘│ ││ ││  ├┤  │  │ ├┤
┴└─└─┘└─┘└─┘┴┴ ┴┘└┘  ┴└─└─┘└─┘┴─┘└─┘ ┴  ┴ └─┘

    ^!!^
  :75YJJ!~^^^^^^^^^^^^^^^^^^~!!77???????JJJJ??7^:::^~:
  ~YYJ??JJJJJJJJJJJJJ????JJJJ5?JJPY???J?JJY5?5GP5Y?:
   ::::::::::^^~?55PY?YYYYYY55555BP??????!777GGGGPJ7!^.
                 ............~5PGJ?55555P555YBGBPY5P5YJ?7~.
                              7Y5~7BBBBBBBBBJPGGGPPPPPGP55:
                              !YY5555PPPP5PPPPGPPPPPGBP5557
                              ^77?J55J7!?PPPP5P5PP55GGP5?J5?:
                                   77    !Y~:.75J~^~7PB5??5PY~
                                   :!    ~!   :?     .?GGGGGP5?.
                                    :^^!!~..:^!:       YGGGGGPP?.
                                      ..::::::         !PGGG5PPP7
                                                       ~PGGGPPGP5^
                                                       !PPGPGGPPP?.
                                                       7GGGGGGGGGP~
                                                       ^7??JJJJJJ?~

"""
print(banner)
sleep(1)
print("Hola, bienvenido a la ruleta rusa, tu objetivo es llegar a 10 vidas. Aunque no puedes hacer nada ya que es RNG xD Made by pepa#7928 and Ryevk#6003")
sleep(1)


while True:
    numero = random.randint(1,6)
    if numero == 1:
      lifes -= 1
      if lifes < 0:
          lifes = 0
      elif lifes > 10:
          lifes = 10
      print("Vaya, el numero 1, al menos solo pierdes una vida. Te quedan", lifes, "vidas.")
      sleep(1)
    elif numero == 2:
        lifes -= 3
        if lifes < 0:
            lifes = 0
        elif lifes > 10:
            lifes = 10
        print("Ups! Numero 2, pierdes 3 vidas. Te quedan", lifes, "vidas.")
        sleep(1)
    elif numero == 3:
        if lifes < 0:
            lifes = 0
        elif lifes > 10:
            lifes = 10
        lifes += 2
        print("Lucky you! Mas 2 vidas. Te quedan", lifes, "vidas.")
        sleep(1)
    elif numero == 7:
        lifes = 0
        if lifes < 0:
            lifes = 0
        elif lifes > 10:
            lifes = 10
        print("Vaya, Game Over, el numero 4 es el numero de  la muerte japones. Has perdido todas tus vidas.")
        sleep(1)
    elif numero == 5:
        lifes += 3
        if lifes < 0:
            lifes = 0
        elif lifes > 10:
            lifes = 10
        print("Mira! El 5, la contrapartida del 2! En vez de perder, ganas 3 vidas! Te quedan", lifes, "vidas.")
        sleep(1)
    elif numero == 6:
        lifes -= 2
        if lifes < 0:
            lifes = 0
        elif lifes > 10:
            lifes = 10
        print("Whoops! El numero 6! -2 vidas, te quedan", lifes, "vidas.")
        sleep(1)
    if lifes <= 0:
        print("Game Over, 0 vidas.")
        wait = input("Press Enter to exit.")
        break
    if lifes >= 10:
        print("Felicidades has ganado.")
        wait = input("Press Enter to exit.")
        break
