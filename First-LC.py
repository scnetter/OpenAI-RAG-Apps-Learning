# Simple prompt chaining with a Model. This is code from the learning course reproduced for reference and practice.

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain

from langchain.prompts import PromptTemplate
import os

def main():

    def demosimple1():
        """
        This Function Demonstrates the use off the of the shelf LLMChain to combine the Prompt and an LLM Call to get the desired response.
        """

        # Create a Prompt Template with an embedded variable
        template = """Question: {question}
        
        Answer:"""

        prompt = PromptTemplate(
            template=template,
            input_variables = ['question']
        )

        # User question
        question = "Which is the most popular game in America?"

        # create the LLM Object
        llm = ChatOpenAI(model='gpt-3.5-turbo')

        # user the LLMChain to stitch the prompt and llm together - LLMChain is used to run queries against LLMs.
        # The LLMChain consists of a PromptTemplate, a language model, and an optional output parser.

        # LLMChain is deprecated. Better to use LCEL:
        # llm_chain = prompt | model
        llm_chain = LLMChain(prompt=prompt, llm=llm)

        # Invoke (run) the LLM Chain - the Chain returns a Dictionary of Named Outputs
        print(llm_chain.invoke(question)['text'])



    def demosimple2():
        """
        This Function Demonstrates a simple use of LCEL to create a custom Chain with the Prompt and Model
        """

        # Create the prompt template
        prompt = ChatPromptTemplate.from_template("Tell me a few key achievements of {name}")

        # Create the LLM Object
        llm = ChatOpenAI(model='gpt-3.5-turbo')

        # Use LCEL to build the chain
        chain = prompt | llm

        # Invoke the chain and print the text response. Pass the named input variable in as a dictionary
        print(chain.invoke({'name': 'Donald Trump'}).content)


    # print(demosimple1.__doc__)
    # demosimple1()

    print(demosimple2.__doc__)
    demosimple2()



if __name__ == '__main__':
    main()