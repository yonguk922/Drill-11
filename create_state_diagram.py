from pathlib import Path


diagram = """<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="600"
 viewBox="0 0 1000 600">
  <defs>
    <marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3"
            orient="auto" markerUnits="strokeWidth">
      <path d="M0,0 L0,6 L9,3 z" fill="#2563eb"/>
    </marker>
  </defs>
  <rect width="1000" height="600" fill="white"/>
  <text x="500" y="42" text-anchor="middle" font-family="Arial"
        font-size="24" font-weight="bold" fill="#1e3a8a">
    LEC12 Boy State Machine
  </text>
  <circle cx="150" cy="190" r="78" fill="#bfdbfe" stroke="#2563eb"
          stroke-width="4"/>
  <text x="150" y="199" text-anchor="middle" font-family="Arial"
        font-size="28" font-weight="bold" fill="#111827">IDLE</text>
  <circle cx="820" cy="190" r="78" fill="#ddd6fe" stroke="#7c3aed"
          stroke-width="4"/>
  <text x="820" y="199" text-anchor="middle" font-family="Arial"
        font-size="28" font-weight="bold" fill="#111827">SLEEP</text>
  <circle cx="470" cy="190" r="78" fill="#bbf7d0" stroke="#16a34a"
          stroke-width="4"/>
  <text x="470" y="199" text-anchor="middle" font-family="Arial"
        font-size="28" font-weight="bold" fill="#111827">RUN</text>
  <path d="M228 170 L387 170" fill="none" stroke="#16a34a" stroke-width="4"
        marker-end="url(#arrow)"/>
  <text x="308" y="145" text-anchor="middle" font-family="Arial"
        font-size="18" fill="#15803d">LEFT / RIGHT</text>
  <path d="M765 245 C690 315, 555 315, 530 262" fill="none"
        stroke="#16a34a" stroke-width="4" marker-end="url(#arrow)"/>
  <text x="650" y="340" text-anchor="middle" font-family="Arial"
        font-size="18" fill="#15803d">LEFT / RIGHT</text>
  <path d="M202 120 C350 55, 620 55, 768 120" fill="none"
        stroke="#2563eb" stroke-width="4"
        marker-end="url(#arrow)"/>
  <text x="485" y="80" text-anchor="middle" font-family="Arial"
        font-size="18" fill="#1e40af">5 seconds</text>
  <path d="M742 225 C620 285, 270 285, 228 225" fill="none"
        stroke="#2563eb" stroke-width="4"
        marker-end="url(#arrow)"/>
  <text x="485" y="315" text-anchor="middle" font-family="Arial"
        font-size="18" fill="#1e40af">SPACE</text>
  <path d="M470 272 C470 365, 250 365, 150 272" fill="none"
        stroke="#16a34a" stroke-width="4" marker-end="url(#arrow)"/>
  <text x="300" y="390" text-anchor="middle" font-family="Arial"
        font-size="18" fill="#15803d">release direction key</text>
  <circle cx="470" cy="470" r="78" fill="#fef3c7" stroke="#d97706"
          stroke-width="4"/>
  <text x="470" y="479" text-anchor="middle" font-family="Arial"
        font-size="24" font-weight="bold" fill="#111827">AUTO_RUN</text>
  <path d="M228 215 C300 440, 380 450, 392 470" fill="none"
        stroke="#d97706" stroke-width="4" marker-end="url(#arrow)"/>
  <text x="285" y="440" text-anchor="middle" font-family="Arial"
        font-size="18" fill="#b45309">A (IDLE only)</text>
  <text x="500" y="555" text-anchor="middle" font-family="Arial"
        font-size="18" fill="#374151">
    AUTO_RUN is invincible and reverses direction at both boundaries
  </text>
  <text x="500" y="580" text-anchor="middle" font-family="Arial"
        font-size="16" fill="#4b5563">
    IDLE → SLEEP after 5 seconds | SLEEP → IDLE on SPACE
  </text>
</svg>
"""

output = Path(__file__).with_name('boy_state_diagram.svg')
output.write_text(diagram, encoding='utf-8')
print(f'Diagram saved as {output}')
