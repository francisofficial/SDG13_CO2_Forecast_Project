# 🌍 AI for Sustainable Development – CO₂ Emission Prediction

## 🎯 SDG Focus: SDG 13 – Climate Action
This project addresses **UN Sustainable Development Goal 13: Climate Action**, which seeks to combat climate change and its impacts.  
The aim of this project is to use **Machine Learning** to analyze and predict trends in **CO₂ emissions per capita** across countries, providing insights that can help guide sustainable environmental policies.

---

## 🧠 Machine Learning Approach
**Type:** Supervised Learning  
**Algorithm:** Linear Regression  

The model was trained using historical CO₂ emission data from the **World Bank Open Data (via Kaggle)**.  
Linear Regression was chosen because it effectively captures continuous numerical trends over time.

### Steps:
1. Data preprocessing and cleaning (removal of missing or unnamed columns).  
2. Visualization of emission trends for key countries.  
3. Building and training a regression model to learn patterns over the years.  
4. Predicting CO₂ emissions per capita for the years **2025–2030**.  

---

## 📊 Results Summary
After training, the model predicted a slight decline in global CO₂ emissions per capita for the next few years.

| Year | Predicted CO₂ per Capita |
|------|--------------------------|
| 2025 | 0.444538 |
| 2026 | 0.432594 |
| 2027 | 0.420650 |
| 2028 | 0.408705 |
| 2029 | 0.396761 |
| 2030 | 0.384817 |

The line chart visualization shows that:
- **China and India** have rising emission trends.
- **USA and Germany** show steady declines.
- **Nigeria** shows a moderate or slightly rising trend.

---

## 💡 Insights & Impact
- Predictive analytics can help **governments and organizations** set realistic emission reduction targets.
- Countries can use this data to **track progress** toward sustainable energy transitions.
- The model provides a **data-driven approach** to climate action decision-making.

---

## ⚖️ Ethical & Social Reflection
- **Data Bias:** Some countries have incomplete or outdated emission data, which may slightly affect accuracy.
- **Fairness:** The model treats all countries equally based on available data, without discrimination.
- **Sustainability:** By highlighting emission patterns, AI supports **evidence-based climate action** and encourages responsible policy development.

---

## 🧩 Tools Used
- **Language:** Python  
- **Libraries:** Pandas, Scikit-learn, Matplotlib  
- **Dataset:** CO₂ emissions per capita (World Bank / Kaggle)  
- **Environment:** Google Colab / VS Code  

---

## 🏁 Conclusion
This project demonstrates how **Machine Learning** can contribute to global sustainability efforts by helping predict and monitor CO₂ emissions.  
It aligns with **SDG 13 (Climate Action)**, showcasing how AI can serve as a bridge between **technology, awareness, and sustainability**.

---

**Author:** Francis Promise  
**Course:** AI for Software Engineering – Week 2  
**Institution:** Power Learn Project (PLP) Academy  
**Date:** October 2025
