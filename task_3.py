class PointsForPlace:
    def get_points_for_place(self,place):
        self.place = place
        place = 0
        if self.place > 100:
            return "Баллы начисляются только первым 100 участникам"
        
        elif self.place <= 0:
            return 'Спортсмен не может занять нулевое или отрицательное место'
        
        else:
            return points + (101 - self.place)


class PointsForPlace:
    def get_points_for_place(self,place):
        self.place = place
        place = 0
        if self.place > 100:
            return "Баллы начисляются только первым 100 участникам"
        
        elif self.place <= 0:
            return 'Спортсмен не может занять нулевое или отрицательное место'
        
        else:
            return points + (101 - self.place)


class PointsForMeters:
    def get_points_for_meters(self,meters):
        self.meters = meters
        if self.meters < 0 :
            return 'Количество метров не может быть отрицательным'
        else:
            return points + int(self.meters * 0.5)

class PointsForPlace:
    def get_points_for_place(self,place):
        self.place = place
        place = 0
        if self.place > 100:
            return "Баллы начисляются только первым 100 участникам"
        
        elif self.place <= 0:
            return 'Спортсмен не может занять нулевое или отрицательное место'
        
        else:
            return points + (101 - self.place)


class PointsForMeters:
    def get_points_for_meters(self,meters):
        self.meters = meters
        if self.meters < 0 :
            return 'Количество метров не может быть отрицательным'
        else:
            return points + int(self.meters * 0.5)

class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        super().__init__()
    def get_total_points(self, meters, place):
        self.total = self.get_points_for_place(place) + self.get_points_for_meters(meters)C
        return self.total
    
points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10)) 
    
points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10)) 


class PointsForMeters:
    def get_points_for_meters(self,meters):
        self.meters = meters
        if self.meters < 0 :
            return 'Количество метров не может быть отрицательным'
        else:
            return points + int(self.meters * 0.5)

class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        super().__init__()
    def get_total_points(self, meters, place):
        self.total = self.get_points_for_place(place) + self.get_points_for_meters(meters)C
        return self.total
    
points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10)) 

class TotalPoints(PointsForPlace, PointsForMeters):
    def __init__(self):
        super().__init__()
    def get_total_points(self, meters, place):
        self.total = self.get_points_for_place(place) + self.get_points_for_meters(meters)C
        return self.total
    
points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10)) 
