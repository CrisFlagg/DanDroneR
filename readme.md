# Drone + GIS in Rail Yards and Infrastructure

## Background

Railroads are using drones to make yard inventory and inspections faster, safer, and more accurate. In intermodal yards, small automated drones fly routine routes to take pictures of container rows and parking spots. Software reads the container numbers and where they’re parked, then updates the yard map so teams can see inventory in near real time. At night, the same systems can support security with thermal cameras. Along tracks and bridges, drones capture clear images without putting people in hazardous areas. Where allowed, “beyond visual line of sight” (BVLOS) lets trained operators run longer routes and monitor flights remotely. Most systems now offer simple scheduling, safe automation, and connections into existing mapping and yard tools.

## Current Status

Major U.S. and Canadian railroads have active drone programs. BNSF runs frequent yard inventory flights (every 30–90 minutes) at key facilities and reports about a 20% accuracy improvement versus manual checks. BNSF also demonstrated long-range inspections over 132 miles of track and has operated remote, dock-based flights up to 100 feet high for security and incident response. CSX is running autonomous yard inspections at multiple sites with docked drones and high‑resolution cameras; flights generally happen when the track is clear. Union Pacific has over 250 certified pilots using drones for yard audits, storm damage, derailment assessment, and bridge/tunnel inspections, and is exploring autonomous yard drones. Norfolk Southern and Canadian National use drones under visual line‑of‑sight to supplement bridge and track work, keeping crews off difficult or dangerous structures. Short lines and contractors (e.g., Norfolk & Portsmouth Belt Line, Watco, ARE Corp.) have shown that drone inspections can cut time (e.g., from a week to two days on a large bridge) and reduce disruptions. BNSF secured a patent in 2024 describing its end‑to‑end automated yard inventory approach.

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
  - Skydio (dock-based operations)
  - FlytBase (autonomous orchestration)
  - Hextronics (drone docks)
  - Phase One (imagery)
  - Collins Aerospace (command and control for long-range flights)
  - Automodality (navigation in confined spaces)
  - American Rail Engineers (ARE)
  - Nordic Unmanned (Staaker Railway Drone)

## Future Use and Applications

Railroads are expanding these programs to more yards and longer stretches of track. Expect broader remote operations from centralized control rooms, more sites with routine inventory updates, and inspection software that can automatically flag issues like loose fasteners or gaps at switches. As safety frameworks mature, BVLOS operations will become easier to run routinely, increasing inspection frequency and reducing downtime. Overall, the aim is fewer manual counts, faster incident response, safer bridge inspections, and better visibility of assets across the network.

## Key Facts and Figures

Plain‑language takeaways drawn from the sources:

- BNSF Railway
  - Runs scheduled yard inventory flights every 30–90 minutes at major intermodal yards; software reads container numbers and parking locations.
  - Reports about a 20% improvement in inventory accuracy versus manual checks; early basemaps covered roughly 50,000 parking spaces.
  - Has operated remote, dock‑based flights up to 100 ft high for security and emergency work; demonstrated a 132‑mile long‑range inspection in New Mexico.
  - Received a 2024 patent describing its automated yard inventory and mapping approach.

- CSX Transportation
  - Operates autonomous yard inspections at 13 sites using docked drones and high‑resolution cameras; missions are run when the track is available.
  - Overseen from a remote operations center; typical flight height around 100 ft.

- Union Pacific
  - Trains and uses more than 250 drone pilots for yard audits, storm damage, derailments, and bridge/tunnel inspections.
  - Exploring autonomous yard drones to detect problems faster; inspects 16,900+ bridges system‑wide.

- Norfolk Southern and Canadian National
  - Use drones under visual line‑of‑sight to supplement bridge and track inspections and to assess derailment sites, improving safety and speed.

- Short lines (selected)
  - Norfolk & Portsmouth Belt Line: inspected a large mechanical lift bridge while it remained in service, including parts under load.
  - Watco (Ohio River Bridge): drone‑supported pre‑inspection reduced time from about a week to around two days and minimized mainline shutdowns.

At‑a‑glance metrics:
- Flight frequency: BNSF yard inventory flights every 30–90 minutes; CSX missions trigger when the track is clear; other inspections are scheduled or ad hoc.
- Altitude: around 100 ft above ground typical for dock‑based yard and track inspections (CSX, BNSF remote ops, Union Pacific).
- Accuracy gains: BNSF reports about 20% better yard inventory accuracy versus manual counts.
- Expansion plans: BNSF planned expansion of yard inventory automation to additional locations; CSX scaling autonomous yard inspections to more sites.

Upcoming rules and frameworks:
- Transport Canada BVLOS final rule (effective November 4, 2025): allows routine BVLOS operations for drones up to 150 kg in Class G (uncontrolled) airspace at low altitudes over sparsely populated areas, without a case‑by‑case SFOC; includes a new BVLOS pilot certification and a transition period to full implementation.
- FAA Part 108 BVLOS NPRM (proposed August 5, 2025; public comment to October 6, 2025): a performance‑based BVLOS framework with mandatory Safety Management Systems, safety technology requirements, personnel vetting, and scalable operator certifications; a final rule is expected in 2026.

Download the dataset:
- [Download rail_yard_drone_use.csv](file:///rail_yard_drone_use.csv)

## Dataset Overview

The CSV includes:
- Organization, Facility/Area, Use Case, Method/Frequency, Regulatory Status, Platform/Vendor, Sensor/Data, Key Facts, Year, Source
- Added metrics columns: Flight_Frequency, Altitude_AGL_ft, Accuracy_Gain_pct, Expansion_Plans

Scope:
- Class I: BNSF, CSX, Union Pacific, Norfolk Southern, Canadian National, Kansas City Southern (now part of CPKC)
- Short lines: Norfolk & Portsmouth Belt Line Railroad; Watco Companies (Ohio River Bridge)
- Operations: yard inventory, yard/track defect detection, emergency response, security, bridge/tunnel inspection, long‑range inspections

## How to Analyze (no code)

Open the CSV in Excel and:
- Create a PivotTable: Organization × Use Case (count of entries)
- Filter Organization = BNSF to review inventory vs. BVLOS inspection use cases
- Slice by Regulatory Status (BVLOS vs. VLOS)
- Chart common operational metrics:
  - Flight_Frequency distributions (e.g., 30–90 minutes, triggered missions)
  - Altitude_AGL_ft (clustered bar by Organization)
  - Accuracy_Gain_pct where present (e.g., BNSF ~20%)

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
11) Autonomy Global. “Understanding FAA Part 108: Why Safety Management Systems Are Central to BVLOS Drone Rules.” Aug 2025. https://www.autonomyglobal.co/understanding-faa-part-108-why-safety-management-systems-are-central-to-bvlos-drone-rules/
12) Pillsbury Law. “FAA Proposes Rule to Enable Routine BVLOS Operations.” Aug 2025. https://www.pillsburylaw.com/en/news-and-insights/faa-proposed-rule-bvlos.html
13) AUVSI. “Unlocking Routine BVLOS Operations: AUVSI’s Initial Analysis of the FAA’s NPRM.” Aug 2025. https://www.auvsi.org/unlocking-routine-bvlos-operations-auvsis-initial-analysis-of-the-faas-nprm/
14) DSLRPros. “FAA BVLOS NPRM Under Part 108: Complete Guide for Drone Buyers and Ops Teams.” Aug 2025. https://www.dslrpros.com/blogs/drone-trends/faa-bvlos-nprm-under-part-108-complete-guide-for-drone-buyers-and-ops-teams
15) Commercial UAV News. “What Can the FAA Learn From Transport Canada’s New BVLOS Regulations?” Apr 2025. https://www.commercialuavnews.com/international/what-can-the-faa-learn-from-transport-canada-s-new-bvlos-regulations

Notes:
- Facility names in examples (e.g., Logistics Park Chicago; San Bernardino Intermodal Facility; Alliance Yard) reflect cited sources; where specific facility deployment is not stated, “intermodal facilities” or “system-wide” is used.
- Altitudes and frequencies are reported only where sources provide explicit values. BVLOS/VLOS statuses are based on cited waivers or general Part 107 operations.
