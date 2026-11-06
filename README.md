# 📱 Automated-SIM-registration-Website

## 📌 Project Overview
This project is a web-based automation system designed to streamline the SIM registration process for telecommunications companies. The application supports both individual customer registration via a web form and bulk registration via CSV upload, significantly reducing manual effort, processing time, and operational costs.

The system simulates customer verification workflows and compares manual (traditional) registration with an automated (streamlined) process using Average Handling Time (AHT) metrics, visualized through interactive dashboards.

To see the project in full swing click the link below:
https://automated-sim-registration-website-llbxzsmi8ya8rpgjbuweyd.streamlit.app/

## 🛠️ Tech Stack
- Backend / App Framework: Python, Streamlit
- Data Processing: Pandas, NumPy
- Data Visualization: Plotly
- Data Generation: Faker
- Storage: CSV (simulated database input)



## ⚙️ Core Features
- Individual SIM registration via web form
- Bulk SIM registration via CSV upload
- Automated data validation and verification simulation
- Execution time tracking for each registration
- AHT comparison between traditional and streamlined processes
- Interactive dashboards for performance monitoring
- Error handling for missing or invalid records



## 🔄 Data Generation
Synthetic customer data was generated using the Faker library (`en_NG` locale) to simulate realistic Nigerian SIM registration records.

**Dataset characteristics:**
- Total records: 100
- Fields:
  - Name  
  - Phone number (valid Nigerian prefixes)  
  - ID number (valid and intentionally invalid lengths)  
  - Address  
  - Registration date  

Controlled data quality issues (missing values and invalid ID formats) were intentionally introduced to test the ETL pipeline, validation logic, and bulk processing robustness.

The raw dataset is saved as:
sim_registration_raw




## 🔄 ETL Pipeline
1. Extract  
   - Load raw CSV data generated with Faker
2. Transform  
   - Standardize phone numbers and ID formats  
   - Handle missing and invalid values  
   - Ensure schema consistency across all columns  
3. Load  
   - Cleaned data is used to validate individual and bulk SIM registration workflows



## 📊 Performance Analysis (AHT)
The application measures and compares:
- Traditional registration AHT (simulated longer handling times)
- Streamlined automated AHT (reduced verification steps)

### Visualizations
- Bar chart comparing average AHT (Traditional vs Streamlined)
- Line chart showing streamlined AHT across multiple activations

Results consistently show that the automated process significantly outperforms manual registration in speed and scalability.



## 📈 Business Impact
- Reduces SIM registration processing time
- Minimizes human error and data inconsistencies
- Improves operational efficiency
- Increases registration throughput without increasing workforce size
- Reduces manpower and operational costs for telecom operators


## 🔮 Future Improvements
- Integrate real-time or near–real-time data ingestion pipelines
- Add role-based authentication and access control
- Implement audit logs for compliance and traceabilit
- Connect to a production-grade database
- Deploy as a scalable cloud-based service
