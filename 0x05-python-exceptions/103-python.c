/* 103-python.c */

/* include header files */

#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <floatobject.h>

/* include prototypes */
void print_python_float(PyObject *p);
void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_float - function that prints basic info
 * about Python float objects
 * @p: float object
 * @a_idk scripting
 *
 * Return: NADA!
 */

void print_python_float(PyObject *p)
{
        /* initializing variables */
        char *buf;
        PyFloatObject *float_obj = (PyFloatObject *)p;

        buf = NULL;
        fflush(stdout);
        /* the output print format yields */
        printf("[.] float object info\n");

        if (strcmp(p->ob_type->tp_name, "float"))
        {
                printf("  [ERROR] Invalid Float Object\n");
                return;
        }

        buf = PyOS_double_to_string(float_obj->ob_fval, 'r', 0,
                        Py_DTSF_ADD_DOT_0, NULL);
        printf("  value: %s\n", buf), PyMem_Free(buf);
}


/**
 * print_python_list - function that prints basic info
 * about Python lists
 * @p: list object
 * @a_idk scripting
 *
 * Return: NADA!
 */

void print_python_list(PyObject *p)
{
	/* declaring variables */
	PyVarObject *var;
	PyListObject *lst;
	Py_ssize_t sz;
	Py_ssize_t alloc;
	Py_ssize_t indx;
	const char *type;

	var = (PyVarObject *)p, lst = (PyListObject *)p;
	sz = var->ob_size, alloc = lst->allocated, fflush(stdout);
	printf("[*] Python list info\n");
	if (strcmp(p->ob_type->tp_name, "list"))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}
	printf("[*] Size of the Python List = %ld\n", sz);
	printf("[*] Allocated = %ld\n", alloc);
	for (indx = 0; indx < sz; indx += 1)
	{
		type = lst->ob_item[indx]->ob_type->tp_name;
		printf("Element %ld: %s\n", indx, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(lst->ob_item[indx]);
		else if (strcmp(type, "float") == 0)
			print_python_float(lst->ob_item[indx]);
	}
}


/**
 * print_python_bytes - function that prints basic info
 * about Python byte objects
 * @p: byte object
 * @a_idk scripting
 *
 * Return: NADA!
 */

void print_python_bytes(PyObject *p)
{
	/* declaring and assigning varibles */
	PyBytesObject *bytes = (PyBytesObject *)p;
	Py_ssize_t indx;
	Py_ssize_t sz; /* size */

	fflush(stdout), printf("[.] bytes object info\n");

	if (strcmp(p->ob_type->tp_name, "bytes"))
	{
		/* error check for NULL */
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);
	if (((PyVarObject *)p)->ob_size >= 10)
	{
		sz = 10;
	} else
	{
		sz = ((PyVarObject *)p)->ob_size + 1;
	}
	printf("  first %ld bytes: ", sz);

	for (indx = 0; indx < sz; indx += 1)
	{
		printf("%02hhx", bytes->ob_sval[indx]);

		if (indx == (sz - 1))
		{
			printf("\n");
		} else
		{
			printf(" ");
		}
	}
}
