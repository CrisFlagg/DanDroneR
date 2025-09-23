# Drone + GIS in Rail Yards and Infrastructure

## Background

Railroads increasingly deploy drones integrated with GIS and AI to meet operational needs in intermodal yards and along rail corridors. In yards, “drone-in-a-box” systems run scheduled low-altitude flights to capture container rows and slot markings; AI/optical character recognition (OCR) extracts container IDs and parking locations while metadata (GPS, yaw, gimbal) supports precise georeferencing. Coupled with facility GIS basemaps, this enables near-real-time inventory, faster gate operations, and better yard space utilization. Along tracks and bridges, drones collect high-resolution visual/thermal imagery for inspection without exposing personnel to hazardous areas; when permitted, BVLOS (Beyond Visual Line of Sight) operations extend coverage and enable remote monitoring. Vendors now provide autonomous mission planning, detect-and-avoid systems, docking/battery-swap infrastructure, edge ML defect detection, and integrations into enterprise GIS and yard systems.

## Current Status

Adoption spans Class I railroads and selected short lines. BNSF’s Automated Yard Check (AYC) flies every 30–90 minutes over intermodal rows, achieving a reported 20% accuracy improvement versus manual yard checks and delivering more frequent checks; BNSF also holds experience with dock-based BVLOS waivers (up to 100 ft AGL) and long-range BVLOS track inspection (132 miles in New Mexico). CSX runs autonomous yard inspections across multiple sites using docks, RTK drones, edge ML, and a remote operations center; missions are triggered when track availability permits. Union Pacific has over 250 certified pilots using drones for yard audits, storm/derailment assessments, and bridge/tunnel inspections, and is exploring autonomous yard drones. Norfolk Southern and Canadian National operate VLOS drone inspections to supplement bridge/track assessments, prioritizing safety and efficiency. Short lines and contractors (e.g., Norfolk & Portsmouth Belt Line, Watco, ARE Corp.) use drones to inspect bridges during operation and to pre-target areas for tactile inspection, cutting durations and minimizing mainline shutdowns.

### Companies involved

- Railroads:
  - BNSF Railway
  - CSX Transportation
  - Union Pacific
  - Norfolk Southern
  - Canadian National (CN)
  - Canadian Pacific Kansas City (CPKC; includes former KCS)
  - Norfolk & Portsmouth Belt Line Railroad (shortline)
  - Watco Companies (shortline)
- Technology providers and partners:
  - DroneDeploy
  - Skydio (dock-based BVLOS ops)
  - FlytBase (autonomous orchestration)
  - Hextronics (drone docks)
  - Phase One (imagery)
  - Collins Aerospace (CNPC radios for BVLOS command/control)
  - Automodality (AMROS/Perceptive Navigation)
  - American Rail Engineers (ARE)
  - Nordic Unmanned (Staaker Railway Drone)

## Future Use and Applications

Growth areas include scaling yard inventory automation to additional intermodal facilities, expanding one-to-many remote operations, and deeper integration with yard management (e.g., automated switch-list optimization, load planning). Track and bridge inspections will incorporate more edge AI (e.g., joint bar bolt detection, switch point gaps, gauge issues), higher-precision positioning (RTK), and coverage beyond yards to “line of road.” Railroads indicate plans to activate autonomous systems at numerous locations (e.g., CSX) and continue expansion of inventory automation (e.g., BNSF). As detect-and-avoid and BVLOS frameworks mature, longer-range remote operations will become more routine, improving inspection frequency and safety while reducing dwell and disruption.

## Key Facts and Figures

This section summarizes sourced evidence of how railroads use drones—often integrated with GIS/AI—for intermodal yard inventory, security, and infrastructure inspection:

- BNSF Railway
  - Automated Yard Check (AYC): drone-in-a-box flights every 30–90 minutes; AI/OCR reads container IDs and slot numbers; thermal imagery supports nighttime security.
  - Reported a 20% inventory accuracy improvement vs. manual checks; initial basemaps included ~50,000 parking spaces.
  - Remote, dock-based BVLOS (nationwide waiver, 2021–2023) for yard security, emergency response, inspections at up to 100 ft AGL.
  - First civil BVLOS long-range (132-mile) inspection flight (New Mexico, FAA Pathfinder).
  - Patent (2024) describes end-to-end drone-based automated yard check and GIS conversion from GPS to lot/row/slot.

- CSX Transportation
  - Autonomous yard defect detection at 13 sites: DJI M350 RTK in Hextronics docks, Phase One camera, FlytBase orchestration, CASIA-G detect-and-avoid. Altitude ~100 ft AGL; remote operations center; GIS-integrated workflow.

- Union Pacific
  - >250 certified pilots; routine yard audits, storm assessments, derailments, and bridge/tunnel inspections; exploring autonomous yard drones (e.g., broken-rail detection) and potential 3D imagery. Typical inspection altitude ~100 ft AGL.

- Norfolk Southern and Canadian National
  - VLOS operations with FAA-certified pilots for bridge/track/derailment assessments. CN notes improved safety from reduced need to place staff on bridges/track.

- Short lines (selected)
  - Norfolk & Portsmouth Belt Line: drone-inspected an in-operation mechanical lift bridge (800 ft long, 200 ft high), capturing pins/bearings under load.
  - Watco’s Ohio River Bridge: drones reduced inspection duration from ~1 week to ~2 days and minimized mainline shutdowns.

Metrics summarized (from sources):
- Flight frequency: inventory flights at BNSF intermodal facilities every 30–90 minutes; CSX missions trigger when track becomes available; other inspections are scheduled/ad hoc.
- Altitude: 100 ft AGL commonly cited for dock-based yard and track inspections (CSX, BNSF remote waiver, Union Pacific).
- Reported accuracy gains: BNSF AYC improved inventory accuracy by 20%.
- Expansion plans: BNSF planned AYC expansion to six more locations (following 2023–2024 pilots); CSX scaling to numerous locations in 2025.

Download the dataset:
- [Download rail_yard_drone_use.csv](file:///rail_yard_drone_use.csv)

## Dataset Overview

The CSV includes:
- Organization, Facility/Area, Use Case, Method/Frequency, Regulatory Status, Platform/Vendor, Sensor/Data, Key Facts, Year, Source
- Added metrics columns: Flight_Frequency, Altitude_AGL_ft, Accuracy_Gain_pct, Expansion_Plans

Scope:
- Class I: BNSF, CSX, Union Pacific, Norfolk Southern, Canadian National, Kansas City Southern (now part of CPKC)
- Short lines: Norfolk & Portsmouth Belt Line Railroad; Watco Companies (Ohio River Bridge)
- Operations: intermodal yard inventory (AI/OCR), yard/track defect detection, emergency response, security, bridge/tunnel inspection, long-range BVLOS flights

## How to Analyze (no code)

Open the CSV in Excel and:
- Create a PivotTable: Organization × Use Case (count of entries)
- Filter Organization = BNSF to review inventory vs. BVLOS inspection use cases
- Slice by Regulatory Status (BVLOS vs. VLOS)
- Chart common operational metrics:
  - Flight_Frequency distributions (e.g., 30–90 minutes, triggered missions)
  - Altitude_AGL_ft (clustered bar by Organization)
  - Accuracy_Gain_pct where present (e.g., BNSF 20%)

## Bibliography (formal)

1) McNabb, Miriam. “What Automation Really Looks Like: BNSF Railway on Drone Docks, Inventory Management and More (DDC 2023).” DRONELIFE, Oct 11, 2023. https://dronelife.com/2023/10/11/what-automation-really-looks-like-bnsf-railway-on-drone-docks-inventory-management-and-more-from-the-floor-of-ddc-23/

2) Culos, Lisa; Manning, Stephen. “Eyes on AI: BNSF innovates to better serve our customers.” BNSF Rail Talk (Innovation), Jan 9, 2025. https://bnsf.com/news-media/railtalk/innovation/artificial-intelligence.html

3) Dukowitz, Zacc. “FAA Issues First National Approval for Remote, Dock-Based Drone Operations to BNSF Railway.” UAV Coach, Jul 1, 2021. https://uavcoach.com/bnsf-remote-ops-waiver/

4) Brajkovic, Vesna. “Inside BNSF’s advanced drone inspection operation.” Progressive Railroading (Rail News: BNSF), Apr 2019. https://www.progressiverailroading.com/bnsf_railway/article/Inside-BNSFs-advanced-drone-inspection-operation--57346

5) United States Patent No. 12,056,931. “Drone based automated yard check.” Justia Patents, Aug 6, 2024. https://patents.justia.com/patent/12056931

6) “BNSF Railway Tests Nordic Unmanned Railway Inspection Drone.” Unmanned Systems Technology (News), Sep 7, 2022. https://www.unmannedsystemstechnology.com/2022/09/bnsf-railway-tests-nordic-unmanned-railway-inspection-drone/

7) “How CSX Transportation is Mitigating Rail Risks using Autonomous Drone Ops in US.” FlytBase Case Study, 2025. https://www.flytbase.com/case-studies/csx-autonomous-drone-rail-inspection

8) “Rising to the Occasion: Union Pacific Drones Support Safe Operations.” Union Pacific News (Safety), Jul 1, 2024. https://www.up.com/news/safety/drones-safe-operations-it-240628

9) Brajkovic, Vesna. “Railroads continue to tap drone technology to inspect track, bridges.” Progressive Railroading (Rail News: MOW), Apr 2019. https://www.progressiverailroading.com/mow/article/Railroads-continue-to-tap-drone-technology-to-inspect-track-bridges--57270

10) Brajkovic, Vesna. “Short lines gain a new perspective on drone inspection.” Progressive Railroading (Rail News: Short Lines & Regionals), Mar 2020. https://www.progressiverailroading.com/short_lines_regionals/article/Short-lines-gain-a-new-perspective-on-drone-inspection--59910

Notes:
- Facility names in examples (e.g., Logistics Park Chicago; San Bernardino Intermodal Facility; Alliance Yard) reflect cited sources; where specific facility deployment is not stated, “intermodal facilities” or “system-wide” is used.
- Altitudes and frequencies are reported only where sources provide explicit values. BVLOS/VLOS statuses are based on cited waivers or general Part 107 operations.
