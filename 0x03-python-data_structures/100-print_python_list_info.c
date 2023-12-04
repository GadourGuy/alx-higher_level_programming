#include <Python.h>

/**
 * print_python_list_info - prints Python lists.
 * @p: object to be printed
 *
 * Return: void.
 */

void print_python_list_info(PyObject *p)
{
	int alloc, size, j;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);
	for (j = 0; j < size; j++)
	{
		printf("Element %d: ", j);
		obj = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
