#Нужно написать три класса для спортивных соревнований — разные способы начислять спортсменам очки:

#1️⃣ PointsForPlace — количество очков высчитывается с учётом места, которое занял спортсмен.

#2️⃣# PointsForMeters — количество очков высчитывается с учётом расстояния, на которое спортсмен метнул диск.

#3️⃣ TotalPoints — умеет работать и с местом спортсмена, и с расстоянием.

#Теперь подробно:

#Напиши класс PointsForPlace. Он получает количество очков в зависимости от места, которое занял спортсмен.

#В этом классе напиши метод get_points_for_place(), который принимает аргумент place — целое число. Причём:

#Если место строго больше 100, должно выводиться сообщение 'Баллы начисляются только первым 100 участникам'.

#Если как аргумент передали значение меньше 1, должно печататься сообщение 'Спортсмен не может занять нулевое или отрицательное место'.

#В остальных случаях начисляются очки по формуле: 101 - place.

#Изначально количество очков равно нулю: подумай, как это отобразить в коде.

#Метод get_points_for_place() должен возвращать points.

<<<<<<< HEAD
 
=======
#Напиши класс PointsForMeters. Он рассчитывает очки в зависимости от количества метров, на которое спортсмен толкнул ядро или метнул диск: расстояние*0,5. Например, если расстояние 10 метров, спортсмен получит 5 очков.
#Напиши метод get_points_for_meters(), который принимает аргумент meters — целое число. Причём:
#Если количество метров меньше нуля, должно выводиться сообщение 'Количество метров не может быть отрицательным'.
#В остальных случаях начисляются очки по формуле: «количество метров умножить на 0.5».
#Метод должен возвращать points. Изначально количество очков — 0.
#
# Напиши класс TotalPoints для многоборцев. Он наследуется сразу от двух классов — PointsForPlace и PointsForMeters и реализует все их методы. Также он должен содержать:
#метод get_total_points(), который принимает как аргументы meters и place;
#переменную total, которая суммирует значения методов get_points_for_place() и get_points_for_meters().
#Метод возвращает переменную total.#
#❗ Подумай, какие методы в этом задании могут быть статическими. Если метод можно сделать статическим — делай.
#Подумай, какая область видимости должна быть у переменной points — глобальная или локальная.
points = 0
class PointsForPlace:
    @staticmethod
    def get_points_for_place(place):   
        
        if place > 100:
            return "Баллы начисляются только первым 100 участникам"
        
        elif place <= 0:
            return 'Спортсмен не может занять нулевое или отрицательное место'
        
        else:
            return points + (101 - place)
>>>>>>> 33629e93cd6179b0a5c54c1dcc1893cbe17a5029

#Напиши класс PointsForMeters. Он рассчитывает очки в зависимости от количества метров, на которое спортсмен толкнул ядро или метнул диск: расстояние*0,5. Например, если расстояние 10 метров, спортсмен получит 5 очков.

#Напиши метод get_points_for_meters(), который принимает аргумент meters — целое число. Причём:

#Если количество метров меньше нуля, должно выводиться сообщение 'Количество метров не может быть отрицательным'.

#В остальных случаях начисляются очки по формуле: «количество метров умножить на 0.5».

#Метод должен возвращать points. Изначально количество очков — 0.

#

# Напиши класс TotalPoints для многоборцев. Он наследуется сразу от двух классов — PointsForPlace и PointsForMeters и реализует все их методы. Также он должен содержать:

#метод get_total_points(), который принимает как аргументы meters и place;

#переменную total, которая суммирует значения методов get_points_for_place() и get_points_for_meters().

#Метод возвращает переменную total.#

#❗ Подумай, какие методы в этом задании могут быть статическими. Если метод можно сделать статическим — делай.

#Подумай, какая область видимости должна быть у переменной points — глобальная или локальная.

points = 0

class PointsForPlace:

    @staticmethod

    def get_points_for_place(place):  

       

        if place > 100:

            return "Баллы начисляются только первым 100 участникам"

       

        elif place <= 0:

            return 'Спортсмен не может занять нулевое или отрицательное место'

       

        else:

            return points + (101 - place)

 

class PointsForMeters:
<<<<<<< HEAD

    @staticmethod

    def get_points_for_meters(meters):

        if meters < 0 :

=======
    @staticmethod
    def get_points_for_meters(meters):
        if meters < 0 :
>>>>>>> 33629e93cd6179b0a5c54c1dcc1893cbe17a5029
            return 'Количество метров не может быть отрицательным'

        else:
<<<<<<< HEAD

            return points + int(meters * 0.5)

 

class TotalPoints(PointsForPlace, PointsForMeters):

    def get_total_points(self,place, meters):

        total = self.get_points_for_place(place) + self.get_points_for_meters(meters)

        return total

   

=======
            return points + int(meters * 0.5)

class TotalPoints(PointsForPlace, PointsForMeters):
    def get_total_points(self,place, meters):
        total = self.get_points_for_place(place) + self.get_points_for_meters(meters)
        return total
    
>>>>>>> 33629e93cd6179b0a5c54c1dcc1893cbe17a5029
points_for_place = PointsForPlace()

print(points_for_place.get_points_for_place(10))

 

points_for_meters = PointsForMeters()

print(points_for_meters.get_points_for_meters(10))

 

total_points = TotalPoints()

print(total_points.get_points_for_place(10))

print(total_points.get_points_for_meters(10))
<<<<<<< HEAD

print(total_points.get_total_points(100, 10))
=======
print(total_points.get_total_points(100, 10)) 
>>>>>>> 33629e93cd6179b0a5c54c1dcc1893cbe17a5029
