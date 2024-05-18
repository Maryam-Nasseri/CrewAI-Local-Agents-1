#set the variables
model_name="mistral"
custom_model_name="mistralcrew"

#pull mistral from ModelFile
ollama pull $model_name

#create a new model based on mistral
ollama create $custom_model_name -f ./mistral-crew-ModelFile
