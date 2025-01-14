# **Historical Construction Estimate Comparison**

## **Overview**
This project focuses on leveraging historical construction preconstruction estimates in the Multi-Family market sector. The goal is to provide a comprehensive comparison tool for creating new estimates, normalizing costs by time and location, and aligning project metrics for better decision-making.

The project utilizes Power BI for dashboard visualization, Python for post-processing data exports, and automation workflows to streamline the data pipeline.

---

## **Key Features**
- **Cost Normalization**:
  - Adjusts costs to the current date using the U.S. Bureau of Labor Statistics (BLS).
  - Applies City Cost Index to normalize estimates for target locations.
- **Proforma Comparisons**:
  - Analyzes key metrics like GSF, RSF, number of floors, rooms, bathrooms, and parking spaces.
  - Provides detailed cost breakdowns (e.g., Cost/GSF, Cost/RSF, Cost/Acre).
- **Subcomponent Analysis**:
  - Compares costs by subcomponents such as Sitework, Parking Deck, Apartment, Amenity, and Retail.

---

## **Technical Details**
### **Tools & Technologies**
- **Power BI**: Interactive dashboard development.
- **Python**: Post-processing with OpenPyXL to stylize Power BI data exports.
- **Power Automate**: Automated workflows for data extraction and processing.
- **Azure Functions**: Cloud execution of Python scripts.
- **SQL**: Data preparation and query optimization.

### **Innovations**
- Implemented the Haversine formula within Power BI to calculate the closest city with City Cost Index data.
- Used Z-scores to identify the most similar components across estimates.

---

## **Deliverables**
- **Power BI Dashboard**:
  - Dynamic filters for estimate comparison.
  - Visualizations for normalized costs and subcomponent breakdowns.
- **Python Post-Processor**:
  - Custom script for styling and formatting Power BI exports.
- **Documentation**:
  - Data flow diagrams and user guides for stakeholders.

---

## **Folder Structure**
```plaintext
Historical_Construction_Estimate_Comparison/
├── README.md                   # Project overview and details
├── data/
│   ├── raw_data.csv            # Sample raw data (if permitted)
│   ├── cleaned_data.csv        # Cleaned and normalized data
├── scripts/
│   ├── post_processor.py       # Python script for styling Power BI exports
│   └── normalization_tool.py   # Script for cost normalization
├── dashboards/
│   └── PowerBI_Dashboard.pbix  # Power BI dashboard file
├── documentation/
│   ├── Data_Flow_Diagram.png   # Diagram of data processing steps
│   ├── City_Cost_Index.xlsx    # Reference data for cost normalization
│   └── User_Guide.pdf          # User guide for stakeholders
