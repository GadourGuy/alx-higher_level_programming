#include <Python.h>

void print_python_list_info(PyObject *p);

/**
 * print_python_list_info - print lists from python
 * @p: list to be printed.
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, alloc, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        printf("[ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    alloc = ((PyListObject *)p)->allocated;
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (i = 0; i < size; ++i)
    {
        item = PyList_GetItem(p, i);

        if (!item)
        {
		printf("Element %ld: %s\n", i, "Unknown");
        }
        else
        {
            printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        }
    }
}

/**
 * print_python_bytes_info - print bytes objects from Python
 * @p: bytes object to be printed.
 *
 * Return: void
 */

void print_python_bytes_info(PyObject *p)
{
    Py_ssize_t size, i;
    char *str;

    if (!PyBytes_Check(p))
    {
        printf("[ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    str = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str ? str : "(null)");

    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; ++i)
    {
        printf("%02x ", str[i] & 0xff);
    }
    printf("\n");
}

