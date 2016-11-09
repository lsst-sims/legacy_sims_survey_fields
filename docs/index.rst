.. _lsst-sims-survey-fields:

########################################################
sims_survey_fields - Simulation Survey Field Information
########################################################

.. _lsst-sims-survey-fields-intro:

Introduction
============

This package contains the sky field information that is used by the Operations Simulator. The fields cover the entire sky and have a field-of-view that is commensurate with the LSST camera which is ~9.5 square degrees. The field information is retrieved by use of SQL queries. Those queries can be generated using the provided construction functions. The field information can be retrieved in a number of different structures.

.. _lsst-sims-survey-fields-getting-started:

Getting Started
===============

A quick example is retriving all fields as a set within a declination from -20 degrees to 0 degrees.

.. code-block:: python

  from lsst.sims.survey.fields import FieldsDatabase, FieldsSelection
  # Create the selection
  fs = FieldSelection()
  query = fs.select_region("Dec", -20.0, 0)
  # Create the set fields
  fd = FieldsDatabase()
  field_set = fd.get_field_set(fs.finish_query(query))

The result is a set of tuples containing the field information. 

.. _lsst-sims-survey-fields-getting-started:

Using sims_survey_fields
========================

A series of sections that cover API usage.

Subsections
-----------

Use sectioning liberally.

Galactic Plane Description
==========================

The galactic plane region is determined by an envelope as shown in the following graphic.

.. _lsst-sims-survey-fields-py-ref:

Python Reference
================

API reference for Python developers.
