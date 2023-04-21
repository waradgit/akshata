from github import Github

# Authenticate with a personal access token
g = Github('<personal-access-token>')

# Get the repository where you want to upload the file
repo = g.get_repo('<username>/<repository>')

# Create a new file in the repository
file_name = 'example.txt'
file_content = 'This is an example file'
repo.create_file(file_name, 'Initial commit', file_content)

print('File uploaded successfully')
