def group_list(members, users):
    member = members.join(user + ":" for user in users)
    return member

print(group_list("Marketting", ["Mike","Karen", "Jake","Tasha"]))