/**
 * Nexus 2026 - FIFA World Cup Smart Stadium & Tournament Operations Suite
 * Comprehensive Simulation Data & Knowledge Graph
 * Built for PromptWars Virtual Challenge 4
 */

const SIMULATION_DATA = {
    matches: [
        {
            id: "match_01",
            title: "USA vs Brazil - Group A Quarterfinal",
            stadium: "MetLife Stadium (New York / New Jersey)",
            date: "June 24, 2026 - 19:30 EST",
            attendance: "81,240 / 82,500 (98.5% Capacity)",
            status: "LIVE - 62' Minute (2 - 1)",
            weather: "74°F / Clear / Humidity 52%",
            energySource: "84% On-site Solar & Microgrid",
            securityLevel: "Level 2 (High Readiness)"
        },
        {
            id: "match_02",
            title: "Mexico vs Germany - Group B Semifinal",
            stadium: "Estadio Azteca (Mexico City)",
            date: "July 02, 2026 - 18:00 CST",
            attendance: "86,400 / 87,523 (98.7% Capacity)",
            status: "Pre-Match - Gates Open (Crowd Influx High)",
            weather: "68°F / Mostly Cloudy / Humidity 45%",
            energySource: "91% Renewable Grid & Geothermal",
            securityLevel: "Level 1 (Standard Operations)"
        },
        {
            id: "match_03",
            title: "Canada vs France - Group C Knockout",
            stadium: "BMO Field (Toronto)",
            date: "June 28, 2026 - 20:00 EST",
            attendance: "44,800 / 45,000 (99.5% Capacity)",
            status: "Halftime Break (Concourse Peak Load)",
            weather: "65°F / Gentle Breeze / Humidity 60%",
            energySource: "100% Hydroelectric & Wind",
            securityLevel: "Level 1 (Standard Operations)"
        }
    ],

    gates: [
        { id: "gate_a", name: "North Gate A (Main VIP & Media)", status: "optimal", density: 24, waitTime: "3 mins", throughput: "1,420 fans/hr", accessibility: "100% ADA Express Lanes Active", recommendation: "Optimal flow. Direct fans from East plaza." },
        { id: "gate_b", name: "East Gate B (General Admission)", status: "warning", density: 72, waitTime: "14 mins", throughput: "3,890 fans/hr", accessibility: "ADA Elevator B2 Under High Load", recommendation: "Open overflow turnstiles 12-16. Dispatch AI wayfinding bots." },
        { id: "gate_c", name: "South Gate C (Transit & Metro Hub)", status: "critical", density: 91, waitTime: "26 mins", throughput: "4,950 fans/hr", accessibility: "Assisted Shuttle Required", recommendation: "CRITICAL: Divert incoming metro passengers to West Gate D via dynamic LED signs & app push alerts." },
        { id: "gate_d", name: "West Gate D (Family & Accessibility Hub)", status: "optimal", density: 31, waitTime: "4 mins", throughput: "1,850 fans/hr", accessibility: "Zero Wait Priority Access", recommendation: "Maintain standard screening protocol." },
        { id: "gate_vip", name: "FIFA Delegation & VIP Gate E", status: "optimal", density: 12, waitTime: "1 min", throughput: "420 guests/hr", accessibility: "Private Concierge Active", recommendation: "Ready for Brazil Presidential Delegation arrival." }
    ],

    stadiumZones: [
        { id: "zone_n_concourse", name: "North Upper Concourse", type: "concourse", density: 42, temp: "71°F", airQuality: "AQI 22 (Optimal)", noise: "78 dB", coordinates: { x: 50, y: 15 }, status: "optimal" },
        { id: "zone_s_concourse", name: "South Food Court & Plaza", type: "concourse", density: 88, temp: "76°F", airQuality: "AQI 45 (Moderate)", noise: "92 dB", coordinates: { x: 50, y: 85 }, status: "critical" },
        { id: "zone_e_stands", name: "East Lower Bowl (Sectors 101-118)", type: "seating", density: 96, temp: "73°F", airQuality: "AQI 28 (Good)", noise: "104 dB", coordinates: { x: 85, y: 50 }, status: "warning" },
        { id: "zone_w_stands", name: "West Lower Bowl (Sectors 119-136)", type: "seating", density: 94, temp: "72°F", airQuality: "AQI 25 (Good)", noise: "102 dB", coordinates: { x: 15, y: 50 }, status: "optimal" },
        { id: "zone_vip_suite", name: "Sky Box VIP Lounge & Club", type: "vip", density: 65, temp: "69°F", airQuality: "AQI 15 (Pristine)", noise: "64 dB", coordinates: { x: 30, y: 25 }, status: "optimal" },
        { id: "zone_medical", name: "Central First Aid & Sensory Room", type: "accessibility", density: 18, temp: "70°F", airQuality: "AQI 12 (Pristine)", noise: "42 dB", coordinates: { x: 75, y: 25 }, status: "optimal" },
        { id: "zone_restroom_1", name: "Smart Restroom Cluster S4", type: "amenity", density: 84, temp: "74°F", airQuality: "AQI 58 (Requires Ventilation)", noise: "80 dB", coordinates: { x: 65, y: 80 }, status: "warning" },
        { id: "zone_shuttle_hub", name: "EV Autonomous Shuttle Terminal", type: "transit", density: 38, temp: "73°F", airQuality: "AQI 20 (Optimal)", noise: "68 dB", coordinates: { x: 50, y: 95 }, status: "optimal" }
    ],

    incidents: [
        {
            id: "inc_101",
            timestamp: "19:42:15 EST",
            severity: "HIGH",
            category: "Crowd Bottleneck",
            location: "South Concourse Gate C Plaza",
            description: "Surge of 3,200 fans arriving simultaneously from NJ Transit Metro train. Density at 91%.",
            aiAction: "Diverting 45% of incoming crowd to West Gate D using synchronized digital wayfinding beacons and push notifications in 8 languages.",
            status: "IN_PROGRESS",
            timeSaved: "18 mins average delay mitigated"
        },
        {
            id: "inc_102",
            timestamp: "19:35:00 EST",
            severity: "MEDIUM",
            category: "Accessibility Request",
            location: "East Sector 112 Wheelchair Bay",
            description: "Elevator E4 maintenance sensor reported temporary speed degradation during halftime transition.",
            aiAction: "Rerouted 14 wheelchair guests to VIP Elevator E2 with personal volunteer escort dispatch. Elevator technician dispatched autonomously.",
            status: "RESOLVED",
            timeSaved: "12 mins delay avoided"
        },
        {
            id: "inc_103",
            timestamp: "19:20:10 EST",
            severity: "LOW",
            category: "Sustainability / Energy Optimization",
            location: "North Concourse Lighting & HVAC Grid",
            description: "Ambient natural sunlight sufficient through solar canopy until 20:15 EST.",
            aiAction: "Dimmed LED flood light bank 3 and reduced HVAC cooling load in empty auxiliary zones, saving 1,420 kWh.",
            status: "AUTOMATED",
            timeSaved: "$480 energy cost saved"
        },
        {
            id: "inc_104",
            timestamp: "19:10:05 EST",
            severity: "HIGH",
            category: "Medical / First Aid Dispatch",
            location: "West Stand Sector 128, Row 14",
            description: "Fan reported heat exhaustion symptoms via mobile SOS QR scan.",
            aiAction: "Dispatched nearest paramedic team equipped with cooling kit. Cleared corridor C-12 via automated turnstile lock release.",
            status: "RESOLVED",
            timeSaved: "3 min response time achieved"
        }
    ],

    multilingualGreetings: {
        en: { welcome: "Welcome to FIFA World Cup 2026 Smart Stadium AI", subtitle: "Your personal GenAI guide for real-time navigation, zero-wait concessions, and accessible tournament experiences.", audioIntro: "Welcome to MetLife Stadium! How can I assist your FIFA World Cup experience today?" },
        es: { welcome: "Bienvenido al Estadio Inteligente IA de la Copa Mundial FIFA 2026", subtitle: "Tu guía personal de IA para navegación en tiempo real, sin esperas y accesibilidad total.", audioIntro: "¡Bienvenido al estadio! ¿Cómo puedo ayudarte a disfrutar de la Copa Mundial hoy?" },
        fr: { welcome: "Bienvenue au Stade Intelligent IA - Coupe du Monde FIFA 2026", subtitle: "Votre assistant IA pour une navigation en temps réel et une expérience accessible.", audioIntro: "Bienvenue au stade! Comment puis-je vous aider aujourd'hui?" },
        pt: { welcome: "Bem-vindo ao Estádio Inteligente IA da Copa do Mundo FIFA 2026", subtitle: "Seu assistente IA para navegação inteligente e acesso VIP sem filas.", audioIntro: "Bem-vindo ao estádio! Como posso ajudar na sua experiência na Copa do Mundo?" },
        de: { welcome: "Willkommen im FIFA WM 2026 Smart Stadium KI-Hub", subtitle: "Ihr persönlicher KI-Assistent für Echtzeit-Navigation und barrierefreie Sporterlebnisse.", audioIntro: "Willkommen im Stadion! Wie kann ich Ihnen bei der FIFA Weltmeisterschaft helfen?" },
        ar: { welcome: "مرحباً بكم في الملعب الذكي بالذكاء الاصطناعي لكأس العالم 2026", subtitle: "دليلك الشخصي للتنقل الفوري وتجربة لا تُنسى في الملعب.", audioIntro: "مرحباً بكم في الملعب! كيف يمكنني مساعدتكم اليوم؟" },
        ja: { welcome: "FIFAワールドカップ2026 スマートスタジアム AIへようこそ", subtitle: "リアルタイムナビゲーションと快適な観戦をサポートする専用生成AIガイド。", audioIntro: "スタジアムへようこそ！本日のワールドカップ観戦をどのようにサポートいたしましょうか？" },
        ko: { welcome: "FIFA 월드컵 2026 스마트 스타디움 AI에 오신 것을 환영합니다", subtitle: "실시간 대기시간 안내, 최적의 이동 경로 및 배리어프리 관람을 위한 AI 가이드.", audioIntro: "스타디움에 오신 것을 환영합니다! 오늘 어떤 도움이 필요하신가요?" }
    },

    faqPrompts: [
        {
            category: "Navigation & Crowd Flow",
            question: "What is the fastest way to Sector 112 right now without getting stuck in crowds?",
            answer: "Based on live thermal sensors, South Gate C currently has a 26-minute wait due to metro arrivals. I recommend entering via West Gate D (4-min wait) and taking the inner Express Corridor W. This route saves 19 minutes and offers an air-conditioned pathway directly to Sector 112."
        },
        {
            category: "Accessibility & Inclusion",
            question: "I am using a wheelchair and need to find a sensory quiet room and accessible seating.",
            answer: "We have dedicated ADA accessibility corridors highlighted in green on your live map. Elevator E2 is currently reserved for priority access with zero wait. The Central Sensory Quiet Room is located at North Zone 25 (next to Medical Hub) and has 4 available relaxation pods right now."
        },
        {
            category: "Transportation & Parking",
            question: "How do I book an autonomous EV shuttle after the match to MetLife train station?",
            answer: "Your smart ticket includes complimentary access to our autonomous EV shuttle fleet. Shuttle Hub S1 has 18 vehicles currently docked. I can reserve your seat right now for departure 15 minutes after final whistle to guarantee zero waiting time."
        },
        {
            category: "Concessions & Zero-Wait Ordering",
            question: "Where can I get halal and gluten-free food nearby with the shortest pickup queue?",
            answer: "Global Gourmet Concourse (Section 108) offers certified Halal and Gluten-Free menus. AI queue prediction shows only a 2-minute wait at 'Green Field Bites'. I can place your order now for express QR locker pickup!"
        },
        {
            category: "Sustainability & Carbon Footprint",
            question: "How is the stadium utilizing AI to achieve carbon neutrality during this World Cup match?",
            answer: "Today's USA vs Brazil match is powered 84% by on-site solar canopies and micro-wind turbines. Our GenAI IoT engine dynamically adjusts HVAC cooling based on real-time crowd heatmaps, while our rainwater recovery system has recycled 42,000 liters for pitch irrigation today alone!"
        }
    ],

    sustainabilityMetrics: {
        solarPowerGenerated: "34,820 kWh",
        hvacEnergySaved: "18.4%",
        waterRecycled: "42,500 L",
        wasteDiverted: "94.2%",
        carbonOffsetTons: "128.5 Tons CO2",
        activeSensors: "4,820 IoT Nodes"
    }
};

if (typeof module !== 'undefined') {
    module.exports = SIMULATION_DATA;
}
