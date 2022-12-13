
from ngshare import configureExchange # pyright: reportMissingImports=false

c = get_config() # pyright: reportUndefinedVariable=false
# Note: It's important to specify the right ngshare URL when not using k8s
configureExchange(c, 'http://127.0.0.1:10101/services/ngshare')

# Add the following to let students access courses without configuration
# For more information, read Notes for Instructors in the documentation
c.CourseDirectory.course_id = '*'