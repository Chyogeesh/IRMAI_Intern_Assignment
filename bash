# Go to your project directory
cd anomaly-detector

# Create a virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
pip install pandas numpy scikit-learn pyod streamlit fastapi neo4j
timestamp,user_id,response_time,bytes_sent
2025-06-21 10:00:00,101,120,1024
2025-06-21 10:01:00,101,8000,4096  <-- Anomaly
2025-06-21 10:02:00,102,150,2048
...
mkdir anomaly-detector
cd anomaly-detector
# Create a virtual environment
python -m venv venv

# Activate it
# For Windows:
venv\Scripts\activate

# For macOS/Linux:
source venv/bin/activate
pip install pandas numpy scikit-learn pyod streamlit fastapi neo4j
mkdir backend data ml_models dashboard neo4j_graph
anomaly-detector/
├── backend/
├── data/
├── ml_models/
├── dashboard/
├── neo4j_graph/
├── venv/
timestamp,user_id,response_time,bytes_sent
2025-06-21 10:00:00,101,120,1024
2025-06-21 10:01:00,101,8000,4096
2025-06-21 10:02:00,102,150,2048
2025-06-21 10:03:00,103,170,2048
2025-06-21 10:04:00,104,160,1024
2025-06-21 10:05:00,101,155,1050
