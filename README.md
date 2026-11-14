# MARSWALK
### Terrain-Aware Traverse Planning for Mars

**NASA Space Apps Challenge 2026**  
**Challenge:** Interplanetary Survival Guide: Martian Map (Intermediate)

MARSWALK is a terrain-aware Martian traverse-planning prototype focused on the Jezero Crater region. It uses high-resolution elevation data from NASA's HiRISE instrument to derive terrain characteristics and generate a traversability cost map. An A* pathfinding algorithm then searches for routes that minimize accumulated terrain traversal cost rather than simply geographical distance.

---

## 1. Project Overview

Planning a traverse across the Martian surface requires more than identifying the shortest distance between two locations. Surface slope and roughness can influence mobility and make certain regions more challenging to cross.

MARSWALK explores a computational approach to this problem by combining planetary elevation data, terrain analysis and graph-based pathfinding.

### Key Objectives

- Process high-resolution Martian elevation data.
- Derive slope and surface roughness information.
- Generate a terrain traversal-cost surface.
- Identify routes using the A* pathfinding algorithm.
- Establish a foundation for incorporating additional planetary datasets and mission constraints.

## 2. How It Works

The current workflow consists of four main stages.

### Stage 1 — Elevation Data

The project uses a 1 metre per pixel HiRISE Digital Terrain Model (DTM) covering the Jezero Crater region.

The elevation model provides the spatial foundation for terrain analysis.

### Stage 2 — Terrain Analysis

Slope and surface roughness are derived from the elevation model.

These characteristics are normalized and combined to construct a relative terrain-cost surface.

### Stage 3 — Traversability Cost

The prototype calculates terrain cost using:

\[
C=(0.6S+0.4R)^{1.2}
\]

Where:

- \(S\) = Normalized slope
- \(R\) = Normalized surface roughness
- \(C\) = Relative terrain traversal cost

The resulting cost values represent relative terrain difficulty. Higher values indicate greater traversal cost.

The weights and exponent are prototype design choices and have not been calibrated against actual rover or crew mobility data.

### Stage 4 — A* Pathfinding

Users specify a starting point and destination using projected map coordinates.

The backend maps these coordinates to raster pixels and applies A* pathfinding to identify a route that minimizes accumulated terrain traversal cost.

The algorithm considers terrain cost during route search rather than optimizing geographical distance alone.

## 3. Technology Stack

| Component | Technology |
|---|---|
| Backend | Python, FastAPI |
| Geospatial processing | Rasterio, GDAL |
| Numerical computation | NumPy |
| Route optimization | A* Pathfinding |
| Frontend | React, Vite |
| GIS inspection | QGIS |
| Version control | Git, GitHub |
| Development assistance | Antigravity, ChatGPT |

## 4. NASA Data Resources

### Primary Dataset

**HiRISE Digital Terrain Model — Jezero Crater**

- Instrument: High Resolution Imaging Science Experiment (HiRISE)
- Mission: Mars Reconnaissance Orbiter
- Spatial resolution: 1 metre per pixel
- Data type: Digital Terrain Model
- Region: Jezero Crater, Mars

**Dataset reference:**

[USGS Astrogeology — Jezero HiRISE DTM](https://astrogeology.usgs.gov/search/map/Mars/Mars2020/JEZ_hirise_soc_006_DTM_MOLAtopography_DeltaGeoid_1m_Eqc_latTs0_lon0_blend40)

**HiRISE instrument website:**

https://www.uahirise.org/

The slope, roughness and terrain-cost layers used by MARSWALK are derived through our own processing of the elevation data. They are not separate independent NASA datasets.

## 5. Validation

The backend pathfinding implementation was tested using a sample start and destination pair.

An example validation run produced:

| Metric | Result |
|---|---:|
| Route distance | 1,434.13 m |
| Route pixels | 1,035 |
| Accumulated weighted cost | 1,545.13 |
| Expanded search nodes | 419,891 |

These values represent a backend validation run and are not measurements from an operational rover or crew traverse.

## 6. Current Development Status

MARSWALK is an early-stage prototype.

**Implemented:**
- HiRISE elevation data integration.
- Terrain-derived slope and roughness processing.
- Terrain-cost raster generation.
- Coordinate-to-raster mapping.
- A* pathfinding backend.
- Backend route validation.

**Work remaining:**
- Complete frontend integration with the backend.
- Operational interactive terrain and route visualization.
- Additional geological and scientific datasets.
- Hazard-aware route planning.
- Mission-specific mobility and safety constraints.
- Three-dimensional terrain visualization.

The current prototype is intended to demonstrate a terrain-aware route-planning approach. It is not a validated flight-planning, rover-navigation or crew-safety system.

## 7. Future Scope

Potential extensions include:

- Integration of geological and scientific observation targets.
- Incorporation of additional terrain and hazard datasets.
- Mission-specific mobility constraints.
- Three-dimensional terrain visualization.
- Comparison of alternative traverse routes.
- Emergency-route and mission-contingency planning.

## 8. Repository

GitHub:  
https://github.com/ayushkatare18/MARSWALK-NASA-Space-Apps-Challenge

## 9. Acknowledgements

Developed for the NASA Space Apps Challenge 2026.

Planetary elevation data is sourced from the HiRISE instrument aboard NASA's Mars Reconnaissance Orbiter and distributed through USGS Astrogeology.

