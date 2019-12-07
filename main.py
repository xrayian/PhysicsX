from os import system as console
try:
    from support import Velocity, Acceleration, Time, Distance
except:
    print("Support Library Missing, Program will terminate")
    exit()
finder = None

def intro():

    print("\n" + '          ' + "#" * 48)
    introtext=("""          ##                                            ##
          ##	              \ \\\/ /   Version: 1.4    ##
          ##	               \ \\\/    Code: xrayian   ##
          ##	               /\ \\\\                    ##
          ##	      PHYSICS_/ /\ \\\\                   ##
          ##                                            ##""")
    print(introtext)
    print('          ' + "#" * 48)
    print("\n" + "#" * 68)
    print("\n  Enter [?] to determine value for the variable.\n  Enter [clear] to clear the console.\n  Press Enter to keep unspecified.")
    start()



def parse_data(string, default = None, zero = 0):

    if string == "":
        return default

    elif string == "?":
        global finder
        if finder is None:
            finder = "self"
            return string
        else:
            print("\n  [Parse_Error]: Multiple [?] values aren't acceptable")
            start()

    elif zero == 0:
        if string == '0':
            return default
        else:
            try:
                return float(string)
            except:
                print("\n  [Parse_Error]: `"+ string + "` is not a valid number or command")
                start()


    elif string == "clear":
        console("cls")
        start()
    else:
        try:
            return float(string)
        except:
            print("\n  [Parse_Error]: `"+ string + "` is not a valid number or command")
            start()

def start():
    
    global finder
    
    finder = None
    
    print("\n" + "#" * 68)
    
    final_velocity = parse_data(input("\n  Enter Velocity(m/s): "),zero='1')
    distance = parse_data(input("  Enter Traveled Distance(m): "))
    time = parse_data(input("  Enter Required Time(s): "))
    initial_velocity = parse_data(input("  Enter Initial Velocity(m/s): "),default=0,zero = '1')
    acceleration = parse_data(input("  Enter Acceleration(m/s²): "))
    
    if final_velocity == '?':

        instance = Velocity(distance=distance,time=time,acceleration=acceleration,initial_velocity=initial_velocity)
        print(f"\n  {instance.calculate()}")
        start()
    
    elif distance == '?':
        instance = Distance(final_velocity=final_velocity,time=time,acceleration=acceleration,initial_velocity=initial_velocity)
        print(f"\n  {instance.calculate()}")
        start()
    
    elif time == '?':
        instance = Time(distance=distance,acceleration=acceleration,final_velocity=final_velocity,initial_velocity=initial_velocity)
        print(f"\n  {instance.calculate()}")
        start()
    
    elif acceleration == '?':
        instance = Acceleration(distance=distance,time=time,final_velocity=final_velocity,initial_velocity=initial_velocity)
        print(f"\n  {instance.calculate()}")
        start()

    elif initial_velocity == '?':
        print("\n  [Coming_Soon]: Calculating initial velocity is not available now")
        start()
    else:
        print("\n  [Coming_Soon]: Proofchecker not ready yet")
        start()

if __name__ == "__main__":
    intro()
