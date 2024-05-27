
# Luften
Luften is a project aimed at evaluating whether an AI Assistant can enhance the reading comprehension and metacognitive skills of children aged between 12-15. 
This involves a chatbot to interact with the children, and the faculty can review these interactions for further analysis.

## Working of Luften from a User Point of View
To start off, we will test the user's base comprehension level. 
Then they will be switched to the Luften tool which will guide the user through reading a paragraph and ensuring they are satisfied with their answers. 
After this process is finished, we will analyze their answers again to measure their improvement. 
Currently, this analysis is performed by GPT, but in the future, there are plans to create a tailor-made system to analyze the users' answers.

## Working of Luften - Reading Tutor (AI Assistant)
When the user is switched to our Luften tool, the reading tutor will first introduce them to the content they are going to read by providing some keywords and asking them to explain those words.
If the user does not give a satisfactory answer, the reading tutor will explain the keywords to them. Next, the user will be made to read the first paragraph. After reading it, the tutor will ask for their understanding of the paragraph.
If the tutor is satisfied with their comprehension, they will proceed to the next paragraph. This process continues until all paragraphs are read and understood. If the tutor is not satisfied, the user will be asked to read the paragraph again until their comprehension meets the tutor's expectations.

## Working of Luften Technically

### Admin Interface
The admin has access to:
- Creating and deleting users
- Exporting the conversation between the reading tutor (AI Assistant) and the user
- Choosing their assistant
- Viewing conversations of all users in the system

The admin will create the username and password for the user, and the user can log in using these credentials.

### User Interface
The user only has access to the page where they can interact with the Reading Tutor (AI Assistant) and can log in with the username and password provided by the admin.


## Tech Stack Used for Luften
- Svelte
- Flask
- Betaassi library
- OpenAI API key


