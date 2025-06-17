from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# Updated dataset and model setup
# Replace with your actual dataset and trained model
data = {
    'Career': [
        'Software Engineer', 'Data Scientist', 'Bioinformatician', 'Graphic Designer', 'Artificial Intelligence',
        'Blockchain Technology', 'Cloud Computing', 'Computer Graphics', 'Computer Vision', 'Cybersecurity',
        'Data Mining', 'Data Privacy', 'Digital Forensics', 'Distributed Systems', 'Game Development',
        'Geographic Information Systems', 'Human-Computer Interaction', 'Information Retrieval', 'IoT (Internet of Things)',
        'Machine Learning', 'Mobile App Development', 'Natural Language Processing', 'Network Security',
        'Quantum Computing', 'Software Development', 'Software Engineering', 'Web Development'
    ],
    'GPA': [8.5, 7.5, 8.0, 6.5, 9.0, 8.2, 7.8, 8.1, 7.7, 8.3, 8.4, 7.9, 8.6, 8.7, 7.6, 8.0, 7.8, 8.1, 7.5, 8.2,
            7.9, 8.3, 8.5, 7.7, 8.6, 8.4, 7.8],
    'Python Skill': ['Strong', 'Average', 'Weak', 'Average', 'Strong', 'Average', 'Strong', 'Weak', 'Average', 'Strong',
                      'Average', 'Strong', 'Average', 'Strong', 'Weak', 'Strong', 'Average', 'Weak', 'Strong', 'Average',
                      'Strong', 'Weak', 'Average', 'Strong', 'Weak', 'Strong', 'Average'],
    'SQL Skill': ['Average', 'Strong', 'Weak', 'Average', 'Strong', 'Weak', 'Average', 'Strong', 'Weak', 'Average',
                   'Strong', 'Average', 'Weak', 'Strong', 'Average', 'Weak', 'Strong', 'Average', 'Weak', 'Strong',
                   'Average', 'Strong', 'Weak', 'Average', 'Strong', 'Weak', 'Average'],
    'Java Skill': ['Strong', 'Weak', 'Average', 'Strong', 'Weak', 'Average', 'Strong', 'Weak', 'Strong', 'Average',
                    'Weak', 'Average', 'Strong', 'Weak', 'Average', 'Strong', 'Weak', 'Average', 'Strong', 'Weak',
                    'Average', 'Strong', 'Weak', 'Average', 'Strong', 'Weak', 'Average']
}
df = pd.DataFrame(data)

# Encoding categorical features
le = LabelEncoder()
df['Python Skill'] = le.fit_transform(df['Python Skill'])
df['SQL Skill'] = le.fit_transform(df['SQL Skill'])
df['Java Skill'] = le.fit_transform(df['Java Skill'])

# Dummy model (replace with your trained model)
model = RandomForestClassifier()
X = df[['GPA', 'Python Skill', 'SQL Skill', 'Java Skill']]
y = df['Career']
model.fit(X, y)

# Career-specific recommendations
recommendations = {
    'Software Engineer': {
        'skills': 'Programming, Problem-solving, Algorithms',
        'resources': 'Codecademy, Coursera - Programming for Everybody',
        'advice': 'Develop strong programming skills and work on personal projects.'
    },
    'Data Scientist': {
        'skills': 'Statistics, Machine Learning, Python',
        'resources': 'Kaggle, DataCamp - Data Scientist with Python',
        'advice': 'Focus on data manipulation and statistical analysis techniques.'
    },
    'Bioinformatician': {
        'skills': 'Bioinformatics, Data Analysis, Python',
        'resources': 'Coursera - Bioinformatics Specialization, Udemy - Python for Bioinformatics',
        'advice': 'Develop strong skills in data analysis, molecular biology, and computational tools.'
    },
    'Graphic Designer': {
        'skills': 'Graphic Design, Creativity, Adobe Creative Suite',
        'resources': 'Udemy - Graphic Design Bootcamp, Lynda - Photoshop CC Tutorials',
        'advice': 'Build a strong portfolio and stay updated with design trends.'
},
    'Artificial Intelligence': {
        'skills': 'Machine Learning, Neural Networks, Python',
        'resources': 'Coursera - AI for Everyone, edX - Artificial Intelligence',
        'advice': 'Focus on developing a deep understanding of AI techniques and algorithms.'
    },
    'Blockchain Technology': {
        'skills': 'Blockchain Fundamentals, Cryptography, Smart Contracts',
        'resources': 'Udemy - Blockchain Basics, Coursera - Blockchain Specialization',
        'advice': 'Understand the principles of blockchain and stay updated with new advancements.'
    },
    'Cloud Computing': {
        'skills': 'Cloud Platforms, Networking, Security',
        'resources': 'AWS Training, Google Cloud Platform - Fundamentals',
        'advice': 'Gain hands-on experience with cloud platforms and learn about cloud architecture.'
    },
    'Computer Graphics': {
        'skills': '3D Modeling, Animation, Graphics Programming',
        'resources': 'Udemy - Computer Graphics Fundamentals, Coursera - Computer Graphics',
        'advice': 'Build a strong portfolio showcasing your graphics projects and animations.'
    },
    'Computer Vision': {
        'skills': 'Image Processing, Machine Learning, OpenCV',
        'resources': 'Udacity - Computer Vision Nanodegree, Coursera - Computer Vision Basics',
        'advice': 'Focus on mastering image processing techniques and machine learning for visual tasks.'
    },
    'Cybersecurity': {
        'skills': 'Network Security, Ethical Hacking, Risk Management',
        'resources': 'Cybrary - Cybersecurity Courses, Udemy - Ethical Hacking Bootcamp',
        'advice': 'Develop strong skills in security protocols and stay updated with cybersecurity trends.'
    },
    'Data Mining': {
        'skills': 'Data Analysis, Data Visualization, SQL',
        'resources': 'Coursera - Data Mining Specialization, Udacity - Data Analyst Nanodegree',
        'advice': 'Learn data mining techniques and practice on large datasets to uncover insights.'
    },
    'Data Privacy': {
        'skills': 'Data Protection, Compliance, Risk Management',
        'resources': 'Coursera - Data Privacy Fundamentals, Udemy - Data Privacy and Protection',
        'advice': 'Understand data privacy regulations and best practices for protecting sensitive information.'
    },
    'Digital Forensics': {
        'skills': 'Digital Investigation, Evidence Collection, Analysis',
        'resources': 'Udemy - Digital Forensics, Coursera - Cybersecurity and Forensics',
        'advice': 'Gain expertise in investigating digital crimes and handling digital evidence.'
    },
    'Distributed Systems': {
        'skills': 'System Architecture, Data Consistency, Scalability',
        'resources': 'Coursera - Distributed Systems, edX - Building Scalable Systems',
        'advice': 'Understand the principles of distributed computing and practice designing scalable systems.'
    },
    'Game Development': {
        'skills': 'Game Design, Programming, 3D Modeling',
        'resources': 'Udemy - Game Development with Unity, Coursera - Game Design and Development',
        'advice': 'Build games and develop a portfolio showcasing your game development skills.'
    },
    'Geographic Information Systems': {
        'skills': 'GIS Software, Spatial Analysis, Cartography',
        'resources': 'Coursera - GIS Specialization, Udemy - GIS Fundamentals',
        'advice': 'Learn to analyze spatial data and work with GIS tools and software.'
    },
    'Human-Computer Interaction': {
        'skills': 'User Research, Interface Design, Usability Testing',
        'resources': 'Coursera - Human-Computer Interaction, Udemy - UX Design',
        'advice': 'Focus on creating user-friendly interfaces and conducting usability tests.'
    },
    'Information Retrieval': {
        'skills': 'Search Algorithms, Data Indexing, Natural Language Processing',
        'resources': 'Coursera - Information Retrieval, edX - Information Retrieval and Search Engines',
        'advice': 'Develop skills in designing and optimizing search algorithms and data retrieval techniques.'
    },
    'IoT (Internet of Things)': {
        'skills': 'Embedded Systems, Networking, Data Analytics',
        'resources': 'Udemy - IoT for Beginners, Coursera - IoT Specialization',
        'advice': 'Understand IoT architecture and develop skills in connecting and managing smart devices.'
    },
    'Machine Learning': {
        'skills': 'Supervised Learning, Unsupervised Learning, Python',
        'resources': 'Coursera - Machine Learning by Andrew Ng, Udacity - Machine Learning Engineer',
        'advice': 'Master machine learning algorithms and work on real-world data projects.'
    },
    'Mobile App Development': {
        'skills': 'App Design, Programming, Mobile Frameworks',
        'resources': 'Udemy - Mobile App Development with Flutter, Coursera - Mobile App Development Specialization',
        'advice': 'Build apps for mobile platforms and stay updated with the latest mobile development trends.'
    },
    'Natural Language Processing Specialist': {
        'Skills': ['Natural Language Processing', 'Text Analysis', 'Machine Learning'],
        'Resources': ['Coursera - Natural Language Processing Specialization', 'Udacity - NLP Nanodegree'],
        'Advice': 'Focus on understanding and developing models for processing and analyzing human language.'
    },
    'Network Security Engineer': {
        'Skills': ['Network Security', 'Firewalls', 'Intrusion Detection'],
        'Resources': ['Cybrary - Network Security Fundamentals', 'Udemy - Network Security and Ethical Hacking'],
        'Advice': 'Strengthen your understanding of network security protocols and protection measures.'
    },
    'Quantum Computing Specialist': {
        'Skills': ['Quantum Computing', 'Quantum Algorithms', 'Mathematics'],
        'Resources': ['Coursera - Quantum Computing Basics', 'Udemy - Introduction to Quantum Computing'],
        'Advice': 'Develop a solid grasp of quantum algorithms and their applications.'
    },
    'Software Development Manager': {
        'Skills': ['Software Development', 'Project Management', 'Team Leadership'],
        'Resources': ['Udemy - Software Development Manager Course', 'Coursera - Software Project Management'],
        'Advice': 'Focus on managing development projects and leading technical teams effectively.'
    },
    'Software Engineering': {
        'Skills': ['Software Engineering', 'System Design', 'Coding Standards'],
        'Resources': ['Coursera - Software Engineering Specialization', 'Udemy - Software Engineering Essentials'],
        'Advice': 'Deepen your knowledge in software design patterns and best practices in software engineering.'
    },
    'Web Developer': {
        'Skills': ['Web Development', 'HTML/CSS', 'JavaScript'],
        'Resources': ['Udemy - The Web Developer Bootcamp', 'Coursera - Web Design for Everybody'],
        'Advice': 'Enhance your skills in frontend and backend web development technologies.'
    }
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    gpa = float(request.form['gpa'])
    python_skill = request.form['python_skill']
    sql_skill = request.form['sql_skill']
    java_skill = request.form['java_skill']

    # Convert skill levels to numeric
    python_skill_encoded = le.transform([python_skill])[0]
    sql_skill_encoded = le.transform([sql_skill])[0]
    java_skill_encoded = le.transform([java_skill])[0]

    # Predict career
    features = np.array([[gpa, python_skill_encoded, sql_skill_encoded, java_skill_encoded]])
    predicted_career = model.predict(features)[0]

    # Get recommendations for the predicted career
    rec = recommendations.get(predicted_career, {
        'skills': 'N/A',
        'resources': 'N/A',
        'advice': 'N/A'
    })

    return render_template('result.html', career=predicted_career, **rec)

if __name__ == '__main__':
    app.run(debug=True)