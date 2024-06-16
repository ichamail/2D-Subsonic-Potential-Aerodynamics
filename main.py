from potential_flow_around_2D_circular_objects import simulate_flow_around_a_2D_circular_object
from potential_flow_around_airfoils import simulate_steady_flow_around_an_Airfoil, simulate_unsteady_flow_around_an_Airfoil


def insert_length(name:str = "Airfoil's chord length", symbol:str="c") -> float:
    
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

def insert_bodyfixed_frame_origin(name:str="Airfoil's leading edge") -> tuple:
    
    origin = (10**5, 10**5)
    
    while (
        abs(origin[0])+abs(origin[1]) > 10**5
    ):
        
        print(
            "\ntype in " + name + " location (xo, yo) and press Enter"
        )
        
        try:
            
            xo = float(input("xo = "))
            yo = float(input("yo = "))
            origin = (xo, yo)
            
        except:
            
            "\nplease insert correct values"
    
    return origin

def insert_velocity() -> float:
    
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

def insert_angle_of_attack() -> float:
    
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
    
def insert_num_of_panels(
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

def insert_airfoil_name(airfoil_list:list[str]=["naca0012 sharp"]) -> str:
    
    is_airfoil_in_list = False
        
    while not is_airfoil_in_list:
        print("\nType aifoil's name and press Enter")
        airfoil_name = input(
            "Airfoil Name: "
        )
        
        if airfoil_name in airfoil_list:
            is_airfoil_in_list = True
        else:
            print("\nAairfoil doesn't exist in the database")
    
    return airfoil_name

def is_steady_state():
    
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

def insert_wake_length_in_chords() -> int:
    
    wake_length = 0
    
    while wake_length <= 0:
        
        print("\nwake length is measured in chords")
                            
        try:
            
            wake_length = int(input("wake length in chords = "))
            
        except:
            
            print("\nplease insert a correct value")
    
    return wake_length
       
def insert_number_of_iterations(type_of_iters:str="time") -> int:
    
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
            radius = insert_length(name="Circle's radius", symbol="r"),
            center = insert_bodyfixed_frame_origin(name="Circle's center"),
            velocity = insert_velocity(),
            angle_of_attack = insert_angle_of_attack(),
            num_panels = insert_num_of_panels(
                name="Suraface", symbol="Ns", min_panels=5, max_panels=200
            )
        )
    
    else:
        
        airfoil_name = insert_airfoil_name(
            airfoil_list = ["naca0012 sharp"]
        )
        
        chord_length = insert_length(
            name="Airfoil's chord length", symbol="c"
        )
        
        leading_edge_location = insert_bodyfixed_frame_origin(
            name="Airfoil's leading edge"
        )
        
        velocity = insert_velocity()
        angle_of_attack = insert_angle_of_attack()
        num_airfoil_panels = insert_num_of_panels(
            name="Surface", symbol="Ns", min_panels=5, max_panels=100
        )
        
        if is_steady_state():
            
            wake_length_in_chords=insert_wake_length_in_chords()
            
                        
            wake_relaxation_iters = insert_number_of_iterations(
                type_of_iters="wake relaxation"
            )
            
            num_wake_panels = insert_num_of_panels(
                name="Wake", symbol="Nw", min_panels=wake_relaxation_iters, max_panels=100
            )
            
            
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
            
            simulate_unsteady_flow_around_an_Airfoil(
                airfoil_name=airfoil_name,
                chord_length=chord_length,
                leading_edge_location=leading_edge_location,
                velocity=velocity,
                angle_of_attack=angle_of_attack,
                num_airfoil_panels=num_airfoil_panels,
                kutta_vertex_id=0,
                num_time_steps = insert_number_of_iterations(
                    type_of_iters="time"
                )
            )
        
        
    return 0

if __name__== "__main__":
    
    main()
