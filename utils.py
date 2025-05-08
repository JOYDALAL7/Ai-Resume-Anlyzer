import openai

def analyze_resume(resume_text, job_description):
    client = openai.OpenAI(api_key="sk-proj-HQxG19U_9LyTu2LFrD6IECns...")

    prompt = f"""You are a resume evaluator...
    Resume: {resume_text}
    Job Description: {job_description}
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
