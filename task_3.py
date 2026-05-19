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
    @staticmethod
    def get_points_for_meters(meters):
        if meters < 0 :
            return 'Количество метров не может быть отрицательным'
        else:
            return points + int(meters * 0.5)

class TotalPoints(PointsForPlace, PointsForMeters):
    def get_total_points(self,place, meters):
        total = self.get_points_for_place(place) + self.get_points_for_meters(meters)
        return total
    
points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10)) 
