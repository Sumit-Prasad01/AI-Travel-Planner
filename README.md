# 🧳 AI Travel Planner Agent

AI Travel Planner Agent is an intelligent **LLM-powered travel itinerary generator** that creates a complete **one-day travel plan** based on the **location** and **places provided by the user**.

The agent returns a structured day schedule with **proper time slots**, optimized flow, travel breaks, meal time suggestions, and a smooth itinerary that helps travelers make the most of their day.

This project is powered by **LangChain + Groq (Llama 70B)** and deployed with a full DevOps stack including **Docker, Kubernetes, GCP VM**, and centralized logging using the **ELK Stack (Elasticsearch, Logstash, Kibana) with Filebeat**.

---

## 🚀 Features

✅ AI-powered full-day travel itinerary generation  
✅ Time-slot based planning (Morning → Afternoon → Evening)  
✅ User provides:
- City / Location
- Places to visit
- Preferences (optional)

✅ Agent outputs:
- Proper travel schedule
- Time allocations per place
- Suggested breaks and meals
- Optimized sequence of travel

✅ Streamlit-based UI for interactive planning  
✅ Containerized with Docker  
✅ Deployable on Kubernetes (Minikube)  
✅ CI/CD ready deployment on GCP VM  
✅ Logging + Monitoring using ELK Stack  
- Elasticsearch
- Logstash
- Kibana
- Filebeat

---

## 🧠 Tech Stack

### 🏗️ Core Development
- **Python**
- **Streamlit** (Frontend UI)
- **LangChain**
- **Groq API**
- **Llama 3 (70B model)**

### ☁️ DevOps / Deployment
- **Docker**
- **Kubernetes (Minikube + kubectl)**
- **Google Cloud Platform (GCP VM)**

### 📊 Logging & Monitoring (Observability)
- **Elasticsearch**
- **Logstash**
- **Filebeat**
- **Kibana**

---

## 📂 Project Structure

```bash
AI-Travel-Planner-Agent/
│── src/
│   ├── chains/              # LangChain agent chains and prompts
│   ├── config/              # API keys, model configs, constants
│   ├── core/                # Core logic of travel planner agent
│   ├── utils/               # Helper utilities
│   └── __init__.py
│
│── app.py                   # Streamlit entry point
│── Dockerfile               # Docker build file
│── requirements.txt         # Python dependencies
│── setup.py
│
│── k8s-deployment.yaml      # Kubernetes deployment manifest
│── elasticsearch.yaml       # Elasticsearch deployment/service
│── logstash.yaml            # Logstash deployment/service
│── kibana.yaml              # Kibana deployment/service
│── filebeat.yaml            # Filebeat configuration
│
│── .env                     # Environment variables (DO NOT COMMIT)
│── .gitignore
│── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Sumit-Prasad01/AI-Travel-Planner.git
cd AI-Travel-Planner-Agent
```

---

### 2️⃣ Create Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_groq_api_key_here
MODEL_NAME=llama-3.1-70b-versatile
```

⚠️ Do not push `.env` to GitHub. Always keep API keys private.

---

## ▶️ Run the Application Locally

```bash
streamlit run app.py
```

Then open in browser:

```
http://localhost:8501
```

---

## 🧪 How It Works

### 📌 User Input
The user provides:

- **Location / City**
- List of **places to visit**
- Optional preferences:
  - Budget
  - Travel style
  - Food preference
  - Start/end time

### 📌 AI Planning
Using LangChain + Groq Llama 70B, the agent generates:

- A complete **day itinerary**
- Proper time slots (example: 9:00 AM - 10:30 AM)
- Suggested breaks and meal times
- Smooth travel flow between places

### 📌 Final Output
The Streamlit UI shows:

- Full itinerary schedule
- Well-formatted time slots
- Travel day plan summary

---

## 📅 Example Output

**Input:**  
📍 Location: Bangalore  
🏛️ Places: Lalbagh, Cubbon Park, UB City, Bangalore Palace  

**Generated Itinerary Example:**

| Time Slot | Activity |
|----------|----------|
| 08:30 AM - 09:00 AM | Breakfast & Start Travel |
| 09:00 AM - 10:30 AM | Visit Lalbagh Botanical Garden |
| 10:30 AM - 11:00 AM | Travel to Cubbon Park |
| 11:00 AM - 12:30 PM | Explore Cubbon Park |
| 12:30 PM - 01:30 PM | Lunch Break |
| 01:30 PM - 02:00 PM | Travel to Bangalore Palace |
| 02:00 PM - 04:00 PM | Visit Bangalore Palace |
| 04:00 PM - 05:00 PM | Coffee Break |
| 05:00 PM - 07:00 PM | Explore UB City & Shopping |
| 07:00 PM - 08:30 PM | Dinner & Wrap-up |

---

# 🐳 Docker Setup

### Build Docker Image

```bash
docker build -t ai-travel-planner-agent .
```

### Run Docker Container

```bash
docker run -p 8501:8501 --env-file .env ai-travel-planner-agent
```

Now access:

```
http://localhost:8501
```

---

# ☸️ Kubernetes Deployment (Minikube)

### 1️⃣ Start Minikube

```bash
minikube start
```

---

### 2️⃣ Apply Kubernetes Deployment

```bash
kubectl apply -f k8s-deployment.yaml
```

---

### 3️⃣ Verify Pods

```bash
kubectl get pods
```

---

### 4️⃣ Access Streamlit Service

If service is configured:

```bash
minikube service ai-travel-planner-service
```

---

# 📊 ELK Stack Setup (Elasticsearch + Logstash + Kibana + Filebeat)

This project integrates centralized logging using the ELK stack.

### 📌 Components

- **Filebeat** → collects application logs
- **Logstash** → processes & forwards logs
- **Elasticsearch** → stores logs
- **Kibana** → visualizes logs & dashboards

---

## 🚀 Deploy ELK Stack on Kubernetes

Apply manifests:

```bash
kubectl apply -f elasticsearch.yaml
kubectl apply -f logstash.yaml
kubectl apply -f kibana.yaml
kubectl apply -f filebeat.yaml
```

Verify running pods:

```bash
kubectl get pods
```

---

## 🔍 Access Kibana Dashboard

Port forward Kibana:

```bash
kubectl port-forward svc/kibana 5601:5601
```

Then open:

```
http://localhost:5601
```

---

# ☁️ Deploy on GCP VM

This project is production-ready for deployment on a Google Cloud VM.

### Steps
1. Create a VM instance (Ubuntu recommended)
2. Install:
   - Docker
   - Kubernetes (Minikube + kubectl)
   - Git
3. Clone the repository
4. Build Docker image
5. Deploy application + ELK stack via Kubernetes YAMLs
6. Access app through VM external IP

---

# 🛡️ Security Best Practices

- Never commit `.env` file
- Use Kubernetes Secrets / GCP Secret Manager
- Store API keys in Jenkins/GitHub secrets
- Rotate Groq API keys if leaked

---

# 📌 Future Improvements

- Multi-day itinerary planning
- Hotel and transport recommendation integration
- Map-based route optimization
- Cost estimation per itinerary
- PDF itinerary export
- User authentication & saved trips

---


