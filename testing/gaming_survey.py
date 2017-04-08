# An instance of the class object, Survey, for practice testing a class:

from survey import Survey
from IPython import embed

# Define a question, make a survey:
question = "What games do you remember first playing?"
my_survey = Survey(question)
# embed()
# Show the question, store the responses to the question:
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Games: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the results:
print("Sweet! Here are the results:")
my_survey.show_results()
