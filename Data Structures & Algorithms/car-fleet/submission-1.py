class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #cars(position, speed) stored in a array representing one fleet.
        #fleets are pushed onto a stack 
        stack = []
        cars = []
        for i in range(len(position)):
            car = (position[i], speed[i]) 
            cars.append(car)
        cars = sorted(cars, key=lambda x: x[0], reverse=True)
        
        stack.append([cars[0]])
        for c in cars[1:]:
            #compre with fleet in the top of the stack
            ttt_curr = (target - c[0])/c[1] 
            prev_car = stack[-1][0]
            ttt_prev = (target - prev_car[0])/prev_car[1]
            if ttt_curr > ttt_prev:
                #current car takes longer to reach destination, will never catch up, add new car to the stack
                stack.append([c])
            else:
                stack[-1].append(c)
        return len(stack)



car1: (100-0)/4 = 25
car2: 98/2. = 49