# %% [markdown]
# # 🗄️ Nexus 2026: Complete FIFA World Cup Smart Stadium Database System
# 
# **PromptWars Virtual Challenge 4 (`[Challenge 4] Smart Stadiums & Tournament Operations`)**  
# **Database Architecture:** Relational SQLite Database (`nexus_stadium_2026.db`) with Python & Pandas Engine  
# **Author:** Ranadeep Saha, Member of Google Developer Group (GDG)  
# 
# ---
# 
# ## 📋 Executive Summary & Database Architecture
# 
# To fulfill every instruction in `[Challenge 4] Smart Stadiums & Tournament Operations` for **FIFA World Cup 2026**, our GenAI solution requires a robust, high-performance **Relational Database System** that unifies real-time IoT sensor telemetry, multi-lingual knowledge graphs, and automated decision support logs.
# 
# This lab notebook constructs and verifies the complete **Relational Database Schema (9 Tables)**:
# 1. `stadium_gates`: Turnstile throughput, wait times, ADA priority lanes, and crowd density.
# 2. `stadium_zones`: Concourse thermal sensors, acoustic decibels, Air Quality Index (`AQI`), and zone status.
# 3. `tournament_fixtures`: Match schedules, attendance, security readiness, and renewable power percentages.
# 4. `genai_knowledge_graph`: Multi-lingual localized prompts across **8 languages** (`en`, `es`, `fr`, `pt`, `de`, `ar`, `ja`, `ko`) with intent routing.
# 5. `operational_incidents_log`: Autonomous AI intervention audit trail (crowd diversions, medical dispatch, elevator alerts).
# 6. `sustainability_metrics_log`: Solar canopy kWh, AI HVAC cooling reduction %, rainwater recycling, and carbon offsets.
# 7. `accessibility_accommodations`: Wheelchair volunteer escort tracking, ADA sensory quiet room pod reservations, and audio descriptions.
# 8. `autonomous_transit_shuttles`: EV shuttle fleet docking, seat availability, and metro arrivals.
# 9. `stadium_system_metadata`: System attribution, author verification (`Ranadeep Saha, Member of Google Developer Group`), and version control.
# 
# Every block in this notebook can be executed sequentially to initialize the database, seed data, execute SQL analytical queries, and trigger atomic GenAI SQL transactions!

# %% [markdown]
# ---
# ## Block 1: Database Initialization & SQLite Connection Setup
# We initialize the SQLite database `nexus_stadium_2026.db`, enable foreign key enforcement, and verify the connection.

# %%
import os
import sys
import sqlite3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Ensure UTF-8 output on Windows CLI consoles
try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

# Safe display handler for both Jupyter and CLI mode
try:
    from IPython.display import display, Markdown
except ImportError:
    def display(obj):
        print(obj)
    def Markdown(obj):
        return obj

# Helper for non-blocking plot display in CLI mode vs interactive inline in Jupyter mode
def safe_plot_show(fig_name=None):
    if fig_name:
        plt.savefig(fig_name, dpi=300, bbox_inches='tight')
    plt.close()
    if fig_name and os.path.exists(fig_name):
        try:
            from IPython.display import Image, display
            display(Image(filename=fig_name, width=1100))
        except Exception:
            pass

# Optional styling imports with graceful fallbacks
try:
    import seaborn as sns
    sns.set_theme(style="darkgrid")
    HAS_SEABORN = True
except ImportError:
    HAS_SEABORN = False

try:
    import networkx as nx
    HAS_NETWORKX = True
except ImportError:
    HAS_NETWORKX = False

# Set visual styles for high-contrast cyberpunk sports-tech theme
plt.style.use('dark_background')
plt.rcParams['figure.facecolor'] = '#0A0E17'
plt.rcParams['axes.facecolor'] = '#101626'
plt.rcParams['text.color'] = '#F0F4FF'
plt.rcParams['axes.labelcolor'] = '#00F0FF'
plt.rcParams['xtick.color'] = '#8F9BB3'
plt.rcParams['ytick.color'] = '#8F9BB3'
plt.rcParams['grid.color'] = '#1A243C'

# Define database file path
db_path = "nexus_stadium_2026.db"
if os.path.exists(db_path):
    try:
        os.remove(db_path) # Fresh initialization for clean reproducible testing
    except Exception:
        pass

conn = sqlite3.connect(db_path)
conn.execute("PRAGMA foreign_keys = ON;")
conn.execute("PRAGMA journal_mode = WAL;")
conn.execute("PRAGMA synchronous = NORMAL;")
conn.execute("PRAGMA auto_vacuum = INCREMENTAL;")

print(f"[Block 1 Verification] Connected to SQLite Database -> [{db_path}] with Foreign Keys, WAL Mode, and Auto-Vacuum enabled.")
print(f"   ► Pandas Version: {pd.__version__} | Optional Seaborn: {HAS_SEABORN} | Optional NetworkX: {HAS_NETWORKX}")

# %% [markdown]
# ---
# ## Block 2: Complete Relational Schema Definition (`CREATE TABLE` Statements & Production B-Tree Indexes)
# We execute DDL (`Data Definition Language`) statements to create our 8 normalized relational tables with primary keys, foreign keys, constraints, checks, and industrial-strength `B-Tree` indexes for ultra-low latency queries.

# %%
schema_ddl = """
-- Table 1: Tournament Fixtures (16 Host Cities & Multi-Session Schedule)
CREATE TABLE IF NOT EXISTS tournament_fixtures (
    match_id VARCHAR(32) PRIMARY KEY,
    title VARCHAR(128) NOT NULL,
    stadium_name VARCHAR(128) NOT NULL,
    kick_off_time VARCHAR(64) NOT NULL,
    attendance_count INTEGER NOT NULL,
    max_capacity INTEGER NOT NULL,
    security_level VARCHAR(32) NOT NULL,
    renewable_energy_pct FLOAT NOT NULL
);

-- Table 2: Stadium Gates & Turnstile Telemetry
CREATE TABLE IF NOT EXISTS stadium_gates (
    gate_id VARCHAR(32) PRIMARY KEY,
    match_id VARCHAR(32),
    name VARCHAR(128) NOT NULL,
    gate_type VARCHAR(64) NOT NULL,
    throughput_hr INTEGER NOT NULL,
    density_pct INTEGER NOT NULL CHECK(density_pct BETWEEN 0 AND 100),
    wait_time_mins FLOAT NOT NULL,
    ada_status VARCHAR(128) NOT NULL,
    status_flag VARCHAR(32) NOT NULL CHECK(status_flag IN ('Optimal', 'Warning', 'Critical')),
    FOREIGN KEY (match_id) REFERENCES tournament_fixtures(match_id)
);
CREATE INDEX IF NOT EXISTS idx_gates_match ON stadium_gates(match_id);
CREATE INDEX IF NOT EXISTS idx_gates_status ON stadium_gates(status_flag, density_pct);

-- Table 3: Stadium Zones & Sensor Telemetry
CREATE TABLE IF NOT EXISTS stadium_zones (
    zone_id VARCHAR(32) PRIMARY KEY,
    match_id VARCHAR(32),
    name VARCHAR(128) NOT NULL,
    category VARCHAR(64) NOT NULL,
    coord_x FLOAT NOT NULL,
    coord_y FLOAT NOT NULL,
    temp_f VARCHAR(32) NOT NULL,
    aqi_index VARCHAR(64) NOT NULL,
    noise_db VARCHAR(32) NOT NULL,
    density_pct INTEGER NOT NULL CHECK(density_pct BETWEEN 0 AND 100),
    status_flag VARCHAR(32) NOT NULL CHECK(status_flag IN ('Optimal', 'Warning', 'Critical')),
    FOREIGN KEY (match_id) REFERENCES tournament_fixtures(match_id)
);
CREATE INDEX IF NOT EXISTS idx_zones_match ON stadium_zones(match_id);

-- Table 4: GenAI Multilingual Knowledge Graph
CREATE TABLE IF NOT EXISTS genai_knowledge_graph (
    rule_id VARCHAR(32) PRIMARY KEY,
    intent_category VARCHAR(64) NOT NULL,
    trigger_keywords VARCHAR(256) NOT NULL,
    response_en TEXT NOT NULL,
    response_es TEXT NOT NULL,
    response_fr TEXT NOT NULL,
    response_pt TEXT NOT NULL,
    response_de TEXT NOT NULL,
    response_ar TEXT NOT NULL,
    response_ja TEXT NOT NULL,
    response_ko TEXT NOT NULL,
    action_code VARCHAR(64) NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_genai_intent ON genai_knowledge_graph(intent_category);

-- Table 5: Operational Incidents & AI Autonomous Resolution Log
CREATE TABLE IF NOT EXISTS operational_incidents_log (
    incident_id VARCHAR(32) PRIMARY KEY,
    match_id VARCHAR(32),
    timestamp VARCHAR(32) NOT NULL,
    severity VARCHAR(32) NOT NULL CHECK(severity IN ('HIGH', 'MEDIUM', 'LOW')),
    category VARCHAR(128) NOT NULL,
    location_name VARCHAR(128) NOT NULL,
    description TEXT NOT NULL,
    ai_autonomous_action TEXT NOT NULL,
    status VARCHAR(32) NOT NULL,
    time_saved_mins INTEGER NOT NULL,
    FOREIGN KEY (match_id) REFERENCES tournament_fixtures(match_id)
);
CREATE INDEX IF NOT EXISTS idx_incidents_match ON operational_incidents_log(match_id);
CREATE INDEX IF NOT EXISTS idx_incidents_severity ON operational_incidents_log(severity, status);

-- Table 6: Sustainability & Net-Zero Metrics Log
CREATE TABLE IF NOT EXISTS sustainability_metrics_log (
    log_id INTEGER PRIMARY KEY AUTOINCREMENT,
    match_id VARCHAR(32),
    timestamp VARCHAR(32) NOT NULL,
    solar_kwh FLOAT NOT NULL,
    hvac_reduction_pct FLOAT NOT NULL,
    water_recycled_l FLOAT NOT NULL,
    waste_diverted_pct FLOAT NOT NULL,
    carbon_offset_tons FLOAT NOT NULL,
    FOREIGN KEY (match_id) REFERENCES tournament_fixtures(match_id)
);
CREATE INDEX IF NOT EXISTS idx_sustainability_match ON sustainability_metrics_log(match_id);

-- Table 7: Universal Accessibility & Sensory Room Accommodations
CREATE TABLE IF NOT EXISTS accessibility_accommodations (
    booking_id VARCHAR(32) PRIMARY KEY,
    match_id VARCHAR(32),
    fan_id VARCHAR(64) NOT NULL,
    service_type VARCHAR(64) NOT NULL,
    location_name VARCHAR(128) NOT NULL,
    pod_or_seat_number VARCHAR(32) NOT NULL,
    volunteer_assigned VARCHAR(64),
    status VARCHAR(32) NOT NULL,
    timestamp VARCHAR(32) NOT NULL,
    FOREIGN KEY (match_id) REFERENCES tournament_fixtures(match_id)
);
CREATE INDEX IF NOT EXISTS idx_accessibility_match ON accessibility_accommodations(match_id);

-- Table 8: Autonomous EV Transit & Shuttle Fleet
CREATE TABLE IF NOT EXISTS autonomous_transit_shuttles (
    shuttle_id VARCHAR(32) PRIMARY KEY,
    hub_location VARCHAR(128) NOT NULL,
    battery_pct INTEGER NOT NULL,
    total_capacity_seats INTEGER NOT NULL,
    available_seats INTEGER NOT NULL,
    next_departure_mins INTEGER NOT NULL,
    status VARCHAR(32) NOT NULL
);

-- Table 9: Stadium System Attribution & Architecture Metadata
CREATE TABLE IF NOT EXISTS stadium_system_metadata (
    metadata_key VARCHAR(64) PRIMARY KEY,
    metadata_value TEXT NOT NULL,
    category VARCHAR(64) NOT NULL
);
"""

for statement in schema_ddl.split(';'):
    if statement.strip():
        conn.execute(statement)
conn.commit()

# Verify created tables
tables_df = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;", conn)
print("[Block 2 Verification] Created 9 Normalized Relational Tables with B-Tree Indexes successfully:")
print(tables_df.to_string(index=False))

# %% [markdown]
# ---
# ## Block 3: Seeding Comprehensive Multi-Session FIFA World Cup 2026 Production Data
# We insert rich, production-grade records covering **16 Match Sessions across all USA, Mexico, and Canada host cities**, turnstile sensor feeds, multi-lingual AI rules, and operational logs.

# %%
# 1. Seed 16 Multi-Session Tournament Fixtures Across All Host Nations
conn.execute("""
INSERT OR REPLACE INTO tournament_fixtures VALUES 
('match_01', 'USA vs Brazil - Group A Quarterfinal', 'MetLife Stadium (New York/New Jersey)', 'June 24, 2026 - 19:30 EST', 81240, 82500, 'Level 2 (High Readiness)', 84.0),
('match_02', 'Mexico vs Germany - Group B Semifinal', 'Estadio Azteca (Mexico City)', 'July 02, 2026 - 18:00 CST', 86400, 87523, 'Level 1 (Standard Operations)', 91.0),
('match_03', 'Canada vs France - Group C Knockout', 'BMO Field (Toronto)', 'June 28, 2026 - 20:00 EST', 44800, 45000, 'Level 1 (Standard Operations)', 100.0),
('match_04', 'Argentina vs Spain - Group A Opening', 'SoFi Stadium (Los Angeles)', 'June 12, 2026 - 17:00 PST', 70100, 70240, 'Level 2 (High Readiness)', 95.0),
('match_05', 'England vs Japan - Round of 16', 'AT&T Stadium (Dallas)', 'June 29, 2026 - 19:00 CST', 79500, 80000, 'Level 1 (Standard Operations)', 88.5),
('match_06', 'Portugal vs Morocco - Group D Clash', 'Hard Rock Stadium (Miami)', 'June 16, 2026 - 20:30 EST', 64200, 64767, 'Level 2 (High Readiness)', 92.0),
('match_07', 'Italy vs Uruguay - Group E Derby', 'Mercedes-Benz Stadium (Atlanta)', 'June 18, 2026 - 18:00 EST', 70800, 71000, 'Level 1 (Standard Operations)', 96.4),
('match_08', 'Netherlands vs Senegal - Group F Match', 'BC Place (Vancouver)', 'June 19, 2026 - 19:30 PST', 54300, 54500, 'Level 1 (Standard Operations)', 98.0),
('match_09', 'Belgium vs Colombia - Quarterfinal 2', 'Gillette Stadium (Boston)', 'July 04, 2026 - 17:00 EST', 65400, 65878, 'Level 2 (High Readiness)', 87.2),
('match_10', 'South Korea vs Australia - Round of 16', 'Estadio BBVA (Monterrey)', 'June 30, 2026 - 20:00 CST', 53200, 53500, 'Level 1 (Standard Operations)', 90.0),
('match_11', 'Croatia vs Nigeria - Group H Showdown', 'Estadio Akron (Guadalajara)', 'June 21, 2026 - 18:30 CST', 48100, 48300, 'Level 1 (Standard Operations)', 93.5),
('match_12', 'FIFA World Cup 2026 Grand Final Trophy Match', 'MetLife Stadium (New York/New Jersey)', 'July 19, 2026 - 15:00 EST', 82500, 82500, 'Level 3 (Maximum Security & Convoy)', 100.0),
('match_13', 'Spain vs Germany - Group Winner Playoff', 'Levis Stadium (San Francisco Bay Area)', 'June 25, 2026 - 19:00 PST', 68300, 68500, 'Level 1 (Standard Operations)', 94.1),
('match_14', 'Brazil vs France - Semifinal 2 Showdown', 'AT&T Stadium (Dallas)', 'July 14, 2026 - 20:00 CST', 80000, 80000, 'Level 2 (High Readiness)', 92.8),
('match_15', 'USA vs Mexico - North American Derby', 'NRG Stadium (Houston)', 'June 26, 2026 - 19:30 CST', 72100, 72220, 'Level 2 (High Readiness)', 89.4),
('match_16', 'Third Place Bronze Medal Playoff', 'Hard Rock Stadium (Miami)', 'July 18, 2026 - 18:00 EST', 64500, 64767, 'Level 1 (Standard Operations)', 96.0);
""")

# 2. Seed Multi-Session Gates Telemetry Across Stadiums
gates_data = [
    # Match 01 - MetLife Stadium
    ('gate_a', 'match_01', 'North Gate A (Main VIP & Media)', 'VIP Express', 1420, 24, 3.2, '100% ADA Express Lanes Active', 'Optimal'),
    ('gate_b', 'match_01', 'East Gate B (General Admission)', 'General Admission', 3890, 72, 14.1, 'ADA Elevator B2 Under High Load', 'Warning'),
    ('gate_c', 'match_01', 'South Gate C (Transit & Metro Hub)', 'Metro Transit Hub', 4950, 91, 25.8, 'Assisted Shuttle Required', 'Critical'),
    ('gate_d', 'match_01', 'West Gate D (Family & Accessibility Hub)', 'Accessibility & Family', 1850, 31, 4.0, 'Zero Wait Priority Access', 'Optimal'),
    ('gate_vip', 'match_01', 'FIFA Delegation & VIP Gate E', 'Presidential VIP', 420, 12, 1.1, 'Private Concierge Active', 'Optimal'),
    # Match 02 - Estadio Azteca
    ('azteca_n1', 'match_02', 'Puerta Norte 1 (Plaza Principal)', 'General Admission', 5200, 84, 21.0, 'Carriles Accesibles Activos', 'Warning'),
    ('azteca_s2', 'match_02', 'Puerta Sur 2 (Estación Tren Ligero)', 'Metro Transit Hub', 6100, 94, 27.5, 'Asistencia para Sillas de Rueda', 'Critical'),
    ('azteca_w3', 'match_02', 'Puerta Oeste 3 (Acceso Familiar)', 'Accessibility & Family', 2100, 28, 3.8, 'Sin Espera ADA', 'Optimal'),
    # Match 04 - SoFi Stadium
    ('sofi_e1', 'match_04', 'East Entry Plaza 1 (VIP & Club)', 'VIP Express', 1800, 18, 2.4, '100% ADA Express Lanes Active', 'Optimal'),
    ('sofi_w2', 'match_04', 'West Entry Plaza 2 (Shuttle Terminal)', 'Metro Transit Hub', 4400, 65, 12.5, 'Assisted Shuttle Ready', 'Warning'),
    # Match 12 - Grand Final MetLife Stadium
    ('final_g1', 'match_12', 'Grand Final North VIP Gateway', 'Presidential VIP', 1600, 22, 2.8, '100% ADA Express Lanes Active', 'Optimal'),
    ('final_g2', 'match_12', 'Grand Final East General Turnstile Bank', 'General Admission', 6200, 88, 24.2, 'High Throughput Escalator Bank Active', 'Warning'),
    ('final_g3', 'match_12', 'Grand Final South Metro Express Gateway', 'Metro Transit Hub', 7100, 96, 28.9, 'Synchronized AI Load Balancing Alert', 'Critical'),
    ('final_g4', 'match_12', 'Grand Final West Family & ADA Gateway', 'Accessibility & Family', 2400, 34, 4.5, 'Zero Wait Priority Access', 'Optimal')
]
conn.executemany("INSERT OR REPLACE INTO stadium_gates VALUES (?,?,?,?,?,?,?,?,?)", gates_data)

# 3. Seed Multi-Session Zones
zones_data = [
    ('zone_n_concourse', 'match_01', 'North Upper Concourse', 'concourse', 50.0, 15.0, '71°F', 'AQI 22 (Optimal)', '78 dB', 42, 'Optimal'),
    ('zone_s_concourse', 'match_01', 'South Food Court & Plaza', 'concourse', 50.0, 85.0, '76°F', 'AQI 45 (Moderate)', '92 dB', 88, 'Critical'),
    ('zone_e_stands', 'match_01', 'East Lower Bowl (Sectors 101-118)', 'seating', 85.0, 50.0, '73°F', 'AQI 28 (Good)', '104 dB', 96, 'Warning'),
    ('zone_w_stands', 'match_01', 'West Lower Bowl (Sectors 119-136)', 'seating', 15.0, 50.0, '72°F', 'AQI 25 (Good)', '102 dB', 94, 'Optimal'),
    ('zone_vip_suite', 'match_01', 'Sky Box VIP Lounge & Club', 'vip', 30.0, 25.0, '69°F', 'AQI 15 (Pristine)', '64 dB', 65, 'Optimal'),
    ('zone_medical', 'match_01', 'Central First Aid & Sensory Room', 'accessibility', 75.0, 25.0, '70°F', 'AQI 12 (Pristine)', '42 dB', 18, 'Optimal'),
    ('zone_restroom_1', 'match_01', 'Smart Restroom Cluster S4', 'amenity', 65.0, 80.0, '74°F', 'AQI 58 (Requires Vent)', '80 dB', 84, 'Warning'),
    ('zone_shuttle_hub', 'match_01', 'EV Autonomous Shuttle Terminal', 'transit', 50.0, 95.0, '73°F', 'AQI 20 (Optimal)', '68 dB', 38, 'Optimal'),
    # Match 12 Final Zones
    ('final_zone_main', 'match_12', 'Grand Final Center Pitch & Lower Bowl', 'seating', 50.0, 50.0, '70°F', 'AQI 18 (Pristine)', '108 dB', 100, 'Optimal'),
    ('final_zone_concourse', 'match_12', 'Grand Final 360 Concourse Ring', 'concourse', 50.0, 25.0, '73°F', 'AQI 32 (Good)', '88 dB', 78, 'Warning')
]
conn.executemany("INSERT OR REPLACE INTO stadium_zones VALUES (?,?,?,?,?,?,?,?,?,?,?)", zones_data)

# 4. Seed GenAI Knowledge Graph (12 Comprehensive 8-Language Tournament Rules)
knowledge_data = [
    ('rule_nav_101', 'navigation', 'fastest,route,sector 112,navigate,concourse,queue,gate,where,how to get,directions,camino,ruta,puerta,secteur,weg,مسار,ルート,경로',
     'Fastest route to Sector 112: Enter through West Gate D (4-min wait) and take Express Corridor W-12 directly into Sector 112. Avoids South concourse bottlenecks!',
     'Ruta más rápida al Sector 112: Ingrese por la Puerta Oeste D (4 min de espera) y tome el Pasillo Expreso W-12 directamente hacia el Sector 112.',
     'Trajet le plus rapide vers le Secteur 112: Entrez par la Porte Ouest D (4 min dattente) et prenez le Couloir Express W-12.',
     'Rota mais rápida para o Setor 112: Entre pelo Portão Oeste D (4 min de espera) e pegue o Corredor Expresso W-12.',
     'Schnellste Route zu Sektor 112: Betreten Sie durch West Tor D (4 Min Wartezeit) und nehmen Sie den Express-Korridor W-12.',
     'أسرع مسار إلى القطاع 112: ادخل عبر البوابة الغربية D (انتظار 4 دقائق) واتخذ الممر السريع W-12 مباشرة.',
     'セクター112への最速ルート：西ゲートD（待ち時間4分）から入場し、エクスプレス通路W-12を通って直行してください。',
     '섹터 112로 가는 가장 빠른 경로: 서쪽 게이트 D(대기 4분)로 입장하여 익스프레스 복도 W-12를 이용하세요.',
     'highlight_route_west'),
     
    ('rule_ada_102', 'accessibility', 'wheelchair,sensory,quiet,ada,elevator,disabled,escort,autism,neurodivergent,silla,discapacidad,ascensor,ascenseur,aufzug,مصعد,車椅子,휠체어',
     'ADA Sensory Quiet Room Pod #3 is available at North Zone 25 (adjacent to Central Medical Hub). Soundproof walls and adjustable lighting active. Elevator E2 has zero wait right now.',
     'La Sala de Tranquilidad Sensorial ADA Pod #3 está disponible en la Zona Norte 25. Paredes insonorizadas activas. Ascensor E2 sin espera.',
     'La salle de calme sensoriel ADA Pod #3 est disponible dans la zone nord 25. Murs insonorisés et éclairage réglable.',
     'A Sala Sensorial ADA Pod #3 está disponível na Zona Norte 25. Paredes à prova de som ativas. Elevador E2 sem filas.',
     'Der ADA Sensorische Ruheraum Pod #3 ist in Nord-Zone 25 verfügbar. Schalldichte Wände aktiv. Aufzug E2 ohne Wartezeit.',
     'غرفة الهدوء الحسي ADA رقم 3 متاحة في المنطقة الشمالية 25. جدران عازلة للصوت وإضاءة مريحة. المصعد E2 متاح فوراً.',
     'ADAセンサリー・クワイエットルーム Pod #3がノースゾーン25で利用可能です。防音壁と調光照明が稼働中。エレベーターE2は待ち時間ゼロです。',
     'ADA 센서리 콰이어트 룸 Pod #3가 노스 존 25에서 이용 가능합니다. 방음벽 및 조명 조절 가능. 엘리베이터 E2 대기 없음.',
     'reserve_sensory_pod'),

    ('rule_food_103', 'concessions', 'food,halal,vegan,gluten,concession,order,drink,beer,water,snack,comida,bebida,kosher,restaurante,nourriture,essen,طعام,食事,음식',
     'Halal & Gluten-Free Hub: Global Gourmet Sector 108 (2-min queue). Place express QR order now and pick up at Locker Bank B4 in exactly 6 minutes without standing in line!',
     'Comida Halal y Sin Gluten: Sector Gourmet 108 (2 min de fila). ¡Pida por código QR y recoja en el Casillero B4 en 6 minutos!',
     'Stands Halal et Sans Gluten: Secteur Gourmet 108 (2 min dattente). Commandez par QR code et récupérez au Casier B4!',
     'Comida Halal e Sem Glúten: Setor Gourmet 108 (2 min de fila). Faça seu pedido QR e retire no Armário B4 em 6 minutos!',
     'Halal & Glutenfrei: Gourmet Sektor 108 (2 Min Schlange). Bestellen Sie per QR-Code und holen Sie es an Schließfach B4 ab!',
     'أطعمة حلال وخالية من الغلوتين: قطاع الذواقة 108 (انتظار دقيقتين). اطلب عبر الاستجابة السريعة واستلم من الخزانة B4 في 6 دقائق!',
     'ハラール＆グルテンフリー拠点：グローバルグルメセクター108（待ち時間2分）。QRコード注文でロッカーB4から6分で受取可能！',
     '할랄 및 글루텐 프리 구역: 글로벌 고메 섹터 108(대기 2분). QR 주문 후 6분 뒤 B4 보관함에서 바로 수령하세요!',
     'place_express_order'),

    ('rule_shuttle_104', 'shuttles', 'shuttle,bus,ev,autonomous,fleet,transport,terminal,autobús,transporte,navette,shuttlebus,حافلة,シャトル,셔틀',
     'Autonomous EV Shuttle Fleet Status: Terminal S1 (South Plaza) has 18 seats available departing every 5 minutes. VIP & ADA express shuttles are docking at West Gate D.',
     'Estado de Flota EV Autónoma: Terminal S1 (Plaza Sur) tiene 18 asientos disponibles con salidas cada 5 minutos. Autobuses ADA en Puerta Oeste D.',
     'Navettes Autonomes EV: Terminal S1 (Parvis Sud) dispose de 18 places disponibles avec départ toutes les 5 minutes.',
     'Frota de Ônibus EV Autônomos: Terminal S1 (Praça Sul) tem 18 assentos disponíveis com partidas a cada 5 minutos.',
     'Autonome E-Shuttles: Terminal S1 (Südplatz) hat 18 freie Plätze mit Abfahrt alle 5 Minuten. ADA Express am Westtor D.',
     'حافلات الكهربائية ذاتية القيادة: محطة S1 (الساحة الجنوبية) بها 18 مقعداً متاحاً للمغادرة كل 5 دقائق.',
     '自律走行EVシャトル：南プラザS1ターミナルに18席の空きがあり、5分間隔で運行中。ADA優先車は西ゲートDに発着します。',
     '자율주행 EV 셔틀: 남쪽 광장 S1 터미널에 18석이 남아 있으며 5분마다 출발합니다. ADA 전용 셔틀은 서쪽 게이트 D에 대기 중입니다.',
     'dispatch_ev_shuttle'),

    ('rule_emerg_105', 'emergency', 'sos,emergency,help,medical,doctor,paramedic,first aid,injury,sick,emergencia,ayuda,médico,urgences,notfall,طوارئ,緊急,응급',
     'EMERGENCY RESPONSE ACTIVE: Paramedic Team #4 is stationed at North Concourse First Aid Hub (Sector 122). SOS automated dispatch alerted. Please remain where you are or tap SOS on your screen.',
     'RESPUESTA DE EMERGENCIA ACTIVA: Equipo de paramédicos #4 en Sector 122. Alerta SOS enviada automáticamente. Permanezca en su lugar.',
     'URGENCES ACTIVÉES: Équipe paramédicale #4 postée au Secteur 122. Alerte SOS envoyée. Restez sur place.',
     'RESPOSTA DE EMERGÊNCIA ATIVA: Equipe de paramédicos #4 no Setor 122. Alerta SOS enviado. Permaneça no local.',
     'NOTFALL-EINSATZ AKTIV: Sanitäter-Team #4 ist in Sektor 122 stationiert. Automatische SOS-Meldung ausgelöst.',
     'استجابة الطوارئ نشطة: فريق المسعفين رقم 4 متواجد في القطاع 122. تم إرسال تنبيه SOS تلقائياً. يرجى البقاء في مكانك.',
     '緊急対応発動：救急医療チーム#4がセクター122に待機中。SOS自動配車が完了しました。現在地から動かないでください。',
     '응급 대응 활성화: 의료진 #4팀이 섹터 122에 대기 중입니다. 자동 SOS 신고가 접수되었습니다. 현재 위치에 머물러 주세요.',
     'trigger_sos_dispatch'),

    ('rule_trans_106', 'transit', 'metro,train,subway,parking,credits,green credit,transit,metrocard,estacionamiento,tren,gare,parkplatz,مترو,地下鉄,지하철',
     'Green Transit Reward: Arriving via Metro Transit or EV Shuttle earns 150 PromptWars Green Credits! Redeemable for $15 concession discounts at any Express Kiosk.',
     'Recompensa de Transporte Verde: ¡Llegar en Metro o Shuttle EV le otorga 150 Créditos Verdes! Canjeables por $15 de descuento en concesiones.',
     'Récompense Transit Vert: Arriver en Métro ou Navette EV donne 150 Crédits Verts! Échangeables contre 15$ de réduction.',
     'Recompensa de Trânsito Verde: Chegar de Metrô ou Shuttle EV rende 150 Créditos Verdes! Resgatáveis por US$ 15 em descontos.',
     'Grüner Transit-Bonus: Anreise per Metro oder E-Shuttle bringt 150 Green Credits! Einlösbar für 15$ Rabatt an allen Kiosken.',
     'مكافأة النقل الأخضر: الوصول عبر المترو يمنحك 150 رصيداً أخضر! قابلة للاستبدال بخصم 15 دولاراً في أي كشك سريع.',
     'グリーン交通リワード：地下鉄やEVシャトルでの来場で150グリーンクレジットを獲得！キオスクで15ドルの割引に利用できます。',
     '친환경 교통 리워드: 지하철이나 EV 셔틀로 방문하시면 150 그린 크레딧이 지급됩니다! 키오스크에서 15달러 할인으로 교환하세요.',
     'claim_green_credits'),

    ('rule_sust_107', 'sustainability', 'solar,hvac,carbon,net zero,sustainability,recycle,water,microgrid,energía,sostenible,carbone,nachhaltigkeit,استدامة,環境,친환경',
     'Net-Zero Microgrid Telemetry: MetLife Stadium solar canopy is currently generating 34,820 kWh. AI thermal ventilation has reduced HVAC cooling load by 18.4% across concourses today.',
     'Telemetría de Microred Cero Netas: La marquesina solar genera 34,820 kWh. La ventilación AI redujo la carga de HVAC un 18.4% hoy.',
     'Télémétrie Microréseau Net-Zéro: La canopée solaire génère 34 820 kWh. La ventilation IA a réduit la charge de climatisation de 18.4%.',
     'Telemetria de Microrrede Líquido Zero: Teto solar gerando 34.820 kWh. Ventilação por IA reduziu o HVAC em 18,4% hoje.',
     'Netto-Null-Mikronetz: Das Solardach erzeugt 34.820 kWh. KI-gestützte Lüftung hat den Klima-Energieverbrauch heute um 18,4% gesenkt.',
     'قياسات الشبكة الدقيقة لانعدام الانبعاثات: تولد المظلة الشمسية حالياً 34,820 كيلوواط/ساعة. خفضت إضاءة وتكييف الذكاء الاصطناعي استهلاك الطاقة بنسبة 18.4%.',
     'ネットゼロ・マイクログリッド：現在ソーラーキャノピーが34,820 kWhを発電中。AI換気制御により空調負荷が18.4%削減されています。',
     '넷제로 마이크로그리드: 현재 태양광 지붕이 34,820 kWh를 발전하고 있습니다. AI 환기 제어로 오늘 공조 에너지를 18.4% 절감했습니다.',
     'display_sust_dashboard'),

    ('rule_tick_108', 'tickets', 'ticket,nfc,entry,seat,upgrade,vip,turnstile,boleto,entrada,billet,ticket,تذكرة,チケット,티켓',
     'Digital Turnstile NFC Entry: Hold your smartphone near the turnstile scanner for instant biometric verification. VIP Sky Box upgrades available at Concierge Hub North.',
     'Entrada NFC Digital: Acerque su teléfono al escáner del torniquete para verificación biométrica instantánea. Mejoras VIP disponibles en Concierge Norte.',
     'Entrée NFC Digitale: Approchez votre smartphone du scanner pour une vérification instantanée. Surclassements VIP disponibles.',
     'Entrada NFC Digital: Aproxime seu celular do leitor da catraca para verificação instantânea. Upgrades VIP disponíveis.',
     'Digitaler NFC-Einlass: Halten Sie Ihr Smartphone an den Scanner für schnellen Zugang. VIP Sky Box Upgrades am Nord-Concierge verfügbar.',
     'دخول سريع عبر تقنية NFC: ضع هاتفك بالقرب من ماسح البوابة للتحقق الفوري. ترقيات كبار الشخصيات متاحة في مكتب الاستقبال الشمالي.',
     'NFCデジタル入場：スマートフォンを改札スキャナーにかざすだけで生体認証入場が可能です。VIPアップグレードも受付中。',
     '디지털 NFC 입장: 스마트폰을 개찰구 스캐너에 가까이 대면 즉시 확인됩니다. VIP 스카이박스 업그레이드는 북쪽 안내소에서 가능합니다.',
     'verify_nfc_pass'),

    ('rule_rest_109', 'restrooms', 'restroom,bathroom,toilet,washroom,baño,aseo,toilettes,toilette,حمام,トイレ,화장실',
     'Smart Restroom Telemetry: North Cluster S4 has a 1-min wait with AQI pristine air filtering active. Avoid South Concourse restrooms currently undergoing automated cleaning.',
     'Telemetría de Baños Inteligentes: Grupo Norte S4 tiene 1 min de espera con filtrado de aire puro. Evite los baños del Sur (en limpieza).',
     'Toilettes Connectées: Groupe Nord S4 avec 1 min dattente et air filtré. Évitez les toilettes Sud actuellement en nettoyage.',
     'Banheiros Inteligentes: Grupo Norte S4 tem 1 min de espera e ar purificado. Evite os banheiros Sul em limpeza automática.',
     'Smart Restrooms: Nord-Gruppe S4 hat nur 1 Min Wartezeit und gereinigte Luft. Meiden Sie die Süd-Toiletten (aktuell Reinigung).',
     'حمامات ذكية: مجموعة الشمال S4 بها دقيقة واحدة انتظار مع تنقية هواء ممتازة. تجنب حمامات الجنوب التي تخضع للتنظيف الآلي الآن.',
     'スマートトイレ情報：ノースクラスターS4は待ち時間1分で空気清浄システム稼働中。清掃中のサウスコンコースはお避けください。',
     '스마트 화장실 안내: 북쪽 S4 구역은 대기 시간 1분이며 공기 청정 가동 중입니다. 현재 자동 청소 중인 남쪽 화장실은 피해주세요.',
     'locate_restroom'),

    ('rule_sched_110', 'schedule', 'schedule,kickoff,match,halftime,time,when,when does,partido,horario,match,spielplan,مباراة,試合,경기',
     'Match Session #01 Schedule: Kick-off is exactly at 20:00 EST. Halftime GenAI Hologram Show begins at 20:45 EST. Stadium gates remain open for express post-match transit until 23:30 EST.',
     'Horario del Partido #01: Inicio exactamente a las 20:00 EST. Espectáculo de Hologramas al medio tiempo a las 20:45 EST. Puertas abiertas hasta las 23:30 EST.',
     'Horaire du Match #01: Coup denvoi à 20h00 EST. Spectacle Holographique à la mi-temps à 20h45 EST. Portes ouvertes jusquà 23h30 EST.',
     'Horário da Partida #01: pontapé inicial às 20:00 EST. Show de Hologramas no intervalo às 20:45 EST. Portões abertos até 23:30 EST.',
     'Spielplan Match #01: Anstoß um genau 20:00 EST. Halftimeshow mit KI-Hologrammen um 20:45 EST. Tore offen bis 23:30 EST.',
     'جدول المباراة رقم 01: ركلة البداية في تمام الساعة 20:00 بتوقيت الشرق. يبدأ عرض الهولوجرام بين الشوطين في 20:45 بتوقيت الشرق.',
     '試合スケジュール#01：キックオフは20:00 EST。ハーフタイムのAIホログラムショーは20:45 EST開始。退場ゲートは23:30まで開放。',
     '경기 일정 #01: 킥오프는 20:00 EST입니다. 하프타임 AI 홀로그램 쇼는 20:45 EST에 시작됩니다. 게이트는 23:30까지 개방됩니다.',
     'display_match_schedule'),

    ('rule_sec_111', 'security', 'security,bag,prohibited,checkpoint,safety,police,seguridad,bolsa,sécurité,sicherheit,أمن,セキュリティ,보안',
     'Universal Security Screening: AI Express E-Lanes are active at Gates A & D. Clear bag policy enforced (max 12x6x12 inches). Prohibited items can be stored at Locker Bank L1.',
     'Seguridad Universal: Carriles Rápidos AI en Puertas A y D. Política de bolsas transparentes (máx 12x6x12 pulgadas). Casilleros en L1.',
     'Contrôle de Sécurité: Files Express IA aux Portes A & D. Sacs transparents obligatoires. Consignes disponibles en L1.',
     'Segurança Universal: Pistas Expressas IA nos Portões A e D. Política de bolsa transparente. Guarda-volumes disponível no L1.',
     'Sicherheitskontrolle: KI Express-Spuren an Toren A & D aktiv. Transparente Taschen pflicht (max 30x15x30cm). Schließfächer in L1.',
     'التفتيش الأمني الشامل: مسارات الذكاء الاصطناعي السريعة نشطة في البوابتين A و D. يُسمح فقط بالحقائب الشفافة. تتوفر خزائن في L1.',
     'セキュリティチェック：AIエクスプレスレーンがゲートAとDで稼働中。透明バッグのみ持込可能です。ロッカーはL1にあります。',
     '보안 검색 안내: 게이트 A와 D에서 AI 익스프레스 레인이 가동 중입니다. 투명 가방 규정(최대 30x15x30cm)이 적용됩니다.',
     'verify_security_policy'),

    ('rule_lost_112', 'lost_found', 'lost,found,missing,item,phone,wallet,perdido,objeto,perdu,verloren,مفقودات,遺失物,분실물',
     'Digital Lost & Found RFID Hub: All turned-in items are cataloged in real-time. Please visit the Central Guest Services Plaza at West Concourse Sector 115 or check your app item tracker.',
     'Objetos Perdidos Digital: Todos los artículos se catalogan en tiempo real. Visite Plaza de Servicios Central en Sector 115.',
     'Objets Trouvés Numériques: Les articles sont catalogués en temps réel. Rendez-vous au Kiosque Central du Secteur 115.',
     'Achados e Perdidos Digital: Itens catalogados em tempo real. Visite o Hub de Atendimento no Setor 115 do Saguão Oeste.',
     'Digitales Fundbüro: Alle Gegenstände werden per RFID erfasst. Bitte besuchen Sie den Gäste-Service in Sektor 115.',
     'مكتب المفقودات الرقمي: يتم تسجيل جميع العناصر بالعلامات الذكية في الوقت الفعلي. يرجى زيارة مكتب خدمة الضيوف في القطاع 115.',
     'デジタル遺失物センター：届出物はすべてリアルタイムで登録されます。西コンコース・セクター115の総合案内所へお越しください。',
     '디지털 분실물 센터: 습득된 모든 물품은 실시간으로 등록됩니다. 서쪽 콘코스 섹터 115의 고객 안내 센터를 방문해 주세요.',
     'check_lost_and_found')
]
conn.executemany("INSERT OR REPLACE INTO genai_knowledge_graph VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", knowledge_data)

# 5. Seed Multi-Session Incidents Across Matches
incidents_data = [
    ('inc_101', 'match_01', '19:42:15 EST', 'HIGH', 'Crowd Bottleneck', 'South Concourse Gate C Plaza', 'Surge of 3,200 fans arriving simultaneously from NJ Transit Metro train. Density at 91%.', 'Diverting 45% of incoming crowd to West Gate D using synchronized digital wayfinding beacons and push notifications in 8 languages.', 'IN_PROGRESS', 18),
    ('inc_102', 'match_01', '19:35:00 EST', 'MEDIUM', 'Accessibility Request', 'East Sector 112 Wheelchair Bay', 'Elevator E4 maintenance sensor reported temporary speed degradation during halftime transition.', 'Rerouted 14 wheelchair guests to VIP Elevator E2 with personal volunteer escort dispatch. Elevator technician dispatched autonomously.', 'RESOLVED', 12),
    ('inc_103', 'match_01', '19:20:10 EST', 'LOW', 'Sustainability / Energy Optimization', 'North Concourse Lighting & HVAC Grid', 'Ambient natural sunlight sufficient through solar canopy until 20:15 EST.', 'Dimmed LED flood light bank 3 and reduced HVAC cooling load in empty auxiliary zones, saving 1,420 kWh.', 'AUTOMATED', 8),
    ('inc_104', 'match_01', '19:10:05 EST', 'HIGH', 'Medical / First Aid Dispatch', 'West Stand Sector 128, Row 14', 'Fan reported heat exhaustion symptoms via mobile SOS QR scan.', 'Dispatched nearest paramedic team equipped with cooling kit. Cleared corridor C-12 via automated turnstile lock release.', 'RESOLVED', 3),
    # Match 02 - Estadio Azteca Incidents
    ('inc_201', 'match_02', '18:15:20 CST', 'HIGH', 'Crowd Bottleneck', 'Puerta Sur 2 Estación Ligera', 'Surge of 4,100 fans arriving via light rail. Density at 94%.', 'Diverted 50% to Puerta Norte 1 via digital dynamic signage in Spanish and English.', 'RESOLVED', 22),
    # Match 12 - Grand Final Incidents
    ('inc_1201', 'match_12', '14:30:00 EST', 'MEDIUM', 'VIP Delegation Security Screening Surge', 'Grand Final North VIP Gateway', 'Simultaneous arrival of 14 diplomatic motorcades requiring rapid biometric clearance.', 'Activated 4 auxiliary AI biometric screening express lanes and dispatched 6 multilingual guest escorts.', 'RESOLVED', 15)
]
conn.executemany("INSERT OR REPLACE INTO operational_incidents_log VALUES (?,?,?,?,?,?,?,?,?,?)", incidents_data)

# 6. Seed Multi-Session Sustainability Time-Series Logs Across All Matches
sustainability_logs = [
    # Match 01
    ('match_01', '19:00 EST', 35200.0, 18.4, 41000.0, 94.2, 120.5),
    ('match_01', '19:15 EST', 34950.0, 18.4, 41500.0, 94.3, 123.0),
    ('match_01', '19:30 EST', 34820.0, 18.4, 42000.0, 94.2, 125.8),
    ('match_01', '19:45 EST', 34600.0, 18.5, 42500.0, 94.4, 128.5),
    # Match 02 - Estadio Azteca
    ('match_02', '17:30 CST', 41200.0, 21.2, 48000.0, 96.1, 142.0),
    ('match_02', '18:00 CST', 40800.0, 21.5, 48500.0, 96.2, 145.2),
    # Match 04 - SoFi Stadium
    ('match_04', '16:30 PST', 48500.0, 24.0, 52000.0, 98.4, 168.0),
    # Match 12 - Grand Final MetLife
    ('match_12', '14:00 EST', 36800.0, 19.8, 45000.0, 95.5, 135.4),
    ('match_12', '15:00 EST', 36400.0, 20.1, 46200.0, 95.8, 138.9)
]
conn.executemany("INSERT INTO sustainability_metrics_log (match_id, timestamp, solar_kwh, hvac_reduction_pct, water_recycled_l, waste_diverted_pct, carbon_offset_tons) VALUES (?,?,?,?,?,?,?)", sustainability_logs)

# 7. Seed Multi-Session Accessibility Accommodations
acc_data = [
    ('book_ada_01', 'match_01', 'FAN-US-8892', 'Sensory Quiet Room Pod', 'North Zone 25 Sensory Hub', 'Pod #3 (Active)', 'Volunteer Escort #42 (Sarah M.)', 'Confirmed', '19:15 EST'),
    ('book_ada_02', 'match_01', 'FAN-BR-1142', 'ADA Wheelchair Bay & Elevator', 'West Lower Bowl Sector 119', 'Bay W-14', 'Volunteer Escort #18 (Carlos R.)', 'Active Escort', '19:25 EST'),
    ('book_ada_03', 'match_01', 'FAN-DE-4412', 'Multi-Lingual Audio Description', 'East Lower Bowl Sector 108', 'Headphone Stream CH-2', 'Autonomous AI Audio Stream', 'Streaming Live', '19:30 EST'),
    ('book_ada_04', 'match_02', 'FAN-MX-9901', 'Sensory Quiet Room Pod', 'Puerta Norte 1 Sensory Hub', 'Pod #1 (Active)', 'Volunteer Escort #12 (Diego L.)', 'Confirmed', '17:45 CST'),
    ('book_ada_05', 'match_12', 'FAN-ES-5512', 'ADA Wheelchair Bay & Express Elevator', 'Grand Final West Lower Bowl', 'Bay W-01 Priority', 'Volunteer Escort #01 (Elena V.)', 'Active Escort', '14:20 EST')
]
conn.executemany("INSERT OR REPLACE INTO accessibility_accommodations VALUES (?,?,?,?,?,?,?,?,?)", acc_data)

# 8. Seed Shuttles Across Hubs
shuttle_data = [
    ('shuttle_ev_01', 'Shuttle Terminal S1 (South Plaza - MetLife)', 96, 24, 18, 5, 'Docked & Ready'),
    ('shuttle_ev_02', 'Shuttle Terminal S1 (South Plaza - MetLife)', 88, 24, 12, 10, 'Boarding'),
    ('shuttle_ev_03', 'West Gate D ADA Priority Terminal (MetLife)', 100, 12, 8, 2, 'Priority ADA Ready'),
    ('shuttle_ev_04', 'North VIP Concourse Hub (MetLife)', 92, 16, 16, 15, 'Reserved for Convoy'),
    ('shuttle_ev_05', 'Estación Ligera Terminal S2 (Azteca)', 94, 30, 22, 4, 'Boarding'),
    ('shuttle_ev_06', 'SoFi West Plaza Express Hub (Los Angeles)', 98, 28, 20, 6, 'Docked & Ready'),
    ('shuttle_ev_07', 'Grand Final VIP Express Terminal (MetLife)', 100, 20, 18, 3, 'Priority Convoy Ready')
]
conn.executemany("INSERT OR REPLACE INTO autonomous_transit_shuttles VALUES (?,?,?,?,?,?,?)", shuttle_data)

# 9. Seed Stadium System Metadata (Author Verification & Attribution)
metadata_records = [
    ('system_author', 'Ranadeep Saha', 'Author & Lead Architect'),
    ('author_affiliation', 'Member of Google Developer Group (GDG)', 'Professional Organization'),
    ('system_title', 'Nexus 2026: Autonomous AI & Relational IoT Database Engine for FIFA World Cup 2026', 'Project Specification'),
    ('database_version', 'Production v2.0 (16-Session Multi-City Schema)', 'System Release'),
    ('last_certified', 'July 2026', 'Certification Date')
]
conn.executemany("INSERT OR REPLACE INTO stadium_system_metadata VALUES (?,?,?)", metadata_records)
conn.commit()

# Optimize Database Statistics and Compact Storage
conn.execute("ANALYZE;")
conn.execute("PRAGMA optimize;")
conn.execute("PRAGMA incremental_vacuum;")
conn.commit()

print("[Block 3 Verification] All 9 Tables Seeded with 16 Multi-Session FIFA World Cup 2026 Production Data & Optimized (Author: Ranadeep Saha, Member of GDG).")

# %% [markdown]
# ---
# ## Block 4: SQL Analytical Queries for Real-Time Crowd Management & Bottleneck Detection
# We execute complex relational SQL queries joining `stadium_gates` with `tournament_fixtures` to identify critical queue bottlenecks and compute clearance SLAs.

# %%
query_bottlenecks = """
SELECT 
    g.gate_id,
    g.name AS gate_name,
    g.gate_type,
    g.density_pct,
    g.wait_time_mins,
    g.throughput_hr,
    g.status_flag,
    f.title AS match_title,
    ROUND(CAST(g.density_pct AS FLOAT) * 0.28, 1) AS computed_wait_sla
FROM stadium_gates g
JOIN tournament_fixtures f ON g.match_id = f.match_id
WHERE g.density_pct >= 70
ORDER BY g.density_pct DESC;
"""

bottlenecks_df = pd.read_sql(query_bottlenecks, conn)
print("[Block 4 Verification] SQL Query: High-Density Turnstile Bottlenecks Identified (>70% Density):")
display(bottlenecks_df)

# Check total stadium attendance via SQL aggregation
total_stats = pd.read_sql("""
SELECT 
    f.stadium_name,
    f.attendance_count,
    f.max_capacity,
    ROUND((CAST(f.attendance_count AS FLOAT) / f.max_capacity) * 100, 1) AS occupancy_rate_pct,
    COUNT(g.gate_id) AS total_gates_monitored,
    AVG(g.wait_time_mins) AS avg_stadium_wait_time
FROM tournament_fixtures f
JOIN stadium_gates g ON f.match_id = g.match_id
WHERE f.match_id = 'match_01'
GROUP BY f.match_id;
""", conn)
print("\n[Block 4 Verification] SQL Query: Total Stadium Occupancy & Gate KPIs:")
display(total_stats)

# %% [markdown]
# ---
# ## Block 5: GenAI Automated Decision Support & Atomic SQL Transaction Execution
# 
# When `stadium_gates` reports **Gate C at 91% density**, our GenAI engine triggers an atomic SQL `UPDATE` transaction inside our SQLite database. It redirects 45% of incoming fan traffic from Gate C (`Critical`) to Gate D (`Optimal`), logs the autonomous intervention into `operational_incidents_log`, and commits the transaction cleanly.

# %%
def execute_genai_sql_transaction(from_gate="gate_c", to_gate="gate_d", divert_pct=45):
    # 1. Inspect state prior to transaction
    pre_df = pd.read_sql("SELECT gate_id, name, density_pct, wait_time_mins, status_flag FROM stadium_gates WHERE gate_id IN (?, ?);", conn, params=(from_gate, to_gate))
    print("[Block 5 Verification] BEFORE SQL TRANSACTION (Gate C Bottleneck vs Gate D Available):")
    display(pre_df)
    
    # 2. Execute Atomic SQL Transaction
    cursor = conn.cursor()
    cursor.execute("BEGIN TRANSACTION;")
    try:
        cursor.execute("SELECT density_pct FROM stadium_gates WHERE gate_id = ?", (from_gate,))
        from_density = cursor.fetchone()[0]
        cursor.execute("SELECT density_pct FROM stadium_gates WHERE gate_id = ?", (to_gate,))
        to_density = cursor.fetchone()[0]
        
        transfer_vol = int(from_density * (divert_pct / 100.0))
        new_from = max(20, from_density - transfer_vol)
        new_to = min(85, to_density + int(transfer_vol * 0.55))
        
        new_from_wait = round(new_from * 0.28, 1)
        new_to_wait = round(new_to * 0.28, 1)
        
        cursor.execute("""
            UPDATE stadium_gates 
            SET density_pct = ?, wait_time_mins = ?, status_flag = 'Optimal' 
            WHERE gate_id = ?
        """, (new_from, new_from_wait, from_gate))
        
        cursor.execute("""
            UPDATE stadium_gates 
            SET density_pct = ?, wait_time_mins = ?, status_flag = 'Optimal' 
            WHERE gate_id = ?
        """, (new_to, new_to_wait, to_gate))
        
        incident_id = f"inc_{int(datetime.now().timestamp())}"
        cursor.execute("""
            INSERT INTO operational_incidents_log VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (incident_id, 'match_01', datetime.now().strftime("%H:%M:%S EST"), 'HIGH', 
              'Automated SQL Turnstile Load Balancing', 'Gate C to Gate D Corridor',
              f'Gate C reached {from_density}% critical density due to metro arrival surge.',
              f'Executed atomic SQL transaction diverting {divert_pct}% of crowd to Gate D. Turnstile lock reversed.',
              'RESOLVED', 19))
        
        conn.commit()
        print(f"\n[Block 5 Verification] GENAI SQL TRANSACTION COMMITTED SUCCESSFULLY! (Diverted {divert_pct}% from {from_gate} -> {to_gate})")
    except Exception as e:
        conn.rollback()
        print(f"Transaction Rolled Back due to error: {e}")

    # 3. Inspect state post transaction
    post_df = pd.read_sql("SELECT gate_id, name, density_pct, wait_time_mins, status_flag FROM stadium_gates WHERE gate_id IN (?, ?);", conn, params=(from_gate, to_gate))
    print("\n[Block 5 Verification] AFTER SQL TRANSACTION (Equilibrium Restored & Wait Time Reduced):")
    display(post_df)

execute_genai_sql_transaction()

# %% [markdown]
# ---
# ## Block 6: Universal Accessibility & Sensory Room SQL Reservation Engine
# We query `accessibility_accommodations` joined with `stadium_zones` to verify ADA priority corridors, check open relaxation pods at North Zone 25, and inspect volunteer escort dispatch logs.

# %%
query_ada = """
SELECT 
    a.booking_id,
    a.fan_id,
    a.service_type,
    a.location_name,
    a.pod_or_seat_number,
    a.volunteer_assigned,
    a.status,
    z.temp_f AS zone_temp,
    z.aqi_index AS zone_air_quality,
    z.noise_db AS zone_noise_level
FROM accessibility_accommodations a
LEFT JOIN stadium_zones z ON z.name LIKE '%Sensory%' OR z.category = 'accessibility'
WHERE a.match_id = 'match_01'
GROUP BY a.booking_id;
"""

ada_df = pd.read_sql(query_ada, conn)
print("[Block 6 Verification] SQL Query: Universal Accessibility & Sensory Room Bookings:")
display(ada_df)

# Check shuttle status
shuttles_df = pd.read_sql("SELECT shuttle_id, hub_location, battery_pct, available_seats, status FROM autonomous_transit_shuttles WHERE available_seats > 0;", conn)
print("\n[Block 6 Verification] SQL Query: Available Autonomous EV Transit Shuttles for Post-Match Departure:")
display(shuttles_df)

# %% [markdown]
# ---
# ## Block 7: Net-Zero Sustainability & Carbon Footprint SQL Aggregations & Plotting
# We execute SQL aggregation queries on `sustainability_metrics_log` to retrieve time-series metrics over the course of the fixture and visualize solar generation vs. AI HVAC savings directly from database records.

# %%
def query_and_plot_sustainability_db():
    sust_df = pd.read_sql("SELECT timestamp, solar_kwh, hvac_reduction_pct, water_recycled_l, carbon_offset_tons FROM sustainability_metrics_log ORDER BY log_id ASC;", conn)
    print("[Block 7 Verification] SQL Query: Sustainability Time-Series Log:")
    display(sust_df)
    
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
    # Chart 1: Solar Output vs Carbon Offset over time
    ax1 = axes[0]
    ax1.plot(sust_df['timestamp'], sust_df['solar_kwh'], color='#00F0FF', linewidth=3, marker='o', label='Solar & Microgrid Output (kWh)')
    ax1.set_title("SQL Time-Series: Solar Canopy Output (kWh)", fontsize=13, fontweight='bold', color='#00F0FF')
    ax1.set_xlabel("Match Timestamp", fontweight='bold')
    ax1.set_ylabel("kWh Generated", fontweight='bold')
    ax1.grid(True, linestyle='--', alpha=0.3)
    ax1.legend(loc='lower left')
    
    # Chart 2: Carbon Offsets Accumulated
    ax2 = axes[1]
    bars = ax2.bar(sust_df['timestamp'], sust_df['carbon_offset_tons'], color='#00FF88', edgecolor='#00F0FF', width=0.45)
    ax2.set_title("SQL Time-Series: Total Net Carbon Offset (Tons CO2)", fontsize=13, fontweight='bold', color='#00FF88')
    ax2.set_xlabel("Match Timestamp", fontweight='bold')
    ax2.set_ylabel("Tons CO2 Offset", fontweight='bold')
    for bar in bars:
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, f"{bar.get_height()}T", ha='center', fontweight='bold', color='#FFF')
    ax2.set_ylim(0, 150)
    
    plt.tight_layout()
    safe_plot_show('sustainability_db_chart.png')

query_and_plot_sustainability_db()
print("[Block 7 Verification] Database sustainability time-series plotted cleanly.")

# %% [markdown]
# ---
# ## Block 8: System Architecture & Relational Database Graph Visualization
# We visualize foreign key relations across all 8 SQLite tables. If NetworkX is available, we render a dynamic directional network diagram; otherwise, we render a high-precision architectural schematic using clean Matplotlib boxes!

# %%
def plot_database_system_architecture():
    entities = {
        "tournament_fixtures": {"label": "tournament_fixtures\n(Match Master)", "color": "#00F0FF", "pos": (50, 85)},
        "stadium_gates": {"label": "stadium_gates\n(Turnstile IoT Feeds)", "color": "#BD00FF", "pos": (20, 60)},
        "stadium_zones": {"label": "stadium_zones\n(Concourse & Thermal)", "color": "#BD00FF", "pos": (50, 60)},
        "operational_incidents_log": {"label": "operational_incidents_log\n(AI Audit Trail)", "color": "#FF3366", "pos": (80, 60)},
        "genai_knowledge_graph": {"label": "genai_knowledge_graph\n(8-Language LLM Core)", "color": "#FF007A", "pos": (20, 30)},
        "sustainability_metrics_log": {"label": "sustainability_metrics_log\n(Solar & HVAC KPIs)", "color": "#00FF88", "pos": (50, 30)},
        "accessibility_accommodations": {"label": "accessibility_accommodations\n(ADA Pod & Escorts)", "color": "#00FF88", "pos": (80, 30)},
        "autonomous_transit_shuttles": {"label": "autonomous_transit_shuttles\n(EV Shuttle Docking)", "color": "#00A3FF", "pos": (50, 5)}
    }
    
    edges = [
        ("tournament_fixtures", "stadium_gates", "FK: match_id"),
        ("tournament_fixtures", "stadium_zones", "FK: match_id"),
        ("tournament_fixtures", "operational_incidents_log", "FK: match_id"),
        ("tournament_fixtures", "sustainability_metrics_log", "FK: match_id"),
        ("tournament_fixtures", "accessibility_accommodations", "FK: match_id"),
        ("stadium_gates", "operational_incidents_log", "Trigger: Density > 85%"),
        ("stadium_zones", "accessibility_accommodations", "Join: Sensory Pods"),
        ("genai_knowledge_graph", "stadium_gates", "SQL UPDATE: Load Balance"),
        ("genai_knowledge_graph", "autonomous_transit_shuttles", "Query: Shuttle ETA")
    ]

    if HAS_NETWORKX:
        G = nx.DiGraph()
        for node, attr in entities.items():
            G.add_node(node, **attr)
        for u, v, label in edges:
            G.add_edge(u, v, label=label)
            
        plt.figure(figsize=(15, 11))
        pos = nx.get_node_attributes(G, 'pos')
        colors = [G.nodes[n]['color'] for n in G.nodes()]
        labels = {n: G.nodes[n]['label'] for n in G.nodes()}
        
        nx.draw_networkx_edges(G, pos, edge_color='#8F9BB3', width=2.5, arrowsize=25, connectionstyle='arc3,rad=0.08')
        edge_labels = nx.get_edge_attributes(G, 'label')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, font_color='#00F0FF', bbox=dict(facecolor='#0A0E17', edgecolor='none', alpha=0.85))
        nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=4200, edgecolors='#FFF', linewidths=2)
        nx.draw_networkx_labels(G, pos, labels=labels, font_size=9, font_weight='bold', font_color='#000')
    else:
        # Fallback pure matplotlib schematic layout
        fig, ax = plt.subplots(figsize=(15, 11))
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        
        # Draw edges as arrows
        for u, v, label in edges:
            x1, y1 = entities[u]["pos"]
            x2, y2 = entities[v]["pos"]
            ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="->", color='#8F9BB3', lw=2))
            ax.text((x1+x2)/2, (y1+y2)/2, label, color='#00F0FF', fontsize=8, ha='center', bbox=dict(boxstyle="round,pad=0.3", facecolor='#0A0E17', edgecolor='#8F9BB3'))
            
        # Draw nodes as boxes
        for node, attr in entities.items():
            x, y = attr["pos"]
            box = patches.FancyBboxPatch((x-12, y-6), 24, 12, boxstyle="round,pad=0.5", facecolor=attr["color"], edgecolor='#FFF', lw=2)
            ax.add_patch(box)
            ax.text(x, y, attr["label"], color='#000', fontsize=9, fontweight='bold', ha='center', va='center')
            
        ax.axis('off')

    plt.title("NEXUS 2026: RELATIONAL DATABASE & GENAI SYSTEM ARCHITECTURE GRAPH\nComplete Foreign Key Schema & Real-Time IoT Sensor Integration",
              fontsize=14, fontweight='bold', color='#00F0FF', pad=20)
    plt.tight_layout()
    safe_plot_show('db_architecture_graph.png')

plot_database_system_architecture()
print("[Block 8 Verification] Database System Architecture Graph plotted cleanly.")

# %% [markdown]
# ---
# # 🎉 Congratulations! Database System Verified Sequentially.
# You have executed all 8 database blocks sequentially. Every table is created, seeded, queried, and updated with atomic SQL transactions.
