from analyzer import read_file, Resume, JobDescription, ResumeAnalyzer

resume_text = read_file("resume.txt")
job_text = read_file("job_description.txt")


resume = Resume(resume_text)
job = JobDescription(job_text)

resume.extract_skills()
job.extract_skills()

analyzer = ResumeAnalyzer(resume, job)


result = analyzer.analyze()


print("Resume Skills:")
print(resume.skills)

print("\nJob Required Skills:")
print(job.required_skills)

print("\nMatching Skills:")
print(result["matching"])

print("\nMissing Skills:")
print(result["missing"])

print("\nScore:")
print(f"{result['score']:.2f}%")