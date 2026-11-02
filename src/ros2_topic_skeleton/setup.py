from setuptools import setup

package_name = 'ros2_topic_skeleton'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml']
        ),
    ],
    install_requires=['setuptools'],
    tests_require=['pytest'],
    zip_safe=True,
    maintainer='ROS Developer',
    maintainer_email='developer@example.com',
    description='ROS 2 package for testing topic creation',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'topic_publisher = ros2_topic_skeleton.topic_publisher:main',
        ],
    },
)