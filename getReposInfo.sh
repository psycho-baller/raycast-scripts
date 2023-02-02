#!/bin/bash

echo "Repository Name, Repository URL, Tech Stack, Languages" > repos_info.csv

org_name="ibm-skills-network"
personal_access_token="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"


# get a list of all repositories in the organization
list1=$(curl -s -H "Authorization: token $personal_access_token" "https://api.github.com/orgs/$org_name/repos?page=1&per_page=100" | jq '.[].name' | tr -d '"')
list2=$(curl -s -H "Authorization: token $personal_access_token" "https://api.github.com/orgs/$org_name/repos?page=2&per_page=100" | jq '.[].name' | tr -d '"')

repo_list=$(echo "$list1 $list2")

# Loop through each repository
for repo in $repo_list; do

  # Check if repository is archived
  is_archived=$(curl -s -H "Authorization: token $personal_access_token" https://api.github.com/repos/$org_name/$repo | jq '.archived')
  
  # If the repository is not archived
  if [ "$is_archived" = "false" ]; then

    # Get the repository URL
    repo_url=$(curl -s -H "Authorization: token $personal_access_token" https://api.github.com/repos/$org_name/$repo | jq -r '.html_url')
    
    # Get the tech stack for the repository
    tech_stack=$(curl -s -H "Authorization: token $personal_access_token" https://api.github.com/repos/$org_name/$repo/topics  | jq -r '.names[]' | tr '\n' ',' | head -c -1)
    echo $tech_stack
    # Get the three most used languages for the repository
    languages=$(curl -s -H "Authorization: token $personal_access_token" https://api.github.com/repos/$org_name/$repo/languages | jq -r 'keys[] as $k | "\($k), \(.[$k])"' | sort -t, -k2 -nr | awk -F, '{print $1}' | tr '\n' ',' | head -c -1)
    echo $languages
    # Write the repository name, URL, languages, and tech stack to a CSV file
    echo "$repo,$repo_url,$tech_stack,$languages" >> repos_info.csv
  fi
done
