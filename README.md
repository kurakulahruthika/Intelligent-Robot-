# Mobile Manipulator Warehouse Simulation: Design, Autonomous Navigation, and Robotic Manipulation

Skill-Based Evaluation Project for **24AI2003 Intelligent Robotics**  
**Institution:** Karunya Institute of Technology and Sciences  
**Team Members:** K Hruthika (URK24CS7107), Jemima Joselin D (URK24CS7106), K Jyothika (URK24CS7102)  

## Overview
This repository contains the ROS 2 Jazzy and Gazebo Harmonic simulation framework for an assistive mobile manipulator engineered for intra-logistics operations within an industrial warehouse. The system features a 4-wheel differential-drive base, a 3-DOF articulated robotic arm, and an electromagnetic end-effector capable of autonomous navigation (Nav2) and precision part retrieval.

## Requirements
- **OS:** macOS Sequoia (via RoboStack) / Ubuntu 24.04 LTS
- **Middleware:** ROS 2 Jazzy Jalisco
- **Simulator:** Gazebo Harmonic (Version 8.10.0)

## Build Instructions
1. Clone this repository into your ROS 2 workspace:
   ```bash
   mkdir -p ~/mobile_manipulator_ws/src
   cd ~/mobile_manipulator_ws/src
   git clone <your-repo-url> mm_description