/**
 * Nexus 2026 - FIFA World Cup Smart Stadium AI Engine
 * Generative AI Intelligence Core, Voice Speech Synthesis, and Autonomous Operations Simulator
 * Built for PromptWars Virtual Challenge 4
 */

class SmartStadiumAIEngine {
    constructor() {
        this.currentLanguage = 'en';
        this.isVoiceEnabled = true;
        this.speechSynth = window.speechSynthesis || null;
        this.activeSimulators = [];
        this.incidentHistory = [...SIMULATION_DATA.incidents];
        this.isSimulating = true;
        this.onStateChangeCallbacks = [];
    }

    subscribe(callback) {
        if (typeof callback === 'function') {
            this.onStateChangeCallbacks.push(callback);
        }
    }

    notifyStateChange(eventType, data) {
        this.onStateChangeCallbacks.forEach(cb => cb(eventType, data));
    }

    setLanguage(langCode) {
        if (SIMULATION_DATA.multilingualGreetings[langCode]) {
            this.currentLanguage = langCode;
            this.notifyStateChange('language_changed', langCode);
            return SIMULATION_DATA.multilingualGreetings[langCode];
        }
        return SIMULATION_DATA.multilingualGreetings['en'];
    }

    /**
     * Synthesize speech for multi-lingual audio assistance
     */
    speak(text, lang = this.currentLanguage) {
        if (!this.isVoiceEnabled || !this.speechSynth) return;
        
        // Cancel ongoing speech
        this.speechSynth.cancel();

        const utterance = new SpeechSynthesisUtterance(text);
        const langMap = {
            'en': 'en-US',
            'es': 'es-ES',
            'fr': 'fr-FR',
            'pt': 'pt-BR',
            'de': 'de-DE',
            'ar': 'ar-SA',
            'ja': 'ja-JP',
            'ko': 'ko-KR'
        };
        utterance.lang = langMap[lang] || 'en-US';
        utterance.rate = 1.05;
        utterance.pitch = 1.0;

        // Try to pick a natural voice if available
        const voices = this.speechSynth.getVoices();
        const matchedVoice = voices.find(v => v.lang.startsWith(utterance.lang.substring(0, 2)));
        if (matchedVoice) {
            utterance.voice = matchedVoice;
        }

        this.speechSynth.speak(utterance);
    }

    stopSpeaking() {
        if (this.speechSynth) {
            this.speechSynth.cancel();
        }
    }

    /**
     * Simulate GenAI Neural Processing and Streaming Output
     */
    async simulateGenAIResponse(promptText, onChunkReceived, onComplete) {
        const query = promptText.toLowerCase();
        let responseObj = {
            title: "GenAI Operational & Fan Assistance Analysis",
            content: "",
            actions: [],
            telemetry: { confidence: "99.4%", processingTime: "142 ms", model: "Nexus-GenAI-2026-V4" }
        };

        // Intent detection
        if (query.includes("gate") || query.includes("crowd") || query.includes("enter") || query.includes("queue") || query.includes("wait") || query.includes("sector")) {
            responseObj.title = "🚀 Real-Time Crowd Flow & Optimal Route Plan";
            responseObj.content = `### Optimal Stadium Navigation Recommendation\n\nBased on live thermal camera and turnstile IoT sensor feeds across **MetLife Stadium**:\n\n* **⚠️ High Bottleneck Detected:** South Gate C is experiencing high influx from metro rail (Wait: **26 mins** | Density: **91%**).\n* **✅ Recommended Express Entry:** Divert via **West Gate D** (Wait: **4 mins** | Density: **31%**).\n* **🧭 Inside Concourse Route:** Take **Express Corridor W-12** directly into Sector 112/118. This avoids the crowded food plaza and saves approximately **19 minutes** of walking time.\n\n**💡 GenAI Proactive Tip:** If you require elevator access, Elevator E2 at West Gate D has zero waiting time right now and is prioritized for accessible ticketholders.`;
            responseObj.actions = [
                { label: "🗺️ Highlight Route on 3D Map", action: "highlight_route_west" },
                { label: "📱 Send Route to Mobile Wallet", action: "send_mobile_wallet" },
                { label: "♿ Request VIP Volunteer Escort", action: "request_escort" }
            ];
        } else if (query.includes("wheelchair") || query.includes("access") || query.includes("sensory") || query.includes("quiet") || query.includes("disabled") || query.includes("ada")) {
            responseObj.title = "♿ Comprehensive Accessibility & Inclusion Assistant";
            responseObj.content = `### Personalized Barrier-Free Tournament Plan\n\nAt **FIFA World Cup 2026**, our stadium is fully optimized for universal accessibility:\n\n1. **Priority Zero-Wait Gates:** North Gate A and West Gate D feature dedicated **ADA Express lanes** with motorized shuttle carts available right upon arrival.\n2. **Sensory Quiet Rooms:** Located at **North Zone 25** (adjacent to the Central Medical Hub). Featuring soundproof acoustic walls, adjustable circadian lighting, and relaxation pods. Currently **4 pods are open**.\n3. **Elevator Health Status:** All 16 elevators are operational. Elevator E2 and E6 have reserved priority status right now.\n4. **Assistive Listening & Audio Description:** Live AI-generated multi-lingual match commentary and audio descriptions can be streamed directly to your Bluetooth headphones via this app.`;
            responseObj.actions = [
                { label: "🎧 Enable Live Audio Description", action: "enable_audio_desc" },
                { label: "🛋️ Reserve Sensory Room Pod #3", action: "reserve_sensory_pod" },
                { label: "🚨 Call Mobile Accessibility Shuttle", action: "call_shuttle" }
            ];
        } else if (query.includes("food") || query.includes("drink") || query.includes("concession") || query.includes("halal") || query.includes("vegan") || query.includes("order")) {
            responseObj.title = "🍔 AI Zero-Wait Concessions & Dietary Guide";
            responseObj.content = `### Smart Culinary & Express Pickup Recommendations\n\nOur GenAI inventory system monitors wait times across all 120 food stalls in real-time:\n\n* **🌱 Certified Halal & Vegan Hub:** **Global Gourmet Sector 108** (Wait: **2 mins**). Fresh Mediterranean bowls, halal grilled skewers, and plant-based tacos.\n* **⚡ Zero-Wait Smart Lockers:** Order via app now and pick up from heated locker **Bank B4** near Section 115 in exactly 6 minutes without standing in line.\n* **🥤 Hydration Stations:** Free cold filtered water refilling stations are active at every corner sector (North, South, East, West).`;
            responseObj.actions = [
                { label: "📦 Place Express Order (Locker B4)", action: "place_express_order" },
                { label: "🗺️ Show Halal/Vegan Stalls on Map", action: "show_food_map" }
            ];
        } else if (query.includes("sustain") || query.includes("solar") || query.includes("carbon") || query.includes("energy") || query.includes("green") || query.includes("eco")) {
            responseObj.title = "🌱 Live Sustainability & Carbon Neutrality Telemetry";
            responseObj.content = `### Real-Time Environmental Impact Analysis\n\nThis stadium operates as a net-zero AI microgrid during **FIFA World Cup 2026**:\n\n* **☀️ Solar Canopy Output:** Generating **34,820 kWh** today, powering 84% of stadium operations including concourse lighting and broadcast servers.\n* **❄️ AI-Optimized HVAC:** By dynamically adjusting ventilation based on real-time crowd density heatmaps, we have reduced cooling energy consumption by **18.4%**.\n* **💧 Rainwater Recycling:** **42,500 Liters** collected and filtered for pitch irrigation and smart restrooms.\n* **♻️ Zero-Waste to Landfill:** **94.2%** compost and recycling diversion rate achieved across all gates today!`;
            responseObj.actions = [
                { label: "📊 View Operations Energy Dashboard", action: "open_command_center" },
                { label: "🏆 Claim Green Fan Carbon Badge", action: "claim_green_badge" }
            ];
        } else if (query.includes("shuttle") || query.includes("transit") || query.includes("train") || query.includes("parking") || query.includes("leave") || query.includes("bus")) {
            responseObj.title = "🚌 Autonomous Transit & Post-Match Evacuation Plan";
            responseObj.content = `### Smart Departure & Autonomous Shuttle Booking\n\nTo ensure a seamless, congestion-free exit after the final whistle:\n\n* **🤖 Autonomous EV Shuttle Fleet:** 18 autonomous electric shuttles are currently docked at **Shuttle Terminal S1** (South Plaza).\n* **🚅 Metro Rail Frequency Check:** NJ Transit express trains depart every **4 minutes**. Next train capacity: **68% available**.\n* **💡 AI Tip:** Leaving via **Gate D** 10 minutes before or 15 minutes after peak final whistle ensures a **zero-traffic departure experience**.`;
            responseObj.actions = [
                { label: "🎟️ Reserve Autonomous Shuttle Seat", action: "reserve_shuttle" },
                { label: "🗺️ Route to Shuttle Hub S1", action: "route_shuttle_hub" }
            ];
        } else {
            responseObj.title = "🧠 GenAI Stadium Operational Intelligence";
            responseObj.content = `### Comprehensive AI Analysis for "${promptText}"\n\nOur **Nexus GenAI 2026** engine has synthesized your query across our 4,820 live IoT stadium sensors:\n\n* **Current Stadium Status:** USA vs Brazil (Group A Quarterfinal) is currently live (62' minute). Attendance: **81,240 fans (98.5%)**.\n* **Concourse Traffic:** North and West concourses are flowing smoothly (**31% density**), while South Concourse food court is experiencing elevated activity (**88% density**).\n* **Operational Command:** First Aid, Accessibility Concierge, and Security Command are fully staffed and running at peak response efficiency (< 3 min response SLA).\n\nHow else can I assist your tournament experience today?`;
            responseObj.actions = [
                { label: "🗺️ Open Interactive 3D Stadium Map", action: "open_stadium_map" },
                { label: "⚡ Switch to Operations Command Center", action: "open_command_center" },
                { label: "📢 Speak AI Summary", action: "speak_summary" }
            ];
        }

        // Simulate streaming chunks
        const fullText = responseObj.content;
        const words = fullText.split(' ');
        let currentText = "";
        
        for (let i = 0; i < words.length; i++) {
            currentText += (i === 0 ? "" : " ") + words[i];
            if (onChunkReceived && typeof onChunkReceived === 'function') {
                onChunkReceived({
                    title: responseObj.title,
                    content: currentText,
                    isStreaming: i < words.length - 1,
                    telemetry: responseObj.telemetry
                });
            }
            // Add slight natural delay between word chunks
            await new Promise(r => setTimeout(r, Math.floor(Math.random() * 25) + 12));
        }

        if (onComplete && typeof onComplete === 'function') {
            onComplete(responseObj);
        }

        // Auto speak if voice mode is on
        if (this.isVoiceEnabled) {
            // Speak a concise summary instead of reading the full markdown
            const cleanText = responseObj.content.replace(/[*#>`]/g, '').split('\n').filter(Boolean)[0] || responseObj.title;
            this.speak(cleanText);
        }

        return responseObj;
    }

    /**
     * Start Autonomous Stadium Operations Simulator
     * Periodically generates live sensor events, crowd diversion actions, and incident alerts
     */
    startAutonomousOrchestrator() {
        if (!this.isSimulating) return;

        const intervalId = setInterval(() => {
            if (!this.isSimulating) return;

            // Generate a random operational event or sensor fluctuation
            const eventTypes = ['gate_fluctuation', 'new_incident', 'energy_optimization', 'crowd_diversion_success'];
            const chosenType = eventTypes[Math.floor(Math.random() * eventTypes.length)];

            if (chosenType === 'gate_fluctuation') {
                // Fluctuating wait times at Gate B and C
                const gateB = SIMULATION_DATA.gates.find(g => g.id === 'gate_b');
                if (gateB) {
                    const delta = (Math.random() > 0.5 ? 1 : -1) * Math.floor(Math.random() * 4 + 1);
                    gateB.density = Math.max(30, Math.min(95, gateB.density + delta));
                    gateB.waitTime = `${Math.floor(gateB.density * 0.22)} mins`;
                    this.notifyStateChange('gate_updated', gateB);
                }
            } else if (chosenType === 'new_incident' && Math.random() > 0.6) {
                const newInc = {
                    id: `inc_${Math.floor(Math.random() * 899 + 100)}`,
                    timestamp: new Date().toLocaleTimeString('en-US', { hour12: false }) + ' EST',
                    severity: Math.random() > 0.6 ? 'HIGH' : 'MEDIUM',
                    category: 'Automated Crowd Load Balancing',
                    location: 'Concourse West Sector 124 Turnstile Bank',
                    description: 'IoT turnstile sensor detected momentary surge in concourse pedestrian flow.',
                    aiAction: 'Autonomous turnstile directional reversal triggered. Digital signage updated to redirect fans to Sector 118 Express Gate.',
                    status: 'AUTOMATED',
                    timeSaved: '7 mins bottleneck avoided'
                };
                this.incidentHistory.unshift(newInc);
                if (this.incidentHistory.length > 12) this.incidentHistory.pop();
                this.notifyStateChange('incident_added', newInc);
            } else if (chosenType === 'energy_optimization') {
                // Update solar output slightly
                const baseVal = 34820 + Math.floor(Math.random() * 300 - 150);
                SIMULATION_DATA.sustainabilityMetrics.solarPowerGenerated = `${baseVal.toLocaleString()} kWh`;
                this.notifyStateChange('sustainability_updated', SIMULATION_DATA.sustainabilityMetrics);
            }
        }, 5000);

        this.activeSimulators.push(intervalId);
    }

    stopOrchestrator() {
        this.isSimulating = false;
        this.activeSimulators.forEach(id => clearInterval(id));
        this.activeSimulators = [];
    }
}

// Global instance
const AI_ENGINE = new SmartStadiumAIEngine();
if (typeof module !== 'undefined') {
    module.exports = AI_ENGINE;
}
