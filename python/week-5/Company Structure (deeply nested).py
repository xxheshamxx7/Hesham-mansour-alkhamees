company = {
    "ceo": "Ahmed",
    "departments": {
        "engineering": {
            "manager": "Sara",
            "team_size": 12,
            "projects": ["Backend API", "Mobile App"],
        },
        "design": {
            "manager": "Omar",
            "team_size": 5,
            "projects": ["Website Redesign"],
        },
    },
}

print(f"CEO: {company['ceo']}")

print(f"Engineering manager: {company['departments']['engineering']['manager']}")

print(f"Design team size: {company['departments']['design']['team_size']}")

print(f"First engineering project: {company['departments']['engineering']['projects'][0]}")

total_teams = company['departments']['engineering']['team_size'] + company['departments']['design']['team_size']
print(f"Total team size: {total_teams}")

company['departments']['design']['team_size'] = 6

company['departments']['marketing'] = {
    "manager": "Lina",
    "team_size": 3,
    "projects": []
}

print(f"Marketing: {company['departments']['marketing']}")
