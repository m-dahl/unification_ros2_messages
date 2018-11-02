# unification_msgs

A ROS2 package providing ROS2 message types and mapping rules for bridging ROS1 and ROS2
messages. Steps to add you own message types and succesfully bridge:

1. Define a message type in your ROS1 package and save it in the msg folder of the package. Name it for example messageX.msg.
2. Edit the CMakeLists.txt file of the ROS1 package:
a. Uncomment the following section and add your message:
```
add_message_files(
  	FILES
	messageX.msg
)
```
b. Uncomment line 5 in the catkin_pakcage section:
```
catkin_package(
	#  INCLUDE_DIRS include
	#  LIBRARIES unification_roscontrol
	#  CATKIN_DEPENDS other_catkin_pkg
	#  DEPENDS system_lib
    	CATKIN_DEPENDS message_runtime
)
```
c. Uncomment the generate_messages section:
```
generate_messages(
	DEPENDENCIES
  	std_msgs  # Or other packages containing msgs
)
```
3. Edit the package.xml file so that you have the following lines uncommented:
```
<build_depend>message_generation</build_depend>
<exec_depend>message_runtime</exec_depend>
<buildtool_depend>catkin</buildtool_depend>
```
4. Source your ROS1 environment file, cd into your workspace and catkin_make.
5. Define a message type in the unification_msgs package (prefferably the same message type with the same name as in step 1) and save it in the msg folder of the unification_msgs package.
6. Define a mapping rule in a messageX_mpr.yaml file between those two messages and save it in the unification_msgs package folder. The mapping rule file should have the following format (NOTE: two spaces define one indentation):
```
-
  ros1_package_name: 'ros1_pkg_name'
  ros1_message_name: 'ros1_msg_name'
  ros2_package_name: 'ros2_pkg_name'
  ros2_message_name: 'ros2_msg_name'
    fields_1_to_2:
    ros1_msg_field_1: 'ros2_msg_field_1'
    ros1_msg_field_2: 'ros2_msg_field_2'
    ros1_msg_field_3: 'ros2_msg_field_3'
```	
7. Edit the CMakeLists.txt file of the ROS2 unification_msgs package:
a. Add your message type in the section:
```
rosidl_generate_interfaces(unification_msgs
  	"msg/message1.msg"
  	"msg/message2.msg"
  	"msg/messageX.msg"
  	DEPENDENCIES builtin_interfaces
)
```
b. After the BUILD_TESTING section, add the installation rule for the messageX_mpr.yaml file:
```
install(
	FILES messageX_mpr.yaml
  	DESTINATION share/${PROJECT_NAME})
```
8. Edit the package.xml so that in the export section you add the mapping rule:
```
<export>
  <ros1_bridge mapping_rules="messageX_mpr.yaml/">
  <build_type>ament_cmake</build_type>
</export>

```
9. In a fresh terminal, source your only your ROS2 environment file, cd into the ROS2 workspace and build the workspace without the ros1_bridge with:
```
colcon build --symlink-install --packages-skip ros1_bridge
```
10. In another fresh terminal, source your ROS1 environment file and then in the same terminal source the ROS2 environment file. cd into your ROS2 workspace and build only the ros1_bridge with:
```
colcon build --symlink-install --packages-select ros1_bridge --cmake-force-configure
```
11. All done.

