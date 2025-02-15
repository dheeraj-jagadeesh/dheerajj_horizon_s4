from setuptools import find_packages, setup

package_name = 'ente_nodes'

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
    maintainer='dheeraj',
    maintainer_email='dheeraj@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['publisher_node = ente_nodes.publisher_node:main',
        'subscriber_node = ente_nodes.subscriber_node:main',

        ],
    },
)
