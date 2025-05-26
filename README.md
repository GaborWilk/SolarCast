# ☀️ SolarCast

**SolarCast** is a machine learning project that forecasts short-term solar power generation in Hungary using energy load data and atmospheric irradiance information.  
Built for sustainability, analytics, and scalable deployment.

## Features
- Short-term forecasting of solar power generation
- Combines historical energy data with weather/irradiance from CAMS
- Streamlit-based UI for interactive exploration
- Docker-ready for scalable deployment

# Requirements
- Python 3.9+
- See requirements.txt for package dependencies

# How to install
1) Clone the repo:
```bash
git clone https://github.com/yourname/solarcast.git
cd solarcast
```

2) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3) Install requirements:
```python
pip install -r requirements.txt
```

4) Launch the app:
```python
streamlit run streamlit_app/app.py
```

# Data sources
- ENTSO-E Transparency (via Open Power System Data)
- CAMS (Copernicus Atmosphere Monitoring Service)

# License
MIT License (see LICENSE for more details)