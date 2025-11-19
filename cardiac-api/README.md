Cardiac Simulator API

## Description

Cette API simule le fonctionnement du coeur humain et permet de générer des données cardiaques selon différentes conditions.
Elle est conçue pour tester des scénarios physiologiques tels que la tachycardie, la bradycardie, l’arythmie, et l’hypertension.

## Endpoints Disponibles

1. Obtenir le statut du coeur
   GET /api/cardiac/status
   Retourne l’état actuel du coeur (condition simulée).
   Exemple de réponse:
   {
   "organ": "heart",
   "condition": "normal"
   }

2. Obtenir les données cardiaques
   GET /api/cardiac/data
   Génère des données cardiaques en fonction de la condition actuelle, incluant:

- heart_rate : fréquence cardiaque
- blood_pressure : pression artérielle (systolique / diastolique)
- timestamp : horodatage Unix
  Exemple de réponse:
  {
  "heart_rate": 120,
  "blood_pressure": {
  "systolic": 130,
  "diastolic": 80
  },
  "timestamp": 1711382400.123456
  }

3. Simuler une condition cardiaque
   POST /api/cardiac/simulate/<condition>
   Change la condition du coeur pour la simulation.
   Paramètres acceptés :

- normal
- tachycardie
- bradycardie
- arythmie
- hypertension
  Exemple:
  POST /api/cardiac/simulate/tachycardie
  Exemple de réponse:
  {
  "message": "Condition applied",
  "condition": "tachycardie"
  }

4. Obtenir les paramètres disponibles
   GET /api/cardiac/parameters
   Retourne la liste des conditions cardiaques pouvant être simulées.
   Exemple de réponse:
   {
   "conditions": ["normal", "tachycardie", "bradycardie", "arythmie", "hypertension"]
   }

## Exemples d’Utilisation

Avec curl :

1. Obtenir le statut actuel du coeur :
   curl [http://localhost:5001/api/cardiac/status](http://localhost:5001/api/cardiac/status)

2. Simuler une tachycardie :
   curl -X POST [http://localhost:5001/api/cardiac/simulate/tachycardie](http://localhost:5001/api/cardiac/simulate/tachycardie)

3. Obtenir les données cardiaques après simulation :
   curl [http://localhost:5001/api/cardiac/data](http://localhost:5001/api/cardiac/data)

4. Voir les conditions simulables :
   curl [http://localhost:5001/api/cardiac/parameters](http://localhost:5001/api/cardiac/parameters)

Remarque :
Le serveur écoute par défaut sur le port 5001 et est configuré pour le mode debug.
