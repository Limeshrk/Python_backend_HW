import unicodedata
names = [['Kovács', 'Béla'], ['Kiss', 'Gyula'], ['Szabó', 'Ervin']]

#Email generálása a név részek összefüzésével és normalizálásával
def generate_email(name_parts):
  normalized_name_parts = [unicodedata.normalize('NFKD', part).encode('ASCII', 'ignore').decode('utf-8').lower() for part in name_parts]
  email = '.'.join(normalized_name_parts) + "@company.hu"
  return email

def create_user_data(names):
  users = []
  for name in names:
    email = generate_email(name)
    familyname = name[0] #a passwordhoz szükséges
    password = f"{unicodedata.normalize('NFKD', familyname).encode('ASCII', 'ignore').decode('utf-8')}123Start"
    user = {
      'name': name,
      'email': email,
      'password': password
    }
    users.append(user)
    print(user)
  return users
    
def write_to_file(users):
  users.sort(key=lambda x: (' '.join(x['name'])).lower()) #ABC sorrend
  with open('nevek.txt', 'w') as f:
    for user in users:
      f.write(f"{' '.join(user['name'])} {user['email']} {user['password']}\n")

users = create_user_data(names)
#print (users)
write_to_file(users)
