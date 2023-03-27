# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

self_assessment_mock = [  
  {
    'id': 1,
    'knowledgeLevel': '2',
  },
  {
    'id': 2,
    'knowledgeLevel': '3',
  },
  {
    'id': 3,
    'knowledgeLevel': '4',
  },
  {
    'id': 4,
    'knowledgeLevel': '1',
  },
]

question = {
    "id": 20,
    "questionBody": "Question 1",
    "questionAnswers": [
        {
            "id": 20,
            "description": "Answer 1",
            "rightAnswer": False
        },
        {
            "id": 21,
            "description": "Answer 2",
            "rightAnswer": True
        },
        {
            "id": 22,
            "description": "Answer 3",
            "rightAnswer": False
        },
        {
            "id": 23,
            "description": "Answer 4",
            "rightAnswer": False
        }
    ]
}

@app.post("/self-assessment")
def add_self_assessment():
    if request.is_json:
        self_assessment = request.get_json()
        
        # save on database

        return {"message": "Self assessment saved with success!"}, 201
    return {"error": "Request must be JSON"}, 415

@app.get("/new-assessment/<engineeringProfile_id>/<collaborator_id>'")
def new_assessment(engineeringProfile):

    #buscar na tabela de users o colaborador com o respectivo ID


    #create new assessment on database and return the assessment id and the first question

    return {"id": 1, "question": question}, 200
    #return jsonify(skills)

@app.post("/save-question-answer")
def add_save_question_answer():
    if request.is_json:
        answer = request.get_json()
        
        # get the answer, process on model
        # when is not the last one:
            # return the next question
        # when is the last one:
            # return question empty

        return jsonify(question), 200
    return {"error": "Request must be JSON"}, 415

@app.get("/assessment/<id>'")
def get_assessment_result(id):
    #get the assessment output
    assessment_result = {}
    return jsonify(assessment_result)
