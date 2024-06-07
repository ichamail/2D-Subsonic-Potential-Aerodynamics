from panel_method_class import PanelMethod
from mesh_class import AeroPanelMesh, SurfacePanelMesh, WakePanelMesh
from airfoil_class import Airfoil, Circle
import numpy as np
from matplotlib import pyplot as plt

def main():
    # airfoil = Airfoil(
    #     name=input("type in Airfoil's name: "),
    #     chord_length=float(input("type in chord's length: ")),
    #     num_points=int(input("type in the number of panels per side: ")) + 1
    # )
    
    airfoil = Airfoil(
        name="naca0012 sharp",
        chord_length=1,
        num_points=30
    )
    vertex = airfoil.coords[0:-1]   
    face = np.array([[i, (i+1)%len(vertex)] for i in range(len(vertex))])
    
    
    surface_mesh = SurfacePanelMesh(
        vertex=vertex,
        face=face,
        CCW=True,
        kutta_vertex_id=0
    )
    
    wake_mesh = WakePanelMesh(
        surface_mesh=surface_mesh,
        length = 10 * airfoil.chord,
        num_faces= 20,
        surface_fixed=True
    )
    
    panel_method = PanelMethod(
        mesh=AeroPanelMesh(
            surface_mesh=surface_mesh,
            wake_mesh=wake_mesh
        )
    )
    
        
    panel_method.mesh.plot(
        BodyFixed_FrameOfReference=True,
        display_normals=True
    )
    
    
    panel_method.mesh.plot(
        BodyFixed_FrameOfReference=False,
        display_normals=True
    )
    
    
    print(
        "kutta vertex id: " 
        + str(panel_method.mesh.surface_mesh.kutta_vertex_id)
        + "\ntop kutta panel id: "
        + str(panel_method.mesh.surface_mesh.top_kutta_face_id)
        + "\nbottom kutta panel id: "
        + str(panel_method.mesh.surface_mesh.bottom_kutta_face_id)
        + "\n \nsurface mesh adjacency matrix = \n"
        + str(panel_method.mesh.surface_mesh.adjacency_matrix)
        + "\n \nwake mesh adjacency matrix = \n"
        + str(panel_method.mesh.surface_mesh.adjacency_matrix)
        + "\n"
    )
    
    
    # panel_method.mesh.wake_mesh.set_BodyFixedFrame_orientation(
    #     float(input("set angle of attack: \n" + "alpha [deg] = "))
    # )
           
    panel_method.set_V_fs(angle_of_attack=5, magnitude=1)
    # panel_method.set_V_inf(angle_of_attack=5, magnitude=1)
    
    
    
    print("\ndisplay mesh in Body-Fixed frame of reference")
    
    panel_method.mesh.plot(
        BodyFixed_FrameOfReference=True,
        display_normals=True
    )
    
    print("\ndisplay mesh in inertial frame of reference")
    panel_method.mesh.plot(
        BodyFixed_FrameOfReference=False,
        display_normals=True
    )
    
    
    print("\ncalculating influence coefficient matrix....")
    panel_method.compute_influence_coefficient_matrices()
    print("\ninfluence coefficient matrix calculation completed")
    
    np.set_printoptions(formatter={'float': lambda x: "{0:0.2f}".format(x)})
    print(
        "\ninfluence coefficient matrix A = \n"
        + str(panel_method.A_ij)
        + "\n\n influence coefficient matrix B = \n"
        + str(panel_method.B_ij)
        + "\n\n influence coefficient matrix C = \n"
        + str(panel_method.C_ij)
    )
    
    
    print("\ncalculating source strengths...")
    panel_method.compute_source_strengths()
    print("\nsource strengths calculation completed")
    
        
    print("\nsolving linear system...")
    panel_method.solve_linear_system()
    print("\n linear system solved")
    
    
    panel_method.compute_surface_velocity()
    
    panel_method.compute_surface_pressure()   
    
    plt.plot(
        [panel.r_cp.x/airfoil.chord for panel in panel_method.surface.panel],
        [panel.Cp for panel in panel_method.surface.panel],
        'ks--', markerfacecolor='r', label='Panel Method'
    )
    plt.xlabel("x/c")
    plt.ylabel("Cp")
    plt.title("Chordwise Pressure Coefficient Distribution")
    plt.legend()
    plt.grid()
    plt.gca().invert_yaxis()
    plt.show()
    
    
    X, Y = np.meshgrid(
        np.linspace(
            start=panel_method.surface.ro.x - airfoil.chord,
            stop=panel_method.surface.ro.x + 2 * airfoil.chord,
            num=100
        ),
        np.linspace(
            start=panel_method.surface.ro.y - airfoil.chord/2,
            stop=panel_method.surface.ro.y + airfoil.chord/2,
            num=50
        ),
        indexing='ij'
    )
    
    # panel_method.display_contour(X, Y)
    # panel_method.display_velocity_field(X, Y)
    # panel_method.display_streamlines(X, Y)
    panel_method.display_streamlines(X, Y, BodyFixed_FrameOfReference=False)
    
    
    
    return 0

if __name__== "__main__":
    
    main()