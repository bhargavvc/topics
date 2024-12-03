
### **Implementing the Facade Pattern in Python**
### **Example: Smart Home System**

Let's consider a **Smart Home System** with various subsystems:

- **Lighting System**: Controls the lights.
- **Climate Control System**: Manages heating and cooling.
- **Security System**: Handles alarms and locks.
- **Entertainment System**: Manages media playback.

**Challenge**:

- The client (user or application) wants to activate predefined modes like "Movie Mode" or "Away Mode" without interacting with each subsystem individually.

**Applying the Facade Pattern**:

- Create a `SmartHomeFacade` class that provides simple methods like `activate_movie_mode()` and `activate_away_mode()`.
- The facade interacts with the subsystems to perform the necessary actions.

#### **Step 1: Define Subsystem Classes**

**Lighting System**:

```python
# lighting_system.py
class LightingSystem:
    def set_brightness(self, level):
        print(f"Setting lighting brightness to {level}%")
```

**Climate Control System**:

```python
# climate_control_system.py
class ClimateControlSystem:
    def set_temperature(self, temperature):
        print(f"Setting temperature to {temperature}°C")
```

**Security System**:

```python
# security_system.py
class SecuritySystem:
    def arm(self):
        print("Arming the security system.")

    def disarm(self):
        print("Disarming the security system.")
```

**Entertainment System**:

```python
# entertainment_system.py
class EntertainmentSystem:
    def play_movie(self, movie):
        print(f"Playing movie: {movie}")

    def stop_movie(self):
        print("Stopping movie playback.")
```

#### **Step 2: Create the Facade Class**

```python
# smart_home_facade.py
from lighting_system import LightingSystem
from climate_control_system import ClimateControlSystem
from security_system import SecuritySystem
from entertainment_system import EntertainmentSystem

class SmartHomeFacade:
    def __init__(self):
        self.lighting = LightingSystem()
        self.climate = ClimateControlSystem()
        self.security = SecuritySystem()
        self.entertainment = EntertainmentSystem()

    def activate_movie_mode(self, movie):
        print("\nActivating Movie Mode...")
        self.security.disarm()
        self.lighting.set_brightness(30)
        self.climate.set_temperature(22)
        self.entertainment.play_movie(movie)

    def activate_away_mode(self):
        print("\nActivating Away Mode...")
        self.entertainment.stop_movie()
        self.lighting.set_brightness(0)
        self.climate.set_temperature(18)
        self.security.arm()

    def activate_relax_mode(self):
        print("\nActivating Relax Mode...")
        self.security.disarm()
        self.lighting.set_brightness(50)
        self.climate.set_temperature(20)
        self.entertainment.play_movie("Relaxing Music Playlist")
```

**Explanation**:

- The `SmartHomeFacade` class simplifies the interaction with various subsystems.
- It provides methods like `activate_movie_mode`, `activate_away_mode`, and `activate_relax_mode`.
- Each method coordinates the subsystems to achieve the desired mode.

#### **Step 3: Use the Facade in Client Code**

```python
# client.py
from smart_home_facade import SmartHomeFacade

def main():
    smart_home = SmartHomeFacade()

    # User wants to watch a movie
    smart_home.activate_movie_mode("Inception")

    # User leaves the house
    smart_home.activate_away_mode()

    # User wants to relax
    smart_home.activate_relax_mode()

if __name__ == "__main__":
    main()
```

**Output**:

```
Activating Movie Mode...
Disarming the security system.
Setting lighting brightness to 30%
Setting temperature to 22°C
Playing movie: Inception

Activating Away Mode...
Stopping movie playback.
Setting lighting brightness to 0%
Setting temperature to 18°C
Arming the security system.

Activating Relax Mode...
Disarming the security system.
Setting lighting brightness to 50%
Setting temperature to 20°C
Playing movie: Relaxing Music Playlist
```

**Explanation**:

- The client code interacts only with the `SmartHomeFacade`, not with the subsystems directly.
- The facade handles the complexity of coordinating multiple subsystems.
- The client code remains clean and simple.

---

### **Benefits of Using the Facade Pattern**

- **Simplifies Client Interface**: Clients interact with a simple interface instead of multiple complex subsystems.
- **Loose Coupling**: Clients are decoupled from the subsystems, reducing dependencies.
- **Ease of Use**: Provides convenience methods for common tasks.
- **Improved Maintainability**: Changes in subsystems do not affect client code as long as the facade interface remains the same.

---