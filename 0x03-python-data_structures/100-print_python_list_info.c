#include <python.h>

/**
  * print_python_list_info - prints some
  * basic info about Python lists
  * @p: python object
  * Return: 0
  */

void print_python_list_info(PyObject *p)
{
int size, allocation, i;
pyobject *obj;

size = PY_SIZE(p);
allocation = ((pylistobject *)p)->allocated;

printf("[*] Size of the Python List = %d\n", size);
printf("[*] Allocated = %d\n", allocation);
for (i = 0, i < size, i++)
{
	printf("Element %d: ", i);
	obj = pylist_GetItem(p, i);
	printf("%s\n", py_TYPE(obj)->tp_name);
}
}
