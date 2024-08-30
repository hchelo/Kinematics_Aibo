# Forward kinematics legg Aibo

The SONY AIBO ERS-7 robot uses the following configuration to obtain the forward kinematics of each of its limbs:

$M = R_x(th_1) \cdot R_y(th_2) \cdot T_z(-L1) \cdot R_y(th_3) \cdot T_z(-L2)$

Where Rx and Ry are the homogeneous rotation matrices corresponding to their respective axes (variables 1, 2, and 3 are the inputs), and the lengths are constants with values 
L1=69.5 y L2=71.5 (distance from elbow to the robot's paw).

![Imagen de ejemplo](https://github.com/hchelo/Kinematics_Aibo/blob/main/img/perruno.png)

It is required to develop a ROS2 program that:

Implements a server that performs the forward kinematics operation of the AIBO robot, using inputs 
Th1, Th2 and Th3 and returns the position 𝑥,𝑦,𝑧 of the front leg.

Implements a client that sends the values of angles Th1,Th2,Th3 to the server. The angles should be sent in degrees and can have the following configuration. This client should be executed only once:

Th1=0∘ , Th2=0∘ , Th3=0∘
Th1=20∘ , Th2=45∘ , Th3=10∘
Th1=10∘ , Th2=−30∘ , Th3=25∘

#Sample:
 
    Server:     ros2 run srvcli_matrix pos_server 
    
    Client:     ros2 run srvcli_matrix pos_client 0 0 0 65 75


Do not forget the arguments after the client command ("pos_client 0 0 0 65 75").
