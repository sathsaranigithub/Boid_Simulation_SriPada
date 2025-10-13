# Boid_Simulation_SriPada
The Sri Pada pilgrimage is a culturally and religiously significant event in Sri Lanka that draws thousands of devotees annually. During peak seasons, managing the dense and dynamic flow of pilgrims along the narrow and steep paths becomes a critical challenge. This study presents a Boid-based crowd simulation model to analyze and predict crowd behavior in the Sri Pada pilgrimage. The Boid algorithm, inspired by the flocking behavior of birds, enables the modeling of individual pilgrims as agents governed by simple local rules—separation, alignment, and cohesion—leading to realistic collective movement patterns .
The simulation was developed using Python and Unity, and it captures the natural interactions of the crowd along the pilgrimage path. Synthetic datasets were generated based on simulation results and used to train a linear regression model for estimating crowd density . Visual outputs such as heatmaps were used to identify areas of high congestion and potential risk. The findings demonstrate that Boid-based modeling can effectively simulate crowd flow, providing valuable insights for authorities to improve crowd management, enhance safety, and design better infrastructure for future pilgrimages .

# Crowd density heatmap
<img width="511" height="384" alt="image" src="https://github.com/user-attachments/assets/1dc70275-f168-4a06-b5e4-2aaeff324727" />

# Overview of the Simulation Architecture
The crowd simulation system designed for the Sri Pada pilgrimage comprises three primary components: the simulation engine, the behavior model, and the data prediction module. The architecture follows a modular approach, allowing each component to be developed and tested independently while maintaining seamless integration. The simulation engine is responsible for managing the virtual environment and updating the agents’ states in real time. The behavior model, based on the Boid algorithm, governs the motion and interaction of each agent. The data prediction module, using linear regression, provides expected crowd densities for specific times and locations, which dynamically influences agent spawning and movement patterns .
This design allows for real-time simulation and visualization, offering decision-makers insights into potential crowd congestion and behavior across different scenarios such as peak pilgrimage hours, weather changes, or route blockages.

# Boid Behavior Implementation (Separation, Alignment, Cohesion)
The Boid algorithm forms the core of the agent behavior model. Each pilgrim in the simulation is represented as an independent agent following three fundamental rules:
•	Separation: Ensures that agents maintain a safe distance from one another to prevent overcrowding or collisions. This rule calculates a repulsive force that pushes agents away from their neighbors within a certain radius.
•	Alignment: Encourages agents to match their direction and velocity with nearby agents. This reflects the natural tendency of individuals in a group to synchronize their movement, particularly on narrow pilgrimage paths.
•	Cohesion: Drives agents to move towards the average position of their local group, maintaining group integrity and ensuring individuals do not stray far from the crowd.
Each of these behaviors is represented as a vector, and their combination determines the final velocity and direction of each agent at every simulation step. Adjustable weight parameters allow fine-tuning of behavior for different crowd densities and movement patterns.

# Simulation Environment Setup
      The virtual environment is designed to reflect the key features of the Sri Pada pilgrimage trail. The 3D terrain includes steep slopes, narrow paths, rest areas, and checkpoints, closely matching real-world conditions. The environment is built using a game engine that supports real-time rendering and agent dynamics, such as Unity or Unreal Engine.
Obstacles and environmental features influence agent paths, encouraging realistic movement behavior. Pilgrims in the simulation are guided by waypoints representing key locations like the Nallathanni entrance, Seetha Gangula, Indikatu Paalama, and the summit. Dynamic lighting and weather elements can also be introduced to study their effects on crowd behavior.

# Data Generation and Collection Process
      To inform and validate the simulation, data was generated and collected from multiple sources:
•	Historical data: Past records of pilgrimage seasons, including average daily pilgrim counts and known congestion periods, were analyzed to build predictive models.
•	Linear regression model: A predictive model was trained to estimate expected crowd density at different time intervals based on historical trends and time-of-day patterns.
•	Manual observation and expert consultation: Interviews with pilgrimage site officials and volunteers provided qualitative data on crowd behavior, high-risk zones, and common patterns observed during past seasons.
The synthesized data is used to control the flow rate of agents, providing a dynamic input to the simulation. This integration allows simulation outcomes to adjust based on realistic and time-dependent crowd estimations.
