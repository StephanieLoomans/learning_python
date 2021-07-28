from user_import import User 
from privileges_import import Privileges, Admin


new_admin = Admin("Harry", "Potter", "Harry280", "01-05-2021", 7 )
print(new_admin.privileges.show_privileges())