courses = {
    "Python for Beginners": ["python", "programming"],
    "Web Development": ["html", "css", "javascript"],
    "Machine Learning": ["python", "machine learning", "ai"],
    "Data Science": ["python", "data analysis", "machine learning"],
    "Cloud Computing": ["cloud", "aws"]
}

user_input = input("Enter your interests: ").lower()

user_interests = user_input.split(",")

for i in range(len(user_interests)):
    user_interests[i] = user_interests[i].strip()

scores = {}

for course in courses:
    score = 0

    for interest in user_interests:
        if interest in courses[course]:
            score += 1

    scores[course] = score

recommended = sorted(scores.items(),
                     key=lambda x: x[1],
                     reverse=True)

print("\nRecommended Courses:")

for course, score in recommended:
    if score > 0:
        print(course, "- Match Score:", score)