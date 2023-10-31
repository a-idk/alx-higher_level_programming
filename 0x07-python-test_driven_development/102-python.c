/* Title: 102-python.c */
/* Include header files */
#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string.h>
#include <wchar.h>


/**
 * print_python_sting - prints info about python strings
 * @p: address of pyobject struct
 * @a_idk scripting
 *
 * Return: NADA!
 */

void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %lu\n", PyUnicode_GET_LENGTH(p));
	printf("  value: %ls\n", PyUnicode_AS_UNICODE(p));
}

