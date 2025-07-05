# EXO-FIN-GPT v2.0.1-PROCFILE
Compatible with Railway using Procfile only.
To test locally:
  uvicorn exo_fin_gpt.exo_interface_api.exo_interface_api:app --port 8000
To test endpoints:
  curl http://localhost:8000/health
