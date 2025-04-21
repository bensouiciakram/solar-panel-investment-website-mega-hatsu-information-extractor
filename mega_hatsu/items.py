"""
Defines the data structure for scraped items from Mega Hatsu listings.

This module uses Scrapy's Item system to define the fields that will be
extracted from property listings on mega-hatsu.com. The `MegaHatsuItem`
class contains all the relevant fields along with optional input and 
output processors to clean and standardize the scraped data.

Processors:
    - output_processor=TakeFirst(): Only the first non-null value is taken from the scraped result.
    - input_processor=lambda: Custom function to convert strings (e.g., with commas) to floats.
"""

import scrapy
from itemloaders.processors import TakeFirst

class MegaHatsuItem(scrapy.Item):
    """
    Defines the fields for scraped property data from mega-hatsu.com.

    Each field represents a specific property detail or metric, such as
    pricing, yield, warranty, technical specifications, and URLs.
    Input and output processors help standardize the data format.
    """
    title = scrapy.Field(
        output_processor = TakeFirst()
    )#
    subtitle = scrapy.Field(
        output_processor = TakeFirst()
    )#
    Map = scrapy.Field(
        output_processor = TakeFirst()
    )#
    sales_price = scrapy.Field(
        output_processor = TakeFirst()
    )#
    Yield = scrapy.Field(
        input_processor = lambda field_list : [float(number.replace(',','')) for number in field_list],
        output_processor = TakeFirst()
    )#
    property_number = scrapy.Field(
        input_processor = lambda field_list : [float(number.replace(',','')) for number in field_list],
        output_processor = TakeFirst()
    )#
    installation_location = scrapy.Field(
        output_processor = TakeFirst()
    )#
    number_of_lots_sold = scrapy.Field(
        output_processor = TakeFirst()
    )#
    guarantee = scrapy.Field(
        output_processor = TakeFirst()
    )#
    system_price = scrapy.Field(
        output_processor = TakeFirst()
    )#
    land_price_or_rent = scrapy.Field(
        output_processor = TakeFirst()
    )#
    interconnection_price = scrapy.Field(
        output_processor = TakeFirst()
    )#
    consumption_tax = scrapy.Field(
        output_processor = TakeFirst()
    )#
    land_developpement = scrapy.Field(
        output_processor = TakeFirst()
    )#
    insurrance_cost = scrapy.Field(
        output_processor = TakeFirst()
    )#
    land_registration = scrapy.Field(
        output_processor = TakeFirst()
    )#
    weed_prevention_sheet = scrapy.Field(
        output_processor = TakeFirst()
    )#
    fence = scrapy.Field(
        output_processor = TakeFirst()
    )#
    sign = scrapy.Field(
        output_processor = TakeFirst()
    )#
    remote_monitoring = scrapy.Field(
        output_processor = TakeFirst()
    )#
    construction_costs = scrapy.Field(
        output_processor = TakeFirst()
    )#
    other_costs_and_features = scrapy.Field(
        #output_processor = TakeFirst()
    )#
    manufacturer = scrapy.Field(
        output_processor = TakeFirst()
    )#
    total_panel_capacity = scrapy.Field(
        input_processor = lambda field_list : [float(number.replace(',','')) for number in field_list],
        output_processor = TakeFirst()
    )#
    Type = scrapy.Field(
        output_processor = TakeFirst()
    )#
    maximum_output = scrapy.Field(
        output_processor = TakeFirst()
    )#
    conversion_efficiency = scrapy.Field(
        input_processor = lambda field_list : [float(number.replace(',','')) for number in field_list],
        output_processor = TakeFirst()
    )#
    output_guarantee = scrapy.Field(
        input_processor = lambda field_list : [float(number.replace(',','')) for number in field_list],
        output_processor = TakeFirst()
    )#
    product_warranty = scrapy.Field(
        input_processor = lambda field_list : [float(number.replace(',','')) for number in field_list],
        output_processor = TakeFirst()
    )#
    assumed_investement_surface_yield = scrapy.Field(
        input_processor = lambda field_list : [float(number.replace(',','')) for number in field_list],
        output_processor = TakeFirst()
    )#
    irr_notes= scrapy.Field(
        output_processor = TakeFirst()
    )#
    geodetic_point = scrapy.Field(
        output_processor = TakeFirst()
    )#
    estimated_annual_power_generation = scrapy.Field(
        input_processor = lambda field_list : [float(number.replace(',','')) for number in field_list],
        output_processor = TakeFirst()
    )#
    unit_price_per_unit_of_electricity_sold = scrapy.Field(
        input_processor = lambda field_list : [float(number.replace(',','')) for number in field_list],
        output_processor = TakeFirst()
    )#
    estimated_electricity_sales_revenue = scrapy.Field(
        input_processor = lambda field_list : [float(number.replace(',','')) for number in field_list],
        output_processor = TakeFirst()
    )#
    estimated_electricity_sales_income = scrapy.Field(
        input_processor = lambda field_list : [float(number.replace(',','')) for number in field_list],
        output_processor = TakeFirst()
    )#
    sales_price2 = scrapy.Field(
        input_processor = lambda field_list : [float(number.replace(',','')) for number in field_list],
        output_processor = TakeFirst()
    )#
    price_notes = scrapy.Field(
        output_processor = TakeFirst()
    )#
    manufacturer2 = scrapy.Field(
        output_processor = TakeFirst()
    )#
    model = scrapy.Field(
        output_processor = TakeFirst()
    )#
    total_capacity_of_power_conditioner = scrapy.Field(
        input_processor = lambda field_list : [float(number.replace(',','')) for number in field_list],
        output_processor = TakeFirst()
    )#
    conversion_efficiency = scrapy.Field(
        input_processor = lambda field_list : [float(number.replace(',','')) for number in field_list],
        output_processor = TakeFirst()
    )#
    product_warranty = scrapy.Field(
        output_processor = TakeFirst()
    )#
    carbon_dioxid_emission_reduction = scrapy.Field(
        output_processor = TakeFirst()
    )
    conversion_to_cedar_tree = scrapy.Field(
        output_processor = TakeFirst()
    )
    identifier = scrapy.Field(
        output_processor = TakeFirst()
    )
    status = scrapy.Field(
        output_processor = TakeFirst()
    )
    url = scrapy.Field(
        output_processor = TakeFirst()
    )
