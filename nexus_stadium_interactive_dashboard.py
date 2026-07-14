# %% [markdown]
# # ⚡ Nexus 2026: Complete Interactive System Architecture & Operations Dashboard (Pure Python)
# 
# **PromptWars Virtual Challenge 4 (`[Challenge 4] Smart Stadiums & Tournament Operations`)**  
# **Author:** Ranadeep Saha, Member of Google Developer Group (GDG)  
# **Database:** Real-Time Relational SQLite (`nexus_stadium_2026.db`)  
# **UI Framework:** Pure Python `ipywidgets` & `IPython.display` for Jupyter Notebooks / Colab / Lab  
# 
# ---
# 
# ## 📋 Executive Summary & Interactive Dashboard Capabilities
# 
# This interactive Python dashboard allows you to visually inspect, monitor, and mutate the complete **Relational Database Schema (9 Tables)** right inside your Jupyter Notebook. Every button click executes **live atomic SQL transactions** inside `nexus_stadium_2026.db` and dynamically updates the visual charts, data grids, and audit logs in real-time!
# 
# ### 🎮 Interactive Features:
# 1. **Tab 1: 🗄️ Relational Schema & Table Explorer:** Select any of the 9 normalized tables (`stadium_system_metadata`, `stadium_gates`, `tournament_fixtures`, `sustainability_metrics_log`, etc.) to view its SQL DDL definition, columns, and live records (`SELECT * FROM table`).
# 2. **Tab 2: ⚡ Atomic SQL Transaction Simulator:** Click buttons to trigger autonomous GenAI interventions:
#    * **`[🚨 Gate C -> Gate D Load Balance]`**: Executes `UPDATE stadium_gates SET density_pct = ...` and commits audit logs. Watch Gate C drop from `91% (Critical)` to `46% (Optimal)` live!
#    * **`[♿ Reserve Sensory Quiet Pod #4]`**: Executes `INSERT INTO accessibility_accommodations` and dispatches volunteer escort Carlos R.
#    * **`[☀️ Insert New Solar Telemetry Record]`**: Inserts live solar generation kWh & HVAC savings into `sustainability_metrics_log`.
# 3. **Tab 3: 📊 Live Visual Analytics Charts:** Real-time `matplotlib` plotting for Turnstile Queue Densities and Net-Zero Carbon Offset time-series.
# 4. **Tab 4: 🤖 8-Language GenAI Concierge Playground:** Test multi-lingual intent recognition across `English`, `Spanish`, `French`, `Portuguese`, `German`, `Arabic`, `Japanese`, and `Korean`.
# 5. **Tab 5: 🌐 Embedded Full-Screen Web HTML Dashboard:** Optionally render our full-screen high-tech `architecture_dashboard.html` right inside your Jupyter cell using `IFrame` or `HTML`!

# %% [markdown]
# ---
# ## Block 1: Environment & Database Connection Setup
# Initialize libraries, verify UTF-8 encoding, and ensure `nexus_stadium_2026.db` is connected with Foreign Keys enabled.

# %%
import os
import sys
import sqlite3
import datetime
import warnings
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

warnings.filterwarnings('ignore')

# Ensure UTF-8 output on Windows CLI consoles
try:
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

# Safe display handler
try:
    from IPython.display import display, Markdown, HTML, IFrame, clear_output
except ImportError:
    def display(obj): print(obj)
    def Markdown(obj): return obj
    def clear_output(wait=False): pass

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

# Set high-contrast dark visual theme for charts
plt.style.use('dark_background')
plt.rcParams['figure.facecolor'] = '#0A0E17'
plt.rcParams['axes.facecolor'] = '#101626'
plt.rcParams['text.color'] = '#F0F4FF'
plt.rcParams['axes.labelcolor'] = '#00F0FF'
plt.rcParams['xtick.color'] = '#8F9BB3'
plt.rcParams['ytick.color'] = '#8F9BB3'
plt.rcParams['grid.color'] = '#1A243C'

db_path = "nexus_stadium_2026.db"
if not os.path.exists(db_path):
    print(f"Warning: {db_path} not found. Please run `python nexus_stadium_db_lab.py` first to initialize and seed the database!")

conn = sqlite3.connect(db_path)
conn.execute("PRAGMA foreign_keys = ON;")
conn.execute("PRAGMA journal_mode = WAL;")

print(f"[Block 1 Verification] Connected to SQLite Database -> [{db_path}] with Foreign Keys and WAL Mode active.")
print(f"   ► Pandas Version: {pd.__version__}")

# %% [markdown]
# ---
# ## Block 2: Interactive Pure Python Jupyter Dashboard (`ipywidgets`)
# Run this block inside your Jupyter Notebook (`JupyterLab`, `VS Code`, `Colab`) to launch the multi-tab interactive UI. Every interactive button modifies the live database and redraws your data tables right before your eyes!

# %%
try:
    import ipywidgets as widgets
    from IPython.display import display, clear_output

    class InteractiveNexusDashboard:
        def __init__(self, db_conn):
            self.conn = db_conn
            self.tables = [
                'stadium_system_metadata',
                'tournament_fixtures', 'stadium_gates', 'stadium_zones',
                'genai_knowledge_graph', 'operational_incidents_log',
                'sustainability_metrics_log', 'accessibility_accommodations',
                'autonomous_transit_shuttles'
            ]
            self.build_ui()

        def build_ui(self):
            # Header
            header_html = widgets.HTML("""
                <div style="background: linear-gradient(135deg, #0A0E17, #1A243C); padding: 18px; border-radius: 12px; border: 2px solid #00F0FF; margin-bottom: 15px; box-shadow: 0 0 20px rgba(0,240,255,0.25);">
                    <h2 style="color: #00F0FF; margin: 0; font-family: monospace; letter-spacing: 1px;">⚡ NEXUS 2026: INTERACTIVE PYTHON SYSTEM DASHBOARD</h2>
                    <p style="color: #8F9BB3; margin: 6px 0 0 0; font-size: 13px;">Real-Time Relational Database (`nexus_stadium_2026.db`) Multi-Tab Explorer & Atomic SQL Transaction Simulator</p>
                    <div style="margin-top: 10px; background: rgba(0,255,136,0.12); border: 1px solid #00FF88; padding: 5px 14px; border-radius: 20px; display: inline-block; font-size: 13px; color: #00FF88; font-weight: 600;">
                        👤 Author: Ranadeep Saha &nbsp;|&nbsp; 🏅 Member of Google Developer Group (GDG)
                    </div>
                </div>
            """)

            # --- TAB 1: Schema & Table Explorer ---
            self.table_selector = widgets.Dropdown(
                options=self.tables,
                value='stadium_gates',
                description='Select Table:',
                layout=widgets.Layout(width='380px')
            )
            self.refresh_btn = widgets.Button(
                description='🔄 Refresh Table Data',
                button_style='info',
                layout=widgets.Layout(width='180px')
            )
            self.table_output = widgets.Output()

            self.table_selector.observe(self.on_table_change, names='value')
            self.refresh_btn.on_click(lambda b: self.render_table(self.table_selector.value))

            tab1_box = widgets.VBox([
                widgets.HBox([self.table_selector, self.refresh_btn]),
                self.table_output
            ])

            # --- TAB 2: Atomic SQL Transaction Simulator ---
            sim_title = widgets.HTML("<h3 style='color: #00FF88; margin-top: 5px;'>⚡ Execute Autonomous GenAI SQL Transactions</h3><p style='color: #8F9BB3; font-size: 12px;'>Clicking any button below commits a live transaction (`BEGIN ... COMMIT;`) across multiple normalized tables and logs the audit trail!</p>")
            
            self.btn_load_balance = widgets.Button(
                description='🚨 Gate C -> Gate D Load Balance',
                button_style='danger',
                layout=widgets.Layout(width='280px', height='45px')
            )
            self.btn_ada_reserve = widgets.Button(
                description='🛋️ Reserve Sensory Quiet Pod #4',
                button_style='success',
                layout=widgets.Layout(width='280px', height='45px')
            )
            self.btn_sust_log = widgets.Button(
                description='☀️ Insert New Solar/HVAC Telemetry',
                button_style='primary',
                layout=widgets.Layout(width='280px', height='45px')
            )
            self.btn_reset_db = widgets.Button(
                description='🔄 Reset Database to Seed State',
                button_style='warning',
                layout=widgets.Layout(width='280px', height='45px')
            )

            self.btn_load_balance.on_click(self.run_load_balance)
            self.btn_ada_reserve.on_click(self.run_ada_reserve)
            self.btn_sust_log.on_click(self.run_sust_log)
            self.btn_reset_db.on_click(self.run_reset_db)

            self.sim_output = widgets.Output()

            tab2_box = widgets.VBox([
                sim_title,
                widgets.HBox([self.btn_load_balance, self.btn_ada_reserve]),
                widgets.HBox([self.btn_sust_log, self.btn_reset_db], layout=widgets.Layout(margin='10px 0 0 0')),
                widgets.HTML("<h4 style='color: #00F0FF; margin: 15px 0 5px 0;'>Live SQL Execution Audit Log & Affected Data Rows:</h4>"),
                self.sim_output
            ])

            # --- TAB 3: Visual Analytics Charts ---
            chart_btn_gates = widgets.Button(description='📊 Plot Turnstile Densities', button_style='info', layout=widgets.Layout(width='220px'))
            chart_btn_sust = widgets.Button(description='☀️ Plot Sustainability Time-Series', button_style='success', layout=widgets.Layout(width='240px'))
            chart_btn_arch = widgets.Button(description='🕸️ Plot Architecture Graph', button_style='primary', layout=widgets.Layout(width='220px'))
            
            self.chart_output = widgets.Output()

            chart_btn_gates.on_click(lambda b: self.plot_chart('gates'))
            chart_btn_sust.on_click(lambda b: self.plot_chart('sust'))
            chart_btn_arch.on_click(lambda b: self.plot_chart('arch'))

            tab3_box = widgets.VBox([
                widgets.HTML("<p style='color: #8F9BB3;'>Click below to render live visual analytics generated directly from your SQLite database records:</p>"),
                widgets.HBox([chart_btn_gates, chart_btn_sust, chart_btn_arch]),
                self.chart_output
            ])

            # --- TAB 4: Multi-Lingual GenAI Concierge ---
            self.query_input = widgets.Text(
                value='What is the fastest way to Sector 112 without getting stuck in crowds?',
                description='Prompt:',
                layout=widgets.Layout(width='65%')
            )
            self.lang_dropdown = widgets.Dropdown(
                options=[('English (US)', 'en'), ('Español (Spanish)', 'es'), ('Français (French)', 'fr'),
                         ('Português (Portuguese)', 'pt'), ('Deutsch (German)', 'de'), ('العربية (Arabic)', 'ar'),
                         ('日本語 (Japanese)', 'ja'), ('한국어 (Korean)', 'ko')],
                value='en',
                description='Language:',
                layout=widgets.Layout(width='30%')
            )
            query_btn = widgets.Button(description='➤ Query AI Core', button_style='info', layout=widgets.Layout(width='160px'))
            self.ai_output = widgets.Output()

            query_btn.on_click(self.run_ai_query)

            tab4_box = widgets.VBox([
                widgets.HTML("<p style='color: #8F9BB3;'>Test the neural intent categorization and localized knowledge graph across 8 primary World Cup languages:</p>"),
                widgets.HBox([self.query_input, self.lang_dropdown]),
                query_btn,
                self.ai_output
            ])

            # --- TAB 5: Embedded Web HTML Dashboard ---
            tab5_box = widgets.VBox([
                widgets.HTML("<h4 style='color: #00F0FF;'>🌐 Full-Screen Web HTML Dashboard Embedded Inside Jupyter Cell:</h4><p style='color: #8F9BB3;'>If you want to view the standalone interactive HTML architecture dashboard directly inside your notebook, run the cell in Block 3!</p>")
            ])

            # Combine into Tab Widget
            self.main_tabs = widgets.Tab(children=[tab1_box, tab2_box, tab3_box, tab4_box, tab5_box])
            self.main_tabs.set_title(0, '🗄️ Table Explorer')
            self.main_tabs.set_title(1, '⚡ SQL Transaction Simulator')
            self.main_tabs.set_title(2, '📊 Live Charts')
            self.main_tabs.set_title(3, '🤖 Multi-Lingual AI')
            self.main_tabs.set_title(4, '🌐 Web Dashboard IFrame')

            display(header_html, self.main_tabs)
            
            # Initial renders
            self.render_table('stadium_gates')
            with self.sim_output:
                print("[System Ready] Select an action above to execute atomic SQL transactions on `nexus_stadium_2026.db`.")
            self.plot_chart('gates')
            self.run_ai_query(None)

        def on_table_change(self, change):
            self.render_table(change['new'])

        def render_table(self, table_name):
            with self.table_output:
                clear_output(wait=True)
                pd.set_option('display.max_columns', None)
                pd.set_option('display.max_rows', None)
                pd.set_option('display.width', 1000)
                df = pd.read_sql(f"SELECT * FROM {table_name};", self.conn)
                print(f"=== Table: [{table_name}] ({len(df)} Active Records) ===")
                try:
                    styled_html = df.to_html(index=False, classes='table table-dark table-striped', border=0)
                    wrapper = f'''
                    <div style="overflow-x: auto; max-height: 550px; border: 1px solid #00F0FF; border-radius: 8px; padding: 12px; background: #0A0E17; margin-top: 8px;">
                        <style>
                            table.table-dark {{ width: 100%; border-collapse: collapse; font-family: monospace; font-size: 13px; color: #F0F4FF; }}
                            table.table-dark th {{ background-color: #1A243C; color: #00F0FF; padding: 10px; border-bottom: 2px solid #00F0FF; text-align: left; position: sticky; top: 0; z-index: 2; }}
                            table.table-dark td {{ padding: 8px 10px; border-bottom: 1px solid #101626; }}
                            table.table-dark tr:nth-child(even) {{ background-color: #101626; }}
                            table.table-dark tr:hover {{ background-color: rgba(0,240,255,0.18); color: #FFF; }}
                        </style>
                        {styled_html}
                    </div>
                    '''
                    display(HTML(wrapper))
                except Exception:
                    display(df)

        def run_load_balance(self, b):
            with self.sim_output:
                clear_output(wait=True)
                print("[EXEC] BEGIN TRANSACTION;")
                cursor = self.conn.cursor()
                try:
                    cursor.execute("SELECT density_pct FROM stadium_gates WHERE gate_id = 'gate_c'")
                    row = cursor.fetchone()
                    from_density = row[0] if row else 91
                    
                    if from_density < 40:
                        print(f"Gate C density is currently {from_density}%. Re-surging Gate C to 91% Critical for simulation test...")
                        cursor.execute("UPDATE stadium_gates SET density_pct = 91, wait_time_mins = 25.8, status_flag = 'Critical' WHERE gate_id = 'gate_c'")
                        from_density = 91

                    transfer_vol = int(from_density * 0.45)
                    new_from = max(20, from_density - transfer_vol)
                    new_from_wait = round(new_from * 0.28, 1)
                    
                    cursor.execute("UPDATE stadium_gates SET density_pct = ?, wait_time_mins = ?, status_flag = 'Optimal' WHERE gate_id = 'gate_c'", (new_from, new_from_wait))
                    cursor.execute("UPDATE stadium_gates SET density_pct = 68, wait_time_mins = 19.0, status_flag = 'Warning' WHERE gate_id = 'gate_d'")
                    
                    incident_id = f"inc_{int(datetime.datetime.now().timestamp())}"
                    cursor.execute("""
                        INSERT INTO operational_incidents_log VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (incident_id, 'match_01', datetime.datetime.now().strftime("%H:%M:%S EST"), 'HIGH',
                          'Automated SQL Turnstile Load Balancing', 'Gate C to Gate D Corridor',
                          f'Gate C reached {from_density}% critical density due to metro arrival surge.',
                          'Executed atomic SQL transaction diverting 45% of crowd to Gate D express turnstiles.',
                          'RESOLVED', 19))
                    
                    self.conn.commit()
                    print("[SUCCESS] COMMIT TRANSACTION; Diverted 45% traffic from Gate C -> Gate D successfully.")
                    print("\n--- Live Updated `stadium_gates` Table ---")
                    display(pd.read_sql("SELECT gate_id, name, density_pct, wait_time_mins, status_flag FROM stadium_gates WHERE gate_id IN ('gate_c', 'gate_d');", self.conn))
                    print("\n--- New Audit Record in `operational_incidents_log` ---")
                    display(pd.read_sql("SELECT incident_id, timestamp, severity, category, ai_autonomous_action, time_saved_mins FROM operational_incidents_log ORDER BY incident_id DESC LIMIT 1;", self.conn))
                except Exception as e:
                    self.conn.rollback()
                    print(f"[ERROR] Transaction rolled back: {e}")

        def run_ada_reserve(self, b):
            with self.sim_output:
                clear_output(wait=True)
                print("[EXEC] BEGIN TRANSACTION;")
                cursor = self.conn.cursor()
                try:
                    booking_id = f"book_ada_{int(datetime.datetime.now().timestamp())}"
                    cursor.execute("""
                        INSERT INTO accessibility_accommodations VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """, (booking_id, 'match_01', 'FAN-ES-9912', 'Sensory Quiet Room Pod',
                          'North Zone 25 Sensory Hub', 'Pod #4 (Active)', 'Volunteer Escort #18 (Carlos R.)',
                          'Confirmed', datetime.datetime.now().strftime("%H:%M EST")))
                    self.conn.commit()
                    print(f"[SUCCESS] COMMIT TRANSACTION; Reserved Sensory Pod #4 and dispatched volunteer Carlos R.")
                    print("\n--- Live Updated `accessibility_accommodations` Table ---")
                    display(pd.read_sql("SELECT * FROM accessibility_accommodations ORDER BY timestamp DESC LIMIT 3;", self.conn))
                except Exception as e:
                    self.conn.rollback()
                    print(f"[ERROR] Transaction rolled back: {e}")

        def run_sust_log(self, b):
            with self.sim_output:
                clear_output(wait=True)
                print("[EXEC] BEGIN TRANSACTION;")
                cursor = self.conn.cursor()
                try:
                    cursor.execute("""
                        INSERT INTO sustainability_metrics_log (match_id, timestamp, solar_kwh, hvac_reduction_pct, water_recycled_l, waste_diverted_pct, carbon_offset_tons)
                        VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, ('match_01', datetime.datetime.now().strftime("%H:%M EST"), 35400.0, 19.2, 43000.0, 95.0, 132.0))
                    self.conn.commit()
                    print("[SUCCESS] COMMIT TRANSACTION; Inserted new Net-Zero microgrid telemetry record (35,400 kWh solar / 19.2% HVAC savings).")
                    print("\n--- Live Updated `sustainability_metrics_log` Table ---")
                    display(pd.read_sql("SELECT * FROM sustainability_metrics_log ORDER BY log_id DESC LIMIT 3;", self.conn))
                except Exception as e:
                    self.conn.rollback()
                    print(f"[ERROR] Transaction rolled back: {e}")

        def run_reset_db(self, b):
            with self.sim_output:
                clear_output(wait=True)
                print("[EXEC] Resetting `nexus_stadium_2026.db` to fresh seed state via `nexus_stadium_db_lab.py`...")
                import subprocess
                subprocess.run(["python", "nexus_stadium_db_lab.py"], cwd=os.getcwd())
                print("[SUCCESS] Database reset cleanly to original production seed values!")
                display(pd.read_sql("SELECT gate_id, name, density_pct, wait_time_mins, status_flag FROM stadium_gates;", self.conn))

        def plot_chart(self, chart_type):
            with self.chart_output:
                clear_output(wait=True)
                if chart_type == 'gates':
                    df = pd.read_sql("SELECT name, density_pct, status_flag FROM stadium_gates;", self.conn)
                    fig, ax = plt.subplots(figsize=(14, 6.5))
                    colors = ['#00FF88' if s == 'Optimal' else '#FFB800' if s == 'Warning' else '#FF3366' for s in df['status_flag']]
                    bars = ax.barh(df['name'], df['density_pct'], color=colors, edgecolor='#00F0FF', height=0.6)
                    ax.set_xlim(0, 105)
                    ax.set_title("Live Turnstile Queue Densities (%) from SQLite Database", fontsize=14, fontweight='bold', color='#00F0FF', pad=15)
                    ax.set_xlabel("Queue Density Percentage (%)", fontweight='bold', fontsize=12)
                    for bar in bars:
                        ax.text(bar.get_width() + 1.5, bar.get_y() + bar.get_height()/2, f"{bar.get_width()}%", va='center', fontweight='bold', color='#FFF', fontsize=10)
                    plt.tight_layout()
                    safe_plot_show('interactive_gates_chart.png')
                elif chart_type == 'sust':
                    df = pd.read_sql("SELECT timestamp, solar_kwh, carbon_offset_tons FROM sustainability_metrics_log ORDER BY log_id ASC;", self.conn)
                    fig, ax1 = plt.subplots(figsize=(14, 6.5))
                    ax1.plot(df['timestamp'], df['solar_kwh'], color='#00F0FF', linewidth=3.5, marker='o', markersize=8, label='Solar Output (kWh)')
                    ax1.set_ylabel("Solar kWh Generated", color='#00F0FF', fontweight='bold', fontsize=12)
                    ax1.grid(True, linestyle='--', alpha=0.3)
                    
                    ax2 = ax1.twinx()
                    ax2.plot(df['timestamp'], df['carbon_offset_tons'], color='#00FF88', linewidth=3.5, marker='s', markersize=8, label='Carbon Offset (Tons CO2)')
                    ax2.set_ylabel("Tons CO2 Offset", color='#00FF88', fontweight='bold', fontsize=12)
                    plt.title("Live Sustainability & Net-Zero Time-Series Telemetry", fontsize=14, fontweight='bold', color='#00FF88', pad=15)
                    plt.tight_layout()
                    safe_plot_show('interactive_sust_chart.png')
                elif chart_type == 'arch':
                    if os.path.exists('db_architecture_graph.png'):
                        from IPython.display import Image
                        display(Image('db_architecture_graph.png', width=1100))
                    else:
                        print("Run `python nexus_stadium_db_lab.py` to generate the architecture schematic chart!")

        def run_ai_query(self, b):
            with self.ai_output:
                clear_output(wait=True)
                lang = self.lang_dropdown.value
                prompt = self.query_input.value
                df = pd.read_sql("SELECT * FROM genai_knowledge_graph;", self.conn)
                
                # Multi-Lingual Semantic Keyword Overlap Scoring Engine
                p_low = prompt.lower()
                best_score = -1
                best_row = df.iloc[0]
                
                for idx, row in df.iterrows():
                    keywords = [k.strip().lower() for k in str(row['trigger_keywords']).split(',')]
                    score = sum(2 if kw in p_low else 1 for kw in keywords if len(kw) > 2 and kw in p_low)
                    # Check intent category direct mention
                    if row['intent_category'].lower() in p_low:
                        score += 3
                    if score > best_score:
                        best_score = score
                        best_row = row

                lang_col = f"response_{lang}"
                response_text = best_row[lang_col] if lang_col in best_row and pd.notna(best_row[lang_col]) else best_row['response_en']
                
                print(f"[GenAI Intent Router | Language: {self.lang_dropdown.label} | Intent: {best_row['intent_category'].upper()} | Confidence Match Score: {max(best_score, 1)}/10]")
                print(f"🤖 RESPONSE ({lang.upper()}): {response_text}")
                print(f"⚡ ACTION HOOK: `{best_row['action_code']}`")
                
                # Display localized action context
                print(f"\n--- Database Rule Record (`genai_knowledge_graph` | ID: {best_row['rule_id']}) ---")
                display(pd.DataFrame([best_row[['rule_id', 'intent_category', 'action_code', lang_col]]]))

    # Launch dashboard instance
    dashboard = InteractiveNexusDashboard(conn)

except ImportError:
    print("Note: ipywidgets is not installed or active in non-interactive CLI mode. Please run this script inside Jupyter Notebook (`.ipynb`) to use the rich interactive UI widgets!")

# %% [markdown]
# ---
# ## Block 3: Option to Embed Full-Screen Web HTML Dashboard inside Jupyter Cell
# If you want to interact directly with our high-tech HTML/JS visual dashboard right inside your notebook cell, run this block!

# %%
try:
    import html
    from IPython.display import display, HTML
    if os.path.exists("architecture_dashboard.html"):
        print("[Block 3 Verification] Displaying standalone interactive web HTML dashboard inside Jupyter cell (Bypassing token login via memory srcdoc):")
        with open("architecture_dashboard.html", "r", encoding="utf-8") as f:
            html_content = f.read()
        safe_html = html.escape(html_content, quote=True)
        display(HTML(f'<iframe srcdoc="{safe_html}" width="100%" height="880px" style="border:none; border-radius:12px; box-shadow: 0 0 20px rgba(0,240,255,0.3);"></iframe>'))
    else:
        print("Note: `architecture_dashboard.html` not found in current directory.")
except Exception as e:
    print(f"Unable to embed HTML dashboard: {e}")
