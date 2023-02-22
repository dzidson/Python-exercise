def has_required_skills(person, skills):
    return all(skill in person[skills] for skill in skills)



john = { 
    'name': 'John Doe',
    'age': 30,
    'skills': ['Phyton', 'JavaScript', 'C++']
}

annie = { 
    'name': 'Annie McDonald',
    'age': 30,
    'skills': ['JavaScript', 'C++']
}

poszukiwany_skill = ['JavaScript', 'Phyton']

print(has_required_skills(john, poszukiwany_skill))
print(has_required_skills(annie, poszukiwany_skill))