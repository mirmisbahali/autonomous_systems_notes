# Autonomous Systems Integration Roadmap

## Purpose and current position

This roadmap is for a recent Master of Engineering graduate in Australia,
working part-time and able to study approximately 30 hours per week. The first
target is interview readiness for autonomous-vehicle integration, robotics/
autonomy integration, and embedded-systems roles within 1–2 months.

That timeline is realistic for building a credible interview foundation and a
small portfolio. It is not realistic for becoming an expert across the entire
autonomy stack. Expertise will be built through later cycles of independent
implementation, debugging, and integration.

The user has a Linux PC, Jetson Nano B01, Arduino, ESP32, and IMU, with a budget
of approximately $200. The plan therefore prioritizes simulation, virtual CAN,
existing hardware, and small experiments before purchasing equipment.

## Learning rules

- Learn the concept, design the interface, implement independently, test it,
  debug a failure, and explain the trade-offs.
- Assessment exercises and showcase-project implementations are completed
  without AI implementation help. AI may be used afterward for explanations,
  progressive hints, review, and test verification.
- A normal exercise is 1–2 hours. A larger artifact is limited to 1–2 weeks.
- Every artifact should contain a README, requirements, design sketch, tests,
  failure cases, test command/results, and a short self-explanation.
- Keep a distinction between theoretical study, guided implementation,
  independent implementation, independent debugging, and system integration.
- Review the [skills matrix](skills_matrix.md) weekly. Do not raise a current
  level above `2` without linked independent evidence.

## Six-week interview-readiness sprint

At 30 hours per week, allocate roughly 20 hours to implementation and testing,
5 hours to mathematics/technical reading, and 5 hours to explanation and mock
interviews. If a week becomes overloaded, remove optional topics rather than
making the core project larger.

### Week 1 — C++ and engineering workflow foundation

Focus: multi-file C++, ownership, STL, bit operations, CMake, unit tests, GDB,
sanitizers, logging, and Git history.

Short exercises:

- Decode and encode packed fields in a byte buffer, including endianness and
  boundary checks.
- Build a small multi-file C++ library with CMake and tests.
- Debug a deliberately faulty program using GDB and AddressSanitizer.
- Measure and log message timestamps, duration, and jitter.

Evidence artifact: `cpp_integration_foundations` — a small tested C++ library
that parses a binary vehicle message and reports malformed input safely.

Interview outcomes: explain pointers versus references, ownership, undefined
behaviour, bit masks, build targets, test strategy, and a debugging process.

### Weeks 2–3 — Vehicle communication and integration

Focus: CAN arbitration and frames, signal packing, SocketCAN/vcan, ISO-TP,
timeouts, latency, jitter, heartbeats, and the autonomy-to-control interface.
Use the existing notes in [03_vehicle_networks](../03_vehicle_networks/) as the
starting point.

Showcase artifact: `virtual_vehicle_bus` — a 1–2 week virtual-CAN integration
demo with:

- a producer that emits a small control/status message set;
- signal encoding/decoding with documented scaling and byte order;
- an ISO-TP request/response path or a clearly scoped reassembler;
- timestamps and sequence counters;
- injected delay, dropped frames, malformed frames, and stale data;
- timeout/heartbeat behaviour and a short root-cause report;
- automated tests for normal and failure paths.

Do not claim this is vehicle-qualified. It demonstrates integration reasoning in
a deterministic, reproducible test environment.

Interview outcomes: explain why ISO-TP reassembly exists, how to isolate a
communication delay, what information a control unit needs, and how to design a
safe response to stale or missing commands.

### Week 4 — ROS 2 integration and robotics foundations

Focus: package structure, interfaces, QoS compatibility, executors, TF2,
timestamps, rosbag, lifecycle concepts, and sensor/actuator boundaries. Use the
Deakin Rover experience as context, but rebuild a small component independently
so the evidence reflects current ability.

Short exercises:

- Create two nodes with incompatible QoS, diagnose the missing data, and fix it.
- Publish a timestamped IMU-like stream and detect stale/out-of-order samples.
- Construct and inspect a three-frame TF2 tree, then diagnose one incorrect
  transform.
- Record and replay a small bag while checking message timing.

Showcase artifact: `ros2_sensor_actuator_bridge` — a small ROS 2 package that
publishes simulated or IMU-derived sensor data, converts it into a safe actuator
command, and exposes diagnostics for stale data and invalid frames.

Interview outcomes: explain topic/service/action choice, QoS trade-offs, TF2
frames, callback timing, and how to debug a node that appears connected but does
not receive usable data.

### Week 5 — Autonomy stack and simulation

Focus: system data flow, localization, planning, control, ODD assumptions,
failure modes, and simulation. Use either Gazebo/Nav2 or CARLA/ROS depending on
which runs reliably on the available PC.

Short exercises:

- Draw the data flow from sensors to localization, planning, control, and
  vehicle/robot interfaces.
- Define an ODD and three failure modes for a simple indoor robot or simulated
  vehicle.
- Compare planned path, trajectory, and actuator command; state what each
  downstream module actually needs.
- Run one simulation scenario and collect timing and failure observations.

Evidence artifact: `autonomy_stack_failure_demo` — a small simulation with one
intentional fault, observable symptoms, measurements, a fault-isolation method,
and a documented degraded response.

### Week 6 — Integration assessment and interview rehearsal

Combine one vehicle-network exercise and one ROS 2 exercise behind a clear
interface. The integration can remain simulated; the important evidence is
requirements, timing, failure handling, tests, and explanation.

Deliverables:

- one-page architecture diagram;
- interface and timing table;
- test matrix with normal, boundary, and fault cases;
- five-minute recorded explanation;
- three debugging write-ups;
- ten technical questions answered from memory;
- one mock C++ modification exercise completed without AI.

Do not begin another large project during this week. Improve clarity and
repeatability of the existing artifacts.

## After the first six weeks

Run two parallel tracks sharing the foundations:

### Vehicle track

Progress from virtual CAN to real ESP32/Arduino communication, then study
embedded scheduling, watchdogs, CAN-FD, diagnostics, Ethernet, HIL, and safety
mechanisms. Later artifacts should include real timing measurements and a
hardware fault or disconnect test.

### Robotics track

Progress from simulated sensor streams to the IMU, calibration, odometry,
filtering, GNSS/RTK concepts, Nav2 behaviour, mapping/SLAM, perception, and
trajectory control. Later artifacts should include rosbag-based replay and
quantitative localization or navigation evaluation.

## Highest-value resources

Use one primary resource per phase rather than collecting many courses.

- C++: [C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines),
  [cppreference](https://en.cppreference.com/), and the
  [CMake tutorial](https://cmake.org/cmake/help/latest/guide/tutorial/index.html).
- Debugging: [GDB documentation](https://sourceware.org/gdb/documentation/) and
  compiler sanitizers. Practise on small broken programs rather than watching
  debugging videos passively.
- Vehicle networking: the existing [CAN](../03_vehicle_networks/CAN.md),
  [ISO-TP](../03_vehicle_networks/ISO-TP.md), and
  [Ethernet](../03_vehicle_networks/Ethernet.md) notes, plus the Linux
  [SocketCAN documentation](https://docs.kernel.org/networking/can.html).
- ROS 2: the official [ROS 2 tutorials](https://docs.ros.org/en/jazzy/Tutorials.html),
  [QoS concepts](https://docs.ros.org/en/jazzy/Concepts/Intermediate/About-Quality-of-Service-Settings.html),
  and [tf2 tutorials](https://docs.ros.org/en/jazzy/Tutorials/Intermediate/Tf2/Tf2-Main.html).
- Robotics navigation: [Nav2 documentation](https://docs.nav2.org/) and its
  system tests. Study configuration and failure recovery, not only happy-path
  demos.
- Simulation and vehicle autonomy: [CARLA ROS bridge documentation](https://carla.readthedocs.io/projects/ros-bridge/en/latest/)
  and [Autoware documentation](https://autowarefoundation.github.io/autoware-documentation/).
- Mathematics and robotics: [Modern Robotics](https://modernrobotics.northwestern.edu/)
  for frames and kinematics, and [Underactuated Robotics](https://underactuated.mit.edu/)
  for planning and control.

## People and communities to follow

Treat these as sources of primary technical material, design discussions, and
maintainer perspectives—not as a list to follow passively:

- Steve Macenski and the Nav2 maintainers for practical ROS 2 navigation;
- Tully Foote and the ROS 2 maintainers for middleware and ecosystem practices;
- Brian Gerkey and the Open Robotics community for robotics software systems;
- Paul Newman and the Oxford Robotics Institute for localization, mapping, and
  autonomous-vehicle research;
- Timothy Barfoot for state estimation, geometry, and robotics mathematics;
- the Autoware Foundation maintainers for open autonomous-driving integration.

Prefer their talks, papers, documentation, and source code. Each study session
should produce a small implementation or a written explanation tied to the
skills matrix.

## Evidence and level progression

`0–2` may describe current understanding while learning. A `3` requires an
independent implementation and debugging record. A `4` requires integration,
failure handling, measured trade-offs, and an interview-quality explanation.
Every level above `2` must link to the evidence artifact in
`00_dashboard/skills_matrix.md`; no level should be raised merely because a
video, paper, or guided tutorial was completed.
