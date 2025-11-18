# IoT Control & Optimization System

![Status](https://img.shields.io/badge/status-production%20ready-green)
![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-latest-009688)

> Advanced IoT device management system with intelligent parameter optimization using metaheuristic algorithms and time-series forecasting

## Overview

This system integrates a **FastAPI backend** for IoT device management with sophisticated **optimization algorithms** to control and predict device behavior. It combines real-time sensor data processing with machine learning techniques (ARIMA/SARIMA) and metaheuristic optimization (Genetic Algorithms, Simulated Annealing, Tabu Search, Iterated Local Search) to achieve intelligent decision-making for embedded systems.

**Key Capabilities:**
- RESTful API for managing IoT devices (lights, voltage controllers, sensors)
- Multi-parameter optimization with customizable constraints and weights
- Time-series forecasting for predictive control
- Heuristic-based decision optimization with cost-aware parameter tuning

**Primary Use Case:** Optimizing environmental control systems (temperature, humidity, pressure) in IoT networks with energy efficiency and cost constraints.

---

## Features ✅

### API & Database
- **CRUD Operations** for 5 device types (DevicesInfo, DevicesRecords, TomaDecisiones, Luces, ControladorVoltaje)
- **SQLite database** with SQLAlchemy ORM
- **Auto-generated API documentation** (Swagger UI / ReDoc)
- **Type-safe data validation** with Pydantic models

### Optimization Algorithms
- **Genetic Algorithm** - Population-based search with crossover and mutation
- **Simulated Annealing** - Temperature-based probabilistic optimization
- **Tabu Search** - Memory-based local search with forbidden moves
- **Iterated Local Search** - Hybrid approach combining local search with perturbation
- **Parameter-aware optimization** - Multi-objective fitness with custom weights and penalties

### Time-Series Forecasting
- **ARIMA** - Autoregressive Integrated Moving Average models
- **SARIMA** - Seasonal ARIMA for periodic patterns
- **Integration with optimization** - Forecast-driven parameter adjustments

---

## Architecture

### System Design

```
┌─────────────────────────────────────────────────────────┐
│                     Client Layer                        │
│            (HTTP Requests / IoT Devices)                │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                  FastAPI Server                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │   Endpoints  │  │     CRUD     │  │    Models    │  │
│  │   (main.py)  │──│   (crud.py)  │──│ (models.py)  │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                SQLite Database                          │
│  (Devices Info, Records, Decisions, Lights, Controllers)│
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│              ML/Optimization Module                     │
│  ┌──────────────────────────────────────────────────┐  │
│  │        OptimizationManager (params.py)           │  │
│  │  - Multi-parameter objective function            │  │
│  │  - Constraint handling & penalty calculation     │  │
│  └────────────┬─────────────────────────────────────┘  │
│               │                                         │
│       ┌───────┴────────┬──────────┬──────────┐         │
│       ▼                ▼          ▼          ▼         │
│  ┌─────────┐  ┌──────────────┐ ┌────────┐ ┌─────┐     │
│  │Genetic  │  │   Simulated  │ │ Tabu   │ │ ILS │     │
│  │Algorithm│  │   Annealing  │ │ Search │ │     │     │
│  └─────────┘  └──────────────┘ └────────┘ └─────┘     │
│                                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │   Time-Series Forecasting (ARIMA/SARIMA)         │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

### Component Breakdown

**API Layer (`main.py`):**
- 25+ RESTful endpoints
- Automatic request validation
- Error handling with HTTP status codes

**Data Layer (`models.py`, `database.py`):**
- SQLAlchemy ORM models
- Pydantic schemas for request/response validation
- SQLite database with automatic table creation

**Optimization Core (`ML/`):**
- `params.py` - Parameter class with satisfaction metrics and penalty functions
- `optimization_manager.py` - Orchestrates multi-parameter optimization
- `genetico.py`, `recocido.py`, `tabu.py`, `iterated_ls.py` - Metaheuristic implementations
- `arima.py`, `sarima.py` - Time-series forecasting models

---

## Technical Stack

**Backend:**
- **Python** 3.7+
- **FastAPI** - Modern async web framework
- **SQLAlchemy** 2.x - ORM for database operations
- **Pydantic** - Data validation and serialization
- **Uvicorn** - ASGI server

**Optimization & ML:**
- **Polars** - High-performance dataframes
- **Matplotlib** - Visualization
- Custom implementations of metaheuristic algorithms

**Database:**
- **SQLite** - Embedded SQL database

---

## Quick Start

### Prerequisites
```bash
python --version  # Python 3.7 or higher required
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Dise-o-Electronico-Embebidos.git
cd Dise-o-Electronico-Embebidos
```

2. Install dependencies:
```bash
pip install fastapi uvicorn sqlalchemy pydantic python-dotenv polars matplotlib
```

3. Configure environment (optional):
```bash
# Create .env file for custom database URL
echo "DATABASE_URL=sqlite:///./mydb.sqlite" > .env
```

### Running the API

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

The API will be available at:
- **Base URL:** `http://localhost:8000`
- **Swagger Docs:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

### Running Optimization Algorithms

Execute the optimization example:
```bash
cd ML
python main.py
```

This will:
1. Initialize 3 parameters (Temperature, Humidity, Pressure)
2. Run Iterated Local Search optimization
3. Generate results CSV and visualization PNG

---

## Project Structure

```
Dise-o-Electronico-Embebidos/
├── main.py                    # FastAPI application entry point
├── models.py                  # SQLAlchemy & Pydantic models
├── crud.py                    # Database CRUD operations
├── database.py                # Database configuration
├── mydb.sqlite                # SQLite database file
├── api_requests_examples.http # API request examples
├── ML/                        # Optimization & forecasting module
│   ├── main.py                # Optimization example runner
│   ├── params.py              # Parameter class definition
│   ├── optimization_manager.py # Multi-parameter optimizer
│   ├── genetico.py            # Genetic algorithm
│   ├── recocido.py            # Simulated annealing
│   ├── tabu.py                # Tabu search
│   ├── iterated_ls.py         # Iterated local search
│   ├── local_search.py        # Base local search
│   ├── arima.py               # ARIMA forecasting
│   ├── sarima.py              # SARIMA forecasting
│   └── results_manager.py     # Result tracking utilities
└── documentacion_*.pdf        # Technical documentation
```

---

## API Documentation

### Core Endpoints

**Device Information Management:**
```bash
GET    /devices/info/              # List all devices
POST   /devices/info/              # Register new device
GET    /devices/info/{id_device}   # Get device by ID
PUT    /devices/info/{id_device}   # Update device
DELETE /devices/info/{id_device}   # Remove device
```

**Device Records:**
```bash
GET    /devices/records/                    # All records
POST   /devices/records/                    # Add record
GET    /devices/records/device/{id_device}  # Records by device
```

**Decision Making:**
```bash
GET    /decisiones/              # List decisions
POST   /decisiones/              # Create decision record
PUT    /decisiones/{id_decision} # Update decision
```

**Smart Devices (Lights & Voltage Controllers):**
```bash
# Lights
GET/POST/PUT/DELETE  /luces/
GET                  /luces/{id_device}

# Voltage Controllers
GET/POST/PUT/DELETE  /controladores/
GET                  /controladores/{id_device}
```

### Example Request

```python
import requests

# Create a new device
device_data = {
    "id_device": 1,
    "id_type": 1,
    "id_signal_type": 2,
    "nombre": "Temperature Sensor",
    "vendor": "DHT22"
}

response = requests.post(
    "http://localhost:8000/devices/info/",
    json=device_data
)
print(response.json())
```

---

## Usage Example: Optimization

```python
from ML.params import Param
from ML.optimization_manager import OptimizationManager
from ML.genetico import Genetico

# Define parameters to optimize
temp = Param(
    name="Temperature",
    min=18, max=28,
    v_actual=25,
    weight=0.5,
    costo_cambio=10,
    optim_mode="min"  # Minimize temperature
)

humidity = Param(
    name="Humidity",
    min=30, max=70,
    v_actual=50,
    weight=0.5,
    costo_cambio=5,
    optim_mode="max"  # Maximize humidity
)

# Initialize optimizer
optimizer = OptimizationManager([temp, humidity])

# Run genetic algorithm
ga = Genetico(tam_poblacion=50, optimizer_inicial=optimizer)
population = ga.generar_poblacion()
fitness_vals = ga.calc_fitness_poblacion(population)

# Select best solution
best_parents = ga.seleccion(num_padres=10, lista_fitness=fitness_vals)
print(f"Best fitness: {best_parents[0][1]}")
best_parents[0][0].show_params()
```

**Output:**
```
Best fitness: 0.87
Parametro: Temperature
  Valor Actual: 18.5
  Satisfacción: 0.95
Parametro: Humidity
  Valor Actual: 68.2
  Satisfacción: 0.94
```

---

## Technical Highlights

### Multi-Objective Optimization
The `OptimizationManager` class implements a sophisticated fitness function that:
- Balances multiple parameters with custom weights
- Applies quadratic penalties for constraint violations
- Accounts for cost-of-change in real-world deployments
- Supports both maximization and minimization objectives simultaneously

**Key Formula (from `params.py:43-55`):**
```python
def calc_satisfaction(self) -> float:
    if self.optim_mode == "max":
        return (self.v_actual - self.min) / (self.max - self.min)
    elif self.optim_mode == "min":
        return (self.max - self.v_actual) / (self.max - self.min)
```

### Database Design Patterns
- Uses SQLAlchemy ORM with separate request/response schemas
- Numeric fields stored as `Numeric` type for precision in sensor readings
- Automatic timestamp tracking for all device records
- Indexed fields on device IDs and names for fast lookups

### Algorithm Implementations
All metaheuristic algorithms share a common interface through `OptimizationManager`:
- **Genetic Algorithm:** Tournament selection, single-point crossover, Gaussian mutation
- **Simulated Annealing:** Exponential cooling schedule with adaptive neighborhood search
- **Tabu Search:** Fixed-size tabu list with aspiration criteria
- **ILS:** Combines gradient-based local search with random perturbations

---

## Current Status & Roadmap

### Implemented ✅
- Full CRUD API for 5 device types
- 4 optimization algorithms with complete implementations
- ARIMA/SARIMA time-series forecasting
- Result visualization and CSV export
- Comprehensive documentation (Spanish & English)

### Known Limitations
- Single-user mode (no authentication/authorization)
- SQLite not recommended for high-concurrency production
- No real-time WebSocket integration for live device updates
- Forecasting models not integrated into API endpoints

### Planned Enhancements 📋
- [ ] Add JWT-based authentication
- [ ] Implement WebSocket support for real-time monitoring
- [ ] Migrate to PostgreSQL for production deployments
- [ ] Create `/optimize` endpoint to trigger algorithms via API
- [ ] Add unit tests and CI/CD pipeline
- [ ] Develop frontend dashboard for visualization

---

## Testing

Use the included HTTP examples:
```bash
# Install REST Client extension in VS Code
# Open api_requests_examples.http
# Click "Send Request" above any request
```

Or use curl:
```bash
# Get all devices
curl http://localhost:8000/devices/info/

# Create a test device
curl -X POST http://localhost:8000/tests/?title=MyTest
```

---

## Learning Outcomes

This project demonstrates:
- **Full-stack development:** From database design to REST API implementation
- **Algorithm engineering:** Implementing academic algorithms in production code
- **Systems thinking:** Balancing multiple constraints in optimization problems
- **Software architecture:** Clean separation of concerns (API/Data/Logic layers)
- **Documentation:** Professional-grade code comments and API docs

**Academic Context:** Developed as part of "Diseño Electrónico Embebido" coursework, extended beyond requirements with:
- ✅ Multiple optimization algorithms (assignment required 1)
- ✅ Full REST API (assignment only required database)
- ✅ Time-series forecasting integration
- ✅ Bilingual documentation

---

## Documentation

- **API Documentation (Spanish):** `documentacion_fastapi.pdf` (138 pages)
- **Unit 2 Documentation:** `documentacion_unidad2.pdf` (182 pages)
- **LaTeX Source:** `documentacion_fastapi.tex`

---

## License

This project is available for educational and portfolio purposes.

---

## Contact & Contributions

For questions or collaboration inquiries, please open an issue on GitHub.

---

**🤖 Generated with [Claude Code](https://claude.com/claude-code)**