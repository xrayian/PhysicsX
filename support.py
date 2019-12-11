from math import sqrt, pow

'''
Sterilized for using as core
core_version: 0.1
    changes in 0.1:
        [1] Added 'self.Value==0' Checks on Calculations with divisons to prevent breaking
'''

class Velocity:
    ''' 
    Velocity class: currently complete
    '''
    def __init__(self, time = None, initial_velocity=None, acceleration=None, distance=None):
        self.time = time
        self.initial_velocity = initial_velocity
        self.acceleration = acceleration
        self.distance = distance
    
    def calculate_without_time(self):
        #Verifying Crucial Arguments
        if self.distance is None or self.acceleration is None:
            return
        if self.initial_velocity is None:
            
            result = sqrt(2 * self.acceleration * self.distance)
        
        else:

            initial_velocity_squared = pow(self.initial_velocity, 2)
            result = sqrt(initial_velocity_squared + 2 * self.acceleration * self.distance)
        
        final_result = round (result, 3)
        return str(final_result)
    
    def calculate_without_acceleration(self):
        #Verifying Crucial Arguments
        if self.distance is None or self.time is None:
            return
        if self.distance == 0 or self.time == 0:
            return
        
        result = self.distance / self.time #flag: division
        
        final_result = round (result, 3)
        return str(final_result)
    
    def calculate_without_distance(self):
        #Verifying Crucial Arguments
        if self.acceleration is None or self.time is None:
            return

        result = self.initial_velocity + (self.acceleration * self.time)
        
        final_result = round (result, 3)
        return str(final_result)

    def Proofchecker(self):
        try:
            result = float(self.calculate_without_distance())
        except:
            return "[ProofCheck_Error]: Invalid Query"
        distance = self.initial_velocity*self.time + .5*self.acceleration*(pow(self.time,2))
        if float(distance) == self.distance:
            return "Velocity is %s m/s" % str(round(result, 3))
        else:
            return "[ProofCheck_Error]: Distance value is incompatible with acceleration value"

    def calculate(self):

        if self.acceleration is None:

            velocity = self.calculate_without_acceleration()

            if velocity is not None:
                return "Velocity is %s m/s" % velocity

            else:
                return "[Critical_Error]: Crucial values are absent"

        elif self.distance is None:

            velocity = self.calculate_without_distance()

            if velocity is not None:
                return "Velocity is %s m/s" % velocity

            else:
                return "[Critical_Error]: Crucial values are absent"

        elif self.time is None:

            velocity = self.calculate_without_time()
            if velocity is not None:
                return "Velocity is %s m/s" % velocity
            else:
                return "[Critical_Error]: Crucial values are absent"

        else:
            return self.Proofchecker()

class Acceleration:
    '''
    Acceleration currently done
    '''
    def __init__(self, time = None, initial_velocity=None, final_velocity=None, distance=None):
        self.time = time
        self.initial_velocity = initial_velocity
        self.final_velocity = final_velocity
        self.distance = distance

    def calculate_without_time(self):
        #must have distance and either initial_velocity or final_velocity

        if self.distance is None:
            return
        if self.final_velocity is None and self.initial_velocity == 0:   
            return

        if self.final_velocity is None: 
            self.final_velocity = 0

        result = (pow(self.final_velocity, 2) - pow(self.initial_velocity, 2)) / (2 * self.distance) #flag: division
        result = round (result, 3)

        return str(result)
    
    def calculate_without_distance(self):

        if self.time is None or self.time == 0:
            return
        elif self.final_velocity is None and self.initial_velocity == 0:
            return
        if self.final_velocity is None: 
            self.final_velocity = 0

        result = (self.final_velocity - self.initial_velocity) / self.time #flag: division
        final_result = round (result, 3)
        
        return str(final_result)
    
    def calculate_without_final_velocity(self):
        if self.time is None or self.distance is None or self.time == 0:
            return
        
        covered_distance =  self.distance - (self.initial_velocity * self.time) 
        time_squared = 0.5 * pow(self.time, 2)
        result = covered_distance / time_squared #flag: division
        
        result = round (result, 3) 
        return str(result)
    
    def Proofchecker(self):
        try:
            acceleration = float(self.calculate_without_distance())
            actual_distance = float(self.initial_velocity*self.time + .5*acceleration*(pow(self.time,2)))
        except:
            return "[ProofCheck_Error]: Invalid Question "

        if self.distance == actual_distance:
            return "Acceleration is %s m/s²" % acceleration
        
        else:
            return "[ProofCheck_Error]: Distance value is incompatible with Acceleration value "

    def calculate(self):
        
        if self.distance is None:
            acceleration = self.calculate_without_distance()
            if acceleration is not None:
                return "Acceleration is %s m/s²" % acceleration
            else:
                return "[Critical_Error]: Crucial values are absent"
        elif self.final_velocity is None:
            acceleration = self.calculate_without_final_velocity()
            if acceleration is not None:
                return "Acceleration is %s m/s²" % acceleration
            else:
                return "[Critical_Error]: Crucial values are absent"
        elif self.time is None:
            acceleration = self.calculate_without_time()
            if acceleration is not None:
                return "Acceleration is %s m/s²" % acceleration
            else:
                return "[Critical_Error]: Crucial values are absent"
        else:
            return self.Proofchecker()

class Time():
    '''
    may have slight bugs
    '''
    def __init__(self, acceleration=None, initial_velocity=None, final_velocity=None, distance=None):
        self.acceleration = acceleration
        self.initial_velocity = initial_velocity
        self.final_velocity = final_velocity
        self.distance = distance
    
    def calculate_without_final_velocity(self):
        if self.distance is None or self.acceleration is None:
            return
        
        if self.initial_velocity == 0:
            if self.acceleration == 0:
                return
            
            result = sqrt((2 * self.distance / self.acceleration)) #flag: division
            result = round (result, 3)
            return "Elapsed time %s seconds" % str(result)
        
        else:
            return "[Math_Error]: Can't solve"
    
    def calculate_with_acceleration(self):
        if self.acceleration is None:
            return
        if self.final_velocity is None and self.initial_velocity == 0:
            return
        if self.final_velocity is None:
            self.final_velocity = 0
        if self.acceleration == 0:
            return

        result = (self.final_velocity - self.initial_velocity) / self.acceleration #flag: division
        final_result = round (result, 3)
        return str(final_result)
    
    def calculate_with_distance(self):
        if self.distance is None:
            return
        if self.final_velocity is None or self.final_velocity == 0:
            return
        try:
            result = self.distance / self.final_velocity #flag: division
        except:
            return "[Error:DT_2]: Impossible value"

        result = round (result, 3)
        return str(result)

    def calculate(self):
        if self.final_velocity is None:
            time = self.calculate_without_final_velocity()
            if time is not None:
                return time
            else:
                return "[Critical_Error]: Crucial values are absent"

        if self.distance is None:
            time = self.calculate_with_acceleration()
            if time is not None:
                return "Elapsed time %s seconds" % time
            else:
                return "[Critical_Error]: Crucial values are absent"
        
        if self.acceleration is None:
            time = self.calculate_with_distance()
            if time is not None:
                return "Elapsed time %s seconds" % time
            else:
                return "[Critical_Error]: Crucial values are absent or absurd"

        else:
            return "[Critical_Error]: Too many variable's to process"

            

class Distance():
    '''
    done
    '''
    def __init__(self, time = None, acceleration=None, initial_velocity=None, final_velocity=None):
        self.final_velocity = final_velocity
        self.initial_velocity = initial_velocity
        self.time = time
        self.acceleration = acceleration
    
    def calculate_without_acceleration(self):
        if self.final_velocity is None or self.time is None:
            return
        result = self.final_velocity * self.time
        result = round (result, 3)
        return str(result)
    
    def calculate_with_acceleration_and_time(self):
        if self.acceleration is None or self.time is None:
            return
        result = self.initial_velocity * self.time + (0.5 * self.acceleration * pow(self.time, 2))
        result = round (result, 3)
        return str(result)
    
    def calculate_without_time(self):
        if self.acceleration is None or self.acceleration == 0:
            return
        if self.final_velocity is None and self.initial_velocity == 0:
            return
        if self.final_velocity is None and self.final_velocity != 0:
            self.final_velocity = 0

        final_velocity_squared = pow(self.final_velocity, 2)
        initial_velocity_squared = pow(self.initial_velocity, 2)
        result = (final_velocity_squared - initial_velocity_squared) / (2 * self.acceleration) #flag: division
        result = round (result, 3)
        return result
    
    def calculate(self):
        if self.time is None:
            distance = self.calculate_without_time()
            if distance is not None:
                return "Covered distance %s meters" % distance
            else:
                return "[Critical_Error]: Crucial values are absent "
        elif self.acceleration is None:
            distance = self.calculate_without_acceleration()
            if distance is not None:
                return "Covered distance %s meters" % distance
            else:
                return "[Critical_Error]: Crucial values are absent "

        elif self.acceleration is not None and self.time is not None:
            distance = self.calculate_with_acceleration_and_time()
            if distance is not None:
                return "Covered distance %s meters" % distance
            else:
                return "[Critical_Error]: Crucial values are absent "
        
        else:
            return "[Critical_Error]: Too many variable's to process"


