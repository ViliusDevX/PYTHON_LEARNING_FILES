import requests


class Questionnaire:
    def __init__(self):
        self.questions = [
            "What is your age?",
            "What is your name?",
            "Tell me about your previous work experience. What were your primary responsibilities?",
            "How do you typically approach problem-solving?",
            "Describe a challenging situation at work and how you handled it.",
            "Are you more inclined toward working independently or in a team setting?",
            "What motivates you professionally?",
            "How do you manage your time and prioritize tasks?",
            "In what ways do you seek personal and professional development?",
            "Describe a situation where you had to adapt to a significant change at work?",
            "Do you prefer structured or more flexible work environments? Why?",
            "How do you handle conflicts or disagreements in a professional setting?",
            "What role do you usually take on in a team setting? Leader, collaborator, or supporter?",
            "Describe a situation where you had to multitask effectively. How did you manage it?",
            "What kind of work environment brings out your best performance?",
        ]
        self.choices = [
            [],  # age input
            [],  # name input
            ["Administrative/Operational", "Creative/Strategic", "Technical/Analytical"],
            ["Methodical and systematic", "Innovative and creative", "Collaborative and team-oriented"],
            ["Through careful planning and analysis", "By thinking outside the box and trying new approaches", "By involving and collaborating with others for solutions"],
            ["Prefer working independently", "Enjoy collaborating in a team", "Comfortable with both, depending on the task"],
            ["Personal growth and learning", "Making an impact and contributing meaningfully", "Recognition and advancement opportunities"],
            ["Follow a structured schedule and prioritize systematically", "Adapt and prioritize based on urgency and importance", "Rely on team collaboration and delegation for task management"],
            ["Pursuing formal education and certifications", "Seeking mentorship and guidance", "Continuous learning through experiences and challenges"],
            ["Adapted through careful planning and preparation", "Embraced change by exploring new possibilities", "Adapted by collaborating and involving others in the transition"],
            ["Prefer structured environments for clarity and focus", "Enjoy flexible settings for adaptability and creativity", "Comfortable with both depending on the nature of the work"],
            ["Address directly and resolve through clear communication", "Find compromises and common ground through discussion", "Seek mediation and involve others to find a solution"],
            ["Leader - prefer taking charge and guiding the team", "Collaborator - enjoy contributing equally with others", "Supporter - thrive in assisting and facilitating the team's success"],
            ["Prioritized tasks and managed them sequentially", "Handled tasks simultaneously by dividing attention effectively", "Delegated tasks or sought help to manage multiple responsibilities"],
            ["Quiet and structured environment for focused work", "Dynamic and collaborative space for idea exchange", "Adaptable settings based on the task at hand"]
        ]

    def conduct_survey(self):
        answers = []
        for i, question in enumerate(self.questions):
            if i == 0:  # Age
                user_age = input("Enter your age: ")
                answers.append(f"I'm {user_age} years old")
            elif i == 1:  # Name
                user_name = input("Enter your name: ")
                answers.append(f"My name is {user_name}")
            else:
                print(f"Question {i - 1}: {question}")
                print("Choose an answer:")
                for j, choice in enumerate(self.choices[i]):
                    print(f"{j + 1}. {choice}")

                user_answer = input("Enter your choice (1, 2, or 3): ")
                while user_answer not in ["1", "2", "3"]:
                    user_answer = input("Invalid input. Please enter 1, 2, or 3: ")

                answers.append(self.choices[i][int(user_answer) - 1])
            print()

        response_text = ", ".join(answers)
        print(f"Survey completed! Summary: {response_text}")

        formatted_output = f"User: {response_text}. Please suggest the top 5 jobs or businesses for me based on this information."
        return formatted_output


class APIRequest:
    def __init__(self, api_endpoint, api_key, api_host):
        self.api_endpoint = api_endpoint
        self.api_key = api_key
        self.api_host = api_host

    def make_request(self, user_profile):
        headers = {
            'X-RapidAPI-Host': self.api_host,
            'X-RapidAPI-Key': self.api_key,
            'Content-Type': 'application/json'
        }

        data = {
            'question': user_profile
        }

        response = requests.post(self.api_endpoint, headers=headers, json=data)

        if response.status_code == 200:
            print("Top 5 Job/Business Recommendations:")
            print(response.text)
        else:
            print(f"Error: {response.status_code} - {response.text}")


questionnaire = Questionnaire()
user_profile = questionnaire.conduct_survey()

api_endpoint = 'https://simple-chatgpt-api.p.rapidapi.com/ask'
api_key = 'my api'
api_host = 'simple-chatgpt-api.p.rapidapi.com'

rapid_api_handler = APIRequest(api_endpoint, api_key, api_host)
rapid_api_handler.make_request(user_profile)
