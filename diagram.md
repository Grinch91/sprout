````mermaid
flowchart TD
 subgraph subGraph0["Hardware Layer"]
        A["Raspberry Pi"]
        B["Moisture Sensor"]
        C["Light Sensor"]
        D["Temperature Sensor"]
        E["Light Control Module"]
        F["Pump/Valve for Nutrient Supply"]
  end
 subgraph subGraph1["Python Application"]
        B1["Analyze Plant Health"]
        A1["Sensor Data Collection"]
        C1["Monitor Environmental Conditions"]
        G1["Lighting Control Algorithm"]
        H1["Nutrient Control Algorithm"]
        F1["Send Data to Frontend"]
  end
 subgraph subGraph2["Frontend Application"]
        A2["User Dashboard"]
        B2["Plant Health Status"]
        C2["Moisture, Light, Temp Levels"]
  end
    A --> B & C & D & E & F
    A1 --> B1 & C1
    C1 --> G1 & H1
    B1 --> F1
    F1 --> A2
    A2 --> B2 & C2
    G1 -- Seasonal Adjustments --> E
    H1 --> F
    A1 -- Read Data --> A
    B1 -- Analyze Data --> A2
    G1 -- Control Lights --> E
    H1 -- Control Nutrients --> F
```
