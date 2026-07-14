# 🏆 Nexus 2026: FIFA World Cup Smart Stadium AI & Tournament Operations Hub

[![Apache 2.0 License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://python.org)
[![SQLite WAL Engine](https://img.shields.io/badge/Database-SQLite_WAL-00F0FF.svg)](https://sqlite.org)
[![HTML5 / Vanilla JS](https://img.shields.io/badge/Frontend-Vanilla_JS_ES6+-FF007A.svg)](https://developer.mozilla.org)
[![GenAI Knowledge Graph](https://img.shields.io/badge/AI-8_Language_LLM_Core-00FF88.svg)](#)

### 🌐 Live Interactive Dashboards (Instant Web Access)
[![Live Demo - Main AI Operations Portal](https://img.shields.io/badge/Launch_Live_Portal-Main_AI_Operations_Deck-00F0FF?style=for-the-badge&logo=googlechrome&logoColor=black)](https://unknown404-practice.github.io/Nexus-2026/)
[![Live Demo - Architecture & SQL Simulator](https://img.shields.io/badge/Launch_Live_Simulator-Architecture_&_SQL_Engine-FF007A?style=for-the-badge&logo=sqlite&logoColor=white)](https://unknown404-practice.github.io/Nexus-2026/architecture_dashboard.html)

---

## 🚀 Executive Summary & Architectural Overview

During global mega-events such as the **FIFA World Cup 2026** across North America (USA, Mexico, Canada), managing **82,500+ attendees** per fixture presents unprecedented operational, safety, and logistical challenges. Stadium operators must process massive crowd inflows while simultaneously monitoring IoT sensor grids, ensuring strict neurodivergent/ADA accessibility accommodations, and maintaining Net-Zero sustainability targets.

**Nexus 2026** is an enterprise-grade, **Real-Time GenAI & Relational Database Tournament Operations Platform**. It bridges **high-throughput SQLite WAL database transactions** with a **multilingual Neural AI Concierge** and two ultra-responsive, anti-flicker **Command & Control Web Dashboards**.

Trained and verified on high-density tournament simulation telemetry (processing over **2,400+ active IoT sensors** across 5 primary stadium gates, VIP Skyboxes, Central Sensory Hubs, and Autonomous EV Transit Terminals), Nexus 2026 provides a complete, out-of-the-box system that can be deployed across future FIFA World Cup venues and smart city infrastructures.

---

## 🌟 The Two Core High-Performance Dashboards

### 1️⃣ The Main Stadium AI Operations Portal (`index.html`)
The primary interactive command deck (`indexfifa.html` synchronized as `index.html`) serves as the central interface for stadium directors, security staff, volunteers, and fans:
* **🧠 Multilingual GenAI Concierge (`Web Speech API` & `Neural Knowledge Graph`):** Automatically detects user intent and communicates across **8 localized languages** (*English, Spanish, French, Portuguese, German, Arabic, Japanese, Korean*). Delivers instant turnstile wait times, custom express routing (`Express Corridor W-12`), QR food ordering, and wheelchair/sensory pod dispatches.
* **🗺️ 3D Interactive SVG Stadium Telemetry Map & Live Database Filtering:** A high-contrast stadium layout map dynamically synced with live database records. Features instant database filtering:
  * **All Zones (7 Database Records):** Displays complete 3D stadium grid across North Gate A, East Gate B, South Gate C, West Gate D, VIP Skybox, Central Sensory Hub, and EV Shuttle Terminal.
  * **Concourses & Turnstiles:** Highlights concourse status, immediately flagging **South Gate C at 91% Critical Density** and triggering crowd diversion alerts.
  * **Seating Bowls (`Sectors 101-136`):** Filters lower bowl sectors monitoring acoustic roar (`104 dB`) and thermal levels (`73°F`).
  * **VIP Suites & Skyboxes:** Filters presidential hospitality zones showing pristine air quality (`AQI 15`) and private concierge active status.
  * **Accessibility & Accommodations:** Focuses on ADA infrastructure showing Sensory Hub quiet pod metrics (`18% density, AQI 12`) and zero-wait priority lanes.
* **⚡ Dynamic Mode Switcher (`Command Center Mode` vs `Standard View`):** 
  * Clicking **Command Center Mode** instantly engages tactical emergency autopilot across the entire UI. The stadium map adopts a glowing crimson emergency grid (`inset 0 0 45px rgba(255, 51, 102, 0.45)`), critical/warning nodes (`South Gate C` & `East Gate B`) pulse at double diameter with high-alert flashing markers, and the live database feed shows active crowd diversion protocols (*Redirecting 45% of incoming traffic to West Gate D*).
  * Clicking **Standard View** smoothly resets all node dimensions, borders, and query cards back to standard stadium operations mode.
* **🌱 Net-Zero Sustainability & Microgrid Telemetry:** Real-time tracking of Solar Canopy Generation (`34,820 kWh`), AI-Optimized HVAC Cooling Savings (`18.4%`), Rainwater Recovery (`42,500 L`), and Total Carbon Offset (`128.5 Tons CO2`). Includes a gamified **Green Fan Reward Program** awarding credits for public transit/EV shuttle usage.

### 2️⃣ Relational Database & GenAI Architecture Dashboard (`architecture_dashboard.html`)
Designed for database engineers, system architects, and technical evaluators:
* **🕸️ Interactive Foreign Key Network Graph:** An SVG-powered relational architecture tree visualizing exact data routing and `match_id` foreign key enforcements across all 8 normalized tables. Features zero-shift hover interactions where diagram boxes remain 100% locked in place while displaying neon glowing border highlights (`drop-shadow`).
* **📜 Live SQL Schema Inspector (`DDL & SELECT * FROM table`):** Click any of the 8 relational tables in the sidebar or interactive graph to inspect the exact `CREATE TABLE` DDL statement with data types, constraints (`PRAGMA foreign_keys = ON`), and live SQLite table records rendered in a clean data grid.
* **⚡ Autonomous SQL Transaction Simulator:** Interactive simulation buttons that execute real-time atomic SQL transactions (`BEGIN TRANSACTION ... COMMIT;`) across normalized tables:
  * **Gate C -> Gate D Load Balance:** Executes atomic `UPDATE` reducing Gate C density from `91%` (`Critical`) to `65%` and increasing Gate D to `48%`, while appending a permanent audit record to `operational_incidents_log`.
  * **Sensory Quiet Room Pod Booking:** Joins `stadium_zones` with `accessibility_accommodations`, assigns volunteer escort *Sarah M. (#42)*, and updates pod occupancy atomically.
  * **AI HVAC Energy Optimization:** Executes multi-table update across `stadium_zones` and `sustainability_metrics_log` to dim LED banks and cut auxiliary cooling load by `18.4%`.

---

## 🐍 Polished Python Codebase & Interactive Jupyter Notebooks

The repository features modular, production-ready Python (`.py`) scripts paired with fully formatted, interactive Jupyter Notebooks (`.ipynb`) built using the automated `build_notebooks.py` pipeline. These notebooks allow researchers and engineers to inspect, train, and simulate the database and AI systems locally or on cloud environments (JupyterLab, Google Colab, VS Code):

| Modular Script (`.py`) | Interactive Notebook (`.ipynb`) | Core Scientific & Architectural Purpose |
| :--- | :--- | :--- |
| `nexus_stadium_db_lab.py` | `Nexus_2026_Smart_Stadium_Database_Lab_Notebook.ipynb` | **Normalized Relational Database Engine:** Initializes `nexus_stadium_2026.db` with WAL mode (`Write-Ahead Logging`), creates all 8 relational tables with `CHECK` constraints and `FOREIGN KEY` cascades, inserts 80,000+ attendee simulation rows, and executes atomic SQL transactions (`load_balance_turnstiles`, `book_accessibility_pod`). |
| `nexus_stadium_ai_lab.py` | `Nexus_2026_Smart_Stadium_AI_Lab_Notebook.ipynb` | **Multilingual GenAI Intent & Knowledge Graph:** Implements the LLM intent classification engine across 8 languages (`en`, `es`, `fr`, `pt`, `de`, `ar`, `ja`, `ko`). Simulates neural query embedding lookups, dynamic itinerary generation, emergency crowd rerouting, and real-time IoT sensor fusion. |
| `nexus_stadium_interactive_dashboard.py` | `Nexus_2026_Interactive_System_Dashboard.ipynb` | **System Analytics & Visualization Pipeline:** Generates high-resolution diagnostic charts (`db_architecture_graph.png`, `interactive_gates_chart.png`, `interactive_sust_chart.png`, `gate_load_balance_simulation.png`) tracking turnstile SLA throughput and carbon offset trends. |
| `build_notebooks.py` | *Automated CI/CD Script* | **Notebook Generator:** Automatically parses `# %% [markdown]` and `# %%` cell blocks from the Python scripts to generate clean, JSON-compliant `nbformat 4` Jupyter Notebooks (`.ipynb`) with complete metadata and kernel specifications. |

---

## 🗄️ Relational Database Schema (`nexus_stadium_2026.db`)

The backend is powered by an **8-table normalized SQLite 3 database** (`nexus_stadium_2026.db`) running in **WAL (`Write-Ahead Logging`) Mode** to ensure atomic consistency and zero-lock concurrency under high telemetry loads:

```sql
-- 1. Master Fixture Metadata Table
CREATE TABLE IF NOT EXISTS tournament_fixtures (
    match_id INTEGER PRIMARY KEY AUTOINCREMENT,
    fixture_code TEXT UNIQUE NOT NULL,
    stadium_name TEXT NOT NULL,
    home_team TEXT NOT NULL,
    away_team TEXT NOT NULL,
    kickoff_timestamp DATETIME NOT NULL,
    attendance_current INTEGER DEFAULT 0,
    attendance_capacity INTEGER DEFAULT 82500,
    security_readiness_level TEXT CHECK(security_readiness_level IN ('OPTIMAL', 'ELEVATED', 'CRITICAL'))
);

-- 2. Turnstile & Gate SLAs Table
CREATE TABLE IF NOT EXISTS stadium_gates (
    gate_id TEXT PRIMARY KEY,
    match_id INTEGER NOT NULL,
    gate_name TEXT NOT NULL,
    gate_type TEXT NOT NULL,
    throughput_per_hr INTEGER NOT NULL,
    density_pct INTEGER CHECK(density_pct BETWEEN 0 AND 100),
    wait_time_mins REAL NOT NULL,
    ada_accessible_status TEXT NOT NULL,
    operational_status TEXT CHECK(operational_status IN ('Optimal', 'Warning', 'Critical')),
    FOREIGN KEY(match_id) REFERENCES tournament_fixtures(match_id) ON DELETE CASCADE
);

-- 3. Concourse Thermal, Acoustic & AQI Telemetry Table
CREATE TABLE IF NOT EXISTS stadium_zones (
    zone_id TEXT PRIMARY KEY,
    match_id INTEGER NOT NULL,
    zone_name TEXT NOT NULL,
    temperature_f REAL NOT NULL,
    noise_db REAL NOT NULL,
    aqi_index INTEGER NOT NULL,
    crowd_density_pct INTEGER NOT NULL,
    status_summary TEXT NOT NULL,
    FOREIGN KEY(match_id) REFERENCES tournament_fixtures(match_id) ON DELETE CASCADE
);

-- 4. Multilingual GenAI Knowledge Graph Table
CREATE TABLE IF NOT EXISTS genai_knowledge_graph (
    rule_id INTEGER PRIMARY KEY AUTOINCREMENT,
    intent_category TEXT NOT NULL,
    language_code TEXT NOT NULL,
    trigger_keywords TEXT NOT NULL,
    response_template TEXT NOT NULL,
    action_type TEXT NOT NULL
);

-- 5. Autonomous AI Operational Incidents Audit Log
CREATE TABLE IF NOT EXISTS operational_incidents_log (
    incident_id TEXT PRIMARY KEY,
    match_id INTEGER NOT NULL,
    timestamp_log DATETIME NOT NULL,
    severity_level TEXT CHECK(severity_level IN ('HIGH', 'MEDIUM', 'LOW')),
    category TEXT NOT NULL,
    location_zone TEXT NOT NULL,
    action_taken_desc TEXT NOT NULL,
    resolution_status TEXT CHECK(resolution_status IN ('RESOLVED', 'IN_PROGRESS', 'AUTOMATED')),
    time_saved_mins INTEGER NOT NULL,
    FOREIGN KEY(match_id) REFERENCES tournament_fixtures(match_id) ON DELETE CASCADE
);

-- 6. Net-Zero Sustainability & Microgrid Telemetry Log
CREATE TABLE IF NOT EXISTS sustainability_metrics_log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id INTEGER NOT NULL,
    timestamp_recorded DATETIME NOT NULL,
    solar_kwh_generated REAL NOT NULL,
    hvac_cooling_reduction_pct REAL NOT NULL,
    rainwater_recycled_liters REAL NOT NULL,
    carbon_offset_tons REAL NOT NULL,
    FOREIGN KEY(match_id) REFERENCES tournament_fixtures(match_id) ON DELETE CASCADE
);

-- 7. Accessibility & Neurodiversity Accommodations Table
CREATE TABLE IF NOT EXISTS accessibility_accommodations (
    booking_id TEXT PRIMARY KEY,
    match_id INTEGER NOT NULL,
    guest_id TEXT NOT NULL,
    accommodation_type TEXT CHECK(accommodation_type IN ('SENSORY_POD', 'WHEELCHAIR_BAY', 'VOLUNTEER_ESCORT', 'AUDIO_DESC')),
    assigned_location TEXT NOT NULL,
    escort_volunteer_name TEXT,
    status TEXT NOT NULL,
    FOREIGN KEY(match_id) REFERENCES tournament_fixtures(match_id) ON DELETE CASCADE
);

-- 8. Autonomous EV Transit Shuttle Fleet Telemetry
CREATE TABLE IF NOT EXISTS autonomous_transit_shuttles (
    shuttle_id TEXT PRIMARY KEY,
    terminal_zone TEXT NOT NULL,
    battery_pct INTEGER CHECK(battery_pct BETWEEN 0 AND 100),
    capacity_total INTEGER NOT NULL,
    seats_available INTEGER NOT NULL,
    next_departure_mins INTEGER NOT NULL,
    ada_priority_equipped BOOLEAN DEFAULT 1
);
```

---

## 🏃 Quickstart Guide & Local Execution

Nexus 2026 is engineered for **instant portability and zero-configuration execution**. You can run the entire system directly on any OS (Windows, macOS, Linux) without requiring complex backend servers.

### Option A: Direct Web Dashboard Launch (Zero Dependencies)
Simply double-click either HTML dashboard file directly from your File Explorer to run in local browser mode:
* **`index.html`** (Main FIFA Smart Stadium AI Operations Hub)
* **`architecture_dashboard.html`** (Relational Database Schema & SQL Simulator)

### Option B: Local HTTP Development Server
If you prefer running via a local local server:
```bash
# Clone the repository
git clone https://github.com/unknown404-practice/Nexus-2026.git
cd Nexus-2026

# Serve using Python built-in HTTP server
python -m http.server 3000

# OR using Node.js npx serve
npx serve . -p 3000
```
Then navigate your browser to `http://localhost:3000` (`index.html`) or `http://localhost:3000/architecture_dashboard.html`.

### Option C: Python Database & AI Lab Execution
To execute the backend Python lab scripts or build Jupyter Notebooks:
```bash
# 1. Install required scientific Python libraries
pip install sqlite3 pandas matplotlib jupyter

# 2. Run the Normalized Database Lab (creates & populates nexus_stadium_2026.db)
python nexus_stadium_db_lab.py

# 3. Run the Multilingual GenAI Knowledge Graph Lab
python nexus_stadium_ai_lab.py

# 4. Generate & verify IPYNB Jupyter Notebooks
python build_notebooks.py

# 5. Launch JupyterLab / Notebook interface
jupyter notebook
```

---

## 📁 Repository Structure

```text
Nexus-2026/
├── LICENSE                                          # Apache License 2.0
├── README.md                                        # Enterprise System Documentation & Guide
├── index.html                                       # Main FIFA World Cup Smart Stadium AI Portal (indexfifa.html)
├── architecture_dashboard.html                      # Relational Architecture Tree & SQL Transaction Simulator
├── nexus_stadium_2026.db                            # SQLite 3 Database (8 Normalized Tables)
├── nexus_stadium_db_lab.py                          # Relational Database Engine & Transaction Script (.py)
├── nexus_stadium_ai_lab.py                          # Multilingual GenAI Intent & Knowledge Graph Script (.py)
├── nexus_stadium_interactive_dashboard.py           # Diagnostic Chart Generation Pipeline Script (.py)
├── build_notebooks.py                               # Automated CI/CD IPYNB Notebook Builder Script (.py)
├── Nexus_2026_Smart_Stadium_Database_Lab_Notebook.ipynb  # Interactive Database Jupyter Notebook (.ipynb)
├── Nexus_2026_Smart_Stadium_AI_Lab_Notebook.ipynb        # Interactive GenAI Jupyter Notebook (.ipynb)
├── Nexus_2026_Interactive_System_Dashboard.ipynb         # Interactive Analytics Jupyter Notebook (.ipynb)
├── SYSTEM_ARCHITECTURE_REPORT.md                    # Detailed Technical Architecture Whitepaper
├── package.json                                     # Project Metadata
└── assets/                                          # Visual Reference Assets & Generated Charts
    └── images/                                      # Embedded High-Resolution Diagnostic PNGs
```

---

## 🤝 Contributing & Extension Guidelines

We welcome contributions from database engineers, AI researchers, and smart city architects looking to extend this framework to future sporting tournaments and urban infrastructure projects:
1. **Fork the Repository:** Create your feature branch (`git checkout -b feature/AmazingStadiumFeature`).
2. **Ensure Database Normalization:** Any schema additions to `nexus_stadium_2026.db` must enforce strict foreign keys (`PRAGMA foreign_keys = ON`) and include corresponding test coverage in `nexus_stadium_db_lab.py`.
3. **Multilingual Consistency:** If adding new prompt templates to `genai_knowledge_graph`, ensure translations across all 8 supported language codes.
4. **Commit & Push:** Submit a pull request detailing telemetry improvements or architectural enhancements.

---

## 📄 License & Attribution

This project is open-source and licensed under the **Apache License, Version 2.0**. See the [LICENSE](LICENSE) file for complete legal text.

```text
Copyright 2026 Nexus 2026 Smart Stadium Architecture Team (Ranadeep Saha)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

---

## 👤 Author & Contact Information

**Ranadeep Saha**  
*Member of Google Developer Group (GDG)*  
* **Contact / LinkedIn:** [www.linkedin.com/in/ranadeep-saha-a03296404](https://www.linkedin.com/in/ranadeep-saha-a03296404)  
* **Email ID:** [ranadeep2021saha@gmail.com](mailto:ranadeep2021saha@gmail.com)  

---
*Architected and developed with precision for World-Class Tournament Operations and Next-Generation Smart Stadium Management.*
