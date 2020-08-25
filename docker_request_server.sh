# curl -d "[\"$1\"]" -H "Content-Type: application/json" -X POST http://localhost:5005/predict_images

curl -d "[\"$1\",\"$2\"]" -H "Content-Type: application/json" -X POST http://localhost:5005/predict_images

# curl -d "[$1]" -H "Content-Type: application/json" -X POST nima-http:5005/prediction