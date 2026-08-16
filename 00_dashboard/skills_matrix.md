## How to read this matrix

`Current` is the user's initial self-assessment from the discovery interview;
it is not a verified industry competency. New skills are initialized to `0`.
`Target` is the practical level needed for the first target roles, not a claim
that the user already has that ability. A current level above `2` is allowed
only when the Evidence column links to independently completed work.

| Level | Meaning |
| --- | --- |
| 0 | I don't understand it yet |
| 1 | I can explain the basic idea |
| 2 | I can implement it with guidance |
| 3 | I can implement and debug it independently |
| 4 | I can integrate it, discuss trade-offs, handle failures, and answer interview questions |

## Shared foundations

| Skill | Current | Target | Evidence |
| --- | ---: | ---: | --- |
| C++ syntax, functions, classes | 0 | 3 | — |
| C++ pointers/references | 2 | 3 | — |
| C++ RAII, ownership, smart pointers | 0 | 3 | — |
| C++ STL and algorithms | 0 | 3 | — |
| C++ templates and type safety | 0 | 2 | — |
| C++ memory/layout/endian | 1 | 3 | — |
| C++ bit manipulation | 0 | 3 | — |
| Error handling and defensive programming | 0 | 3 | — |
| C++ concurrency primitives | 0 | 2 | — |
| Linux processes, files, permissions, signals | 0 | 2 | — |
| Bash and terminal-based workflows | 1 | 2 | — |
| Git branching, commits, and debugging history | 2 | 3 | — |
| CMake multi-file builds | 0 | 3 | — |
| Unit and integration testing | 0 | 3 | — |
| GDB debugging | 0 | 3 | — |
| Sanitizers and static analysis | 0 | 2 | — |
| Profiling and performance measurement | 0 | 2 | — |
| Logging, tracing, and timestamps | 0 | 3 | — |
| Requirements and interface contracts | 0 | 2 | — |
| Coordinate frames and rigid-body transforms | 1 | 3 | — |
| Linear algebra | 2 | 2 | — |
| Probability and statistics | 2 | 2 | — |
| Calculus and differential equations | 2 | 2 | — |
| Simulation fundamentals | 0 | 2 | — |

## Vehicle integration and embedded systems

| Skill | Current | Target | Evidence |
| --- | ---: | ---: | --- |
| Embedded C/C++ build and memory constraints | 0 | 3 | — |
| Microcontroller peripherals and timers | 0 | 2 | — |
| Interrupts and scheduling | 0 | 2 | — |
| UART/RS485 integration | 0 | 3 | — |
| CAN frame structure and arbitration | 0 | 3 | — |
| CAN signal packing, scaling, and endianness | 0 | 3 | — |
| CAN-FD | 0 | 2 | — |
| SocketCAN and virtual CAN | 0 | 3 | — |
| ISO-TP segmentation and reassembly | 0 | 3 | — |
| Ethernet/TCP/UDP fundamentals | 0 | 2 | — |
| Network timing, latency, jitter, and loss | 0 | 3 | — |
| Time synchronization and monotonic clocks | 0 | 2 | — |
| Real-time scheduling and deadlines | 0 | 3 | — |
| Watchdogs, heartbeats, and timeout behaviour | 0 | 3 | — |
| Vehicle/autonomy/control interfaces | 0 | 3 | — |
| Actuator commands and feedback signals | 0 | 3 | — |
| Hardware-in-the-loop concepts | 0 | 2 | — |
| Fault injection and degraded operation | 0 | 3 | — |
| Automotive diagnostics concepts | 0 | 2 | — |

## Robotics and autonomy integration

| Skill | Current | Target | Evidence |
| --- | ---: | ---: | --- |
| ROS 2 package, node, launch, and parameter structure | 0 | 3 | — |
| ROS 2 publishers, subscribers, services, and actions | 2 | 3 | — |
| ROS 2 QoS policies and compatibility | 0 | 3 | — |
| ROS 2 executors, callbacks, and composition | 0 | 2 | — |
| ROS 2 lifecycle and managed nodes | 0 | 2 | — |
| TF2 tree design and transform debugging | 2 | 3 | — |
| rosbag recording and replay | 0 | 2 | — |
| Nav2 configuration and recovery behaviour | 0 | 2 | — |
| Sensor drivers and timestamped messages | 0 | 3 | — |
| IMU measurement models and calibration | 0 | 2 | — |
| Odometry and dead reckoning | 0 | 2 | — |
| GNSS and RTK concepts | 0 | 2 | — |
| Kalman filtering and sensor fusion | 0 | 2 | — |
| Computer-vision pipeline fundamentals | 0 | 2 | — |
| LiDAR and point-cloud fundamentals | 0 | 1 | — |
| Mapping and SLAM concepts | 0 | 2 | — |
| Behaviour and mission planning | 0 | 2 | — |
| Motion planning and trajectory constraints | 0 | 2 | — |
| Feedback control and PID tuning | 0 | 2 | — |
| Vehicle kinematics and dynamics | 0 | 2 | — |
| System architecture and data flow | 0 | 3 | — |
| Simulation with Gazebo or CARLA | 0 | 2 | — |

## Safety and integration reasoning

| Skill | Current | Target | Evidence |
| --- | ---: | ---: | --- |
| ODD definition and assumptions | 0 | 2 | — |
| Failure-mode analysis and FMEA | 0 | 2 | — |
| Safety mechanisms and safe-state design | 0 | 2 | — |
| Functional-safety vocabulary | 0 | 1 | — |
| Cybersecurity fundamentals for connected systems | 0 | 1 | — |
| End-to-end system integration debugging | 0 | 3 | — |
| Test strategy, acceptance criteria, and traceability | 0 | 3 | — |
| Root-cause analysis and fault isolation | 0 | 3 | — |

## Evidence policy

The first target is not to inflate numbers; it is to produce evidence. For any
future `Current` value above `2`, add a link to an artifact and record:

- independent implementation and debugging status;
- test command and result;
- failure cases considered;
- a short design explanation;
- date completed.

Current level `3` or `4` values should not be added merely because a resource was
read or a guided tutorial was completed.
