from os.path import isfile as doFileExists
from potential_flow_around_2D_circular_objects import simulate_flow_around_a_2D_circular_object
from potential_flow_around_airfoils import simulate_steady_flow_around_an_Airfoil, simulate_unsteady_flow_around_an_Airfoil


def getLengthFromUser(
    name:str = "Airfoil's chord length", symbol:str="c"
) -> float:
    
    length = -1.0
    
    while length <= 0.0:
        
        print(
            "\ntype in " + name +
            " and press Enter ("+ symbol + ">0)")
                    
        try:
            
            length = float(input(symbol + " = "))
            
        except:
            
            print("\nplease insert a correct value")
    
    return length

def getBodyFixedFrameFromUser(name:str="Airfoil's leading edge") -> tuple:
    
    origin = (0.0, 0.0)
    is_true = True
    
    while is_true:
        
        print(
            "\ntype in " + name + " location (xo, yo) and press Enter"
        )
        
        try:
            
            origin = (float(input("xo = ")), float(input("yo = ")))
            is_true = False
            
        except:
            
            "\nplease insert correct values"
    
    return origin

def getVelocityFromUser() -> float:
    
    velocity = -1
    
    while velocity <= 0:
        
        print(
            "\ntype in velocity's magnitude V and press Enter (V>0)"
        )
        
        try:
            
            velocity = float(input("V = "))
            
        except:
            
            print("\nplease insert a correct value")
    
    return velocity

def getAngleOfAttackFromUser() -> float:
    
    angle_of_attack = 180
    
    while not (-90 < angle_of_attack < 90):
            
        print(
            "\ntype in the angle of attack AoA and press Enter (-90 <= AoA <= 90)"
        )
        
        try:
            
            angle_of_attack = float(input("AoA = "))
            
        except:
            
            print("\nplease insert a correct value")
    
    return angle_of_attack
    
def getNumOfPanelsFromUser(
    name:str="surface", symbol:str="Ns", min_panels:int=5, max_panels:int=200
) -> int:
    
    num_panels = -1
    
    while not (min_panels <= num_panels <= max_panels):
            
        print(
            "\ntype in the number of " + name + " panels " + symbol + " ( " 
            + str(min_panels) +  " < " + symbol + " < " + str(max_panels) + " )"
        )

        try:
            num_panels = int(input(symbol + " = "))
        except:
            print("\nplease insert a correct value")
            num_panels = 0
    
    return num_panels

def getAirfoilNameFromUser(airfoil_list:list[str]=["naca0012 sharp"]) -> str:
    
    airfoil_in_database = False

    folderPath= "Airfoils/"
    fileExtension = ".dat"
    
    while not airfoil_in_database:
        print("\nType aifoil's name and press Enter")
        airfoil_name = input(
            "Airfoil Name: "
        )
        
        if doFileExists(folderPath + airfoil_name + fileExtension):
            airfoil_in_database = True
        else:
            print("\nAirfoil doesn't exist in the database")
    
    return airfoil_name

def getIfSteadyStateFromUser():
    
    userInput = -1
    
    while userInput !=1 and userInput !=2:
        print(
            "\n1.Steady state simulation \n2.Unsteady Simulation"
        )
        
        try:
            userInput = int(
                input(
                    "Select one from the above simulation types by typing their corresponding number, and then press Enter:"
                )
            )
            
        except:
            print("\nplease insert a correct value")
    
    if userInput == 1:
        return True
    else:
        return False

def getWakeLengthInChordsFromUser() -> int:
    
    wake_length = 0
    
    while wake_length <= 0:
        
        print("\nwake length is measured in chords")
                            
        try:
            
            wake_length = int(input("wake length in chords = "))
            
        except:
            
            print("\nplease insert a correct value")
    
    return wake_length
       
def getNumOfIterationsFromUser(type_of_iters:str="time") -> int:
    
    iters = -1
    
    while iters < 0:
        
        print("type in the number of " + type_of_iters + " iterations")
        
        try:
            
            iters = int(input("iters = "))
            
        except:
            
            print("\nplease insert a correct value")
            
    return iters
            
def main():
    
    userInput = 0
    
    while userInput != 1 and userInput !=2:
        
        print(
            "\n1.Potential Flow around a Circle \n"
            + "2.Potential Flow around an Airfoil"
        )
                
        try:
            
            userInput = int(
                input(
                    "Select one from the above test cases by typing their corresponding number, and then press Enter:"
                )
            )
            
        except:
            
            print("\nplease insert a correct value")
    
    
    if userInput == 1:                 
        
        simulate_flow_around_a_2D_circular_object(
            radius = getLengthFromUser(name="Circle's radius", symbol="r"),
            center = getBodyFixedFrameFromUser(name="Circle's center"),
            velocity = getVelocityFromUser(),
            angle_of_attack = getAngleOfAttackFromUser(),
            num_panels = getNumOfPanelsFromUser(
                name="Suraface", symbol="Ns", min_panels=5, max_panels=200
            )
        )
    
    else:
        
        airfoil_name = getAirfoilNameFromUser(
            airfoil_list = ["naca0012 sharp"]
        )
        chord_length = getLengthFromUser(
            name="Airfoil's chord length", symbol="c"
        )
        leading_edge_location = getBodyFixedFrameFromUser(
            name="Airfoil's leading edge"
        )
        velocity = getVelocityFromUser()
        angle_of_attack = getAngleOfAttackFromUser()
        num_airfoil_panels = getNumOfPanelsFromUser(
            name="Surface", symbol="Ns", min_panels=5, max_panels=100
        )
        
        if getIfSteadyStateFromUser():
            
            wake_length_in_chords=getWakeLengthInChordsFromUser()
            
                        
            wake_relaxation_iters = getNumOfIterationsFromUser(
                type_of_iters="wake relaxation"
            )
            
            num_wake_panels = getNumOfPanelsFromUser(
                name="Wake", symbol="Nw",
                min_panels=wake_relaxation_iters, max_panels=100
            )
            
            print("\n\nSimulation Results:")
            
            simulate_steady_flow_around_an_Airfoil(
                airfoil_name = airfoil_name,
                chord_length = chord_length,
                leading_edge_location = leading_edge_location,
                velocity = velocity,
                angle_of_attack = angle_of_attack,
                num_airfoil_panels = num_airfoil_panels,
                wake_length_in_chords = wake_length_in_chords,
                num_wake_panels = num_wake_panels,
                kutta_vertex_id = 0,
                wake_relaxation_iters = wake_relaxation_iters 
            )
            
        
        else:
            
            print("\n\nSimulation Results:")
            
            simulate_unsteady_flow_around_an_Airfoil(
                airfoil_name=airfoil_name,
                chord_length=chord_length,
                leading_edge_location=leading_edge_location,
                velocity=velocity,
                angle_of_attack=angle_of_attack,
                num_airfoil_panels=num_airfoil_panels,
                kutta_vertex_id=0,
                num_time_steps = getNumOfIterationsFromUser(
                    type_of_iters="time"
                )
            )
        
        
    return 0

if __name__== "__main__":
    
    main()
