import streamlit as st
import pandas as pd
import joblib
from genai import generate_ai_insight

# ==================================
# Load saved model
# ==================================

saved_data = joblib.load(
    "best_model.joblib"
)

model = saved_data["model"]

feature_names = saved_data["features"]

mean_values = saved_data["mean_values"]

# ==================================
# App UI
# ==================================

st.title(
    "Flipkart Customer Satisfaction Predictor"
)

st.write(
    "Predict customer satisfaction and generate AI recommendations"
)

customer_age = st.number_input(
    "Customer Age",
    min_value=18,
    max_value=80,
    value=30
)

order_priority = st.selectbox(
    "Order Priority",
    ["Low","Medium","High"]
)

customer_remark = st.text_area(
    "Customer Remark"
)

# ==================================
# Prediction
# ==================================

if st.button("Predict"):

    input_data = {}

    # Fill model inputs with average values

    for feature in feature_names:

        if feature in mean_values:

            input_data[feature] = mean_values[feature]

        else:

            input_data[feature] = 0


    # Update with user values

    if "Customer_Age" in input_data:

        input_data["Customer_Age"] = customer_age


    if "Order_Priority" in input_data:

        priority_map = {

            "Low":0,
            "Medium":1,
            "High":2

        }

        input_data["Order_Priority"] = priority_map[order_priority]


    sample = pd.DataFrame(
        [input_data]
    )

    prediction = model.predict(
        sample
    )[0]


    # Decode output

    if prediction == 1:

        result = "Unsatisfied"

    else:

        result = "Satisfied"


    st.success(
        f"Prediction: {result}"
    )

    insight = generate_ai_insight(
        result,
        customer_remark
    )

    st.subheader(
        "AI Insight"
    )

    st.write(
        insight
    )