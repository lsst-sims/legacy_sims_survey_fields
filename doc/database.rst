.. currentmodule:: lsst.sims.survey.fields

.. _sims-survey-fields-database:

###################################################
Retrieving Field Information from Selection Queries
###################################################

With a selection query in hand from the :ref:`Creating Queries from Selections<sims-survey-fields-selections>`, we can now retrieve field information from the internal field database contained within the :py:class:`FieldsDatabase` class. The examples will assume a `query` variable was created by mechnaisms shown previously.

Using the query that retrieves all fields, we can pull a field set from the database.

.. code-block:: python

  from lsst.sims.survey.fields import FieldsDatabase
  fd = FieldsDatabase()
  fields = fd.get_field_set(query)

This produces a set of tuples for all 5292 fields. The contents of each individual tuple are in ordered in the following way.

.. code-block:: python

  (Id, Field-of-View (diameter) RA, Dec, GL, GB, EL, EB)

All units for the FOV and field coordinates are degrees. To retrieve RA and Dec numpy arrays, we use the following function with the WFD region query.

.. code-block:: python

  from lsst.sims.survey.fields import FieldsDatabase
  fd = FieldsDatabase()
  ra, dec = fd.get_ra_dec_arrays(query)

This produces RA and Dec arrays (both in units of degrees) each of which has a length of 2293.

The row information from the fields database can also be extracted. This example uses the query created from the NES region. We will assume now that an instance of :py:obj:`FieldsDatabase` has been created as `fd`.

.. code-block:: python

  rows = fd.get_rows(query)

This produces a list of tuples with a list length of 523 fields. The list contents are tuples containing the field information in the order specified previously. The last function is used for configuration files from version 3 of the Operations Simulator. For this, we will use the fields from the DD1 proposal.

.. code-block:: python

  output = fd.get_opsim3_userregions(query)
  print(output)
  'userRegion = 349.39,-63.32,0.03\nuserRegion = 0.00,-45.52,0.03\nuserRegion = 53.01,-27.44,0.03\nuserRegion = 34.39,-5.09,0.03\nuserRegion = 150.36,2.84,0.03'
