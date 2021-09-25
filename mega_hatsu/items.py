# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from itemloaders.processors import TakeFirst

class MegaHatsuItem(scrapy.Item):
    title = scrapy.Field(
        output_processor = TakeFirst()
    )
    subtitle = scrapy.Field(
        output_processor = TakeFirst()
    )
    Map = scrapy.Field(
        output_processor = TakeFirst()
    )
    sales_price = scrapy.Field(
        output_processor = TakeFirst()
    )
    Yield = scrapy.Field(
        output_processor = TakeFirst()
    )
    property_number = scrapy.Field(
        output_processor = TakeFirst()
    )
    installation_location = scrapy.Field(
        output_processor = TakeFirst()
    )
    number_of_lots_sold = scrapy.Field(
        output_processor = TakeFirst()
    )
    gurantee = scrapy.Field(
        output_processor = TakeFirst()
    )
    stem_price = scrapy.Field(
        output_processor = TakeFirst()
    )
    land_price_or_rent = scrapy.Field(
        output_processor = TakeFirst()
    )
    interconnection_price = scrapy.Field(
        output_processor = TakeFirst()
    )
    consumption_tax = scrapy.Field(
        output_processor = TakeFirst()
    )
    land_developpement = scrapy.Field(
        output_processor = TakeFirst()
    )
    insurrance_cost = scrapy.Field(
        output_processor = TakeFirst()
    )
    land_registration = scrapy.Field(
        output_processor = TakeFirst()
    )
    land_registration_fee = scrapy.Field(
        output_processor = TakeFirst()
    )
    weed_prevention_sheet = scrapy.Field(
        output_processor = TakeFirst()
    )
    fence = scrapy.Field(
        output_processor = TakeFirst()
    )
    signane = scrapy.Field(
        output_processor = TakeFirst()
    )
    remote_monitoring = scrapy.Field(
        output_processor = TakeFirst()
    )
    construction_costs = scrapy.Field(
        output_processor = TakeFirst()
    )
    other_costs_and_features = scrapy.Field(
        output_processor = TakeFirst()
    )
    manufacturer = scrapy.Field(
        output_processor = TakeFirst()
    )
    total_panel_capacity = scrapy.Field(
        output_processor = TakeFirst()
    )
    Type = scrapy.Field(
        output_processor = TakeFirst()
    )
    maximum_output = scrapy.Field(
        output_processor = TakeFirst()
    )
    conversion_efficiency = scrapy.Field(
        output_processor = TakeFirst()
    )
    output_guarantee = scrapy.Field(
        output_processor = TakeFirst()
    )
    product_warranty = scrapy.Field(
        output_processor = TakeFirst()
    )
    assumed_investement_surface_yield = scrapy.Field(
        output_processor = TakeFirst()
    )
    irr_notes= scrapy.Field(
        output_processor = TakeFirst()
    )
    geodic_point = scrapy.Field(
        output_processor = TakeFirst()
    )
    estimated_annual_power_generation = scrapy.Field(
        output_processor = TakeFirst()
    )
    unit_price_per_unit_of_electricity_sold = scrapy.Field(
        output_processor = TakeFirst()
    )
    estimated_electricity_sales_revenue = scrapy.Field(
        output_processor = TakeFirst()
    )
    estimated_electricity_sales_income = scrapy.Field(
        output_processor = TakeFirst()
    )
    sales_price2 = scrapy.Field(
        output_processor = TakeFirst()
    )
    price_notes = scrapy.Field(
        output_processor = TakeFirst()
    )
    manufacturer = scrapy.Field(
        output_processor = TakeFirst()
    )
    model = scrapy.Field(
        output_processor = TakeFirst()
    )
    total_capacity_of_power_conditioner = scrapy.Field(
        output_processor = TakeFirst()
    )
    conversion_efficiency = scrapy.Field(
        output_processor = TakeFirst()
    )
    product_warranty = scrapy.Field(
        output_processor = TakeFirst()
    )
    carbon_dioxid_emission_reduction = scrapy.Field(
        output_processor = TakeFirst()
    )
    conversion_to_cedar_tree = scrapy.Field(
        output_processor = TakeFirst()
    )
