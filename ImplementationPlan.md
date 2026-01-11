# Implementation Plan - Neuraverse Integration

This plan integrates `linorobot2` with the Neuraverse platform using the **NEURA Sync** bridge. 

## User Review Required

> [!IMPORTANT]
> **NEURA Sync Configuration**: Since I do not have direct access to the NEURA Sync SDK, I will create a template package `linorobot2_neuraverse`. You will need to verify the specific topic mappings (e.g., if NEURA Sync expects a different topic than `/cmd_vel` or `/odom`) and potentially configure the bridge executable path if it's external.

> [!NOTE]
> **Dependencies**: The new package `linorobot2_neuraverse` will depend on `linorobot2_bringup`. Ensure your internal NEURA Sync software is installed and accessible in the system path or a known location.

## Proposed Changes

### linorobot2_neuraverse [NEW PACKAGE]

Create a new ROS2 package `linorobot2_neuraverse` to house the integration logic.

#### [NEW] [package.xml](file:///c:/Users/chuchu/linorobot2/linorobot2_neuraverse/package.xml)
- Standard ROS2 package definition.
- Depends on `linorobot2_bringup`.

#### [NEW] [CMakeLists.txt](file:///c:/Users/chuchu/linorobot2/linorobot2_neuraverse/CMakeLists.txt)
- Standard build configuration.

#### [NEW] [launch/neuraverse_bridge.launch.py](file:///c:/Users/chuchu/linorobot2/linorobot2_neuraverse/launch/neuraverse_bridge.launch.py)
- Launches `linorobot2_bringup` (bringup.launch.py).
- Launches the NEURA Sync bridge node (placeholder command or node, configurable).
- Sets up any parameter bridges or remappings.

#### [NEW] [config/neuraverse_bridge.yaml](file:///c:/Users/chuchu/linorobot2/linorobot2_neuraverse/config/neuraverse_bridge.yaml)
- Configuration for the bridge (topics, credentials, endpoints).
- **Format**:
  ```yaml
  neura_sync_bridge:
    ros__parameters:
      neuraverse_endpoint: "wss://api.neuraverse.com/..." # Example
      robot_id: "linorobot2_001"
      topics:
        - "/cmd_vel"
        - "/odom"
        - "/scan"
  ```

## Verification Plan

### Automated Tests
- **Launch Test**: Verify that `ros2 launch linorobot2_neuraverse neuraverse_bridge.launch.py` starts without errors.
- **Topic Echo**: Verify that topics are being published/subscribed as expected by the bridge (using `ros2 topic list` and `ros2 topic echo`).

### Manual Verification
1.  User starts the `neuraverse_bridge.launch.py`.
2.  User logs into Neuraverse backend/portal.
3.  User verifies if "linorobot2" appears online in the Neuraverse dashboard.
4.  User tries to teleoperate the robot from the Neuraverse interface and checks if `linorobot2` moves.
