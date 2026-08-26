
def read_file(filename):

    with open(filename, "r") as file:
        content = file.read()
    return content


def find_matching_skills (resume_skills, job_skills) :
    matching=[]
    for skill in job_skills:
        if skill in resume_skills:
            matching.append(skill)
    
    return matching

 
def find_missing_skills(resume_skills, job_skills):

    missing = []

    for skill in job_skills:

        if skill not in resume_skills:
            missing.append(skill)

    return missing


def calculate_score(matching,job_skills ) :
    if len(matching) ==0 or len(job_skills) ==0 :
        return 0
    
    score= (len(matching)/len(job_skills)) *100
    
    return score
    
 

class Resume :
    def __init__(self, text):
        self.text= text
        self.skills =[]
        
    def extract_skills(self):

        available_skils = [
        "React",
        "Next.js",
        "JavaScript",
        "TypeScript",
        "Node.js",
        "Python",
        "FastAPI",
        "AWS",
        "GraphQL",
        "Redux",
        "CI/CD",
        "Linux",
        "HTML",
        "Mongoose",
        ]   
         
        for skill in available_skils:
            if skill.lower() in self.text.lower() :
                self.skills.append(skill)

   


class JobDescription:

    def __init__(self, text):
        self.text = text
        self.required_skills = []
        
    def extract_skills(self):

        available_skills = [
            "React",
            "Next.js",
            "JavaScript",
            "TypeScript",
            "Node.js",
            "Python",
            "FastAPI",
            "AWS",
            "GraphQL",
            "Redux",
        ]

        for skill in available_skills:

            if skill.lower() in self.text.lower():
                self.required_skills.append(skill)
                
                
                

class ResumeAnalyzer:

    def __init__(self, resume, job_description):
        self.resume = resume
        self.job_description = job_description

    def find_matching_skills(self):

        matching = []

        for skill in self.job_description.required_skills:

            if skill in self.resume.skills:
                matching.append(skill)

        return matching
    
    def find_missing_skills(self):

        missing = []

        for skill in self.job_description.required_skills:

            if skill not in self.resume.skills:
                missing.append(skill)

        return missing
    
    def calculate_score(self):

        matching = self.find_matching_skills()

        total_required = len(
            self.job_description.required_skills
        )

        if total_required == 0:
            return 0

        score = (len(matching) / total_required) * 100

        return score
    
    def analyze(self):

        matching = self.find_matching_skills()
        missing = self.find_missing_skills()
        score = self.calculate_score()

        return {
            "matching": matching,
            "missing": missing,
            "score": score
        }