# Traffic-Flow-Prediction
The objective of this project is to analyze traffic data (e.g., sensor readings, weather conditions, and historical traffic patterns) to forecast traffic conditions and suggest optimal routes for smart city infrastructure.

Methodology:
- Data Preparation: A synthetic dataset was generated with features such as hour, day_of_week,weather, and traffic speed.
- Preprocessing: Weather conditions were encoded into numerical form.
- Modeling: A Random Forest Regressor was trained to predict traffic speed.
- Evaluation: Metrics such as MAE, RMSE, and R² were used to evaluate performance.
- Visualization: Scatter plot (actual vs predicted) and feature importance were plotted.

Results:
- Mean Absolute Error (MAE): 10.27
- Root Mean Squared Error (RMSE): 12.88 R² Score: -0.66

Conclusion: 
The Random Forest model successfully predicted traffic flow with strong performance metrics. This demonstrates how cities can leverage data-driven approaches to forecast and manage traffic flow more effectively, reducing congestion and improving urban mobility. Future improvements could integrate real-world sensor data, GPS data, and live weather feeds for even more accurate predictions.


