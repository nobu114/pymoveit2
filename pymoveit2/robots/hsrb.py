from typing import List

MOVE_GROUP_ARM: str = "arm"
MOVE_GROUP_WHOLE_BODY: str = "whole_body"
MOVE_GROUP_GRIPPER: str = "gripper"

OPEN_GRIPPER_JOINT_POSITIONS: List[float] = [1.0]
CLOSED_GRIPPER_JOINT_POSITIONS: List[float] = [0.0]


def arm_joint_names(prefix: str = "") -> List[str]:
    return [
        prefix + "arm_lift_joint",
        prefix + "arm_flex_joint",
        prefix + "arm_roll_joint",
        prefix + "wrist_flex_joint",
        prefix + "wrist_roll_joint"
    ]


def whole_body_joint_names(prefix: str = "") -> List[str]:
    return [
        prefix + "odom_x",
        prefix + "odom_y",
        prefix + "odom_t",
        prefix + "arm_lift_joint",
        prefix + "arm_flex_joint",
        prefix + "arm_roll_joint",
        prefix + "wrist_flex_joint",
        prefix + "wrist_roll_joint"
    ]


def base_link_name(prefix: str = "") -> str:
    return prefix + "base_link"


def end_effector_name(prefix: str = "") -> str:
    return prefix + "hand_palm_link"


def gripper_joint_names(prefix: str = "") -> List[str]:
    return [
        prefix + "hand_motor_joint",
    ]
