import hashlib

u_usernames = []
u_hashes = []
s_passwords = []
s_hashes = []

with open("dump.txt", "r") as f:
  for s in f.read().split("\n"):
    a = s.split(":")
    u_usernames.append(a[0])
    u_hashes.append(a[1])

with open("p_in.txt", "r") as f:
  pass_raw = f.read().split("\n")

with open("p_out.txt", "r") as f:
  for s in f.read().split("\n"):
    a = s.split(":")
    s_hashes.append(a[0])
    s_passwords.append(a[1])

# print(*list(set(u_hashes)^set(s_hashes)), sep="\n")

# if hashlib.md5(a[1].encode()).hexdigest() == a[0]:
#   print(f"Verified: {a[0]}")
# else:
#   print(f"Failed: {a[0]}")
  
print("username,md5_hash,password")
for i in range(len(s_passwords)):
  curr_password = s_passwords[i]
  curr_hash = s_hashes[i]
  if curr_hash in u_hashes:
    curr_username = u_usernames[u_hashes.index(curr_hash)]
    print(curr_username, curr_hash, curr_password, sep=",")