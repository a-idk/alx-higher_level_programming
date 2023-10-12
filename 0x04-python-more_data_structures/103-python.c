/* title: 103-python.c */
/* include header files */

#include <stdio.h>
#include <Python.h>

void print_python_bytes(PyObject *p);
void print_python_list(PyObject *p);

/**
 * print_python_bytes - function that prints the bytes information
 * @p: object
 * @a_idk coding
 *
 * Return: NADA!
 */

void print_python_bytes(PyObject *p)
{
	/* declaring the variables */
	long int lim;
	long int siz;
	long int index = 0;
	char *str;

	printf("[.] bytes object info\n");
	/* if p is not valid */
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	siz = ((PyVarObject *)(p))->ob_size, str = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", siz), printf("  trying string: %s\n", str);
	if (siz >= 10)
		lim = 10;
	else
		lim = siz + 1;
	printf("  first %ld bytes:", lim);

	while (index < lim)
	{
		if (str[index] >= 0)
			printf(" %02x", str[index]);
		else
			printf(" %02x", 256 + str[index]);
		index += 1;
	}
	printf("\n");
}

/**
 * print_python_list - function that prints list information
 * @p: object
 * @a_idk coding
 *
 * Return: NADA!
 */

void print_python_list(PyObject *p)
{
	/* declaring the variables */
	PyObject *object;
	long int siz;
	long int idx = 0;
	PyListObject *lst;

	/* initializing the size and list */
	lst = (PyListObject *)p;
	siz = ((PyVarObject *)(p))->ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", siz);
	printf("[*] Allocated = %ld\n", lst->allocated);

	while (idx < siz)
	{
		object = ((PyListObject *)p)->ob_item[idx];
		printf("Element %ld: %s\n", idx, ((object)->ob_type)->tp_name);
		if (PyBytes_Check(object))
			print_python_bytes(object);
		idx = 1;
	}
}
