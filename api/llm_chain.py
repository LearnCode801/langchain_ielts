from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI


model=ChatOpenAI(
            temperature=0.6,
            model="gpt-3.5-turbo-16k"
            )


Prompt_template = PromptTemplate(
                            input_variables=["Question","Answer"],
                            template=""" As an expert in IELTS (International English Language Testing System), your role is to 
                              assess the writing proficiency of a user-entered answer, which is provided below:
                              
                              {Answer}
                                
                              You are required to examine the relevance of the answer to the given question, indicated as "{Question}" and "{Answer}" respectively.
                              Evaluate the answer {Answer} based on the following aspects of the IELTS writing test:

                              Task Achievement: Measure the relevance of the answer {Answer} to the question {Question}.
                              
                              Coherence and Cohesion: Assess the organization and logical flow of ideas in the response.
                              
                              Lexical Resource: Evaluate the richness and appropriateness of vocabulary used in the context.
                              
                              Grammatical Range and Accuracy: Examine the variety and correctness of grammatical structures in the answer.
                              
                              Total Score: Average of all above scores
                              
                              Your Output Should be the Just Python Dictionary that contains the key-value pair
                              in keys their exist different aspects and their respective score in the values of the dictionary

                              Remember: The All Results should be based OUT of 10 """,
                             
                             )

chain= LLMChain (llm=model, prompt=Prompt_template)


if __name__=="__main__":
    print(chain.run({
        "Question":"What is Your Name",
        "Answer":"My name is Muhammad Talha"
    }))