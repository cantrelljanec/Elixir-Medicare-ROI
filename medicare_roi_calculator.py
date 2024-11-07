import streamlit as st

# Define the ROI calculator function
def calculate_medicare_roi(communications_volume, time_reduction, cost_per_doc_manual, cost_per_doc_auto, 
                           error_reduction, engagement_uplift, revenue_per_member, initial_investment):
    # Calculate cost savings from time reduction
    cost_savings_time_reduction = communications_volume * (time_reduction / 100) * (cost_per_doc_manual - cost_per_doc_auto)
    
    # Calculate cost savings from compliance error reduction
    cost_savings_compliance = communications_volume * (error_reduction / 100) * cost_per_doc_manual
    
    # Calculate revenue uplift from customer engagement improvement
    revenue_uplift = communications_volume * (engagement_uplift / 100) * revenue_per_member
    
    # Total savings and ROI calculation
    total_savings = cost_savings_time_reduction + cost_savings_compliance + revenue_uplift
    roi = total_savings - initial_investment
    
    return {
        "Cost Savings from Time Reduction (USD)": round(cost_savings_time_reduction, 2),
        "Cost Savings on Compliance (USD)": round(cost_savings_compliance, 2),
        "Revenue Uplift from Engagement (USD)": round(revenue_uplift, 2),
        "Total Savings (USD)": round(total_savings, 2),
        "ROI (USD)": round(roi, 2)
    }

# Streamlit App Interface
st.title("Medicare ROI Calculator")

# Fixed values for the other parameters
time_reduction = 40              # Time Reduction in Content Creation (%)
cost_per_doc_manual = 10         # Cost per Document (Manual)
cost_per_doc_auto = 3            # Cost per Document (Automated)
error_reduction = 30             # Error Reduction in Compliance (%)
engagement_uplift = 25           # Customer Engagement Uplift (%)
revenue_per_member = 150         # Revenue per Medicare Member
initial_investment = 85000       # Initial Investment

# Display fixed values in the app (optional, for transparency)
st.write("### Fixed Input Values")
st.write(f"Time Reduction in Content Creation: {time_reduction}%")
st.write(f"Cost per Document (Manual): ${cost_per_doc_manual}")
st.write(f"Cost per Document (Automated): ${cost_per_doc_auto}")
st.write(f"Error Reduction in Compliance: {error_reduction}%")
st.write(f"Customer Engagement Uplift: {engagement_uplift}%")
st.write(f"Revenue per Medicare Member: ${revenue_per_member}")
st.write(f"Initial Investment: ${initial_investment}")

# Input field for Communications Volume (user-editable)
communications_volume = st.number_input("Communications Volume", min_value=1, value=10000, step=1000)

# Calculate and display results
if st.button("Calculate ROI"):
    result = calculate_medicare_roi(
        communications_volume, time_reduction, cost_per_doc_manual, cost_per_doc_auto, 
        error_reduction, engagement_uplift, revenue_per_member, initial_investment
    )
    st.write("### Savings & ROI")
    for key, value in result.items():
        st.write(f"{key}: ${value}")
