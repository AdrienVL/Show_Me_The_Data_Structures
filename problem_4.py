class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
child2 = Group("child2")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)
parent_user = "parent_user"
parent.add_user(parent_user)

child.add_group(sub_child)
parent.add_group(child)
parent.add_group(child2)

#Hierarchy:
    # G-Parent -> G-Child -> G-Sub_Child -> U-sub_child


# print(sub_child.get_users()[0])

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """

    #Recursion - Assume Transitive relationship

    for username in group.get_users():
        if username == user:
            return True

    for sub_dir in group.get_groups():
        if is_user_in_group(user,sub_dir):
            return True
    
    return False

#Parent has no users. Child has no users... (sub-child-user, parent)

print(is_user_in_group("parent_user", parent))