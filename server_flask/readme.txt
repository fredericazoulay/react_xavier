https://medium.com/code-divoire/cr%C3%A9ation-dune-application-web-avec-python-et-react-partie-2-frontend-ced7e2883030
https://medium.com/code-divoire/cr%C3%A9ation-dune-application-web-avec-python-et-react-partie-1-backend-b5efb8a6a0c5

cd C:\Users\DELL\Documents\Projets\notes\server_python

sudo pip3 install Flask mysqlclient python-docx
python app.py

curl -i -H “Accept: application/json” -H “Content-Type: application/json” -X GET http://localhost:5000/api/v1.0/etudiant
curl -X POST  -H "Accept: Application/json" -H "Content-Type: application/json" http://localhost:5000/api/v1.0/etudiant -d '{"matricule":"1234","nom":"test", "prenom": "test"}'
