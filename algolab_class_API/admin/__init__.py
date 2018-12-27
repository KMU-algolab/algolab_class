from .course import CourseAdmin, StudentInCourse, LanguageOfCourseAdmin
from .language import LanguageAdmin
from .board import BoardAdmin
from .problem import ProblemAdmin, ProblemInCourseAdmin, ProblemTestCaseAdmin
from .userInfo import UserInfoAdmin

__all__ = ['CourseAdmin', 'StudentInCourse', 'LanguageOfCourseAdmin',
           'LanguageAdmin',
           'BoardAdmin',
           'ProblemAdmin', 'ProblemTestCaseAdmin', 'ProblemInCourseAdmin',
           'UserInfoAdmin']