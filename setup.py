import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'srvcli_matrix'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kubu',
    maintainer_email='hiperchelo@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pos_server = srvcli_matrix.position_service:main',
            'pos_client = srvcli_matrix.position_client:main',
        ],
    },
)
