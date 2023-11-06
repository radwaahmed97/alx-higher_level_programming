#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Print list info about Python
 *
 * @p: Pyobjext pointer
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t i;
	Py_ssize_t len = PyList_Size(p);
	PyListObject *pob = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %ld\n", pob->allocated);

	for (i = 0; i < len; i++)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(pob->ob_item[i])->tp_name);
	}
}
