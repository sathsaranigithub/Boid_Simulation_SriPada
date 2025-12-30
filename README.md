# 🕉️ Boid-Based Simulation and Modeling of Crowd Flow During the Sri Pada Pilgrimage

## 📖 Introduction
The Sri Pada pilgrimage is a culturally and religiously significant event in Sri Lanka that draws thousands of devotees annually. During peak seasons, managing the dense and dynamic flow of pilgrims along the narrow and steep paths becomes a critical challenge.

This study presents a **Boid-based crowd simulation model** to analyze and predict crowd behavior during the Sri Pada pilgrimage. The **Boid algorithm**, inspired by the flocking behavior of birds, enables the modeling of individual pilgrims as agents governed by simple local rules — **separation**, **alignment**, and **cohesion** — leading to realistic collective movement patterns.

The simulation was developed using **Python** and **Unity**, and it captures the natural interactions of the crowd along the pilgrimage path. Synthetic datasets were generated based on simulation results and used to train a **linear regression model** for estimating crowd density. Visual outputs such as **heatmaps** were used to identify areas of high congestion and potential risk.

The findings demonstrate that Boid-based modeling can effectively simulate crowd flow, providing valuable insights for authorities to improve crowd management, enhance safety, and design better infrastructure for future pilgrimages.

---

## 🌡️ Crowd Density Heatmap

<img width="511" height="384" alt="image" src="https://github.com/user-attachments/assets/b4b3386f-d6ae-47fe-b5f4-02b008d4d4f6" />

---

## 🧠 Overview of the Simulation Architecture
The crowd simulation system designed for the Sri Pada pilgrimage comprises **three primary components**:
1. **Simulation Engine** – Manages the virtual environment and updates agents’ states in real time.  
2. **Behavior Model** – Based on the Boid algorithm, governs the motion and interaction of each agent.  
3. **Data Prediction Module** – Uses linear regression to estimate crowd density for specific times and locations.

The architecture follows a modular approach, enabling independent development and testing of each component. This design supports **real-time simulation and visualization**, providing insights into potential congestion during scenarios such as **peak hours**, **weather changes**, or **route blockages**.

---

## 🕊️ Boid Behavior Implementation (Separation, Alignment, Cohesion)
Each pilgrim in the simulation is modeled as an agent following three fundamental rules:

- **Separation:** Maintains a safe distance from nearby agents to prevent collisions.  
- **Alignment:** Aligns direction and velocity with neighboring agents, mimicking synchronized movement.  
- **Cohesion:** Moves toward the average position of nearby agents, maintaining group integrity.

Each rule is represented as a **vector**, and the combined influence determines the agent’s final velocity and direction at every simulation step. **Adjustable weight parameters** allow fine-tuning for various crowd densities and behaviors.

---

## 🏔️ Simulation Environment Setup
The virtual environment replicates the **Sri Pada pilgrimage trail**, featuring:
- Steep slopes, narrow paths, rest areas, and checkpoints.  
- Waypoints representing key locations: **Nallathanni Entrance**, **Seetha Gangula**, **Indikatu Paalama**, and the **Summit**.  
- Realistic elements such as **obstacles**, **lighting**, and **weather conditions** using **Unity** or **Unreal Engine**.

These factors influence agent paths and simulate realistic crowd dynamics along the pilgrimage route.

---

## 📊 Data Generation and Collection Process
Data for the simulation and prediction modules were obtained from multiple sources:

- **Historical Data:** Past records of pilgrim counts and congestion periods.  
- **Linear Regression Model:** Predicts expected crowd density at different time intervals.  
- **Manual Observation & Expert Consultation:** Insights from pilgrimage officials and volunteers.  

The synthesized data controls **agent spawn rates** and **flow**, allowing simulation outcomes to adapt dynamically based on realistic crowd conditions.

---

## 📚 References
1. C. W. Reynolds, “Flocks, herds and schools: A distributed behavioral model,” *ACM SIGGRAPH Computer Graphics*, vol. 21, no. 4, pp. 25–34, 1987.  
2. A. Schadschneider et al., “Evacuation dynamics: Empirical results, modeling and applications,” *Encyclopedia of Complexity and Systems Science*, Springer, 2009.  
3. L. F. Henderson, “The statistics of crowd fluids,” *Nature*, vol. 229, no. 5284, pp. 381–383, 1971.  
4. D. Obeyesekere, *Buddhism, Nationhood, and Cultural Identity in Sri Lanka*, Orient Longman, 1992.  
5. R. Gombrich and G. Obeyesekere, *Buddhism Transformed: Religious Change in Sri Lanka*, Princeton University Press, 1988.  
6. C. Bandara, “Managing Pilgrimage Tourism in Sri Lanka: The Case of Sri Pada,” *Journal of Tourism and Cultural Change*, vol. 15, no. 2, pp. 185–202, 2017.  
7. H. Helbing and P. Molnár, “Social Force Model for Pedestrian Dynamics,” *Physical Review E*, vol. 51, no. 5, pp. 4282–4286, 1995.  
8. D. Helbing, I. Farkas, and T. Vicsek, “Simulating dynamical features of escape panic,” *Nature*, vol. 407, no. 6803, pp. 487–490, 2000.  
9. N. Pelechano, J. M. Allbeck, and N. I. Badler, “Controlling individual agents in high-density crowd simulation,” *ACM SIGGRAPH/Eurographics Symposium on Computer Animation*, 2007.  
10. J. van den Berg, M. C. Lin, and D. Manocha, “Reciprocal velocity obstacles for real-time multi-agent navigation,” *IEEE International Conference on Robotics and Automation*, 2008.  
11. T. Kretz et al., “Experimental study of pedestrian counterflow in a corridor,” *Journal of Statistical Mechanics*, 2006.  
12. J. Shao and C. S. Chen, “Deep learning for crowd flow prediction in transportation,” *IEEE Transactions on Intelligent Transportation Systems*, vol. 22, no. 6, pp. 3721–3732, 2021.  
13. C. Li et al., “Crowd density estimation using regression analysis,” *International Journal of Computer Applications*, vol. 50, no. 7, 2012.  
14. A. Johansson, D. Helbing, and P. K. Shukla, “Specification of the social force pedestrian model,” *Advances in Complex Systems*, vol. 10, 2007.  
15. D. Helbing, A. Johansson, and H. Z. Al-Abideen, “Dynamics of crowd disasters: An empirical study,” *Physical Review E*, vol. 75, no. 4, 2007.

---

## 🧩 Technologies Used
- **Programming Languages:** Python, C#  
- **Simulation Engine:** Unity  
- **Modeling Techniques:** Boid Algorithm, Linear Regression  
- **Visualization Tools:** Heatmaps, 3D Terrain Modeling  

---

## 💡 Key Outcomes
- Realistic modeling of large-scale crowd flow.  
- Identification of **high-risk congestion zones**.  
- Insights for **crowd management** and **infrastructure design**.  
- Dynamic integration of predictive data models for adaptive simulations.  

---

## 🧍‍♂️🧍‍♀️ Future Enhancements
- Integration of **real-time sensor data** for live crowd tracking.  
- Implementation of **AI-driven anomaly detection** for emergency prediction.  
- Expansion to simulate **evacuation and emergency response scenarios**.  

---

## 🏁 Conclusion
This project demonstrates the effectiveness of **Boid-based simulation** in analyzing and managing large crowds during the **Sri Pada pilgrimage**. By combining behavioral modeling with predictive analytics, it provides a foundation for **data-driven crowd management** and **safety optimization** during mass events.

---

