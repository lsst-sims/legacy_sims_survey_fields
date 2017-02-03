.. currentmodule:: lsst.sims.survey.fields

.. _sims-survey-fields-selections:

################################
Creating Queries from Selections
################################

The :py:class:`FieldSelection` is used to construct a query for selecting fields from the 
:py:class:`FieldsDatabase`. The simplest query is to gather all the fields from the database.

.. code-block:: python

  from lsst.sims.survey.fields import FieldSelection
  fs = FieldSelection()
  query = fs.get_all_fields()
  print(query)

  select * from Field;

The simple declination band example shown in the :ref:`Getting Started <lsst-sims-survey-fields-getting-started>` section gives a good feel for how to start to use the API. Other simple band type cuts can be made from other coordinates. The strings avialable to pass to the :py:meth:`FieldSelection.select_region` method are::

  * RA (right-ascention)
  * Dec (declination)
  * EL (ecliptic longitude)
  * EB (ecliptic latitude)
  * GL (galactic longitude)
  * GB (galactic latitude)

More complicated selections can be constructed in a similar manner. We will now look at two examples from the LSST science proposals sky coverage. This is graphically shown in the plot below.

.. image:: /_static/sims_survey_fields/LSST_proposal_sky_coverage.png
    :alt: LSST Science Proposal Footprints

.. _sims-survey-fields-selections-wfd:

Wide, Fast, Deep Coverage
=========================

The Wide, Fast, Deep (WFD) proposal covers a region of the sky extending from a declination of -62.5 degrees up to 2.8 degrees. It also contains an exclusion zone around the galactic plane. The selection is created as follows.

.. code-block:: python

  from lsst.sims.survey.fields import FieldSelection
  fs = FieldSelection()
  query1 = fs.select_region("Dec", -62.5, 2.8)
  query2 = fs.galactic_region(10.0, 0.0, 90.0, exclusion=True)
  query = fs.combine_queries(query1, query2, combiners=('and', ))

The :py:meth:`FieldSelection.select_region` was shown before. The :py:meth:`FieldSelection.galactic_region` is used to create the region in the galactic plane. The keyword `exclusion` is set to `True` so that it will remove fields from any selction that it overlaps. The 
:py:meth:`FieldSelection.combine_queries` is used to join the queries into a single call. The `combiners` keyword is how this is done. This is a set of logical operations for the query joins. The size of the required tuple is one less than the number of queries to combine. A single query does not require the use of `combiners` as seen before. Two queries requires the tuple to be formatted like the one shown in this example.

The parameters used in :py:meth:`FieldSelection.galactic_region` except `exclusion` are explained in the figure below.

.. _sims-survey-fields-galactic-plane:

Galactic Plane Region Description
=================================

The galactic plane region is determined by an envelope as shown in the following graphic.

.. image:: /_static/sims_survey_fields/galactic_plane_envelope.png
    :alt: Galactic Plane Region Definition

It is specified by three values::

  maxB
      This is the value of the maximum extent of the envelope in terms of galactic latitude (degrees) at the galactic longitude of zero degrees.

  minB
      This is the value of the minimum extent of the envelope in terms of galatic latitdue (degrees) at the galatic longitude specified by endL

  endL
      This is the end of the galactic plane envelope in terms of galactic longitude (degrees).

North Ecliptic Spur
===================

The North Ecliptic Spur (NES) proposal covers a region around the ecliptic and north of 2.8 degrees declination. There is no exclusion zone for the NES. Further examples will assume a :py:obj:`FieldSelection` instance is available as `fs`. To create the NES region, the cuts are arranged as follows.

.. code-block:: python

  query1 = fs.select_region("EB", -30.0, 10.0)
  query2 = fs.select_region("Dec", 2.8, 90.0)
  query = fs.combine_queries(query1, query2, combiners=('and', ))  

Selecting by Individual Fields
==============================

:py:class:`FieldSelection` has a method by which one can specify a list of field Id's to retrieve from the field database. The LSST Deep Drilling Cosmology1 (DD1) proposal is handled via this mechanism. To duplicate the list of fields for that proposal, use the following construct.

.. code-block:: python

  query1 = fs.select_user_regions([290, 744, 1427, 2412, 2786])
  query1 = fs.combine_queries(query1)

While this method could be used to retrieve all fields in the database, it is best to limit its use to about a dozen fields.
