# SDG13 CO₂ Forecast Project – Nigeria

## Objective
This project analyzes and forecasts Nigeria’s CO₂ emissions per capita (1990–2030), supporting the UN Sustainable Development Goal 13: Climate Action.

## Dataset
- **Source:** [World Bank – CO₂ Emissions (metric tons per capita)](https://data.worldbank.org/indicator/EN.ATM.CO2E.PC)
- **File:** CO2_emissions_per_capita.xlsx
- **Years Covered:** 1990–2021
- **Country Focus:** Nigeria

## Tools Used
- Python (Google Colab)
- Libraries: pandas, numpy, matplotlib, scikit-learn

## Methodology
1. Imported and cleaned World Bank CO₂ data.
2. Filtered for Nigeria and transposed data by year.
3. Visualized trends (Nigeria, USA, China, India, Germany).
4. Built a **Linear Regression model** to forecast emissions for 2025–2030.

## Forecast Results
| Year | Predicted CO₂ per Capita |
|------|---------------------------|
| 2025 | 0.4445 |
| 2026 | 0.4326 |
| 2027 | 0.4207 |
| 2028 | 0.4087 |
| 2029 | 0.3968 |
| 2030 | 0.3848 |

📉 The model predicts a gradual decrease in Nigeria’s CO₂ emissions per capita by 2030.

## Key Insights
- China & India → Increasing trends
- US & Germany → Decreasing trends
- Nigeria → Relatively stable, with slight future decline

## Conclusion
Nigeria’s CO₂ emissions are expected to decline slowly if current policies continue, supporting climate action goals.

## References
- World Bank Open Data – CO₂ Emissions per capita
- United Nations SDG13 – Climate Action
