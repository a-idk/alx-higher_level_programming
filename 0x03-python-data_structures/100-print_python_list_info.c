#include <Python.h>

/**
 * print_python_list_info - function that prints basic info
 * about Python lists.
 * @p: PyObject list
 * @a_idk code
 *
 * Return: Nada!
 */

void print_python_list_info(PyObject *p)
{
	/* declaring variable */
	PyObject *object;
	int size;
	int idx;
	int allocate;

	/* initializing variables */
	size = Py_SIZE(p);
	allocate = ((PyListObject *)p)->allocated;
	/* print size of list */
	printf("[*] Size of the Python List = %d\n", size);
	/* print no. of allocation */
	printf("[*] Allocated = %d\n", allocate);
	for (idx = 0; (idx < size); idx += 1)
	{
		printf("Element %d: ", idx), object = PyList_GetItem(p, idx);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}
