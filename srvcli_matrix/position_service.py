from custom_interface.srv import GetPosition
import rclpy
import numpy as np
from rclpy.node import Node

class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(GetPosition, 'get_position_aibo', self.get_pos_callback)

    def get_pos_callback(self, req, res):
        th1 = req.th1
        th2 = req.th2
        th3 = req.th3
        L1 = req.l1
        L2 = req.l2
        print('Los datos ingresados son: ')
        print('th1 th2 th3 L1 L2')
        # Llamar a la función cinema para obtener x, y, z
        result = self.cinema(th1, th2, th3, L1, L2)
        res.x = float(result[0])
        res.y = float(result[1])
        res.z = float(result[2])

        return res
    
    def cinema(self, th1, th2, th3, L1, L2):
        # Convertir ángulos de grados a radianes
        th1 = np.deg2rad(th1)
        th2 = np.deg2rad(th2)
        th3 = np.deg2rad(th3)

        # Definir las matrices de transformación
        Ry1 = np.array([
            [np.cos(-th1), 0, np.sin(-th1), 0],
            [0, 1, 0, 0],
            [-np.sin(-th1), 0, np.cos(-th1), 0],
            [0, 0, 0, 1]
        ])

        Rx1 = np.array([
            [1, 0, 0, 0],
            [0, np.cos(th2), -np.sin(th2), 0],
            [0, np.sin(th2), np.cos(th2), 0],
            [0, 0, 0, 1]
        ])

        Tz1 = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, -L1],
            [0, 0, 0, 1]
        ])

        Ry2 = np.array([
            [np.cos(-th3), 0, np.sin(-th3), 0],
            [0, 1, 0, 0],
            [-np.sin(-th3), 0, np.cos(-th3), 0],
            [0, 0, 0, 1]
        ])

        Tz2 = np.array([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, -L2],
            [0, 0, 0, 1]
        ])

        # Calcular la matriz M
        M = Ry1 @ Rx1 @ Tz1 @ Ry2 @ Tz2

        # Multiplicar la matriz M por el vector [0, 0, 0, 1]
        M_simplified = M @ np.array([0, 0, 0, 1])

        # Extraer los valores de x, y, z
        x = M_simplified[0]
        y = M_simplified[1]
        z = M_simplified[2]

        # Retornar los resultados
        return [x, y, z]

def main():
    rclpy.init()
    min_svc = MinimalService()
    rclpy.spin(min_svc)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
