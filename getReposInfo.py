import csv
import requests
import json

org_name = "ibm-skills-network"
personal_access_token = "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"

# Define the headers for the API requests
headers = {
    "Authorization": f"token {personal_access_token}",
}

# Get a list of all repository names in the organization
url = f"https://api.github.com/orgs/{org_name}/repos?page=1&per_page=100"
response = requests.get(url, headers=headers)
list1 = response.json()
list1 = [repo["name"] for repo in list1]

url = f"https://api.github.com/orgs/{org_name}/repos?page=2&per_page=100"
response = requests.get(url, headers=headers)
list2 = response.json()
list2 = [repo["name"] for repo in list2]

repo_list = list1 + list2

# Create a CSV file and write the header row
with open("repos_info.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Repository Name", "Repository URL", "Tech Stack", "Languages"])

    # Loop through each repository
    for repo in repo_list:
        # Check if repository is archived
        url = f"https://api.github.com/repos/{org_name}/{repo}"
        response = requests.get(url, headers=headers)
        is_archived = response.json()["archived"]

        # If the repository is not archived
        if not is_archived:
            # Get the repository URL
            repo_url = response.json()["html_url"]

            # Get the tech stack for the repository
            url = f"https://api.github.com/repos/{org_name}/{repo}/topics"
            response = requests.get(url, headers=headers)
            tech_stack = response.json().get("names", [])
            tech_stack = ",".join(tech_stack)

            # Get the three most used languages for the repository
            url = f"https://api.github.com/repos/{org_name}/{repo}/languages"
            response = requests.get(url, headers=headers)
            languages = response.json()
            sorted_langs = sorted(languages.items(), key=lambda x: x[1], reverse=True)
            top_3_langs = [lang[0] for lang in sorted_langs[:3]]
            languages = ",".join(top_3_langs)

            # Write the repository name, URL, languages, and tech stack to a CSV file
            writer.writerow([repo, repo_url, tech_stack, languages])
