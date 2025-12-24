"""
Job / Course Recommendation System (Rule-Based)
Author: Student Project
Language: Python
"""

def recommend_job_and_courses(skills, interest):
    """
    Recommends job role and courses based on skills and interest
    """
    skills = [skill.strip().lower() for skill in skills]

    recommendations = {
        "data": {
            "python": (
                "Data Analyst",
                ["SQL", "Power BI", "Statistics", "Excel Advanced"]
            )
        },
        "ai": {
            "python": (
                "Machine Learning Engineer",
                ["Machine Learning", "Deep Learning", "Python Advanced"]
            )
        },
        "web": {
            "java": (
                "Backend Developer",
                ["Spring Boot", "REST APIs", "SQL"]
            ),
            "html": (
                "Frontend Developer",
                ["JavaScript", "React", "UI/UX Basics"]
            )
        }
    }

    if interest in recommendations:
        for skill in skills:
            if skill in recommendations[interest]:
                return recommendations[interest][skill]

    return (
        "Career Exploration",
        ["Python Basics", "Problem Solving", "Data Structures"]
    )


def main():
    print("=" * 45)
    print("   JOB / COURSE RECOMMENDATION SYSTEM")
    print("=" * 45)

    skills_input = input("Enter your skills (comma separated): ").split(",")
    interest_input = input("Enter your interest (data / ai / web): ").lower()

    job, courses = recommend_job_and_courses(skills_input, interest_input)

    print("\nRecommended Job Role:", job)
    print("Recommended Courses:")
    for course in courses:
        print(" -", course)


if _name_ == "_main_":
    main()