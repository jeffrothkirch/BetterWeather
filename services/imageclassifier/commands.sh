curl -u "$BLUEMIX_USERNAME":"$BLUEMIX_PASSWORD" -X POST -F "images_file=@mountain.jpg" -F "classifier_ids=<classifierlist.json" "https://gateway.watsonplatform.net/visual-recognition-beta/api/v2/classify?version=2015-12-02"
curl -u "$BLUEMIX_USERNAME":"$BLUEMIX_PASSWORD" -X POST -F "images_file=@images.zip"  "https://gateway.watsonplatform.net/visual-recognition-beta/api/v2/classify?version=2015-12-02"