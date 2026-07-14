/**
 * Nexus 2026 - FIFA World Cup Smart Stadium & Tournament Operations Suite
 * Master Application Orchestrator & UI Controller
 * Built for PromptWars Virtual Challenge 4
 */

document.addEventListener('DOMContentLoaded', () => {
    initApp();
});

function initApp() {
    renderGates();
    renderStadiumMapNodes('all');
    renderIncidents();
    renderSustainability();
    initEventListeners();
    initMultilingualGreeting();
    
    // Start autonomous simulation orchestrator
    AI_ENGINE.startAutonomousOrchestrator();
    
    // Subscribe to real-time simulation updates
    AI_ENGINE.subscribe((eventType, data) => {
        if (eventType === 'gate_updated') {
            renderGates();
            showToast(`🔄 Gate Telemetry Updated: ${data.name} wait time is now ${data.waitTime}`, 'info');
        } else if (eventType === 'incident_added') {
            renderIncidents();
            showToast(`🚨 New AI Autonomous Action: ${data.category} - ${data.aiAction}`, 'warning');
        } else if (eventType === 'sustainability_updated') {
            renderSustainability();
        } else if (eventType === 'language_changed') {
            updateUILanguage(data);
        }
    });

    console.log("🚀 Nexus 2026 Smart Stadium AI Core initialized successfully.");
}

/**
 * Event Listeners Initialization
 */
function initEventListeners() {
    // Mode Switcher (Fan Mode vs Command Center Mode)
    const modeBtns = document.querySelectorAll('.mode-btn');
    modeBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            modeBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const mode = btn.getAttribute('data-mode');
            if (mode === 'command') {
                document.body.classList.add('command-center-mode');
                switchTab('tab-ops');
                showToast("⚡ Switched to Operations Command Center Deck - Full IoT Telemetry Active", "primary");
            } else {
                document.body.classList.remove('command-center-mode');
                switchTab('tab-map');
                showToast("👋 Switched to Fan Navigation & VIP Concierge Mode", "primary");
            }
        });
    });

    // Tab Navigation
    const tabBtns = document.querySelectorAll('.tab-btn');
    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const tabId = btn.getAttribute('data-tab');
            switchTab(tabId);
        });
    });

    // Language Selector
    const langSelect = document.getElementById('lang-selector');
    if (langSelect) {
        langSelect.addEventListener('change', (e) => {
            const greeting = AI_ENGINE.setLanguage(e.target.value);
            // Append language welcome message to chat
            appendAIMessage(`🌐 **${greeting.welcome}**\n\n${greeting.subtitle}`, []);
            if (AI_ENGINE.isVoiceEnabled && greeting.audioIntro) {
                AI_ENGINE.speak(greeting.audioIntro);
            }
        });
    }

    // Voice Toggle
    const voiceToggle = document.getElementById('voice-toggle');
    if (voiceToggle) {
        voiceToggle.addEventListener('click', () => {
            AI_ENGINE.isVoiceEnabled = !AI_ENGINE.isVoiceEnabled;
            if (AI_ENGINE.isVoiceEnabled) {
                voiceToggle.classList.remove('muted');
                voiceToggle.innerHTML = '🔊';
                showToast("🔊 Live AI Voice Assistance & Multi-Lingual Speech Enabled", "success");
            } else {
                voiceToggle.classList.add('muted');
                voiceToggle.innerHTML = '🔇';
                AI_ENGINE.stopSpeaking();
                showToast("🔇 AI Voice Assistance Muted", "warning");
            }
        });
    }

    // Map Filter Buttons
    const filterBtns = document.querySelectorAll('.map-filter-btn');
    filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            filterBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            const filter = btn.getAttribute('data-filter');
            renderStadiumMapNodes(filter);
        });
    });

    // AI Chat Input Submission
    const aiForm = document.getElementById('ai-input-form');
    const aiInput = document.getElementById('ai-input-field');
    if (aiForm && aiInput) {
        aiForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const prompt = aiInput.value.trim();
            if (!prompt) return;
            aiInput.value = '';
            
            appendUserMessage(prompt);
            await processAIQuery(prompt);
        });
    }

    // Quick Prompts Chips
    const promptChips = document.querySelectorAll('.prompt-chip');
    promptChips.forEach(chip => {
        chip.addEventListener('click', async () => {
            const prompt = chip.getAttribute('data-prompt') || chip.innerText;
            appendUserMessage(prompt);
            await processAIQuery(prompt);
        });
    });
}

function switchTab(tabId) {
    document.querySelectorAll('.tab-btn').forEach(b => {
        b.classList.toggle('active', b.getAttribute('data-tab') === tabId);
    });
    document.querySelectorAll('.tab-panel').forEach(p => {
        p.classList.toggle('active', p.id === tabId);
    });
}

/**
 * AI Chat UI & Query Processing
 */
async function processAIQuery(promptText) {
    const chatBody = document.getElementById('ai-chat-body');
    if (!chatBody) return;

    // Create streaming AI bubble container
    const bubbleId = 'ai_bubble_' + Date.now();
    const bubbleDiv = document.createElement('div');
    bubbleDiv.className = 'msg-bubble msg-ai';
    bubbleDiv.id = bubbleId;
    bubbleDiv.innerHTML = `<h3 id="${bubbleId}_title">🧠 Processing Telemetry...</h3><div id="${bubbleId}_content">Searching 4,820 live stadium sensors and GenAI knowledge graph...</div>`;
    chatBody.appendChild(bubbleDiv);
    chatBody.scrollTop = chatBody.scrollHeight;

    // Stream response
    await AI_ENGINE.simulateGenAIResponse(
        promptText,
        (chunk) => {
            const titleEl = document.getElementById(`${bubbleId}_title`);
            const contentEl = document.getElementById(`${bubbleId}_content`);
            if (titleEl) titleEl.innerText = chunk.title;
            if (contentEl) contentEl.innerHTML = markedOrFormatText(chunk.content);
            chatBody.scrollTop = chatBody.scrollHeight;
        },
        (completed) => {
            const contentEl = document.getElementById(`${bubbleId}_content`);
            if (contentEl) contentEl.innerHTML = markedOrFormatText(completed.content);
            
            // Add action buttons
            if (completed.actions && completed.actions.length > 0) {
                const actionsDiv = document.createElement('div');
                actionsDiv.className = 'ai-action-buttons';
                completed.actions.forEach(act => {
                    const btn = document.createElement('button');
                    btn.className = 'ai-action-btn';
                    btn.innerHTML = act.label;
                    btn.addEventListener('click', () => triggerAIAction(act.action, act.label));
                    actionsDiv.appendChild(btn);
                });
                bubbleDiv.appendChild(actionsDiv);
            }

            // Add telemetry footer
            if (completed.telemetry) {
                const telDiv = document.createElement('div');
                telDiv.className = 'ai-telemetry';
                telDiv.innerHTML = `<span>⚡ Confidence: ${completed.telemetry.confidence}</span><span>Model: ${completed.telemetry.model} (${completed.telemetry.processingTime})</span>`;
                bubbleDiv.appendChild(telDiv);
            }
            chatBody.scrollTop = chatBody.scrollHeight;
        }
    );
}

function appendUserMessage(text) {
    const chatBody = document.getElementById('ai-chat-body');
    if (!chatBody) return;
    const div = document.createElement('div');
    div.className = 'msg-bubble msg-user';
    div.innerText = text;
    chatBody.appendChild(div);
    chatBody.scrollTop = chatBody.scrollHeight;
}

function appendAIMessage(markdownText, actions = []) {
    const chatBody = document.getElementById('ai-chat-body');
    if (!chatBody) return;
    const div = document.createElement('div');
    div.className = 'msg-bubble msg-ai';
    div.innerHTML = markedOrFormatText(markdownText);
    
    if (actions && actions.length > 0) {
        const actionsDiv = document.createElement('div');
        actionsDiv.className = 'ai-action-buttons';
        actions.forEach(act => {
            const btn = document.createElement('button');
            btn.className = 'ai-action-btn';
            btn.innerHTML = act.label;
            btn.addEventListener('click', () => triggerAIAction(act.action, act.label));
            actionsDiv.appendChild(btn);
        });
        div.appendChild(actionsDiv);
    }

    chatBody.appendChild(div);
    chatBody.scrollTop = chatBody.scrollHeight;
}

function triggerAIAction(actionCode, label) {
    switch (actionCode) {
        case 'highlight_route_west':
            switchTab('tab-map');
            highlightMapRoute('zone_w_stands');
            showToast("🧭 Express Route to West Gate D & Sector 112 highlighted on Interactive Map!", "success");
            break;
        case 'send_mobile_wallet':
            showToast("📱 Express Navigation Pass & VIP Turnstile QR sent to your Apple/Google Wallet!", "success");
            break;
        case 'request_escort':
            showToast("♿ Accessibility Volunteer Escort #42 dispatched to your GPS location (ETA: 2 mins)", "primary");
            break;
        case 'enable_audio_desc':
            if (!AI_ENGINE.isVoiceEnabled) {
                document.getElementById('voice-toggle')?.click();
            }
            AI_ENGINE.speak("Live audio description for USA versus Brazil is now streaming to your headphones. USA just won a corner kick on the right flank.");
            showToast("🎧 Live Multi-Lingual Audio Commentary & Description Stream Active", "success");
            break;
        case 'reserve_sensory_pod':
            showToast("🛋️ Sensory Quiet Room Relaxation Pod #3 reserved under your Smart Ticket ID for 45 minutes.", "success");
            break;
        case 'place_express_order':
            showToast("📦 Halal & Gluten-Free Combo #2 ordered! Your code is LOCKER-B4-889. Zero queue waiting!", "success");
            break;
        case 'open_command_center':
            document.querySelector('.mode-btn[data-mode="command"]')?.click();
            break;
        case 'open_stadium_map':
            switchTab('tab-map');
            break;
        case 'speak_summary':
            AI_ENGINE.speak("Current stadium status: 81,240 fans in attendance. North and West concourses have optimal flow. South gate congestion is being actively diverted by our Gen AI engine.");
            showToast("📢 Speaking Stadium Operational Summary...", "info");
            break;
        default:
            showToast(`✅ Action Executed: ${label}`, "success");
    }
}

/**
 * Render Interactive SVG Stadium Map Nodes
 */
function renderStadiumMapNodes(filter = 'all') {
    const svgGroup = document.getElementById('map-nodes-group');
    const detailsCard = document.getElementById('zone-details-card');
    if (!svgGroup) return;

    svgGroup.innerHTML = '';
    const filteredZones = SIMULATION_DATA.stadiumZones.filter(z => filter === 'all' || z.type === filter);

    filteredZones.forEach(zone => {
        const g = document.createElementNS("http://www.w3.org/2000/svg", "g");
        g.setAttribute("class", "map-zone-node");
        g.setAttribute("transform", `translate(${zone.coordinates.x * 6.5}, ${zone.coordinates.y * 4.8})`);

        let color = '#00FF88';
        if (zone.status === 'warning') color = '#FFB800';
        if (zone.status === 'critical') color = '#FF3366';
        if (zone.type === 'vip') color = '#BD00FF';

        // Outer glow circle
        const circle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        circle.setAttribute("r", "16");
        circle.setAttribute("fill", color);
        circle.setAttribute("opacity", "0.25");

        // Inner node
        const innerCircle = document.createElementNS("http://www.w3.org/2000/svg", "circle");
        innerCircle.setAttribute("r", "8");
        innerCircle.setAttribute("fill", color);
        innerCircle.setAttribute("stroke", "#FFF");
        innerCircle.setAttribute("stroke-width", "2");

        // Text label
        const text = document.createElementNS("http://www.w3.org/2000/svg", "text");
        text.setAttribute("x", "22");
        text.setAttribute("y", "5");
        text.setAttribute("fill", "#F0F4FF");
        text.setAttribute("font-family", "Outfit, sans-serif");
        text.setAttribute("font-size", "13");
        text.setAttribute("font-weight", "700");
        text.textContent = zone.name.split(' ')[0] + ' ' + (zone.name.split(' ')[1] || '');

        g.appendChild(circle);
        g.appendChild(innerCircle);
        g.appendChild(text);

        g.addEventListener('click', () => {
            selectMapZone(zone);
        });

        svgGroup.appendChild(g);
    });

    // Auto select first zone if details card is empty
    if (filteredZones.length > 0 && detailsCard) {
        selectMapZone(filteredZones[0]);
    }
}

function selectMapZone(zone) {
    const card = document.getElementById('zone-details-card');
    if (!card) return;

    let statusText = `<span class="stat-value status-optimal">● OPTIMAL FLOW (${zone.density}%)</span>`;
    if (zone.status === 'warning') statusText = `<span class="stat-value status-warning">● MODERATE CROWD (${zone.density}%)</span>`;
    if (zone.status === 'critical') statusText = `<span class="stat-value status-critical">● CRITICAL BOTTLENECK (${zone.density}%)</span>`;

    card.innerHTML = `
        <h3>📍 ${zone.name}</h3>
        <div class="stat-row">
            <span class="stat-label">Crowd Density Level:</span>
            ${statusText}
        </div>
        <div class="stat-row">
            <span class="stat-label">Zone Category:</span>
            <span class="stat-value" style="text-transform: uppercase; color: var(--color-primary);">${zone.type}</span>
        </div>
        <div class="stat-row">
            <span class="stat-label">Ambient Temperature:</span>
            <span class="stat-value">${zone.temp}</span>
        </div>
        <div class="stat-row">
            <span class="stat-label">Air Quality Index (AQI):</span>
            <span class="stat-value">${zone.airQuality}</span>
        </div>
        <div class="stat-row">
            <span class="stat-label">Acoustic Level:</span>
            <span class="stat-value">${zone.noise}</span>
        </div>
        <div class="ai-recommendation-box" style="margin-top: 0.8rem;">
            <span>🤖</span>
            <span><strong>AI Operational Guidance:</strong> ${zone.status === 'critical' ? 'Automated turnstile diversion active. Diverting fans to West concourse express lanes.' : 'Crowd flow normal. Sensory quiet rooms nearby are open and available.'}</span>
        </div>
        <button class="btn-primary" style="margin-top: 1rem;" onclick="appendUserMessage('Get directions to ${zone.name}'); processAIQuery('Get directions to ${zone.name}');">🧭 Navigate Here with AI Wayfinder</button>
    `;
}

function highlightMapRoute(zoneId) {
    const zone = SIMULATION_DATA.stadiumZones.find(z => z.id === zoneId) || SIMULATION_DATA.stadiumZones[3];
    selectMapZone(zone);
}

/**
 * Render Gates Telemetry Grid
 */
function renderGates() {
    const grid = document.getElementById('gates-grid-container');
    if (!grid) return;

    grid.innerHTML = '';
    SIMULATION_DATA.gates.forEach(gate => {
        const card = document.createElement('div');
        card.className = `glass-panel gate-card ${gate.status}`;
        
        let badgeClass = 'optimal';
        let badgeText = '● Optimal Flow';
        if (gate.status === 'warning') { badgeClass = 'warning'; badgeText = '▲ Moderate Queue'; }
        if (gate.status === 'critical') { badgeClass = 'critical'; badgeText = '🔴 Bottleneck Surge'; }

        card.innerHTML = `
            <div class="gate-header">
                <div>
                    <h4>${gate.name}</h4>
                    <span style="font-size: 0.82rem; color: var(--color-text-dim);">Throughput: ${gate.throughput}</span>
                </div>
                <span class="gate-badge ${badgeClass}">${badgeText}</span>
            </div>
            <div>
                <div style="display: flex; justify-content: space-between; font-size: 0.85rem; font-family: var(--font-mono);">
                    <span>Wait Time: <strong style="color: #FFF;">${gate.waitTime}</strong></span>
                    <span>Density: <strong style="color: #FFF;">${gate.density}%</strong></span>
                </div>
                <div class="progress-container">
                    <div class="progress-bar ${gate.status}" style="width: ${gate.density}%;"></div>
                </div>
            </div>
            <div style="font-size: 0.82rem; color: #CBD5E1; background: rgba(255,255,255,0.03); padding: 0.6rem; border-radius: 6px;">
                ♿ <strong>Accessibility:</strong> ${gate.accessibility}
            </div>
            <div class="ai-recommendation-box">
                <span>⚡</span>
                <span><strong>GenAI Action:</strong> ${gate.recommendation}</span>
            </div>
        `;
        grid.appendChild(card);
    });
}

/**
 * Render Operations Command Center Incidents Log
 */
function renderIncidents() {
    const container = document.getElementById('incidents-log-container');
    if (!container) return;

    container.innerHTML = '';
    AI_ENGINE.incidentHistory.forEach(inc => {
        const item = document.createElement('div');
        item.className = 'incident-item';
        item.innerHTML = `
            <div class="incident-top">
                <span class="inc-title">${inc.category} — <span style="color: var(--color-text-dim); font-weight: 400;">${inc.location}</span></span>
                <span class="inc-severity ${inc.severity}">${inc.severity} PRIORITY</span>
            </div>
            <p style="font-size: 0.85rem; color: #CBD5E1;">${inc.description}</p>
            <div class="inc-ai-action">
                🤖 <strong>Autonomous GenAI Resolution:</strong> ${inc.aiAction}
            </div>
            <div style="display: flex; justify-content: space-between; font-size: 0.75rem; font-family: var(--font-mono); color: var(--color-text-dim);">
                <span>⏱️ Logged at: ${inc.timestamp}</span>
                <span style="color: var(--color-success);">✔ ${inc.timeSaved}</span>
            </div>
        `;
        container.appendChild(item);
    });
}

/**
 * Render Sustainability & Net-Zero Dashboard
 */
function renderSustainability() {
    const solarEl = document.getElementById('kpi-solar');
    const hvacEl = document.getElementById('kpi-hvac');
    const waterEl = document.getElementById('kpi-water');
    const carbonEl = document.getElementById('kpi-carbon');

    if (solarEl) solarEl.innerText = SIMULATION_DATA.sustainabilityMetrics.solarPowerGenerated;
    if (hvacEl) hvacEl.innerText = SIMULATION_DATA.sustainabilityMetrics.hvacEnergySaved;
    if (waterEl) waterEl.innerText = SIMULATION_DATA.sustainabilityMetrics.waterRecycled;
    if (carbonEl) carbonEl.innerText = SIMULATION_DATA.sustainabilityMetrics.carbonOffsetTons;
}

/**
 * Multilingual Greeting Initialization
 */
function initMultilingualGreeting() {
    const greeting = SIMULATION_DATA.multilingualGreetings['en'];
    appendAIMessage(`🌟 **${greeting.welcome}**\n\n${greeting.subtitle}\n\nAsk me anything or click one of the quick action buttons below!`, [
        { label: "🗺️ Fastest Route to Sector 112", action: "highlight_route_west" },
        { label: "🍔 Zero-Wait Concessions Order", action: "place_express_order" },
        { label: "♿ Request Sensory Quiet Room", action: "reserve_sensory_pod" }
    ]);
}

function updateUILanguage(langCode) {
    const greeting = SIMULATION_DATA.multilingualGreetings[langCode] || SIMULATION_DATA.multilingualGreetings['en'];
    showToast(`🌐 Language updated to ${langCode.toUpperCase()}`, 'info');
}

/**
 * Simple Markdown Parser / Formatter helper
 */
function markedOrFormatText(text) {
    if (!text) return '';
    return text
        .replace(/^### (.*$)/gim, '<h4 style="color: var(--color-primary); margin: 0.7rem 0 0.35rem 0; font-size: 1rem; font-weight: 700; display: flex; align-items: center; gap: 0.35rem;">$1</h4>')
        .replace(/^## (.*$)/gim, '<h3 style="color: #FFF; margin: 0.8rem 0 0.45rem 0; font-size: 1.08rem; font-weight: 700; border-bottom: 1px solid rgba(0, 240, 255, 0.2); padding-bottom: 0.3rem;">$1</h3>')
        .replace(/\*\*(.*?)\*\*/gim, '<strong style="color: #00F0FF; font-weight: 600;">$1</strong>')
        .replace(/\*(.*?)\*/gim, '<em style="color: #E2E8F0;">$1</em>')
        .replace(/^\* (.*$)/gim, '<li style="margin-left: 1.1rem; margin-bottom: 0.3rem; line-height: 1.5; color: #CBD5E1;">$1</li>')
        .replace(/\n\n/g, '<div style="height: 0.65rem;"></div>')
        .replace(/\n/g, '<br>');
}

/**
 * Toast Notification System
 */
function showToast(message, type = 'info') {
    let container = document.getElementById('toast-container');
    if (!container) {
        container = document.createElement('div');
        container.id = 'toast-container';
        container.className = 'toast-container';
        document.body.appendChild(container);
    }

    const toast = document.createElement('div');
    toast.className = 'toast';
    let icon = 'ℹ️';
    if (type === 'success') icon = '✅';
    if (type === 'warning') icon = '⚠️';
    if (type === 'primary') icon = '⚡';

    toast.innerHTML = `<span style="font-size: 1.3rem;">${icon}</span><div style="font-size: 0.88rem; font-weight: 500;">${message}</div>`;
    container.appendChild(toast);

    setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transform = 'translateX(30px)';
        toast.style.transition = 'all 0.4s ease';
        setTimeout(() => toast.remove(), 400);
    }, 4500);
}
