class Dom():
    def __init__(self):
        self.kitlight = False
        self.holllight = False
        self.roomlight = False
        self.toiletlight = False

        self.teapot = False

        self.kitchenblits = False
        self.roomblits = False
        self.hollblits = False

        self.roomtemp = 20.3
        self.kittemp = 22.4
        self.toilettemp = 20.7
        self.holltemp = 25.1

        self.vacuum = False
        self.tv = False


        self.a = f"Кухня 0, свет:{self.kitlight},жалюзи:{self.kitchenblits}, тепмература:{self.kittemp}, чайник:{self.teapot} \n"
        self.b = f"гостиная 1, свет:{self.holllight},жалюзи:{self.hollblits}, тепмература:{self.holltemp}\n"
        self.c = f"Комната 2, свет:{self.roomlight},жалюзи:{self.roomblits}, тепмература:{self.roomtemp}\n"
        self.d = f"Туалет 3, свет:{self.toilettemp}, температура:{self.toilettemp}\n"
        self.Start()
    def Start(self):
        print(self.a)
        print(self.b)
        print(self.c)
        print(self.d)
        self.ans = int(input("выберите ту комнату в которой хотите что-то сделать(нажмите на цифру)"))
        if self.ans == "0":
            self.kitchen1 = int(input("что вы хотите сделать на кухне:\n0 Включить\\выключить свет\n1 Заправить зановеску\n2 Изменить температуру\n3 Включить\\Выключить чайник"))
        elif self.ans == "1":
            self.holl1 = int(input("что вы хотите сделать в гостинице:\n0 Включить\\выключить свет\n1 Заправить зановеску\n2 Изменить температуру\n3 Включить\\Выключить телевизор"))
            Holl()
        elif self.ans == "2":
            self.holl1 = int(input("что вы хотите сделать в комнате:\n0 Включить\\выключить свет\n1 Заправить зановеску\n2 Изменить температуру\n3 Включить\\Выключить Пылесос"))
            Room()
        elif self.ans == "3":
            self.holl1 = int(input("что вы хотите сделать в туалете:\n0 Включить\\выключить свет\n2 Изменить температуру"))
            Toilet()
class Kitchen(Dom):
    def kitchen(self, light, blits, temp, teapot):
        """Изменения на кухне"""
        self.kitlight = light
        self.kitchenblits = blits
        self.toilettemp = temp
        self.teapot = teapot
        if self.kitchen1 == 0:
            if light == False:
                light = True
            else:
                light = False
            self.Start()
        elif self.kitchen1 == 1:
            if blits == False:
                blits = True
            else:
                blits = False
            self.Start()
        elif self.kitchen1 == 2:
            self.tempk = int(input("Введите градусы от 15 - 30"))
            if self.tempk <30 and self.tempk > 15:
                temp = self.tempk
            else:
                self.exitt = int(input("Минимальная температура 15 градуссов, Макс 30"))
            self.Start()
        elif self.kitchen1 == 3:
            if teapot == False:
                teapot = True
            else:
                teapot = False
            self.Start()
        else:
            self.exit1 = int(input("Вы ввели не правильное действие(цифру)хотите продолжить\nда\\нет"))
        if self.exit1 == "Да":
            self.Start()
        else:
            exit()
class Holl(Dom):
    def holl(self, light, blits, temp, tv):
        """Изменения в гостинице"""
        self.kitlight = light
        self.kitchenblits = blits
        self.toilettemp = temp
        self.tv = tv
        if self.holl1 == 0:
            if light == False:
                light = True
            else:
                light = False
            self.Start()
        elif self.holl1 == 1:
            if blits == False:
                blits = True
            else:
                blits = False
            self.Start()
        elif self.holl1 == 2:
            self.tempk = int(input("Введите градусы от 15 - 30"))
            if self.tempk <30 and self.tempk > 15:
                temp = self.tempk
            else:
                self.exitt = int(input("Минимальная температура 15 градуссов, Макс 30: Хотите поменять \n да\\нет"))
                if self.exitt == "да":
                    self.Start()
                else:
                    exit()
            self.Start()
        elif self.holl1 == 3:
            if tv == False:
                tv = True
            else:
                tv = False
            self.Start()
        else:
            self.exit1 = int(input("Вы ввели не правильное действие(цифру)хотите продолжить\nда\\нет"))
        if self.exit1 == "Да":
            self.Start()
        else:
            exit()
class Room(Dom):
    def room(self, light, blits, temp, vacume):
        """Изменения в комнате"""

        self.kitlight = light
        self.kitchenblits = blits
        self.toilettemp = temp
        self.vacuum = vacume
        if self.holl1 == 0:
            if light == False:
                light = True
            else:
                light = False
            self.Start()
        elif self.holl1 == 1:
            if blits == False:
                blits = True
            else:
                blits = False
            self.Start()
        elif self.holl1 == 2:
            self.tempk = int(input("Введите градусы от 15 - 30"))
            if self.tempk <30 and self.tempk > 15:
                temp = self.tempk
            else:
                self.exitt = int(input("Минимальная температура 15 градуссов, Макс 30"))
                if self.exitt == "да":
                    self.Start()
                else:
                    exit()
            self.Start()
        elif self.holl1 == 3:
            if vacume == False:
                vacume = True
            else:
                vacume = False
            self.Start()
        else:
            self.exit1 = int(input("Вы ввели не правильное действие(цифру)хотите продолжить\nда\\нет"))
        if self.exit1 == "Да":
            self.Start()
        else:
            exit()
class Toilet(Dom):
    def toilet(self, light, temp):
        """Изменения в туалете"""
        super().Start()
        self.kitlight = light
        self.toilettemp = temp

        if self.holl1 == 0:
            if light == False:
                light = True
            else:
                light = False
            self.Start()
        elif self.holl1 == 1:
            self.tempk = int(input("Введите градусы от 15 - 30"))
            if self.tempk <30 and self.tempk > 15:
                temp = self.tempk
            else:
                self.exitt = int(input("Минимальная температура 15 градуссов, Макс 30"))
                if self.exitt == "да":
                    self.Start()
                else:
                    exit()
            self.Start()
        else:
            self.exit1 = int(input("Вы ввели не правильное действие(цифру)хотите продолжить\nда\\нет"))
        if self.exit1 == "Да":
            self.Start()
        else:
            exit()
dom = Dom
dom()



