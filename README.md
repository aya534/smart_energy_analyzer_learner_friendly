# ⚡ Smart Energy Analyzer

**Learning Python through real-world energy problems.**

Smart Energy Analyzer is a beginner-friendly, console-based Python application that estimates household appliance energy consumption and electricity costs.

The project connects Python programming with everyday electrical engineering concepts, making it useful for students, beginners, and anyone interested in understanding how electrical appliances consume energy.

##  Project Goals

- Apply Python fundamentals to a practical problem.
- Explore energy consumption and electricity cost calculations.
- Practice problem-solving, debugging, and code organization.
- Build an evolving project through meaningful improvements.
- Make programming concepts easier to understand through real-world examples.

##  Current Features

- **Appliance management:** Add appliances with their names, power ratings, and daily operating hours.
- **Input validation:** Check appliance names and operating values.
- **Daily energy calculation:** Estimate energy consumption in kilowatt-hours (kWh).
- **Monthly energy estimation:** Calculate consumption using a 30-day month.
- **Electricity cost estimation:** Apply a simplified tiered pricing model.
- **Budget monitoring:** Warn users when estimated monthly costs exceed a defined budget.
- **Consumption summary:** Display appliance information and basic statistics, including maximum daily energy consumption and minimum operating hours.

##  Energy Calculation

Energy consumption is calculated using:

\[
E = \frac{P \times t}{1000}
\]

Where:

- \(E\) = energy consumption in kWh
- \(P\) = appliance power in watts
- \(t\) = operating time in hours

**Example**

An appliance rated at 1,500 watts running for 4 hours per day consumes:

`(1500 × 4) / 1000 = 6 kWh/day`

Assuming 30 days per month, its estimated monthly consumption is 180 kWh.

##  Electricity Cost Estimation

The application uses a configurable electricity price, a monthly consumption threshold, and an additional multiplier for consumption above that threshold.

These values demonstrate how conditional statements and arithmetic can model a simplified tiered pricing system. They are illustrative settings, not a representation of any specific electricity provider's tariff.

##  Technologies and Concepts

- Python 3
- Variables and data types
- User input and output
- Conditional statements
- Loops
- Lists and list operations
- Input validation
- Basic statistics and built-in functions
- Mathematical calculations
- Problem-solving and debugging

##  Getting Started

### Prerequisites

Install Python 3 on your computer.

### Run the application

1. Clone this repository:

   ```bash
   git clone https://github.com/YOUR-USERNAME/smart-energy-analyzer.git
   ```

2. Navigate to the project directory:

   ```bash
   cd smart-energy-analyzer
   ```

3. Run the application:

   ```bash
   python main.py
   ```

4. Follow the console menu to add appliances and view the energy and cost summary.

##  Development Roadmap

The project will evolve through meaningful, incremental improvements, including:

- Refactoring calculations into reusable functions.
- Searching for and removing appliances.
- Improving reports and handling edge cases.
- Adding automated tests.
- Saving appliance data between sessions.
- Exploring energy-data visualization.
- Applying data analysis and machine learning to energy-related problems.

##  Learning Philosophy

Rather than treating programming as a collection of isolated exercises, this project uses a practical energy-analysis problem to explore programming concepts step by step.

The aim is to keep the code understandable while gradually improving its structure, reliability, and functionality.

##  Disclaimer

Energy consumption and cost figures are estimates based on user-provided values and simplified assumptions. Actual electricity bills depend on the applicable tariff, taxes, fees, and other factors.

---

**Status:** Under active development.

**Built with Python and a curiosity for connecting software with real-world engineering problems.**
