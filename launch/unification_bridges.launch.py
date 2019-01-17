#!/usr/bin/env python

from launch import LaunchDescription
import launch_ros.actions


def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package='ros1_bridge', node_executable='sb_pose_updater_sp_to_uni', output='screen'),
        launch_ros.actions.Node(
            package='ros1_bridge', node_executable='sb_pose_updater_uni_to_sp', output='screen'),
        launch_ros.actions.Node(
            package='ros1_bridge', node_executable='sb_scene_updater_sp_to_uni', output='screen'),
        launch_ros.actions.Node(
            package='ros1_bridge', node_executable='sb_scene_updater_uni_to_sp', output='screen'),
        launch_ros.actions.Node(
            package='ros1_bridge', node_executable='sb_ur_pose_sp_to_uni', output='screen'),
        launch_ros.actions.Node(
            package='ros1_bridge', node_executable='sb_ur_pose_uni_to_sp', output='screen')])
