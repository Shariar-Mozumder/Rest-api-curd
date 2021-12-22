from rest_framework import routers
from employeeapi.viewsets import EmployeeViewset

router=routers.DefaultRouter()
router.register('employee',EmployeeViewset)

#GET,POST,PUT,DELETE
#GET: list of all or retrive single object by id
