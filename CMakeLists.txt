cmake_minimum_required(VERSION 3.5)
project(unification_ros2_messages)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

find_package(builtin_interfaces REQUIRED)
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(unification_ros2_messages

  "msg/AecuSPToUni.msg"
  "msg/AecuUniToSP.msg"
  "msg/Common.msg"
  "msg/HecuUniToSP.msg"
  "msg/Tooldrivertointerfacer.msg"
  "msg/Toolinterfacertodriver.msg"
  "msg/Toolinterfacertosp.msg"
  "msg/Toolsptointerfacer.msg"
  "msg/HumanJoints.msg"
  "msg/JointPosition.msg"
  "msg/KinectHumans.msg"
  "msg/PoseUpdaterSPToUni.msg"
  "msg/PoseUpdaterSPToUniRicochet.msg"
  "msg/PoseUpdaterUniToSP.msg"
  "msg/RecuSPToUni.msg"
  "msg/RecuUniToSP.msg"
  "msg/RobotiqSPToUni.msg"
  "msg/RobotiqUniToSP.msg"
  "msg/SavedPoses.msg"
  "msg/SceneUpdaterSPToUni.msg"
  "msg/SceneUpdaterSPToUniRicochet.msg"
  "msg/SceneUpdaterUniToSP.msg"
  "msg/URPoseSPToUni.msg"
  "msg/URPoseSPToUniRicochet.msg"
  "msg/URPoseUniToSP.msg"
  DEPENDENCIES builtin_interfaces
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # remove the line when a copyright and license is present in all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # remove the line when this package is a git repo
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

#install(
#  FILES moveit_sp_to_uni_mpr.yaml
#  DESTINATION share/${PROJECT_NAME})
#
#install(
#  FILES moveit_uni_to_sp_mpr.yaml
#  DESTINATION share/${PROJECT_NAME})
#
#install(
#  FILES robotiq_sp_to_uni_mpr.yaml
#  DESTINATION share/${PROJECT_NAME})
#
#install(
#  FILES robotiq_uni_to_sp_mpr.yaml
#  DESTINATION share/${PROJECT_NAME})
#
#install(
#  FILES updater_sp_to_uni_mpr.yaml
#  DESTINATION share/${PROJECT_NAME})
#
#install(
#  FILES updater_uni_to_sp_mpr.yaml
#  DESTINATION share/${PROJECT_NAME})
install(
  FILES pose_updater_sp_to_uni_mpr.yaml
  pose_updater_sp_to_uni_ricochet_mpr.yaml
  pose_updater_uni_to_sp_mpr.yaml
  saved_poses.yaml
  scene_updater_sp_to_uni_mpr.yaml
  scene_updater_sp_to_uni_ricochet_mpr.yaml
  scene_updater_uni_to_sp_mpr.yaml
  ur_pose_sp_to_uni_mpr.yaml
  ur_pose_sp_to_uni_ricochet_mpr.yaml
  ur_pose_uni_to_sp_mpr.yaml
  DESTINATION share/${PROJECT_NAME})

# Install launch files.
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}/
)



ament_package()
