from typing import List
from math import pi

RAD = pi/180.0
GRIPPER_MIN = -40.62*RAD + 0.001
GRIPPER_MAX = 38.27*RAD - 0.001

MOVE_GROUP_ARM: str = "arm"
MOVE_GROUP_GRIPPER: str = "gripper"

OPEN_GRIPPER_JOINT_POSITIONS: List[float] = [GRIPPER_MIN]
CLOSED_GRIPPER_JOINT_POSITIONS: List[float] = [GRIPPER_MAX]

robot_prefix = "crane_plus_"

def joint_names(prefix: str = robot_prefix) -> List[str]:
    return [
        prefix + "joint1",
        prefix + "joint2",
        prefix + "joint3",
        prefix + "joint4",
    ]


def base_link_name(prefix: str = robot_prefix) -> str:
    return prefix + "base"


def end_effector_name(prefix: str = robot_prefix) -> str:
    return prefix + "link4"


def gripper_joint_names(prefix: str = "crane_plus_") -> List[str]:
    return [
        prefix + "joint_hand",
    ]
