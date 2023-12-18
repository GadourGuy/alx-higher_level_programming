#include <Python.h>

void print_python_bytes(PyObject *p) {
    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        fflush(stdout);
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    char *str = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", str);

    printf("  first 10 bytes: ");
    for (Py_ssize_t i = 0; i < size && i < 10; ++i) {
        printf("%02x ", str[i] & 0xff);
    }
    printf("\n");

    fflush(stdout);
}

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *element;

    printf("[*] Python list info\n");

    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid List Object\n");
        fflush(stdout);
        return;
    }

    size = PyList_Size(p);

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; ++i) {
        element = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);

        if (PyBytes_Check(element))
            print_python_bytes(element);
        else if (PyFloat_Check(element))
            print_python_float(element);
    }

    fflush(stdout);
}

void print_python_float(PyObject *p) {
    printf("[.] float object info\n");

    if (!PyFloat_Check(p)) {
        printf("  [ERROR] Invalid Float Object\n");
        fflush(stdout);
        return;
    }

    printf("  value: %f\n", PyFloat_AS_DOUBLE(p));
    fflush(stdout);
}

