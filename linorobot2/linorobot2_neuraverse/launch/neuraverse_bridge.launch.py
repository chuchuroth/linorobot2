from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    neuraverse_package = FindPackageShare('linorobot2_neuraverse')
    bringup_package = FindPackageShare('linorobot2_bringup')
    
    neura_config_path = PathJoinSubstitution(
        [neuraverse_package, 'config', 'neuraverse_bridge.yaml']
    )

    return LaunchDescription([
        # Launch the base robot
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([bringup_package, 'launch', 'bringup.launch.py'])
            )
        ),

        # PLACEHOLDER: NEURA Sync Bridge Node
        # Replace 'neura_sync_pkg' and 'bridge_node' with actual package and executable names
        # Node(
        #     package='neura_sync_pkg',
        #     executable='bridge_node',
        #     name='neura_sync_bridge',
        #     parameters=[neura_config_path],
        #     output='screen'
        # )
        
        # Log a warning that the bridge is not yet active
        from launch.actions import LogInfo
        LogInfo(msg=["Neuraverse Bridge placeholder launched. Configure 'neuraverse_bridge.yaml' and uncomment bridge node to enable."])
    ])
